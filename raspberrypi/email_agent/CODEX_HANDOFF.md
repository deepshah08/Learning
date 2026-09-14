# CODEX AGENT HANDOFF: Pi-loop Email Intelligence Platform

> **Target Audience**: Autonomous AI Engineering Agents (Codex, Cursor, Claude Code) & Developers taking over development, maintenance, and architectural extension of the **Pi-loop Email Intelligence Platform**.
> **Status**: Production-Active on Raspberry Pi 5.
> **Date**: September 2026.

---

## 🧭 1. Executive System Overview

The **Pi-loop Email Intelligence Platform** is a local, privacy-preserving email automation and intelligence daemon. It performs autonomous email triage, spam/noise archiving, executive briefings, follow-up tracking, subscription auditing, and semantic natural language Q&A (`/ask`) over an encrypted local SQLite database.

```
                              EMAIL INGRESS & PROCESSING TOPOLOGY
  +---------------------------------+
  |      deepshah7977@gmail.com     |  (Primary Identity, Advanced Protection Program)
  |   (Auto-forwarding Filter Rule) |  Transports raw RFC822 messages
  +----------------+----------------+
                   |
                   v
  +----------------+----------------+
  |      sl4ught3rcl4y@gmail.com    |  (Operational Processing Mailbox)
  |   (Holds OAuth Tokens & Labels) |  All labels: AI/Category-*, AI/Priority-*, AI/Auto-Archived
  +----------------+----------------+
                   |
                   v (OAuth2 REST API over HTTPS)
  +----------------+-------------------------------------------------------------+
  |  RASPBERRY PI 5 (`192.168.1.92` / `pi5`)                                     |
  |                                                                              |
  |  • `email-agent.timer` (Runs `gmail_agent.py` every 6 hours)                 |
  |  • `email-bot.service` (Runs `bot_service.py` continuous Telegram listener)  |
  |  • `ollama.service`    (Local Ollama: `qwen2.5:3b` + `all-minilm`, 15m idle) |
  |  • SQLite DB: `/home/deepshah08/email-agent/data/emails.db` (WAL Mode)       |
  |                                                                              |
  |  Telegram Bot: `@PiLoopBot` -> Pushes to Chat ID: `955908960`                |
  +------------------------------------------------------------------------------+
```

---

## 🔐 2. Hardware, Access & Credentials Matrix

### Host & Remote Access
* **Target Hardware**: Raspberry Pi 5 Model B (Broadcom BCM2712 Quad-Core Cortex-A76 @ 2.4GHz, **16 GB LPDDR4X RAM**, 128 GB MicroSD).
* **Local IP**: `192.168.1.92` (Static DHCP).
* **SSH Hostname / User**: `deepshah08@192.168.1.92` (configured as SSH alias `pi5`).
* **OpenSSH Multiplexing**: Sockets are active in `~/.ssh/controlmasters/`. Always use persistent control masters for $<25$ms command execution:
  ```bash
  ssh pi5 "<command>"
  ```
* **Remote Application Root**: `/home/deepshah08/email-agent/`
* **Python Virtualenv**: `/home/deepshah08/email-agent/venv/` (Python 3.11/3.12)
* **Local Repository Working Directory**: `/Users/deep/Desktop/DATA ORG/email-agent/`

### Active Credentials & Config Files

| Configuration Item | Location on Pi 5 | Location on Local Mac | Description / Values |
| :--- | :--- | :--- | :--- |
| **Telegram Credentials** | `/home/deepshah08/email-agent/config/.env` | `.../email-agent/config/.env` | Stored in `config/.env`. Read via `cat config/.env`. Contains `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` (`955908960`). |
| **Google Cloud OAuth Client** | `/home/deepshah08/email-agent/credentials/credentials.json` | `.../email-agent/credentials/credentials.json` | Project: `emailreviewer-508419`. Full OAuth client secrets file resides in `credentials/credentials.json`. Read via `cat credentials/credentials.json`. |
| **Active OAuth User Token** | `/home/deepshah08/email-agent/credentials/token.json` | `.../email-agent/credentials/token.json` | Offline refresh token & authorized scopes for `sl4ught3rcl4y@gmail.com`. Refreshed automatically by Google auth library. |
| **Multi-Tenant User Registry** | `/home/deepshah08/email-agent/config/users.json` | `.../email-agent/config/users.json` | Defines tenant IDs (`deep`), priority levels, assigned databases, and Telegram chat mappings. |
| **Gemini Studio API Key** | `/home/deepshah08/email-agent/config/.env` | `.../email-agent/config/.env` | **Pending Addition**: Add `GEMINI_API_KEY="AIzaSy..."` to `config/.env` for Mission 1. |

---

## 🗄️ 3. Database Schema & State Architecture (`emails.db`)

All state is stored in SQLite at `/home/deepshah08/email-agent/data/emails.db` configured with `PRAGMA journal_mode=WAL;` and `PRAGMA busy_timeout=10000;`.

```sql
-- 1. Master Processed Emails Table
CREATE TABLE processed_emails (
    msg_id            TEXT PRIMARY KEY,
    thread_id         TEXT,
    sender            TEXT,
    subject           TEXT,
    priority          TEXT,          -- 'URGENT', 'IMPORTANT', 'NORMAL', 'LOW'
    category          TEXT,          -- 'Work', 'Finance', 'Travel', 'Shopping', 'Newsletter', 'ColdOutreach', 'Other'
    action_needed     INTEGER,       -- 1 or 0
    action_type       TEXT,          -- 'Reply', 'Review', 'Pay', 'Schedule', 'Call', 'None'
    summary           TEXT,
    auto_archived     INTEGER,       -- 1 if removed from INBOX
    status            TEXT DEFAULT 'active', -- 'active', 'pending_action', 'corrected'
    reminded_count    INTEGER DEFAULT 0,
    last_reminded_at  TEXT,
    resolved_at       TEXT,
    processed_at      TEXT DEFAULT (datetime('now')),
    original_recipient TEXT DEFAULT '',
    trackers_blocked  INTEGER DEFAULT 0
);

-- 2. Deterministic O(1) Learned Sender & Domain Rules
CREATE TABLE sender_rules (
    sender_pattern     TEXT PRIMARY KEY, -- Exact email ('user@brand.com') or domain ('@brand.com')
    priority           TEXT,
    category           TEXT,
    action_needed      INTEGER,
    action_type        TEXT,
    auto_archive       INTEGER,
    rule_source        TEXT,             -- 'feedback_learning', 'domain_convergence', 'gemini_teacher'
    updated_at         TEXT DEFAULT (datetime('now'))
);

-- 3. Historical Human Corrections Audit Log
CREATE TABLE user_corrections (
    id                 INTEGER PRIMARY KEY AUTOINCREMENT,
    msg_id             TEXT,
    sender             TEXT,
    subject            TEXT,
    predicted_prio     TEXT,
    corrected_prio     TEXT,
    predicted_cat      TEXT,
    corrected_cat      TEXT,
    predicted_archive  INTEGER,
    corrected_archive  INTEGER,
    corrected_at       TEXT DEFAULT (datetime('now'))
);

-- 4. O(1) Label Hashtable State Tracking
CREATE TABLE email_label_state (
    msg_id             TEXT PRIMARY KEY,
    last_category      TEXT,
    last_priority      TEXT,
    is_archived        INTEGER,
    checksum           TEXT,             -- 'Category:Priority:Archived'
    updated_at         TEXT DEFAULT (datetime('now'))
);

-- 5. Dense Semantic Vector Embeddings (384-dimensional all-minilm)
CREATE TABLE email_embeddings (
    msg_id             TEXT PRIMARY KEY,
    embedding          TEXT,             -- Unit-normalized JSON array of 384 floats
    subject            TEXT,
    sender             TEXT,
    summary            TEXT,
    created_at         TEXT DEFAULT (datetime('now'))
);

-- 6. Full-Text Search FTS5 Virtual Table (Lexical Search)
CREATE VIRTUAL TABLE emails_fts USING fts5(
    msg_id UNINDEXED, sender, subject, summary,
    content='processed_emails', content_rowid='rowid'
);

-- 7. Subscriptions & Recurring Bills
CREATE TABLE subscriptions (
    vendor             TEXT PRIMARY KEY,
    amount             REAL,
    frequency          TEXT DEFAULT 'monthly',
    last_billed_at     TEXT,
    next_renewal_at    TEXT,
    last_msg_id        TEXT,
    category           TEXT DEFAULT 'Subscription',
    status             TEXT DEFAULT 'active',
    detected_at        TEXT DEFAULT (datetime('now'))
);
```

---

## 🤖 4. Local LLM & Ollama Runtime Configuration

* **Dynamic RAM Residency & CPU Throttling**:
  * Configured via systemd drop-in override: `/etc/systemd/system/ollama.service.d/override.conf`:
    ```ini
    [Service]
    Environment="OLLAMA_KEEP_ALIVE=15m"
    Nice=10
    CPUQuota=250%
    ```
  * **15-Minute RAM Keep-Alive**: Python calls in `email_classifier.py`, `bot_service.py`, and `vector_store.py` send `"keep_alive": "15m"`. Models stay warm in RAM for 15 minutes after any query for instant response, then automatically evict to free RAM down to ~43 MB.
  * **250% CPU Quota & Pi-hole FTL Shield (CRITICAL)**:
    * *Audit Finding (Sept 13, 2026)*: Un-throttled Ollama was observed consuming **338% CPU** across all 4 cores during batch email processing, causing 15-minute system load averages to spike to 4.2 and triggering Pi-hole FTL load warnings (`WARNING: Long-term load larger than number of processors: 4.2 > 4`).
    * *Hard Ceiling*: `CPUQuota=250%` restricts Ollama to a maximum of 2.5 CPU cores, strictly reserving 1.5 cores for Pi-hole v6 FTL (`Nice=-10`), Unbound recursive DNS (`127.0.0.1:5335`), and kernel network interrupts.
    * *Process Priority*: `Nice=10` ensures background AI model generation yields CPU cycles to DNS lookups and DHCP handshakes.
* **Models**:
  1. `qwen2.5:3b` (Q4_K_M, 1.8 GB disk, ~2.4 GB RAM when warm): Tier-4 advisory triage and RAG QA synthesis.
  2. `all-minilm` (44 MB disk, ~120 MB RAM when warm): 384-dimensional dense semantic vector embeddings.


---

## 🚀 5. The Mission: Two Major Enhancements for Codex

The core platform runs smoothly, but requires two major architectural elevations:

---

### MISSION 1: The Recursive Learning Pipeline (Gemini as Authoritative Teacher)

#### The Problem
Emails with dollar figures or receipts frequently trigger the "Finance" category when they are actually retail shopping purchases (e.g. Under Armour clothing receipt), developer tool invoices (AWS bill), or newsletters discussing market prices. The local 3B model lacks deep world context to reliably distinguish these nuances.

#### The Solution: Asynchronous Teacher-Student Distillation
Use Google AI Studio's Gemini API (e.g. `gemini-1.5-flash` or `gemini-2.0-flash`) as the high-reasoning, authoritative Teacher/Auditor.

#### Architecture Blueprint:
1. **Gemini Teacher Client (`gemini_teacher.py`)**:
   - Create a dedicated module using `google-generativeai` or raw HTTPS REST requests to `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent`.
   - Read `GEMINI_API_KEY` from `config/.env`.
2. **Ambiguity Audit Trigger**:
   - Following each 6-hour batch (or on demand), audit emails classified into ambiguous categories (`Finance`, `Other`, or emails with low confidence).
3. **Ground-Truth Taxonomy Prompt**:
   - Pass email headers and body (first 1,500 chars) to Gemini.
   - Instruct Gemini:
     > *"You are the authoritative email classifier. Choose strictly from: [Work, Finance, Travel, Shopping, Newsletter, Personal, ColdOutreach]. If this is an e-commerce purchase, clothing item, order confirmation, or commercial retail receipt, it is Shopping, NOT Finance. Return strictly JSON: `{"category": "...", "priority": "...", "reason": "..."}`."*
4. **Auto-Reconciliation in Gmail**:
   - If Gemini's classification disagrees with the local prediction:
     a) Call `service.users().messages().modify()` to remove the old label (e.g. `AI/Category-Finance`) and apply the corrected label (e.g. `AI/Category-Shopping`).
     b) Update `processed_emails.category` in SQLite.
     c) Insert into new SQLite table `model_mistakes`:
        ```sql
        CREATE TABLE IF NOT EXISTS model_mistakes (
            msg_id TEXT PRIMARY KEY,
            sender TEXT,
            subject TEXT,
            slm_predicted TEXT,
            gemini_authoritative TEXT,
            reasoning TEXT,
            audited_at TEXT DEFAULT (datetime('now'))
        );
        ```
     d) Insert/update `sender_rules` with `rule_source = 'gemini_teacher'` so future emails from this sender/domain are classified correctly in $O(1)$ time without calling any LLM.
5. **Recursive Few-Shot Distillation into Qwen 2.5**:
   - Update `get_recent_corrections()` in `gmail_agent.py` to pull the top 3 most recent entries from `model_mistakes` and inject them as few-shot examples into Qwen 2.5's prompt during subsequent runs.

---

### MISSION 2: Live Telegram Interactive Feedback & Persona Testing

#### The Problem
Current test cases are purely synthetic (asserting code doesn't crash). They do not measure how a real human experiences the bot, nor do they provide a zero-friction interface for the user to correct classifications in real time.

#### Part A: Interactive Inline Telegram Buttons (`bot_service.py`)
Telegram Bot API supports `InlineKeyboardMarkup` and callback queries.
1. **Interactive Email Briefings (`/digest`)**:
   - Under each surfaced email in the briefing, attach an inline button: `[ 🏷️ Move Label ]`.
   - Tapping the button responds with an inline keyboard menu:
     ```
     [ 🛍️ Shopping ]  [ 💼 Work ]      [ 💳 Finance ]
     [ ✈️ Travel   ]  [ 📰 Newsletter] [ 🚫 Cold Pitch ]
     ```
   - In `bot_service.py`, handle `callback_query` updates:
     1) Extract `msg_id` and chosen `category`.
     2) Call Gmail API to swap the label in the user's live Gmail account.
     3) Update `processed_emails` and `sender_rules` in SQLite.
     4) Call `bot.edit_message_text` to update the Telegram message in-place:
        *"✅ Moved to Shopping and learned permanent rule for @brand.com!"*
2. **Interactive Answer Rating for `/ask`**:
   - Below every `/ask` response, add two inline buttons: `[ 👍 Accurate ]` `[ 👎 Bad Context ]`.
   - If user taps `👎`, log the question, retrieved sources, and context to `rag_feedback_log` in SQLite for automated failure analysis.

#### Part B: Automated Persona UX Test Suite (`test_user_experience.py`)
Create a test runner simulating real human user inquiries:
1. Define 10 diverse user personas/queries:
   - **Executive**: `/ask any urgent deadlines or payments due today?`
   - **Shopper**: `/ask did my sneakers or packages ship?`
   - **Developer**: `/ask any emails on system design or architecture?`
   - **Finance**: `/ask what was my monthly statement from Chase or Amex?`
   - **Negative**: `/ask did John send the contract?` (Must return *"No emails found"*, not hallucinate).
2. Run each query through `hybrid_search()` and local `qwen2.5:3b`.
3. Feed the retrieved sources and generated answer to **Gemini as the Evaluator Judge**:
   - Score: **Faithfulness (0-100%)**, **Relevance (0-100%)**, **Completeness (0-100%)**.
   - Output an Executive Persona Report highlighting any retrieval gaps.

---

## 🛠️ 6. Runbook & Developer Commands

### 1. SSH into Pi 5
```bash
ssh pi5
```

### 2. Inspect Running Services
```bash
# Telegram interactive bot daemon
sudo systemctl status email-bot.service

# 6-hour ingestion timer
systemctl status email-agent.timer

# Ollama local LLM daemon
systemctl status ollama.service

# Check active model in RAM and idle countdown
ollama ps
```

### 3. Restarting Services
```bash
# Restart Telegram bot after code changes
sudo systemctl restart email-bot.service

# Manually trigger a 6-hour ingestion batch run
sudo systemctl start email-agent.service

# View live bot logs
journalctl -u email-bot.service -f
```

### 4. Running Pipeline Tests on Pi 5
```bash
cd /home/deepshah08/email-agent
./venv/bin/python test_accuracy_pipeline.py
```

### 5. Syncing Changes from Mac to Pi 5
From `/Users/deep/Desktop/DATA ORG/email-agent/`:
```bash
rsync -avz --exclude '__pycache__' --exclude 'data' --exclude 'logs' --exclude 'credentials' \
  ./ pi5:/home/deepshah08/email-agent/
```

### 6. SQLite Direct Inspection on Pi 5
```bash
python3 -c "
import sqlite3
conn = sqlite3.connect('/home/deepshah08/email-agent/data/emails.db')
c = conn.cursor()
print('Total Emails:', c.execute('SELECT count(*) FROM processed_emails').fetchone()[0])
print('Learned Rules:', c.execute('SELECT count(*) FROM sender_rules').fetchone()[0])
print('Vector Embeddings:', c.execute('SELECT count(*) FROM email_embeddings').fetchone()[0])
print('Categories:', c.execute('SELECT category, count(*) FROM processed_emails GROUP BY category').fetchall())
"
```

---

## 🛡️ 7. Hard Guardrails & Operational Constraints (Zero Host Mutation)

1. **Zero Host Mutation**: Never install packages globally on the Pi 5 OS (`apt install`). All dependencies must stay strictly inside `/home/deepshah08/email-agent/venv/`.
2. **Network & DNS Safety**: Pi 5 runs alongside Pi-hole DNS infrastructure. Never modify core network routing, bind to `0.0.0.0:53`, or introduce network timeouts that stall whole-home DNS.
3. **Database Concurrency**: Always access SQLite through `get_db_connection(db_path)` which enforces WAL mode and a 10,000ms busy timeout to prevent locking conflicts between Telegram commands and batch ingestion.
4. **Safety Invariants**: Never allow an email with priority `URGENT` or `IMPORTANT` to have `auto_archived = 1`. This invariant is monitored by `background_evaluator.py`.
5. **CPU Throttling & Pi-hole Protection**: Never remove or increase `CPUQuota=250%` or `Nice=10` from `/etc/systemd/system/ollama.service.d/override.conf`, and never configure Ollama/llama-server to utilize 4 full CPU threads. The primary Pi 5 node handles whole-home DNS/DHCP (`pihole-FTL`); background AI triage must never starve DNS resolution of CPU cycles. `email-agent.service` is also throttled (`CPUQuota=50%`, `Nice=15`, `MemoryMax=1G`).

