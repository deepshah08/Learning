"""
gmail_agent.py
Pi-loop Email Intelligence Agent — Gmail API + Pipeline Orchestrator
Fetches unread Gmail, classifies with local LLM, applies labels/archives,
tracks actionable emails for reminders, and learns from user label corrections.
Supports pluggable multi-user setups (Deep, Pranali, etc.).
"""

import argparse
import base64
import html
import json
import logging
import os
import re
import sqlite3
import sys
import time
import resource
from datetime import datetime, timedelta, timezone
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from email_classifier import classify_email, EmailClassification
from notifier import send_telegram_digest, send_urgent_alert

def with_retry(max_attempts: int = 3, base_delay: float = 1.0):
    """Exponential backoff decorator for Gmail API calls on transient rate limits."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except HttpError as e:
                    if e.resp.status in (429, 500, 502, 503, 504) and attempt < max_attempts:
                        delay = base_delay * (2 ** (attempt - 1))
                        logging.warning(f"Gmail API HTTP {e.resp.status}, retrying in {delay:.1f}s (attempt {attempt}/{max_attempts})...")
                        time.sleep(delay)
                    else:
                        raise
        return wrapper
    return decorator

# ── Base Directory & Scopes ───────────────────────────────────────────────────

BASE_DIR = Path(__file__).parent

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.modify",
]

MAX_PER_RUN = 50

# ── Logging ───────────────────────────────────────────────────────────────────

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "agent.log"

_log_handlers: list[logging.Handler] = [logging.StreamHandler(sys.stdout)]
# systemd already appends stdout/stderr to agent.log. Attaching a second file
# handler in that environment duplicates every line and doubles log churn.
if not os.getenv("INVOCATION_ID"):
    _log_handlers.insert(0, logging.FileHandler(LOG_FILE))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=_log_handlers,
)
logger = logging.getLogger(__name__)

# ── Multi-User Profile Resolver ───────────────────────────────────────────────

def get_user_profile(user_id: str = "deep") -> dict:
    """
    Resolve paths for a given user profile.
    Allows isolated credentials, databases, and config per user.
    """
    user_id = user_id.lower().strip()
    creds_dir = BASE_DIR / "credentials"
    data_dir  = BASE_DIR / "data"
    conf_dir  = BASE_DIR / "config"

    creds_dir.mkdir(parents=True, exist_ok=True)
    data_dir.mkdir(parents=True, exist_ok=True)
    conf_dir.mkdir(parents=True, exist_ok=True)

    # Token file: per-user or default fallback
    user_token = creds_dir / f"{user_id}_token.json"
    default_token = creds_dir / "token.json"
    token_file = user_token if user_token.exists() else (default_token if user_id in ("deep", "default") else user_token)

    # Database: per-user or default
    db_file = data_dir / f"{user_id}_emails.db" if user_id not in ("deep", "default") else data_dir / "emails.db"

    # Env file for notifications
    user_env = conf_dir / f"{user_id}.env"
    default_env = conf_dir / ".env"
    env_file = user_env if user_env.exists() else default_env

    client_secrets = creds_dir / "credentials.json"

    return {
        "user_id": user_id,
        "token_file": token_file,
        "client_secrets": client_secrets,
        "db_file": db_file,
        "env_file": env_file,
        "label": user_id.capitalize(),
    }

# ── Auth ──────────────────────────────────────────────────────────────────────

def get_gmail_service(profile: dict):
    """
    Build an authenticated Gmail API service for the specified user profile.
    Silent token refresh on every automated run.
    Fails closed in headless environments instead of hanging on browser auth.
    """
    token_file = profile["token_file"]
    creds_file = profile["client_secrets"]
    creds = None

    if token_file.exists():
        creds = Credentials.from_authorized_user_file(str(token_file), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            logger.info(f"[{profile['label']}] Refreshing expired access token...")
            try:
                creds.refresh(Request())
            except Exception as e:
                logger.error(f"[{profile['label']}] Token refresh failed: {e}")
                raise RuntimeError(
                    f"[{profile['label']}] OAuth token expired/revoked and refresh failed: {e}. "
                    "Run auth_setup.py interactively via SSH to re-authenticate."
                )
        else:
            # Check if running in headless/unattended environment
            is_headless = not os.isatty(0) or os.getenv("INVOCATION_ID") is not None
            if is_headless:
                raise RuntimeError(
                    f"[{profile['label']}] Headless environment detected: cannot launch browser auth. "
                    "Run auth_setup.py interactively via SSH to generate credentials."
                )

            if not creds_file.exists():
                raise FileNotFoundError(
                    f"credentials.json not found at {creds_file}. Download it from Google Cloud Console."
                )
            logger.info(f"[{profile['label']}] First-time auth: launch browser...")
            flow = InstalledAppFlow.from_client_secrets_file(str(creds_file), SCOPES)
            creds = flow.run_local_server(port=0, access_type="offline", prompt="consent")

        token_file.parent.mkdir(parents=True, exist_ok=True)
        token_file.write_text(creds.to_json())
        logger.info(f"[{profile['label']}] Token saved to {token_file}")

    return build("gmail", "v1", credentials=creds, cache_discovery=False)


# ── Label Management ──────────────────────────────────────────────────────────

AI_LABELS = {
    "AI/Processed":            "labelShow",
    "AI/Needs-Action":         "labelShow",   # One-stop inbox view for pending tasks
    "AI/Action-Done":          "labelHide",   # Cleared items
    "AI/Priority-Urgent":      "labelShow",
    "AI/Priority-Important":   "labelShow",
    "AI/Category-Work":        "labelShow",
    "AI/Category-Personal":    "labelShow",
    "AI/Category-Finance":     "labelShow",
    "AI/Category-Travel":      "labelShow",
    "AI/Category-Newsletter":  "labelShow",
    "AI/Category-Shopping":    "labelShow",
    "AI/Category-ColdOutreach":"labelShow",
    "AI/Auto-Archived":        "labelHide",   # Tracks auto-filtered items
}

def ensure_labels(service) -> dict[str, str]:
    """Create missing AI labels and return name→id mapping."""
    existing = {
        lbl["name"]: lbl["id"]
        for lbl in service.users().labels().list(userId="me").execute().get("labels", [])
    }

    label_ids: dict[str, str] = {}
    for name, visibility in AI_LABELS.items():
        if name in existing:
            label_ids[name] = existing[name]
        else:
            created = service.users().labels().create(
                userId="me",
                body={
                    "name": name,
                    "labelListVisibility": visibility,
                    "messageListVisibility": "show",
                },
            ).execute()
            label_ids[name] = created["id"]
            logger.info(f"Created label: {name}")

    return label_ids

# ── SQLite Database Architecture ──────────────────────────────────────────────

def get_db_connection(db_path: Path) -> sqlite3.Connection:
    """Produce SQLite connection with busy timeout and WAL configuration."""
    conn = sqlite3.connect(db_path, timeout=15.0)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA busy_timeout=10000;")
    return conn


def init_db(db_path: Path):
    """Initialize tables for processing, reminders, feedback learning, FTS5 search, and sender rules with WAL concurrency."""
    conn = get_db_connection(db_path)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS processed_emails (
            msg_id            TEXT PRIMARY KEY,
            thread_id         TEXT,
            sender            TEXT,
            subject           TEXT,
            priority          TEXT,
            category          TEXT,
            action_needed     INTEGER,
            action_type       TEXT,
            summary           TEXT,
            auto_archived     INTEGER,
            status            TEXT DEFAULT 'active',
            reminded_count    INTEGER DEFAULT 0,
            last_reminded_at  TEXT,
            resolved_at       TEXT,
            processed_at      TEXT DEFAULT (datetime('now')),
            original_recipient TEXT DEFAULT ''
        )
    """)

    # Safe column migrations if table already existed
    cols = [col[1] for col in conn.execute("PRAGMA table_info(processed_emails)").fetchall()]
    if "original_recipient" not in cols:
        conn.execute("ALTER TABLE processed_emails ADD COLUMN original_recipient TEXT DEFAULT '';")
    if "trackers_blocked" not in cols:
        conn.execute("ALTER TABLE processed_emails ADD COLUMN trackers_blocked INTEGER DEFAULT 0;")

    # High-performance B-tree compound indexes
    conn.execute("CREATE INDEX IF NOT EXISTS idx_processed_pending ON processed_emails(action_needed, status, processed_at);")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_processed_sender ON processed_emails(sender);")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_processed_thread ON processed_emails(thread_id);")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_processed_category ON processed_emails(category);")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_processed_priority ON processed_emails(priority);")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_processed_recipient ON processed_emails(original_recipient);")

    # Subscriptions & Recurring Bills tracking table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            vendor             TEXT PRIMARY KEY,
            amount             REAL,
            frequency          TEXT DEFAULT 'monthly',
            last_billed_at     TEXT,
            next_renewal_at    TEXT,
            last_msg_id        TEXT,
            category           TEXT DEFAULT 'Subscription',
            status             TEXT DEFAULT 'active',
            detected_at        TEXT DEFAULT (datetime('now'))
        )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_sub_renewal ON subscriptions(next_renewal_at);")

    # Feedback loop: records when user corrects the model's classification in Gmail
    conn.execute("""
        CREATE TABLE IF NOT EXISTS user_corrections (
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
        )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_corrections_cat ON user_corrections(corrected_cat);")

    # Teacher/student distillation: authoritative cloud audits are kept separate
    # from human corrections so their provenance remains explicit.
    conn.execute("""
        CREATE TABLE IF NOT EXISTS model_mistakes (
            msg_id                 TEXT PRIMARY KEY,
            sender                 TEXT,
            subject                TEXT,
            slm_predicted          TEXT,
            gemini_authoritative   TEXT,
            reasoning              TEXT,
            audited_at             TEXT DEFAULT (datetime('now'))
        )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_model_mistakes_audited ON model_mistakes(audited_at);")

    # Telegram RAG answers are recorded before delivery and rated later through
    # callback buttons. Context stays local in SQLite.
    conn.execute("""
        CREATE TABLE IF NOT EXISTS rag_feedback_log (
            id                 INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id            TEXT NOT NULL,
            chat_id            TEXT NOT NULL,
            question           TEXT NOT NULL,
            answer             TEXT NOT NULL,
            sources            TEXT NOT NULL DEFAULT '[]',
            context            TEXT NOT NULL DEFAULT '',
            match_count        INTEGER NOT NULL DEFAULT 0,
            synthesis_ms       INTEGER NOT NULL DEFAULT 0,
            over_budget        INTEGER NOT NULL DEFAULT 0,
            rating             TEXT,
            created_at         TEXT DEFAULT (datetime('now')),
            rated_at           TEXT
        )
    """)
    rag_columns = {row[1] for row in conn.execute("PRAGMA table_info(rag_feedback_log)")}
    for name, definition in (
        ("match_count", "INTEGER NOT NULL DEFAULT 0"),
        ("synthesis_ms", "INTEGER NOT NULL DEFAULT 0"),
        ("over_budget", "INTEGER NOT NULL DEFAULT 0"),
    ):
        if name not in rag_columns:
            conn.execute(f"ALTER TABLE rag_feedback_log ADD COLUMN {name} {definition}")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_rag_feedback_rating ON rag_feedback_log(rating, created_at);")

    # Durable run/resource ledger. A row is inserted before external calls and
    # checkpointed through the run, so a systemd kill remains visible as an
    # interrupted run instead of disappearing from operational history.
    conn.execute("""
        CREATE TABLE IF NOT EXISTS pipeline_runs (
            id                     INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id                TEXT NOT NULL,
            started_at             TEXT DEFAULT (datetime('now')),
            finished_at            TEXT,
            status                 TEXT NOT NULL DEFAULT 'running',
            emails_found           INTEGER DEFAULT 0,
            emails_processed       INTEGER DEFAULT 0,
            errors                 INTEGER DEFAULT 0,
            fallback_count         INTEGER DEFAULT 0,
            classification_seconds REAL DEFAULT 0,
            max_classify_seconds   REAL DEFAULT 0,
            gemini_seconds         REAL DEFAULT 0,
            gemini_audited         INTEGER DEFAULT 0,
            gemini_errors          INTEGER DEFAULT 0,
            gemini_deferred        INTEGER DEFAULT 0,
            duration_seconds       REAL DEFAULT 0,
            max_rss_mb             REAL DEFAULT 0,
            temperature_c          REAL,
            overages               TEXT DEFAULT '[]',
            notes                  TEXT DEFAULT ''
        )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_pipeline_runs_started ON pipeline_runs(started_at);")

    # Learned sender rules: explicit overrides that bypass or guide the model
    conn.execute("""
        CREATE TABLE IF NOT EXISTS sender_rules (
            sender_pattern     TEXT PRIMARY KEY,
            priority           TEXT,
            category           TEXT,
            action_needed      INTEGER,
            action_type        TEXT,
            auto_archive       INTEGER,
            rule_source        TEXT DEFAULT 'feedback_learning',
            updated_at         TEXT DEFAULT (datetime('now'))
        )
    """)

    # VIP frequency tracking
    conn.execute("""
        CREATE TABLE IF NOT EXISTS sender_stats (
            email_address      TEXT PRIMARY KEY,
            incoming_count     INTEGER DEFAULT 0,
            last_seen          TEXT
        )
    """)

    # SQLite FTS5 Virtual Table for sub-millisecond full-text search
    conn.execute("""
        CREATE VIRTUAL TABLE IF NOT EXISTS emails_fts USING fts5(
            msg_id UNINDEXED,
            sender,
            subject,
            summary,
            content='processed_emails',
            content_rowid='rowid'
        );
    """)

    # Triggers to keep FTS5 synchronized automatically on INSERT/UPDATE/DELETE
    conn.execute("""
        CREATE TRIGGER IF NOT EXISTS processed_emails_ai AFTER INSERT ON processed_emails BEGIN
            INSERT INTO emails_fts(rowid, msg_id, sender, subject, summary)
            VALUES (new.rowid, new.msg_id, new.sender, new.subject, new.summary);
        END;
    """)
    conn.execute("""
        CREATE TRIGGER IF NOT EXISTS processed_emails_ad AFTER DELETE ON processed_emails BEGIN
            INSERT INTO emails_fts(emails_fts, rowid, msg_id, sender, subject, summary)
            VALUES('delete', old.rowid, old.msg_id, old.sender, old.subject, old.summary);
        END;
    """)
    conn.execute("""
        CREATE TRIGGER IF NOT EXISTS processed_emails_au AFTER UPDATE ON processed_emails BEGIN
            INSERT INTO emails_fts(emails_fts, rowid, msg_id, sender, subject, summary)
            VALUES('delete', old.rowid, old.msg_id, old.sender, old.subject, old.summary);
            INSERT INTO emails_fts(rowid, msg_id, sender, subject, summary)
            VALUES (new.rowid, new.msg_id, new.sender, new.subject, new.summary);
        END;
    """)

    # One-time FTS backfill for existing rows
    fts_count = conn.execute("SELECT COUNT(*) FROM emails_fts").fetchone()[0]
    total_processed = conn.execute("SELECT COUNT(*) FROM processed_emails").fetchone()[0]
    if total_processed > 0 and fts_count == 0:
        conn.execute("""
            INSERT INTO emails_fts(rowid, msg_id, sender, subject, summary)
            SELECT rowid, msg_id, sender, subject, summary FROM processed_emails;
        """)

    # O(1) Label state hashtable for fast change detection and delta audits
    conn.execute("""
        CREATE TABLE IF NOT EXISTS email_label_state (
            msg_id            TEXT PRIMARY KEY,
            last_category     TEXT,
            last_priority     TEXT,
            is_archived       INTEGER,
            checksum          TEXT,
            updated_at        TEXT DEFAULT (datetime('now'))
        );
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_state_cat ON email_label_state(last_category);")

    # Initialize dense vector embeddings table
    try:
        from vector_store import init_vector_tables
        init_vector_tables(conn)
    except Exception as e:
        logger.debug(f"Vector tables init warning: {e}")

    conn.commit()
    conn.close()


def _resource_snapshot() -> dict:
    """Read lightweight process/thermal metrics without new dependencies."""
    rss = float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    # Linux reports KiB; macOS reports bytes.
    rss_mb = rss / (1024.0 if sys.platform.startswith("linux") else 1024.0 * 1024.0)
    temperature_c = None
    thermal_path = Path("/sys/class/thermal/thermal_zone0/temp")
    if thermal_path.exists():
        try:
            temperature_c = int(thermal_path.read_text().strip()) / 1000.0
        except (OSError, ValueError):
            pass
    return {"max_rss_mb": round(rss_mb, 2), "temperature_c": temperature_c}


def _env_float(name: str, default: float) -> float:
    try:
        return float(os.getenv(name, str(default)))
    except ValueError:
        logger.warning("Invalid %s; using %.1f", name, default)
        return default


def _start_pipeline_run(db_path: Path, user_id: str) -> int:
    conn = get_db_connection(db_path)
    conn.execute("""
        UPDATE pipeline_runs
        SET status = 'interrupted', finished_at = datetime('now'),
            notes = CASE WHEN notes = '' THEN 'Previous run did not reach completion' ELSE notes END
        WHERE user_id = ? AND status = 'running'
    """, (user_id,))
    cursor = conn.execute(
        "INSERT INTO pipeline_runs (user_id, status) VALUES (?, 'running')",
        (user_id,),
    )
    run_id = int(cursor.lastrowid)
    conn.commit()
    conn.close()
    return run_id


_PIPELINE_RUN_FIELDS = {
    "status", "emails_found", "emails_processed", "errors", "fallback_count",
    "classification_seconds", "max_classify_seconds", "gemini_seconds",
    "gemini_audited", "gemini_errors", "gemini_deferred", "duration_seconds",
    "max_rss_mb", "temperature_c", "overages", "notes", "finished_at",
}


def _update_pipeline_run(db_path: Path, run_id: int, **values) -> None:
    values = {key: value for key, value in values.items() if key in _PIPELINE_RUN_FIELDS}
    if not values:
        return
    assignments = ", ".join(f"{key} = ?" for key in values)
    conn = get_db_connection(db_path)
    conn.execute(
        f"UPDATE pipeline_runs SET {assignments} WHERE id = ?",
        (*values.values(), run_id),
    )
    conn.commit()
    conn.close()

# ── Feedback Loop: Query Learned Rules & Few-Shot Examples ────────────────────

def get_sender_override(sender: str, db_path: Path) -> dict | None:
    """Check if the user has an explicit or learned rule for this sender."""
    conn = get_db_connection(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Extract email and domain hierarchy
    match = re.search(r"<(.+?)>", sender)
    email_addr = match.group(1).lower() if match else sender.lower()
    domain = email_addr.split("@")[-1] if "@" in email_addr else ""
    domain_parts = domain.split(".")
    root_domain = ".".join(domain_parts[-2:]) if len(domain_parts) >= 2 else domain

    # Check exact email first, then @domain, then @root_domain
    cursor.execute("""
        SELECT * FROM sender_rules
        WHERE sender_pattern = ? OR sender_pattern = ? OR sender_pattern = ?
        ORDER BY CASE 
            WHEN sender_pattern = ? THEN 1 
            WHEN sender_pattern = ? THEN 2 
            ELSE 3 
        END
        LIMIT 1
    """, (email_addr, f"@{domain}", f"@{root_domain}", email_addr, f"@{domain}"))
    row = cursor.fetchone()
    conn.close()

    if row:
        return dict(row)
    return None


def get_recent_corrections(db_path: Path, limit: int = 4) -> list[dict]:
    """
    Retrieve diverse user corrections across different categories
    to provide the highest-information few-shot signal into Ollama.
    """
    conn = get_db_connection(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    rows: list[dict] = []
    # Pull a slightly wider recent window, then retain diverse categories. This
    # avoids SQLite's undefined GROUP BY row selection and mixes human and
    # teacher feedback in true recency order.
    cursor.execute("""
        SELECT sender, subject, priority, category, auto_archive, learned_at
        FROM (
            SELECT sender, subject,
                   corrected_prio AS priority,
                   corrected_cat AS category,
                   corrected_archive AS auto_archive,
                   corrected_at AS learned_at
            FROM user_corrections
            UNION ALL
            SELECT sender, subject,
                   COALESCE((SELECT priority FROM processed_emails p WHERE p.msg_id = m.msg_id), 'NORMAL'),
                   gemini_authoritative,
                   COALESCE((SELECT auto_archived FROM processed_emails p WHERE p.msg_id = m.msg_id), 0),
                   audited_at
            FROM model_mistakes m
        )
        ORDER BY learned_at DESC
        LIMIT ?
    """, (max(limit * 4, limit),))
    seen_categories: set[str] = set()
    for row in cursor.fetchall():
        item = dict(row)
        if item["category"] in seen_categories:
            continue
        seen_categories.add(item["category"])
        item.pop("learned_at", None)
        rows.append(item)
        if len(rows) >= limit:
            break
    conn.close()
    return rows

# ── Feedback Loop: Detect Manual User Changes in Gmail ────────────────────────

def sync_user_feedback(service, db_path: Path, label_ids: dict[str, str]) -> list[str]:
    """
    Sync back: Efficiently query Gmail for user label modifications and unarchived emails.
    Uses target label searches (O(1) queries instead of O(N) message fetches).
    Detects corrections across the entire mailbox regardless of ingestion order,
    saves to user_corrections, updates sender_rules, and marks processed_emails as corrected.
    """
    learned_notes: list[str] = []
    conn = get_db_connection(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 1. Category label changes
    categories = ["Shopping", "Work", "Finance", "Travel", "Newsletter", "ColdOutreach"]
    for cat in categories:
        q = f"label:AI-Category-{cat}"
        try:
            res = service.users().messages().list(userId="me", q=q, maxResults=50).execute()
            messages = res.get("messages", [])
        except Exception as e:
            logger.debug(f"Label query error {cat}: {e}")
            continue

        for m in messages:
            msg_id = m["id"]
            row = cursor.execute("""
                SELECT sender, subject, priority, category, auto_archived
                FROM processed_emails WHERE msg_id = ?
            """, (msg_id,)).fetchone()

            if row and row["category"] != cat:
                sender = row["sender"]
                subject = row["subject"]
                pred_prio = row["priority"]
                pred_cat = row["category"]
                pred_arch = bool(row["auto_archived"])
                corr_cat = cat

                note = f"Category changed: {sender[:35]} -> {cat}"
                learned_notes.append(note)
                logger.info(f"💡 Detected user correction for '{subject[:50]}': {pred_cat} -> {cat}")

                # Save to user_corrections
                cursor.execute("""
                    INSERT INTO user_corrections
                    (msg_id, sender, subject, predicted_prio, corrected_prio,
                     predicted_cat, corrected_cat, predicted_archive, corrected_archive)
                    VALUES (?,?,?,?,?,?,?,?,?)
                """, (msg_id, sender, subject, pred_prio, pred_prio,
                      pred_cat, corr_cat, int(pred_arch), int(pred_arch)))

                # Update sender_rules so this sender is permanently adapted
                match = re.search(r"<(.+?)>", sender)
                email_addr = match.group(1).lower() if match else sender.lower()
                cursor.execute("""
                    INSERT OR REPLACE INTO sender_rules
                    (sender_pattern, priority, category, action_needed, action_type, auto_archive, rule_source, updated_at)
                    VALUES (?, ?, ?, ?, 'None', ?, 'feedback_learning', datetime('now'))
                """, (email_addr, pred_prio, corr_cat, int(pred_prio in ("URGENT", "IMPORTANT")), int(pred_arch)))

                # Check domain-level convergence
                domain = email_addr.split("@")[-1] if "@" in email_addr else ""
                domain_parts = domain.split(".")
                root_domain = ".".join(domain_parts[-2:]) if len(domain_parts) >= 2 else domain
                if root_domain:
                    domain_matches = cursor.execute("""
                        SELECT COUNT(*) FROM sender_rules 
                        WHERE sender_pattern LIKE ? AND category = ?
                    """, (f"%@{root_domain}", corr_cat)).fetchone()[0]
                    if domain_matches >= 2:
                        cursor.execute("""
                            INSERT OR REPLACE INTO sender_rules
                            (sender_pattern, priority, category, action_needed, action_type, auto_archive, rule_source, updated_at)
                            VALUES (?, ?, ?, ?, 'None', ?, 'domain_convergence', datetime('now'))
                        """, (f"@{root_domain}", pred_prio, corr_cat, int(pred_prio in ("URGENT", "IMPORTANT")), int(pred_arch)))
                        logger.info(f"🎯 Domain rule converged: @{root_domain} -> {corr_cat} (supported by {domain_matches} sender corrections)")

                # Update the processed_emails entry so we don't repeat
                cursor.execute("""
                    UPDATE processed_emails
                    SET category = ?, status = 'corrected'
                    WHERE msg_id = ?
                """, (corr_cat, msg_id))

                # Update O(1) label state hashtable
                cursor.execute("""
                    INSERT OR REPLACE INTO email_label_state
                    (msg_id, last_category, last_priority, is_archived, checksum, updated_at)
                    VALUES (?, ?, ?, ?, ?, datetime('now'))
                """, (msg_id, corr_cat, pred_prio, int(pred_arch), f"{corr_cat}:{pred_prio}:{int(pred_arch)}"))

    # 2. Unarchived emails (moved back to INBOX)
    try:
        res = service.users().messages().list(userId="me", q="label:INBOX label:AI-Auto-Archived", maxResults=50).execute()
        for m in res.get("messages", []):
            msg_id = m["id"]
            row = cursor.execute("""
                SELECT sender, subject, priority, category, auto_archived
                FROM processed_emails WHERE msg_id = ?
            """, (msg_id,)).fetchone()
            if row and row["auto_archived"] == 1:
                sender = row["sender"]
                subject = row["subject"]
                pred_prio = row["priority"]
                pred_cat = row["category"]
                corr_prio = "IMPORTANT" if pred_prio == "LOW" else pred_prio

                note = f"Unarchived: {sender[:35]} (now Kept in Inbox)"
                learned_notes.append(note)
                logger.info(f"💡 Detected unarchived correction for '{subject[:50]}'")

                cursor.execute("""
                    INSERT INTO user_corrections
                    (msg_id, sender, subject, predicted_prio, corrected_prio,
                     predicted_cat, corrected_cat, predicted_archive, corrected_archive)
                    VALUES (?,?,?,?,?,?,?,?,?)
                """, (msg_id, sender, subject, pred_prio, corr_prio,
                      pred_cat, pred_cat, 1, 0))

                match = re.search(r"<(.+?)>", sender)
                email_addr = match.group(1).lower() if match else sender.lower()
                cursor.execute("""
                    INSERT OR REPLACE INTO sender_rules
                    (sender_pattern, priority, category, action_needed, action_type, auto_archive, rule_source, updated_at)
                    VALUES (?, ?, ?, ?, 'None', 0, 'feedback_learning', datetime('now'))
                """, (email_addr, corr_prio, pred_cat, int(corr_prio in ("URGENT", "IMPORTANT"))))

                cursor.execute("""
                    UPDATE processed_emails
                    SET priority = ?, auto_archived = 0, status = 'corrected'
                    WHERE msg_id = ?
                """, (corr_prio, msg_id))
    except Exception as e:
        logger.debug(f"Unarchive query check note: {e}")

    # 3. Priority escalation to URGENT
    try:
        res = service.users().messages().list(userId="me", q="label:AI-Priority-Urgent", maxResults=50).execute()
        for m in res.get("messages", []):
            msg_id = m["id"]
            row = cursor.execute("""
                SELECT sender, subject, priority, category, auto_archived
                FROM processed_emails WHERE msg_id = ?
            """, (msg_id,)).fetchone()
            if row and row["priority"] != "URGENT":
                sender = row["sender"]
                subject = row["subject"]
                pred_prio = row["priority"]
                pred_cat = row["category"]
                pred_arch = bool(row["auto_archived"])

                note = f"Priority escalated to URGENT: {subject[:40]}"
                learned_notes.append(note)

                cursor.execute("""
                    INSERT INTO user_corrections
                    (msg_id, sender, subject, predicted_prio, corrected_prio,
                     predicted_cat, corrected_cat, predicted_archive, corrected_archive)
                    VALUES (?,?,?,?,?,?,?,?,?)
                """, (msg_id, sender, subject, pred_prio, "URGENT",
                      pred_cat, pred_cat, int(pred_arch), 0))

                match = re.search(r"<(.+?)>", sender)
                email_addr = match.group(1).lower() if match else sender.lower()
                cursor.execute("""
                    INSERT OR REPLACE INTO sender_rules
                    (sender_pattern, priority, category, action_needed, action_type, auto_archive, rule_source, updated_at)
                    VALUES (?, 'URGENT', ?, 1, 'Review', 0, 'feedback_learning', datetime('now'))
                """, (email_addr, pred_cat))

                cursor.execute("""
                    UPDATE processed_emails
                    SET priority = 'URGENT', status = 'corrected'
                    WHERE msg_id = ?
                """, (msg_id,))
    except Exception as e:
        logger.debug(f"Urgent query check note: {e}")

    conn.commit()
    conn.close()
    return learned_notes


# ── Follow-Up Reminder & Unresolved Action Tracker ────────────────────────────

def check_pending_reminders(service, db_path: Path, label_ids: dict[str, str]) -> list[dict]:
    """
    Check emails requiring action. If user already replied in the Gmail thread,
    mark as resolved and clear AI/Needs-Action label.
    If still pending after > 24 hours, surface in reminder digest.
    """
    conn = get_db_connection(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT msg_id, thread_id, sender, subject, action_type, processed_at, reminded_count
        FROM processed_emails
        WHERE action_needed = 1 AND status = 'pending_action'
        ORDER BY processed_at ASC
    """)
    pending = cursor.fetchall()
    unresolved_reminders: list[dict] = []

    for row in pending:
        msg_id = row["msg_id"]
        thread_id = row["thread_id"]
        proc_time = datetime.fromisoformat(row["processed_at"])
        age = datetime.now() - proc_time

        # Check if the thread has a sent reply by the user
        is_resolved = False
        try:
            thread = service.users().threads().get(userId="me", id=thread_id).execute()
            messages = thread.get("messages", [])
            for m in messages:
                labels = m.get("labelIds", [])
                if "SENT" in labels:
                    is_resolved = True
                    break
        except HttpError:
            pass

        if is_resolved:
            # User replied! Clear Needs-Action label
            logger.info(f"✅ Action resolved (reply detected): {row['subject'][:50]}")
            cursor.execute("""
                UPDATE processed_emails
                SET status = 'resolved', resolved_at = datetime('now')
                WHERE msg_id = ?
            """, (msg_id,))

            remove_lbls = []
            add_lbls = []
            if label_ids.get("AI/Needs-Action"):
                remove_lbls.append(label_ids["AI/Needs-Action"])
            if label_ids.get("AI/Action-Done"):
                add_lbls.append(label_ids["AI/Action-Done"])

            try:
                service.users().messages().modify(
                    userId="me", id=msg_id,
                    body={"addLabelIds": add_lbls, "removeLabelIds": remove_lbls}
                ).execute()
            except HttpError:
                pass
        else:
            # Still pending. Remind if older than 20 hours
            if age > timedelta(hours=20):
                days = age.days
                age_str = f"{days}d ago" if days > 0 else f"{int(age.total_seconds() // 3600)}h ago"
                unresolved_reminders.append({
                    "msg_id": msg_id,
                    "sender": row["sender"],
                    "subject": row["subject"],
                    "action_type": row["action_type"],
                    "age_desc": age_str,
                })
                cursor.execute("""
                    UPDATE processed_emails
                    SET reminded_count = reminded_count + 1, last_reminded_at = datetime('now')
                    WHERE msg_id = ?
                """, (msg_id,))

    conn.commit()
    conn.close()
    return unresolved_reminders

# ── Email Fetch & Parsing ──────────────────────────────────────────────────────

def fetch_unprocessed(service, max_results: int = MAX_PER_RUN) -> list[dict]:
    if max_results <= 0:
        return []
    result = service.users().messages().list(
        userId="me",
        q="is:unread -label:AI/Processed",
        maxResults=max_results,
    ).execute()
    return result.get("messages", [])


def parse_recipient_headers(headers: dict) -> str:
    """
    Determine original recipient from email headers.
    Handles direct To, envelope Delivered-To, and multi-hop forwarding headers
    (X-Forwarded-For, X-Forwarded-To, X-Forwarded-By).
    """
    x_forwarded = f"{headers.get('x-forwarded-for', '')} {headers.get('x-forwarded-to', '')} {headers.get('x-forwarded-by', '')}".lower()
    to_header = headers.get("to", "").lower()
    delivered_to = headers.get("delivered-to", "").lower()

    if "deepshah7977" in x_forwarded or "deepshah7977" in to_header or "deepshah7977" in delivered_to:
        return "deepshah7977"
    elif "sl4ught3rcl4y" in to_header or "sl4ught3rcl4y" in delivered_to:
        return "sl4ught3rcl4y"
    elif to_header:
        m = re.search(r"[\w\.-]+(?=@)", headers.get("to", ""))
        return m.group(0) if m else headers.get("to", "")[:25]
    return ""


def get_email_data(service, msg_id: str) -> dict:
    msg = service.users().messages().get(
        userId="me", id=msg_id, format="full"
    ).execute()

    headers = {h["name"].lower(): h["value"]
               for h in msg["payload"].get("headers", [])}

    sender  = headers.get("from", "")
    subject = headers.get("subject", "(no subject)")
    list_unsub = headers.get("list-unsubscribe", "")
    thread_id  = msg.get("threadId", "")

    original_recipient = parse_recipient_headers(headers)
    body, trackers_blocked = _extract_body(msg["payload"])

    return {
        "id": msg_id,
        "thread_id": thread_id,
        "sender": sender,
        "subject": subject,
        "body": body,
        "list_unsubscribe": list_unsub,
        "label_ids": msg.get("labelIds", []),
        "original_recipient": original_recipient,
        "trackers_blocked": trackers_blocked,
    }


TRACKER_PATTERNS = [
    r"https?://[^\"'\s>]+/(?:open|track|pixel|beacon|wf/open|e/open|trk|tr/open)[^\"'\s>]*",
    r"https?://[^\"'\s>]*(?:hs-analytics|hubspot|mailfoogae|mandrillapp|superhuman|mixmax|yesware|salesforceiq|streak\.com|sendgrid\.net)[^\"'\s>]*",
]

def clean_html_to_text(raw_html: str) -> tuple[str, int]:
    """
    Convert HTML email body to clean readable plain text and strip tracking pixels.
    Returns (cleaned_text, tracking_pixels_blocked_count).
    """
    if not raw_html:
        return "", 0

    trackers_blocked = 0

    # 1. Detect 1x1 zero-pixel tracking beacons in <img> tags
    pixel_img_pattern = re.compile(
        r'<img[^>]+(?:width=[\'"]?[01](?:px)?[\'"]?[^>]*height=[\'"]?[01](?:px)?[\'"]?|height=[\'"]?[01](?:px)?[\'"]?[^>]*width=[\'"]?[01](?:px)?[\'"]?)[^>]*>',
        re.IGNORECASE
    )
    trackers_blocked += len(pixel_img_pattern.findall(raw_html))
    text = pixel_img_pattern.sub("", raw_html)

    # 2. Detect known tracker service URLs in <img> tags
    for pat in TRACKER_PATTERNS:
        tracker_img_pat = re.compile(r'<img[^>]+src=[\'"]' + pat + r'[\'"][^>]*>', re.IGNORECASE)
        matches = tracker_img_pat.findall(text)
        trackers_blocked += len(matches)
        text = tracker_img_pat.sub("", text)

    # 3. Strip script and style blocks
    text = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", text, flags=re.DOTALL | re.IGNORECASE)
    # 4. Replace block-level tags with newlines
    text = re.sub(r"<(p|br|div|tr|li|h[1-6])[^>]*>", "\n", text, flags=re.IGNORECASE)
    # 5. Strip remaining HTML tags
    text = re.sub(r"<[^>]+>", " ", text)
    # 6. Unescape HTML entities (&nbsp;, &amp;, etc.)
    text = html.unescape(text)
    # 7. Normalize excessive newlines and spaces
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    return text.strip(), trackers_blocked


def _extract_body(payload: dict) -> tuple[str, int]:
    """
    Extract readable email body text and count blocked trackers.
    Prefers text/plain. If missing or accompanied by HTML, strips tracker beacons.
    Returns (body_text, trackers_blocked_count).
    """
    plain_parts: list[str] = []
    html_parts: list[str] = []

    def _walk(part):
        mime = part.get("mimeType", "")
        data = part.get("body", {}).get("data", "")
        if data:
            try:
                decoded = base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")
                if mime == "text/plain":
                    plain_parts.append(decoded)
                elif mime == "text/html":
                    html_parts.append(decoded)
            except Exception:
                pass
        for subpart in part.get("parts", []):
            _walk(subpart)

    _walk(payload)

    total_trackers = 0
    cleaned_html = ""
    if html_parts:
        full_html = "\n\n".join(html_parts)
        cleaned_html, total_trackers = clean_html_to_text(full_html)

    if plain_parts:
        return "\n\n".join(plain_parts).strip(), total_trackers
    if cleaned_html:
        return cleaned_html, total_trackers
    return "", 0

# ── Apply to Gmail ─────────────────────────────────────────────────────────────

def apply_to_gmail(
    service,
    msg_id: str,
    classification: EmailClassification,
    label_ids: dict[str, str],
):
    add_ids   = [label_ids["AI/Processed"]]
    remove_ids: list[str] = []

    # Priority labels
    if classification.priority == "URGENT":
        add_ids.append(label_ids["AI/Priority-Urgent"])
        add_ids.append("STARRED")
    elif classification.priority == "IMPORTANT":
        add_ids.append(label_ids["AI/Priority-Important"])

    # Category labels
    cat_map = {
        "Work":       "AI/Category-Work",
        "Personal":   "AI/Category-Personal",
        "Finance":    "AI/Category-Finance",
        "Travel":     "AI/Category-Travel",
        "Newsletter":   "AI/Category-Newsletter",
        "Shopping":     "AI/Category-Shopping",
        "ColdOutreach": "AI/Category-ColdOutreach",
    }
    if classification.category in cat_map:
        add_ids.append(label_ids[cat_map[classification.category]])

    # Action tracker label
    if classification.action_needed and label_ids.get("AI/Needs-Action"):
        add_ids.append(label_ids["AI/Needs-Action"])

    # Auto-archive
    if classification.auto_archive:
        remove_ids.append("INBOX")
        add_ids.append(label_ids["AI/Auto-Archived"])

    service.users().messages().modify(
        userId="me",
        id=msg_id,
        body={"addLabelIds": add_ids, "removeLabelIds": remove_ids},
    ).execute()

# ── Save to DB ─────────────────────────────────────────────────────────────────

def save_email(email_data: dict, classification: EmailClassification, db_path: Path):
    conn = get_db_connection(db_path)
    status = "pending_action" if classification.action_needed else ("archived" if classification.auto_archive else "active")

    conn.execute("""
        INSERT OR REPLACE INTO processed_emails
        (msg_id, thread_id, sender, subject, priority, category,
         action_needed, action_type, summary, auto_archived, status, original_recipient, trackers_blocked)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (
        email_data["id"],
        email_data["thread_id"],
        email_data["sender"],
        email_data["subject"],
        classification.priority,
        classification.category,
        int(classification.action_needed),
        classification.action_type,
        classification.summary,
        int(classification.auto_archive),
        status,
        email_data.get("original_recipient", ""),
        email_data.get("trackers_blocked", 0),
    ))

    # Subscription / Recurring bill detection
    body_text = email_data.get("body", "")
    subj_text = email_data.get("subject", "")
    combined = f"{subj_text} {body_text[:1200]}".lower()

    sub_keywords = ["subscription", "membership", "recurring", "monthly bill", "auto-renew", "receipt", "invoice", "payment receipt", "statement"]
    if classification.category in ("Finance", "Shopping") or any(k in combined for k in sub_keywords):
        # Extract dollar amount
        amt_match = re.search(r"\$\s*(\d+(?:\.\d{2})?)", combined)
        if amt_match:
            try:
                amt = float(amt_match.group(1))
                if 0.50 <= amt <= 2500.0:  # Reasonable subscription/bill bounds
                    # Extract vendor
                    vendor = email_data.get("sender", "")
                    if "<" in vendor:
                        vendor = vendor.split("<")[0].strip().strip('"').strip("'")
                    if not vendor:
                        vendor = email_data.get("sender", "")[:35]

                    freq = "annual" if any(w in combined for w in ["annual", "yearly", "per year", "/yr"]) else "monthly"

                    conn.execute("""
                        INSERT INTO subscriptions (vendor, amount, frequency, last_billed_at, last_msg_id, category, status)
                        VALUES (?, ?, ?, datetime('now'), ?, ?, 'active')
                        ON CONFLICT(vendor) DO UPDATE SET
                            amount = excluded.amount,
                            frequency = excluded.frequency,
                            last_billed_at = datetime('now'),
                            last_msg_id = excluded.last_msg_id
                    """, (vendor[:40], amt, freq, email_data["id"], classification.category))
            except Exception as e:
                logger.debug(f"Subscription parse error: {e}")

    # Sender stats
    raw_sender = email_data["sender"]
    match = re.search(r"<(.+?)>", raw_sender)
    addr = match.group(1).lower() if match else raw_sender.lower()
    conn.execute("""
        INSERT INTO sender_stats (email_address, incoming_count, last_seen)
        VALUES (?, 1, datetime('now'))
        ON CONFLICT(email_address) DO UPDATE SET
            incoming_count = incoming_count + 1,
            last_seen = datetime('now')
    """, (addr,))

    # Update O(1) Label State Hashtable
    conn.execute("""
        INSERT OR REPLACE INTO email_label_state
        (msg_id, last_category, last_priority, is_archived, checksum, updated_at)
        VALUES (?, ?, ?, ?, ?, datetime('now'))
    """, (
        email_data["id"],
        classification.category,
        classification.priority,
        int(classification.auto_archive),
        f"{classification.category}:{classification.priority}:{int(classification.auto_archive)}"
    ))

    conn.commit()
    conn.close()

    # Generate dense vector embedding (all-minilm via Ollama)
    try:
        from vector_store import upsert_email_embedding
        upsert_email_embedding(
            db_path,
            email_data["id"],
            email_data.get("subject", ""),
            email_data.get("sender", ""),
            classification.summary,
            email_data.get("body", "")[:300]
        )
    except Exception as e:
        logger.debug(f"Embedding generation note: {e}")

def check_thermal_headroom():
    """
    Hardware safety check per AGENTS.md directives.
    Monitors Pi 5 thermal zone before CPU-bound LLM tasks.
    If Pi core temperature exceeds 78°C (near 80°C throttle threshold),
    pauses execution to let active cooler drop core temp.
    """
    thermal_path = Path("/sys/class/thermal/thermal_zone0/temp")
    if thermal_path.exists():
        try:
            temp_c = int(thermal_path.read_text().strip()) / 1000.0
            if temp_c >= 78.0:
                logger.warning(f"⚠️ Pi 5 core temp high ({temp_c:.1f}°C). Throttling 6s for cooling...")
                time.sleep(6.0)
        except Exception:
            pass


def run_pipeline_for_user(user_id: str = "deep", max_emails: int = 15):
    profile = get_user_profile(user_id)
    pipeline_started = time.monotonic()
    logger.info("=" * 55)
    logger.info(f"Pipeline starting for [{profile['label']}] ({profile['db_file'].name}) [Quota: {max_emails}]")

    init_db(profile["db_file"])
    run_id = _start_pipeline_run(profile["db_file"], user_id)
    service   = get_gmail_service(profile)
    label_ids = ensure_labels(service)

    # 1. Feedback Loop: check if user corrected any labels in Gmail
    learned_feedback = sync_user_feedback(service, profile["db_file"], label_ids)
    if learned_feedback:
        logger.info(f"[{profile['label']}] Feedback learned: {len(learned_feedback)} updates")

    # 2. Check pending action reminders
    pending_reminders = check_pending_reminders(service, profile["db_file"], label_ids)

    # 3. Fetch newly arriving emails with fair-share chunk limit
    messages = fetch_unprocessed(service, max_results=max_emails)
    logger.info(f"[{profile['label']}] Found {len(messages)} unread, unprocessed emails")

    surfaced: list[dict] = []
    teacher_candidates: list[dict] = []
    stats = {"total": len(messages), "urgent": 0, "important": 0,
             "archived": 0, "llm": 0, "errors": 0, "processed": 0,
             "fallbacks": 0, "classification_seconds": 0.0,
             "max_classify_seconds": 0.0}
    _update_pipeline_run(profile["db_file"], run_id, emails_found=len(messages))

    # Fetch dynamic few-shot corrections from user's past feedback
    few_shot_examples = get_recent_corrections(profile["db_file"], limit=3)

    for msg in messages:
        try:
            check_thermal_headroom()
            email = get_email_data(service, msg["id"])

            # Check learned sender rule override first
            override = get_sender_override(email["sender"], profile["db_file"])

            classify_started = time.monotonic()
            classification = classify_email(
                sender=email["sender"],
                subject=email["subject"],
                body=email["body"],
                list_unsubscribe=email["list_unsubscribe"],
                sender_override=override,
                few_shot_examples=few_shot_examples,
            )
            classify_seconds = time.monotonic() - classify_started
            stats["classification_seconds"] += classify_seconds
            stats["max_classify_seconds"] = max(stats["max_classify_seconds"], classify_seconds)
            if classification.summary.startswith(("(Classification fallback)", "(LLM Unavailable")):
                stats["fallbacks"] += 1

            apply_to_gmail(service, msg["id"], classification, label_ids)
            save_email(email, classification, profile["db_file"])
            stats["processed"] += 1
            teacher_candidates.append({
                **email,
                "classification": classification,
                # Explicit human/teacher rules remain authoritative and must
                # not be silently replaced by a fresh cloud audit.
                "sender_override": override,
            })

            if classification.auto_archive:
                stats["archived"] += 1

            recip = email.get("original_recipient", "")
            if classification.priority == "URGENT":
                stats["urgent"] += 1
                surfaced.append({**email, "classification": classification})
                send_urgent_alert(
                    email["sender"],
                    email["subject"],
                    classification.summary,
                    env_path=profile["env_file"],
                    recipient=recip,
                )
            elif classification.priority == "IMPORTANT":
                stats["important"] += 1
                surfaced.append({**email, "classification": classification})

            logger.info(
                f"[{profile['label']}] [{classification.priority:9}] [{classification.category:12}] "
                f"{f'[{recip}] ' if recip else ''}"
                f"{'[ARCHIVE] ' if classification.auto_archive else ''}"
                f"{email['subject'][:55]}"
            )

            time.sleep(0.1)

        except HttpError as e:
            logger.error(f"Gmail API error on {msg['id']}: {e}")
            stats["errors"] += 1
        except Exception as e:
            logger.error(f"Error on {msg['id']}: {e}", exc_info=True)
            stats["errors"] += 1

    # 4. Optional teacher audit. This is a strict no-op unless GEMINI_API_KEY is
    # configured in the user's environment file.
    _update_pipeline_run(
        profile["db_file"], run_id,
        emails_processed=stats["processed"], errors=stats["errors"],
        fallback_count=stats["fallbacks"],
        classification_seconds=round(stats["classification_seconds"], 3),
        max_classify_seconds=round(stats["max_classify_seconds"], 3),
    )
    # Core ingestion is durable at this point. Record it before optional
    # teacher/network work so a cloud outage cannot hide successful mailbox
    # processing from operators.
    conn = get_db_connection(profile["db_file"])
    conn.execute("CREATE TABLE IF NOT EXISTS system_metadata (key TEXT PRIMARY KEY, val TEXT);")
    conn.execute("""
        INSERT INTO system_metadata (key, val) VALUES ('last_ingestion_completed_at', datetime('now'))
        ON CONFLICT(key) DO UPDATE SET val = excluded.val
    """)
    conn.commit()
    conn.close()
    teacher_stats = {"audited": 0, "corrected": 0, "errors": 0, "deferred": 0}
    teacher_started = time.monotonic()
    try:
        from dotenv import load_dotenv
        load_dotenv(profile["env_file"], override=False)
        from gemini_teacher import audit_ambiguous_emails
        teacher_stats = audit_ambiguous_emails(
            service, profile["db_file"], label_ids, teacher_candidates
        )
        if teacher_stats["audited"] or teacher_stats["errors"]:
            logger.info(
                "[%s] Gemini audit: %d checked, %d corrected, %d errors",
                profile["label"], teacher_stats["audited"],
                teacher_stats["corrected"], teacher_stats["errors"],
            )
    except Exception as e:
        logger.warning(f"[{profile['label']}] Gemini teacher audit unavailable: {e}")
    teacher_seconds = time.monotonic() - teacher_started
    _update_pipeline_run(
        profile["db_file"], run_id,
        gemini_seconds=round(teacher_seconds, 3),
        gemini_audited=teacher_stats.get("audited", 0),
        gemini_errors=teacher_stats.get("errors", 0),
        gemini_deferred=teacher_stats.get("deferred", 0),
    )

    # 5. Push Telegram Briefing (New urgent/important + pending follow-up reminders + learned feedback)
    if surfaced or pending_reminders or learned_feedback:
        send_telegram_digest(
            surfaced,
            stats,
            pending_reminders=pending_reminders,
            learned_feedback=learned_feedback,
            user_label=profile["label"],
            env_path=profile["env_file"],
        )

    # 6. WAL Checkpoint & Operational Heartbeat (Prunes WAL and records liveness)
    try:
        conn = get_db_connection(profile["db_file"])
        conn.execute("PRAGMA wal_checkpoint(TRUNCATE);")
        conn.execute("CREATE TABLE IF NOT EXISTS system_metadata (key TEXT PRIMARY KEY, val TEXT);")
        conn.execute("""
            INSERT INTO system_metadata (key, val) VALUES ('last_successful_run_at', datetime('now'))
            ON CONFLICT(key) DO UPDATE SET val = excluded.val;
        """)
        conn.commit()
        conn.close()
    except Exception as e:
        logger.debug(f"Post-run maintenance warning: {e}")

    # 7. Autonomous Post-Batch Background Evaluation Suite
    try:
        from background_evaluator import run_post_batch_evaluations, dispatch_eval_alert_if_needed
        eval_report = run_post_batch_evaluations(profile["db_file"])
        logger.info(f"[{profile['label']}] 🛡️ Post-batch evaluation: health={eval_report['health_score']:.1f}%, invariants_ok={eval_report['ok']}")
        if not eval_report["ok"]:
            chat_id = os.getenv("TELEGRAM_CHAT_ID", "")
            if chat_id:
                dispatch_eval_alert_if_needed(eval_report, chat_id)
    except Exception as e:
        logger.debug(f"Post-batch evaluation warning: {e}")

    duration_seconds = time.monotonic() - pipeline_started
    final_resources = _resource_snapshot()
    overages = []
    runtime_budget = _env_float("PIPELINE_RUNTIME_BUDGET_SEC", 840.0)
    classify_budget = _env_float("OLLAMA_CLASSIFY_BUDGET_SEC", 25.0)
    gemini_budget = _env_float("GEMINI_AUDIT_BUDGET_SEC", 45.0)
    rss_budget = _env_float("EMAIL_AGENT_RSS_BUDGET_MB", 1024.0)
    if duration_seconds > runtime_budget:
        overages.append({"metric": "pipeline_duration_sec", "actual": round(duration_seconds, 2), "budget": runtime_budget})
    if stats["max_classify_seconds"] > classify_budget + 1.0:
        overages.append({"metric": "classification_latency_sec", "actual": round(stats["max_classify_seconds"], 2), "budget": classify_budget})
    if teacher_seconds > gemini_budget + 1.0:
        overages.append({"metric": "gemini_audit_sec", "actual": round(teacher_seconds, 2), "budget": gemini_budget})
    if final_resources["max_rss_mb"] > rss_budget:
        overages.append({"metric": "email_agent_rss_mb", "actual": final_resources["max_rss_mb"], "budget": rss_budget})
    _update_pipeline_run(
        profile["db_file"], run_id,
        status="completed_over_budget" if overages else "completed",
        finished_at=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        emails_processed=stats["processed"], errors=stats["errors"],
        fallback_count=stats["fallbacks"],
        duration_seconds=round(duration_seconds, 3),
        max_rss_mb=final_resources["max_rss_mb"],
        temperature_c=final_resources["temperature_c"],
        overages=json.dumps(overages, separators=(",", ":")),
    )

    logger.info(
        f"[{profile['label']}] Finished — {stats['total']} new, "
        f"{stats['urgent']} urgent, {stats['important']} important, "
        f"{stats['archived']} archived, {len(pending_reminders)} pending reminders"
        f", duration={duration_seconds:.1f}s, max_rss={final_resources['max_rss_mb']:.1f}MB"
    )


def main():
    parser = argparse.ArgumentParser(description="Pi-loop Email Intelligence Agent")
    parser.add_argument("--user", default="", help="Specific user profile ID (e.g. deep, pranali)")
    parser.add_argument("--all-users", action="store_true", help="Process all configured users with fair-share scheduling")
    parser.add_argument("--max-emails", type=int, default=15, help="Max emails to process per user per run")
    args = parser.parse_args()

    if args.user:
        run_pipeline_for_user(args.user, max_emails=args.max_emails)
    else:
        # Default or --all-users: load registry
        try:
            from user_manager import get_active_users
            active_users = get_active_users()
        except Exception:
            active_users = []

        if active_users:
            logger.info(f"Multi-tenant fair-share scheduling: {len(active_users)} active user(s)")
            for u in active_users:
                try:
                    quota = args.max_emails if args.max_emails != 15 else u.max_emails_per_run
                    run_pipeline_for_user(u.id, max_emails=quota)
                except Exception as e:
                    logger.error(f"Pipeline failure for user {u.id}: {e}", exc_info=True)
        else:
            # Fallback single user
            run_pipeline_for_user("deep", max_emails=args.max_emails)


if __name__ == "__main__":
    main()
