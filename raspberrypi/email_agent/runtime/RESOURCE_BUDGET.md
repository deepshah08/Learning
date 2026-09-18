# Pi-loop Resource Budget and Overage Ledger

This file records measured production costs, declared limits, and corrective
actions. Secrets and email content are intentionally excluded.

## Active budgets

| Resource | Budget | Enforcement |
|---|---:|---|
| Pipeline wall time | 840 seconds | Internal overage ledger; systemd hard stop at 900 seconds |
| One local classification | 25 seconds | Ollama HTTP connect/read deadline |
| One `/ask` synthesis | 45 seconds | Ollama HTTP connect/read deadline; sources still returned on timeout |
| Gemini audit phase | 45 seconds | Batch deadline; unfinished audits are deferred |
| Gemini retries | 2 attempts, 12 seconds of waiting | Bounded retry budget |
| Email-agent RSS | 1,024 MB | systemd `MemoryMax=1G` |
| Telegram bot RSS | 150 MB | systemd `MemoryMax=150M` |
| Bot CPU | 15% | systemd `CPUQuota=15%` |
| Email-agent CPU | 50% | systemd `CPUQuota=50%` |
| Thermal pause threshold | 78 C | Pipeline thermal gate |

Every new pipeline execution writes a `pipeline_runs` row containing duration,
email count, fallback count, classification time, Gemini time, process peak
RSS, temperature, completion state, and structured overages. Telegram command
`/resources` shows the five newest rows and the current bot/Ollama footprint.

## Production baseline — 2026-09-14 15:06 PDT

| Measurement | Observed | Assessment |
|---|---:|---|
| Pi memory | 1.2 GiB used / 15 GiB; 14 GiB available | Healthy |
| Swap | 0 / 2 GiB | Healthy |
| Core temperature | 43.3 C | Healthy |
| Root filesystem | 17 GiB / 117 GiB (15%) | Healthy |
| Telegram bot RSS | 53.2 MB / 150 MB | Healthy |
| Idle Ollama server RSS | 38.6 MB | Healthy; no model resident |
| Email database | 6.8 MB | Healthy |
| Agent log | 512 KB | Small, but duplicated records were present |

## Overage ledger

### 2026-09-14 12:36–12:51 PDT — ingestion hard timeout

- Observed: `email-agent.service` reached its 900-second systemd limit and was
  terminated. The run processed messages but never wrote its final heartbeat.
- Local classification calls intended to stop at 25 seconds actually consumed
  approximately 101–126 seconds because executor shutdown waited for the
  blocked worker.
- Gemini encountered HTTP 503 and 429 responses. Seven-attempt retry policy
  admitted 60-second sleeps and consumed at least 135 seconds near the end of
  the run.
- Logs contained every record twice because Python `FileHandler` and systemd
  stdout redirection both appended to the same file.
- Evaluator emitted many historical sender-rule conflicts that predated the
  learned rules and therefore were not actionable current drift.

Corrective actions:

- Replaced thread-based Ollama timeout with an HTTP socket deadline.
- Reduced classification output allowance from 256 to 160 tokens.
- Bounded Gemini to two attempts, 12 seconds of retry waiting, 15 seconds per
  request, and 45 seconds for the complete audit phase. Exhausted work is
  deferred without changing labels.
- Reduced Gemini JSON output allowance from 1,024 to 256 tokens.
- Restricted rule conflicts to emails processed after the rule was learned.
- Disabled Python file handlers under systemd to eliminate double writes.
- Added durable `pipeline_runs` instrumentation so interrupted and
  over-budget runs remain queryable.

### 2026-09-14 15:14 PDT — controlled Ollama deadline validation

- Cold `qwen2.5:3b` classification stopped at 25.03 seconds with a real HTTP
  read timeout. This validates the deadline that previously leaked to more
  than 100 seconds.
- A second warm request completed in 23.27 seconds with a 165-byte JSON
  response.
- Loading `qwen2.5:3b` plus `all-minilm` raised total system memory use from
  1.2 GiB to 3.5 GiB; 12 GiB remained available and swap stayed at zero.
- Core temperature rose from 43.3 C to 49.4 C, far below the 78 C pause
  threshold.
- Existing fallback prevalence is high: 5/25 recent emails (20%), 16/50
  (32%), and 52/100 (52%). The deadline prevents runaway runtime but does not
  solve local-model throughput; deterministic coverage and measured teacher
  auditing should be expanded before raising the time budget.

### 2026-09-13 persona suite — serialized Q&A latency

- Ten-query serialized synthesis exceeded a 180-second validation window.
- A representative warm shopping/shipping answer completed in about 16
  seconds and remained grounded in retrieved sources.
- `/ask` now has a 45-second socket deadline, reduces answer output from 200 to
  120 tokens, returns retrieved sources on timeout, and records synthesis time
  plus overage state in `rag_feedback_log`.

### 2026-09-14 15:22 PDT — duplicate Telegram digest request

- The completed validation run delivered its digest, but unescaped email text
  caused Telegram's Markdown parser to reject the first request with HTTP 400.
  The existing plaintext fallback then made a second request successfully.
- Notification digests, urgent alerts, and evaluator guardrail alerts now use
  plaintext on the first attempt. Permanent 4xx responses are not retried;
  only HTTP 429 and 5xx responses receive one bounded retry.
- The review also found that evaluator alerts referenced a missing direct-send
  function. The function is now implemented and covered by a regression test,
  so genuine guardrail failures are no longer silently discarded.

### 2026-09-18 14:29 PDT — avoidable chat synthesis (within deadline)

- Observed: `/ask can you mark all as read` retrieved two unrelated records
  and spent 41,458 ms in Qwen synthesis. This remained below the 45-second RAG
  deadline, so it is not a formal overage and did not change Gmail.
- Cause: an operational bulk-read intent reached semantic retrieval instead of
  a command-specific path.
- Corrective action: natural latest-N requests now read SQLite directly;
  natural bulk-read requests are refused by read-only `/ask` and directed to
  `/mark-read all`. The latter needs a user/chat/action-bound, five-minute,
  single-use confirmation before it lists `is:unread` and removes `UNREAD` in
  batches of at most 1,000 messages.
- Validation: local and Pi unit suites verified the guard, token consumption,
  and batch request shape. No confirmation was tapped during validation; no
  live Gmail mutation or pipeline run occurred.
- Live post-deploy snapshot: FTL RSS about 69 MB, bot RSS about 52 MB, Ollama
  RSS about 40 MB. FTL remained nice -10 with `oom_score_adj=-1000`;
  CPU/I/O/pids cgroups are available, memory cgroups are not.

## Operating policy

- Do not increase the 900-second systemd timeout to hide slow dependencies.
- A failed teacher audit must never block ingestion or apply an unverified
  correction; defer it to a future batch.
- Treat repeated local-model timeouts as a classification-capacity signal.
  Expand deterministic rules or reduce batch size before increasing budgets.
- Record new measured overages here, including cause and corrective action.
