# Pi-loop Email Agent — Durable Knowledge

> Companion: investigation journey at
> [`pi_loop_email_agent_investigation.md`](./pi_loop_email_agent_investigation.md)
> 
> Runtime source snapshot: [`runtime/`](./runtime/)

## System purpose

Pi-loop is a privacy-first Gmail triage and inbox-intelligence service deployed
on a 16 GB Raspberry Pi 5. It ingests forwarded Gmail messages, classifies and
archives them, tracks follow-up state, learns from user corrections, indexes
content for retrieval, provides Telegram commands, and optionally uses Gemini
as an advisory teacher.

The system is subordinate to whole-home networking. Pi-hole FTL and Unbound
remain the P0 workload; email processing and local model generation are
background work.

## Component boundaries

| Component | Responsibility | Availability rule |
|---|---|---|
| `gmail_agent.py` | Gmail ingestion, classification orchestration, SQLite state, reminders, metrics | Core ingestion must finish or record an interrupted/over-budget run |
| `email_classifier.py` | Deterministic rules, Ollama classification, pessimistic fallback | A model timeout must return within the socket deadline |
| `gemini_teacher.py` | Optional authoritative audit and correction proposal | Advisory only; defer on budget/error |
| `background_evaluator.py` | Invariant, drift, and current-rule conflict checks | Historical messages do not create current conflicts |
| `bot_service.py` | Telegram commands, RAG, feedback, resource status | Fail closed; deterministic mailbox intent bypasses RAG; mutations require confirmation |
| `notifier.py` | Digest, urgent alerts, evaluator alerts | Dynamic content is plaintext; transient-only retry |
| SQLite | WAL-backed state, FTS5 retrieval, embeddings, run ledger | Use the shared connection factory and busy timeout |
| Ollama | Local `qwen2.5:3b` and `all-minilm` inference | Capped and lower priority than DNS |

## Data and safety invariants

1. An `URGENT` or `IMPORTANT` message must never be automatically archived.
2. Teacher failures never apply an unverified label correction.
3. Zero retrieval matches produce zero RAG sources and zero context tokens.
4. Unknown Telegram chat IDs fail closed and cannot query tenant data.
5. Dynamic email text is never parsed as Telegram Markdown; plaintext payloads
   omit `parse_mode`.
6. Every ingestion run has a durable `pipeline_runs` record, including failure,
   interruption, and overage information.
7. Sender-rule conflicts are evaluated only against messages processed after
   the rule was learned.
8. Gmail quota zero means no Gmail request.
9. Pi-hole FTL remains OOM-immune and higher scheduler priority than AI work.
10. Natural-language chat alone cannot mutate Gmail. A mutation needs a
    tenant-bound, chat-bound, expiring, single-use confirmation callback.
11. Sender-level priority learning occurs only after an explicit target and
    priority selection; candidate lookup itself is read-only.

## Active resource contracts

| Resource | Contract | Measurement |
|---|---:|---|
| Full pipeline | 840 s internal budget; 900 s systemd hard stop | `pipeline_runs.duration_seconds` |
| Local classification | 25 s socket read deadline | `max_classify_seconds` |
| RAG synthesis | 45 s socket deadline, 120-token answer target; retrieval questions only | `rag_feedback_log.synthesis_ms` |
| Gemini audit phase | 45 s batch budget | `gemini_seconds`, deferred count |
| Gemini retries | Two attempts and 12 s configured wait budget | teacher audit metrics |
| Email-agent RSS | 1,024 MB budget | `pipeline_runs.max_rss_mb` |
| Bot RSS | 150 MB systemd ceiling | service cgroup / `/resources` |
| Email-agent CPU | 50% quota, nice +15 | systemd unit |
| Bot CPU | 15% quota, nice +15 | systemd unit |
| Ollama CPU | 150% quota, nice +15 | systemd drop-in |
| FTL | nice -10, `OOMScoreAdjust=-1000`, restart 1 s | systemd unit and process state |
| Thermal pause | 78 C | pipeline thermal gate |

The current kernel exposes CPU, I/O, and pids cgroup controllers but not the
memory controller. Do not describe the configured memory ceilings as hard
reservations; rely on RSS telemetry, FTL OOM immunity, and measured headroom.

## Inference policy

The classifier is deterministic-first and model-assisted. It sends bounded
context to Ollama and validates/sanitizes structured output. If local inference
fails, the pessimistic fallback preserves safety by escalating clear urgency
signals rather than silently archiving or normalizing them.

Gemini is a teacher, not a gate. It audits a measured subset after core
ingestion. A 429, 503, timeout, or exhausted budget defers work without
changing the stored label.

## Notification policy

Telegram messages are chunked below the API limit. Digest, urgent, and evaluator
messages use plaintext because subjects, senders, summaries, and learned rules
are arbitrary external text. Only rate-limit and server-error responses get one
retry. A permanent 4xx is logged once and not duplicated.

Bot command views containing mailbox text follow the same plaintext-first
contract. The bot omits the optional Telegram `parse_mode` field for those
views, avoiding an invalid JSON null parameter and avoiding Markdown-failure
fallback requests.

## Interactive command policy

| Intent | Path | Side effect |
|---|---|---|
| Retrieve a fact from email content | `/ask <question>` | Bounded RAG only after intent screening |
| List most recent mail | `/latest [1-20]` or natural latest-N `/ask` wording | SQLite read only; no Qwen |
| Correct a category or priority | `/correct <email words>` or `/rules <correction>` | Candidate lookup is read-only; a tenant-bound button applies the correction |
| Mark all mail read | `/mark-read all` | One explicit, five-minute, single-use confirmation; batched Gmail `UNREAD` removal |

Priority corrections preserve manual Gmail state such as stars. `URGENT` and
`IMPORTANT` map to the managed Gmail priority labels; `NORMAL` and `LOW`
remove managed priority labels without adding a replacement. The feedback
transaction updates Gmail first, then records local correction and sender-rule
state.

## Operational verification

Run from the runtime directory with a configured virtual environment:

```bash
python3 -m py_compile *.py
python3 test_pipeline.py
python3 test_accuracy_pipeline.py
python3 challenge_suite.py
```

On the Pi, inspect the bounded system without triggering a full ingestion run:

```bash
systemctl status email-bot.service ollama.service email-agent.timer
curl -fsS http://127.0.0.1:11434/api/ps
free -h
vcgencmd measure_temp
```

Use the Telegram `/resources` command for recent pipeline rows, overages, bot
RSS, resident Ollama models, and temperature. Do not print or commit `.env`,
OAuth files, databases, or Telegram/Gemini credentials.

## Corrections to historical documents

> **Post-Session Correction (2026-09-15):** Earlier README and handoff sections
> describe Telegram Markdown fallback and Ollama `CPUQuota=250%`, `Nice=10`.
> Those values are historical design/incident notes. The current deployed
> runtime uses plaintext-first notifications and live Ollama `CPUQuota=150%`,
> `Nice=15`; this document and the runtime snapshot are authoritative for the
> current state.
