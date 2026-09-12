# 📬 Pi-loop Email Intelligence Agent

> **Autonomous, privacy-first email triage, semantic classification, and proactive task-tracking pipeline running on Raspberry Pi 5 with local Ollama LLMs and real-time Telegram Bot intelligence.**

---

## 🌟 1. System Architecture & Component Design

The **Pi-loop Email Intelligence Agent** runs 24/7 on a local **Raspberry Pi 5 (16 GB LPDDR4X)**. It combines Google Gmail API integration, on-device quantized LLMs (`qwen2.5:3b`), SQLite FTS5 full-text indexing, multi-tenant fair-share scheduling, and an interactive Telegram bot.

### Architecture Dataflow Diagram

```
                                      +------------------------------------+
                                      | Google Gmail API (OAuth2 Refresh)  |
                                      +-----------------+------------------+
                                                        |
                                                        v
+---------------------------------------------------------------------------------------------------+
| Raspberry Pi 5 (16 GB LPDDR4X)                                                                    |
|                                                                                                   |
|   +--------------------------+         +-------------------------------+         +-------------+  |
|   |   email-agent.timer      | ------> |        gmail_agent.py         | ------> | SQLite DB   |  |
|   |   (Every 15 minutes)     |         |  (Fair-Share Quota Ingestion) |         | (WAL Mode)  |  |
|   +--------------------------+         +---------------+---------------+         +------+------+  |
|                                                        |                                |         |
|                                                        v                                v         |
|                                        +---------------+---------------+         +------+------+  |
|                                        |      email_classifier.py      |         | SQLite FTS5 |  |
|                                        |  (Ollama Local qwen2.5:3b)    |         | Virtual Idx |  |
|                                        +---------------+---------------+         +------+------+  |
|                                                        |                                ^         |
|                                                        v                                |         |
|   +--------------------------+         +---------------+---------------+                |         |
|   |   email-bot.service      | ------> |        bot_service.py         | ---------------+         |
|   |   (Long-Polling Daemon)  |         |  (Interactive Commands)       |                          |
|   +--------------------------+         +---------------+---------------+                          |
+--------------------------------------------------------|------------------------------------------+
                                                         |
                                                         v
                                      +------------------------------------+
                                      | Telegram Bot API / User Alerts     |
                                      +------------------------------------+
```

---

## ⚙️ 2. Core Subsystems & Technical Innovations

### A. Google Advanced Protection Program (APP) Forwarding Strategy
- **The Challenge**: Accounts enrolled in Google Advanced Protection Program block direct OAuth desktop consent flows and third-party apps.
- **The Architectural Solution**: Auto-forward emails from the primary APP-protected account (`deepshah7977@gmail.com`) to an auxiliary operational inbox (`sl4ught3rcl4y@gmail.com`).
- **Ground-Truth Recipient Preservation**: Gmail preserves true sender in `From:` and preserves original target recipient in `To:` or `X-Forwarded-For:`. The agent parses and indexes `original_recipient`, tagging alerts as `[deepshah7977]` vs `[sl4ught3rcl4y]`.

### B. SQLite FTS5 Full-Text Search Virtual Tables
- High-performance full-text search indexing on `(msg_id, subject, summary, sender)`.
- Synchronized via automatic triggers:
  - `processed_emails_ai` (AFTER INSERT)
  - `processed_emails_ad` (AFTER DELETE)
  - `processed_emails_au` (AFTER UPDATE)
- Sub-millisecond retrieval on Telegram `/search <query>` commands.

### C. Multi-Tenant Fair-Share Round-Robin Engine (`user_manager.py`)
- Declarative tenant configuration in `config/users.json`.
- Supports up to 10+ users simultaneously.
- Isolates user databases (`data/<user>_emails.db`) and credential tokens (`credentials/<user>_token.json`).
- Prevents single-user mailbox starvation using per-cycle quota chunking (`max_emails_per_run=15`).

### D. Interactive Telegram Command Center (`bot_service.py`)
- Running as systemd daemon (`email-bot.service`) via Telegram long-polling.
- Commands supported:
  - `/status` — Live Pi 5 core temperatures, system memory, timer status, and database metrics.
  - `/briefing` — Category breakdown (Work, Finance, Personal, Newsletter) and recent triage activity.
  - `/reminders` — Pending action items awaiting user reply or review.
  - `/rules` — Displays active learned sender overrides.
  - `/search <query>` — Sub-millisecond FTS5 search across all indexed emails.
  - `/help` — Command menu.

---

## 🧪 3. Verification & Red-Team Challenge Suite (`challenge_suite.py`)

A formal 3-iteration stress-testing suite guarantees system reliability:
1. **Iteration 1: Scalability & Concurrency Stress Test**:
   - 10 concurrent threads (5 writers inserting 100 emails, 5 readers querying FTS5 simultaneously).
   - Zero `database is locked` errors under SQLite WAL mode with 100% trigger index parity.
2. **Iteration 2: Adversarial Injection & Malformed JSON Robustness**:
   - Hardened prompt injection containment using `<<<UNTRUSTED_EMAIL_CONTENT_START>>>` delimiters.
   - Robust JSON extraction fallback: gracefully handles malformed LLM outputs and coerces unparseable responses to `NORMAL` priority.
3. **Iteration 3: Fault Recovery, Thermal Limits & User Isolation**:
   - Automated schema self-healing: automatically reconstructs dropped FTS5 virtual tables and triggers.
   - Thermal headroom gating (monitors `/sys/class/thermal/thermal_zone0/temp`, enforces threshold $< 78.0^\circ\text{C}$).
   - Multi-user isolation verification with 10 distinct tenants.

---

## 📋 4. Deployment & Service Management

### Systemd Units
- `email-agent.timer`: Triggers ingestion every 15 minutes.
- `email-agent.service`: Executes one-shot ingestion cycle.
- `email-bot.service`: Continuous background long-polling daemon.

### Service Commands on Pi 5
```bash
# Check service states
sudo systemctl status email-bot.service
systemctl status email-agent.timer

# View live logs
tail -f ~/email-agent/logs/bot_service.log
tail -f ~/email-agent/logs/agent.log
```

---

## 📊 5. Worst-Case Resource Footprint & System Priority Matrix

To safeguard real-time home networking (`pihole-FTL` DNS) and maintain thermal headroom, the email agent subsystem operates under strict Linux cgroup limits and process priority policies.

### Resource Footprint Analysis

| Component | Idle / Baseline | Nominal Processing | Worst-Case Peak (Hard Capped) | Enforcement Mechanism |
| :--- | :--- | :--- | :--- | :--- |
| **`bot_service.py`** | ~36 MB | ~45 MB | **150 MB** | Systemd `MemoryMax=150M`, `CPUQuota=15%` |
| **`gmail_agent.py`** | 0 MB (oneshot) | ~110 MB | **1.0 GB** | Systemd `MemoryMax=1G`, `CPUQuota=50%` |
| **`ollama` (`qwen2.5:3b`)** | ~43 MB (unloaded) | ~2.1 GB | **2.4 GB** | Weight footprint + 4K KV-cache (auto-unloads after 5m) |
| **SQLite + FTS5** | ~8 MB | ~25 MB | **64 MB** | In-memory page cache for WAL + FTS5 index scans |
| **Total Subsystem** | **~80 MB** | **~2.3 GB** | **~3.6 GB max** | **< 23%** of Pi 5's 16 GB LPDDR4X RAM |

### CPU Scheduling & Blast-Radius Decoupling

- **`Nice=15` (Email Agent & Bot)**: Background classification willingly yields CPU time slices to higher-priority processes.
- **`Nice=-10` & `OOMScoreAdjust=-1000` (`pihole-FTL`)**: Real-time whole-home DNS resolution runs with top CPU scheduling priority and complete immunity from kernel OOM termination.
- **Thermal Safety Gate**: Active cooling maintains Pi 5 temperatures at 43°C–54°C. A software watchdog enforces immediate processing suspension if temperatures exceed **78.0°C**.
