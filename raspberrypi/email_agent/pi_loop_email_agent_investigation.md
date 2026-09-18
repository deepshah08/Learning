# Pi-loop Email Agent — Investigation Journal

> Companion: durable current-state knowledge at
> [`pi_loop_email_agent_knowledge.md`](./pi_loop_email_agent_knowledge.md)
> 
> Runtime source snapshot: [`runtime/`](./runtime/)

## Scope and outcome

This record preserves the reasoning path, experiments, rejected approaches,
measured overages, and validation evidence from the September 2026 production
hardening cycle. The target was a live Raspberry Pi 5 email-triage pipeline
using Gmail, SQLite, Ollama, Gemini auditing, Telegram, and Pi-hole/Unbound
network services.

The final outcome was a bounded, observable pipeline that does not allow slow
local inference, teacher retries, malformed notifications, or evaluator noise
to block ingestion or threaten whole-home DNS.

## Iteration 0 — Baseline review and incident reconstruction

### Observations

- Pi 5 baseline: 15 GiB RAM, about 1.2 GiB used, no swap use, 43.3 C, 15%
  root filesystem usage.
- Telegram bot RSS was about 53 MB; idle Ollama RSS about 39 MB; database about
  6.8 MB.
- `email-agent.service` had reached the 900-second systemd stop limit during a
  production run.
- Recent fallback prevalence was high: 5/25 (20%), 16/50 (32%), and 52/100
  (52%).

### Root causes established

1. The local classifier used a `ThreadPoolExecutor` timeout. The caller timed
   out at 25 seconds, but executor context-manager shutdown waited for the
   blocked worker, producing observed calls of roughly 101–126 seconds.
2. Gemini used seven attempts and long backoff. HTTP 503/429 responses admitted
   60-second sleeps and consumed at least 135 seconds near the failed run.
3. Python file handlers and systemd stdout both appended to the same log, so
   records appeared twice.
4. The evaluator compared historical messages against rules learned later,
   creating false conflict storms.
5. The Telegram digest used legacy Markdown around arbitrary email subjects and
   senders. A malformed entity caused an HTTP 400, followed by a second
   plaintext request.
6. Evaluator alert dispatch imported `send_telegram_direct`, but the function
   was absent; a real alert could be swallowed by the exception handler.

## Iteration 1 — Real local-model deadlines

### Decision

Replace thread-based cancellation with an actual HTTP connect/read deadline to
Ollama. Keep the classifier’s pessimistic urgency fallback, but make timeout
behavior truthful.

### Changes

- Direct `requests.post` to `/api/generate`, `stream=false`.
- Connect timeout 3 seconds; per-call read timeout 25 seconds.
- Classification output allowance reduced from 256 to 160 tokens.

### Evidence

- Controlled cold request stopped at 25.03 seconds with a real read timeout.
- Warm request completed in 23.27 seconds with a 165-byte response.
- During model residency, system memory rose to about 3.5 GiB used, with 12 GiB
  available, zero swap use, and temperature 49.4 C.

### Rejected path

Increasing the systemd 900-second ceiling was rejected. It would hide leaked
work rather than correct the dependency boundary.

## Iteration 2 — Bounded Gemini teacher auditing

### Decision

Teacher auditing is advisory. It must never block ingestion, rewrite a label
after an exhausted budget, or consume an unbounded retry schedule.

### Changes

- Two attempts by default, with retry waits of 3 and 6 seconds.
- Maximum three attempts can be configured, but the phase has a hard 45-second
  batch budget.
- Per-request timeout is 15 seconds, adjusted downward by remaining budget.
- Gemini JSON output allowance reduced to 256 tokens.
- Exhausted or failed work is marked deferred; no unverified correction is
  applied.
- Audit batch size defaults to three and is capped at ten.

### Evidence

A live bounded run encountered a 429, retried once after about 2.8 seconds,
then deferred a 503. The full Gemini phase completed in about 7.9 seconds.

### Rejected path

Keeping seven retries was rejected because quota errors and server errors are
not fixed by repeated long sleeps, and the retry cost competed with core
ingestion.

## Iteration 3 — Observability and evaluator correctness

### Decisions

Make every pipeline run durable and make drift checks time-aware.

### Changes

- Added `pipeline_runs` with status, counts, fallback count, classification and
  Gemini timings, RSS, temperature, errors, and structured overages.
- Stale `running` rows are marked interrupted on the next start.
- Budgets are recorded, not inferred after the fact: 840-second pipeline,
  25-second classification (with small measurement tolerance), 45-second
  Gemini phase, and 1,024 MB email-agent RSS.
- Rule conflicts only consider emails processed after the rule’s update time and
  ignore corrected rows.
- Added `/resources` reporting for recent pipeline rows and current bot/Ollama
  footprint.
- Added ingestion heartbeat metadata before optional teacher work.

### Evidence

The historical failed run remains queryable as a structured overage:

| Metric | Actual | Budget |
|---|---:|---:|
| Pipeline duration | 900 s | 840 s |
| Classification latency | 126 s | 25 s |
| Gemini retry backoff | 135 s | 45 s |

The live evaluator against the repaired database reported health 100, zero
invariant violations, zero drift warnings, and zero current rule conflicts.

## Iteration 4 — RAG and quota boundary hardening

### Changes

- `/ask` synthesis uses a real 45-second Ollama socket deadline.
- Synthesis output was reduced to 120 tokens.
- Retrieved sources are still returned when synthesis times out.
- `rag_feedback_log` stores match count, synthesis time, and over-budget state.
- Gmail fetch now returns immediately for `max_results <= 0`.

### Evidence

The zero-quota regression was reproduced, fixed, and covered so control runs do
not issue an unnecessary Gmail request. Persona and RAG challenge coverage
continued to pass.

## Iteration 5 — Notification safety and guardrail delivery

### Decision

Use plaintext for dynamic notification content. Email subjects, senders, and
learned rules are untrusted text and should not be interpreted as Telegram
Markdown.

### Changes

- Digest, urgent-alert, and evaluator-alert payloads are plaintext on the first
  request.
- Permanent HTTP 4xx responses are not retried.
- HTTP 429 and 5xx responses receive one bounded retry.
- Implemented `send_telegram_direct` for explicit evaluator alert routing.

### Evidence

The permanent-400 test now makes one request, while a transient-503 test makes
exactly one retry. Challenge suite notification chunking still passes.

### Rejected path

Escaping every Markdown field was considered, but plaintext is lower-risk for
arbitrary external content and removes the duplicate-request failure class.

## Iteration 6 — Pi-hole FTL protection review

### Findings

- FTL was active for multiple days, with about 90 MB RSS and 11 tasks.
- FTL runs with nice -10, `OOMScoreAdjust=-1000`, and `Restart=always` with a
  one-second restart delay.
- Ollama is capped at 150% CPU and nice +15; email-agent is capped at 50% and
  nice +15; the bot is capped at 15% and nice +15.
- Ten local DNS probes measured 13.3 ms median and 23.0 ms maximum.
- The kernel exposes CPU/I/O/pids cgroup controllers but not the memory
  controller. Memory limits shown by systemd therefore are not hard memory
  partitions on this host.

### Decision

Keep dynamic CPU scheduling priority and quotas. Do not pin FTL to a core or
raise AI ceilings without evidence of DNS degradation. OOM immunity and
relative CPU priority are the effective P0 protections currently available.

## Iteration 7 — Chat-driven command routing and feedback repair

### Trigger and evidence

Telegram history on 2026-09-18 exposed command classes that should not enter
semantic retrieval:

| Chat request | Observed pre-fix behavior | Cost / defect |
|---|---|---|
| `/ask can you mark all as read` | Matched two unrelated records and called Qwen | 41,458 ms synthesis; no Gmail state change |
| `/ask last 5 emails` | Attempted retrieval rather than a local list | Could return no matches instead of inbox state |
| `/rules 💸 Pets, partners and pools was not imp` | Ignored the argument and ran Gmail feedback sync | Could not correct the intended priority |

The 41,458 ms request remained below the 45-second RAG deadline, so it was
not a recorded resource overage. It was still an avoidable model allocation
for an operational intent. Existing long-poll connection resets were observed
in historical logs; the daemon recovered and remained active, so no restart
policy change was justified.

### Decisions

1. Classify deterministic mailbox intents before RAG. A latest-N request reads
   SQLite directly; a bulk mark-as-read request never invokes Qwen.
2. Treat every Gmail mutation as an explicit confirmation flow. Natural
   language only explains the safe command; it cannot mutate Gmail.
3. Convert bot views containing email-derived fields to direct plaintext.
   `parse_mode` is omitted rather than sent as JSON `null`.
4. Make priority corrections a first-class, target-bound feedback operation.
   The natural correction phrase finds candidates but a user tap selects and
   applies the priority.

### Implemented behavior

- `/latest [N]` lists the latest 1--20 processed records from SQLite.
- `/ask last 5 emails` and equivalent latest/recent wording use that path;
  no retrieval or Qwen synthesis occurs.
- `/ask ... mark all ... read` responds that `/ask` is read-only and
  directs the user to `/mark-read all`.
- `/mark-read all` creates a user/chat/action-bound random nonce with a
  five-minute TTL. The confirmation callback atomically consumes it once,
  lists only `is:unread`, and removes Gmail's `UNREAD` label in batches of
  at most 1,000 IDs.
- The bulk operation was unit-tested but not pressed against the live inbox;
  deployment therefore made no Gmail read-state change.
- `/rules <correction>` and `/correct <correction>` find candidates using
  local subject terms. Both category and priority keyboards are tenant-bound.
  A priority tap updates Gmail labels, `processed_emails`,
  `email_label_state`, `user_corrections`, and the sender rule together.
- Briefing, reminders, rules, search results, RAG answers, and correction
  cards now use plaintext for dynamic fields. Search rejects punctuation-only
  FTS input before it can create an invalid query.

### Validation and live state

- Added tests for plaintext payload omission, priority feedback persistence,
  correction lookup, single-use confirmation, Gmail batch payloads, and the
  no-Qwen bulk-read guard.
- Local: `py_compile`, `test_pipeline.py`, `test_accuracy_pipeline.py`,
  and `challenge_suite.py` passed. The expected evaluator-invariant message
  in the accuracy suite is a test fixture, not a live incident.
- Pi: staged compile and `venv/bin/python test_pipeline.py` passed; bot
  deployed and last restarted cleanly at 2026-09-18 14:52 PDT.
- Live service check: Pi-hole FTL, bot, Ollama, and agent timer were active.
  FTL process nice was -10, `oom_score_adj=-1000`, RSS about 69 MB; bot RSS
  about 52 MB; Ollama RSS about 40 MB. CPU/I/O/pids cgroups remain available,
  but memory cgroups do not.

## Validation sequence and final evidence

The following were run after implementation:

1. Local `py_compile`, pipeline tests, accuracy tests, and all five challenge
   iterations — passed.
2. Pi temporary-copy compile and pipeline tests — passed.
3. Controlled cold/warm Ollama deadline and thermal checks — passed.
4. Full production run — 15/15 messages processed in 145.7 seconds, two local
   fallbacks, maximum classification call 25.1 seconds, Gemini 7.9 seconds,
   peak agent RSS 70.9 MB, no recorded overage.
5. Zero-email control run — completed in 4.9 seconds with no overage.
6. Bot restart and service/timer verification — bot and Ollama active; timer
   waiting for its next scheduled run.
7. Runtime snapshot copied into this repository, secret-scanned, committed,
   and pushed.
8. Chat-driven bot review and deployment — deterministic routing, explicit
   bulk-read confirmation, priority feedback, and plaintext bot views passed
   local and Pi unit checks without a production Gmail mutation or pipeline
   overage.

## Remaining questions

- Fallback prevalence remains the largest performance signal. Expand
  deterministic rules and measure smaller batches before increasing timeouts.
- The memory controller is unavailable on the current kernel. Treat RSS and
  temperature instrumentation as the practical guardrail until kernel/cgroup
  support changes.
- The parent README and original handoff contain historical values; the paired
  knowledge document below is the current-state authority.
