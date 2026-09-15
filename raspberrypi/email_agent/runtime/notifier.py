"""
notifier.py
Pi-loop Email Intelligence Agent — Telegram Push Notifications
Sends morning digest, pending action reminders, feedback learning alerts,
and real-time URGENT alerts to your phone.
Supports pluggable multi-user configs.
"""

import logging
import os
import time
from datetime import datetime
from pathlib import Path

import requests
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

PRIORITY_EMOJI = {
    "URGENT":    "🔴",
    "IMPORTANT": "🟡",
    "NORMAL":    "🟢",
    "LOW":       "⚪",
}

CATEGORY_EMOJI = {
    "Work":       "💼",
    "Personal":   "👤",
    "Finance":    "💰",
    "Travel":     "✈️",
    "Shopping":   "🛒",
    "Newsletter": "📰",
    "ColdOutreach": "🧊",
    "Spam":       "🚫",
    "Other":      "📧",
}


def split_telegram_message(text: str, max_len: int = 4000) -> list[str]:
    """
    Split text into chunks smaller than Telegram's 4096-character limit.
    Splits preferentially along double newlines, then single newlines, then spaces.
    """
    if len(text) <= max_len:
        return [text]

    chunks = []
    current_chunk = []
    current_len = 0

    lines = text.split("\n")
    for line in lines:
        line_len = len(line) + 1
        if current_len + line_len > max_len:
            if current_chunk:
                chunks.append("\n".join(current_chunk))
                current_chunk = []
                current_len = 0
            
            # If a single line exceeds max_len, hard-split it
            while len(line) > max_len:
                chunks.append(line[:max_len])
                line = line[max_len:]
        
        current_chunk.append(line)
        current_len += len(line) + 1

    if current_chunk:
        chunks.append("\n".join(current_chunk))

    if len(chunks) > 1:
        return [f"({i+1}/{len(chunks)})\n{c}" for i, c in enumerate(chunks)]
    return chunks


def _get_telegram_creds(env_path: Path | None = None) -> tuple[str, str]:
    """Load credentials from user-specific or default .env."""
    if env_path and env_path.exists():
        load_dotenv(env_path, override=True)
    else:
        load_dotenv(Path(__file__).parent / "config" / ".env")

    token = os.getenv("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "")
    return token, chat_id


def _send(
    text: str,
    env_path: Path | None = None,
    chat_id_override: str | int | None = None,
):
    """
    Send untrusted email-derived text to Telegram with:
    1. Automatic chunking for payloads > 4000 characters
    2. Plain-text delivery so arbitrary subjects cannot break entity parsing
    3. One bounded retry for rate limits and transient server failures
    """
    bot_token, configured_chat_id = _get_telegram_creds(env_path)
    chat_id = chat_id_override or configured_chat_id
    if not bot_token or not chat_id:
        logger.debug("Telegram not configured — skipping notification")
        return

    chunks = split_telegram_message(text, max_len=4000)
    for chunk in chunks:
        try:
            for attempt in range(2):
                resp = requests.post(
                    f"https://api.telegram.org/bot{bot_token}/sendMessage",
                    json={
                        "chat_id": chat_id,
                        "text": chunk,
                        "disable_web_page_preview": True,
                    },
                    timeout=10,
                )
                if resp.ok:
                    break
                transient = resp.status_code == 429 or resp.status_code >= 500
                if attempt == 0 and transient:
                    logger.warning(
                        "Telegram send failed transiently (%s); retrying once",
                        resp.status_code,
                    )
                    time.sleep(1)
                    continue
                logger.error("Telegram send failed (%s): %s", resp.status_code, resp.text)
                break
        except Exception as e:
            logger.error(f"Telegram notification network failure: {e}")


def send_telegram_direct(chat_id: str | int, text: str, env_path: Path | None = None):
    """Send a guardrail alert to an explicit chat using the configured bot."""
    _send(text, env_path=env_path, chat_id_override=chat_id)



def send_telegram_digest(
    surfaced_emails: list[dict],
    stats: dict,
    pending_reminders: list[dict] | None = None,
    learned_feedback: list[str] | None = None,
    user_label: str = "Deep",
    env_path: Path | None = None,
):
    """
    Push a digest of URGENT + IMPORTANT emails, pending action reminders,
    and any feedback learned from user manual corrections.
    """
    now = datetime.now().strftime("%a %b %-d, %-I:%M %p")

    urgent = [e for e in surfaced_emails if e["classification"].priority == "URGENT"]
    important = [e for e in surfaced_emails if e["classification"].priority == "IMPORTANT"]

    lines = [f"📬 Email Briefing ({user_label}) — {now}"]
    lines.append(f"Processed {stats.get('total', 0)} unread · {stats.get('archived', 0)} archived")
    lines.append("")

    # 1. Urgent Emails
    if urgent:
        lines.append(f"🔴 {len(urgent)} URGENT — needs action")
        for e in urgent[:5]:
            cls = e["classification"]
            cat_emoji = CATEGORY_EMOJI.get(cls.category, "📧")
            recip = f"[{e.get('original_recipient')}] " if e.get("original_recipient") else ""
            lines.append(f"  {cat_emoji} {recip}[{cls.action_type}] — {e['subject'][:50]}")
            lines.append(f"  {cls.summary[:90]}")

    # 2. Important Emails
    if important:
        lines.append(f"\n🟡 {len(important)} Important")
        for e in important[:5]:
            cls = e["classification"]
            cat_emoji = CATEGORY_EMOJI.get(cls.category, "📧")
            recip = f"[{e.get('original_recipient')}] " if e.get("original_recipient") else ""
            action = f"[{cls.action_type}] " if cls.action_needed else ""
            lines.append(f"  {cat_emoji} {recip}{action}{e['subject'][:60]}")

    # 3. Follow-up Reminders (Emails waiting on user action)
    if pending_reminders:
        lines.append(f"\n⏳ {len(pending_reminders)} Unresolved Reminders (Waiting on you)")
        for rem in pending_reminders[:5]:
            action_tag = f"[{rem.get('action_type', 'Action')}]"
            recip = f"[{rem.get('original_recipient')}] " if rem.get("original_recipient") else ""
            lines.append(f"  • {recip}{action_tag} {rem.get('subject', '')[:50]}")
            lines.append(f"    From: {rem.get('sender', '')[:35]} · {rem.get('age_desc', 'pending')}")

    # 4. Learned Corrections (Model self-improvement notification)
    if learned_feedback:
        lines.append("\n💡 Learned from your label corrections:")
        for rule in learned_feedback[:3]:
            lines.append(f"  • {rule}")

    if not urgent and not important and not pending_reminders and not learned_feedback:
        lines.append("✅ All caught up — inbox looking clean")

    _send("\n".join(lines), env_path=env_path)


def send_urgent_alert(sender: str, subject: str, summary: str, env_path: Path | None = None, recipient: str = ""):
    """Real-time alert for an incoming critical/urgent email."""
    recip_tag = f"[{recipient}] " if recipient else ""
    text = (
        f"🚨 URGENT EMAIL ALERT {recip_tag}\n"
        f"From: {sender[:60]}\n"
        f"Subject: {subject[:80]}\n"
        f"Summary: {summary[:120]}"
    )
    _send(text, env_path=env_path)
