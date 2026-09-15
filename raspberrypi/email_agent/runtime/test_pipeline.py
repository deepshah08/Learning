"""
test_pipeline.py
Automated test suite verifying email classification, HTML body extraction,
prompt injection resistance, few-shot feedback learning, and reminder state transitions.
"""

import sqlite3
import tempfile
from pathlib import Path
from unittest.mock import patch

from email_classifier import (
    classify_email,
    quick_prefilter,
    EmailClassification,
    CLASSIFY_SYSTEM,
    CLASSIFY_TEMPLATE,
    _call_ollama_with_timeout,
)
from gmail_agent import (
    _extract_body,
    clean_html_to_text,
    get_sender_override,
    get_recent_corrections,
    fetch_unprocessed,
    init_db,
    parse_recipient_headers,
    save_email,
)
from bot_service import query_rag
from bot_service import (
    _category_keyboard,
    apply_category_feedback,
    rate_rag_interaction,
    record_rag_interaction,
)
from gemini_teacher import (
    TeacherError,
    TeacherClassification,
    classify_with_gemini,
    reconcile_classification,
)
from notifier import _send, send_telegram_direct


def test_telegram_plaintext_and_bounded_retry_policy():
    class Response:
        def __init__(self, status_code):
            self.status_code = status_code
            self.ok = status_code == 200
            self.text = "test response"

    permanent_calls = []

    def permanent_post(*args, **kwargs):
        permanent_calls.append(kwargs)
        return Response(400)

    with patch("notifier._get_telegram_creds", return_value=("token", "configured")), \
         patch("notifier.requests.post", side_effect=permanent_post):
        _send("subject_with_[untrusted]*markup*")
    assert len(permanent_calls) == 1
    assert "parse_mode" not in permanent_calls[0]["json"]

    transient_calls = []

    def transient_post(*args, **kwargs):
        transient_calls.append(kwargs)
        return Response(503 if len(transient_calls) == 1 else 200)

    with patch("notifier._get_telegram_creds", return_value=("token", "configured")), \
         patch("notifier.requests.post", side_effect=transient_post), \
         patch("notifier.time.sleep"):
        send_telegram_direct("guardrail-chat", "alert")
    assert len(transient_calls) == 2
    assert transient_calls[-1]["json"]["chat_id"] == "guardrail-chat"


def test_real_ollama_http_deadline_and_gemini_retry_budget():
    class OllamaResponse:
        def raise_for_status(self):
            return None

        def json(self):
            return {"response": '{"category":"Work"}'}

    class OllamaSession:
        def __init__(self):
            self.calls = []

        def post(self, *args, **kwargs):
            self.calls.append((args, kwargs))
            return OllamaResponse()

    ollama_session = OllamaSession()
    raw = _call_ollama_with_timeout("classify", timeout_sec=7.0, session=ollama_session)
    assert raw == '{"category":"Work"}'
    assert ollama_session.calls[0][1]["timeout"] == (3.0, 7.0)
    assert ollama_session.calls[0][1]["json"]["stream"] is False

    class LimitedResponse:
        ok = False
        status_code = 429
        headers = {}
        text = "quota exhausted"

    class LimitedSession:
        def __init__(self):
            self.calls = 0

        def post(self, *args, **kwargs):
            self.calls += 1
            return LimitedResponse()

    limited = LimitedSession()
    try:
        classify_with_gemini(
            "sender@example.com", "subject", "body", api_key="test-key",
            model="gemini-3.8-flash", session=limited, retry_budget_sec=0,
        )
        raise AssertionError("Expected a deferred teacher error")
    except TeacherError as exc:
        assert "deferred" in str(exc)
    assert limited.calls == 1


class FakeGmailService:
    def __init__(self):
        self.modifications = []

    def users(self):
        return self

    def messages(self):
        return self

    def modify(self, **kwargs):
        self.modifications.append(kwargs)
        return self

    def execute(self):
        return {}


def seed_feedback_email(db_path: Path, msg_id: str = "feedback-1"):
    conn = sqlite3.connect(db_path)
    conn.execute("""
        INSERT INTO processed_emails
            (msg_id, sender, subject, priority, category, action_needed,
             action_type, summary, auto_archived, status)
        VALUES (?, 'Store <orders@brand.com>', 'Your order receipt', 'NORMAL',
                'Finance', 0, 'None', 'A retail order', 0, 'active')
    """, (msg_id,))
    conn.execute("""
        INSERT INTO email_label_state
            (msg_id, last_category, last_priority, is_archived, checksum)
        VALUES (?, 'Finance', 'NORMAL', 0, 'Finance:NORMAL:0')
    """, (msg_id,))
    conn.commit()
    conn.close()


def test_zero_quota_skips_gmail_request():
    class NoCallsAllowed:
        def users(self):
            raise AssertionError("Gmail must not be called for a zero quota")

    assert fetch_unprocessed(NoCallsAllowed(), max_results=0) == []


def test_clean_html_fallback():
    html_sample = """
    <html>
        <body>
            <h2>Invoice #10492</h2>
            <p>Your payment of <b>$49.99</b> is due tomorrow.</p>
            <a href="https://pay.example.com">Click here to pay</a>
            <img src="https://pixel.tracking.com/open.gif" width="1" height="1">
            <img src="https://mandrillapp.com/track/open.php?u=123">
        </body>
    </html>
    """
    text, trackers = clean_html_to_text(html_sample)
    assert "Invoice #10492" in text
    assert "$49.99" in text
    assert "due tomorrow" in text
    assert "<p>" not in text
    assert "<b>" not in text
    assert trackers >= 2  # Blocked tracking beacons

def test_extract_body_html_fallback():
    # Payload with text/html only
    import base64
    html_content = "<p>Urgent server maintenance notification for cluster us-east-1.</p><img src='https://track.hubspot.com/beacon' width='1' height='1'>"
    encoded = base64.urlsafe_b64encode(html_content.encode("utf-8")).decode("utf-8")
    payload = {
        "mimeType": "multipart/alternative",
        "parts": [
            {
                "mimeType": "text/html",
                "body": {"data": encoded}
            }
        ]
    }
    extracted, trackers = _extract_body(payload)
    assert "Urgent server maintenance notification" in extracted
    assert trackers >= 1

def test_quick_prefilter_newsletters_and_cold_outreach():
    # Test unsubscribe header
    res1 = quick_prefilter("news@acme.com", "Weekly update", "<https://acme.com/unsub>")
    assert res1 is not None
    assert res1.auto_archive is True
    assert res1.category == "Newsletter"

    # Test noreply sender
    res2 = quick_prefilter("noreply@marketing.com", "Special holiday discount", "")
    assert res2 is not None
    assert res2.auto_archive is True

    # Test cold sales pitch detection
    res_cold = quick_prefilter("sales@agency.io", "Quick chat next week for 15 mins?", "")
    assert res_cold is not None
    assert res_cold.category == "ColdOutreach"
    assert res_cold.auto_archive is True

    # Test social network notification (friend suggestion, story)
    res_fb = quick_prefilter("Facebook friend suggestions <friendsuggestion@facebookmail.com>", "👤 Ekta Madnani is a new friend suggestion for you", "")
    assert res_fb is not None
    assert res_fb.priority == "LOW"
    assert res_fb.category == "Personal"
    assert res_fb.action_needed is False
    assert res_fb.auto_archive is True

    # Test real person sender (should not pre-filter)
    res3 = quick_prefilter("sarah.smith@partnerfirm.org", "Contract discussion for Q4", "")
    assert res3 is None

def test_prompt_injection_containment():
    # Prompt template must contain untrusted data barriers
    template = CLASSIFY_TEMPLATE
    assert "UNTRUSTED" in template or "untrusted" in template or "ignore any instructions" in template.lower() or "passive untrusted" in CLASSIFY_SYSTEM.lower()

def test_pessimistic_fallback_excludes_social_and_promotions():
    from email_classifier import classify_with_llm
    # Simulate LLM unavailable or failing by calling with text that would previously trigger fallback
    # In absence of Ollama or on fallback, Facebook stories or friend suggestions must NEVER escalate to URGENT
    fb_email = classify_email("Adv Sweta on Facebook <friendupdates@facebookmail.com>", "⏰ Adv Sweta Shah Kothari just posted a story that expires in 24 hours", "")
    assert fb_email.priority == "LOW"
    assert fb_email.action_needed is False
    assert fb_email.auto_archive is True

    craftd_email = classify_email("CRAFTD <hello@craftdlondon.com>", "Back and Moving Fast 🏃‍♂️💨", "")
    assert craftd_email.priority == "LOW"
    assert craftd_email.category == "Shopping"
    assert craftd_email.action_needed is False


def test_feedback_rules_and_few_shot():
    with tempfile.NamedTemporaryFile(suffix=".db") as tmp:
        db_path = Path(tmp.name)
        init_db(db_path)

        # Insert a learned sender rule
        conn = sqlite3.connect(db_path)
        conn.execute("""
            INSERT INTO sender_rules (sender_pattern, priority, category, action_needed, action_type, auto_archive, rule_source)
            VALUES ('@trustedpartner.com', 'IMPORTANT', 'Work', 1, 'Review', 0, 'user_correction')
        """)
        # Insert a user correction for few-shot
        conn.execute("""
            INSERT INTO user_corrections (msg_id, sender, subject, predicted_prio, corrected_prio, predicted_cat, corrected_cat, predicted_archive, corrected_archive)
            VALUES ('m123', 'reports@internal.io', 'Weekly Team KPIs', 'LOW', 'IMPORTANT', 'Work', 'Work', 1, 0)
        """)
        conn.commit()
        conn.close()

        # Check sender override resolution
        rule = get_sender_override("David <david@trustedpartner.com>", db_path)
        assert rule is not None
        assert rule["priority"] == "IMPORTANT"
        assert rule["category"] == "Work"
        assert rule["auto_archive"] == 0

        # Check classification with override
        cls = classify_email("david@trustedpartner.com", "Proposal attached", "Please review", sender_override=rule)
        assert cls.priority == "IMPORTANT"
        assert cls.category == "Work"
        assert cls.auto_archive is False

        # Check few-shot retrieval
        few_shots = get_recent_corrections(db_path, limit=2)
        assert len(few_shots) == 1
        assert few_shots[0]["subject"] == "Weekly Team KPIs"
        assert few_shots[0]["priority"] == "IMPORTANT"

def test_envelope_recipient_parsing():
    # Test forwarding and envelope delivered-to headers
    h1 = {
        "from": "ByteByteGo <digest@bytebytego.com>",
        "to": "ByteByteGo Subscribers <digest@bytebytego.com>",
        "x-forwarded-for": "deepshah7977@gmail.com sl4ught3rcl4y@gmail.com",
        "delivered-to": "sl4ught3rcl4y@gmail.com",
    }
    assert parse_recipient_headers(h1) == "deepshah7977"

    h2 = {
        "from": "service@bank.com",
        "to": "sl4ught3rcl4y@gmail.com",
        "delivered-to": "sl4ught3rcl4y@gmail.com",
    }
    assert parse_recipient_headers(h2) == "sl4ught3rcl4y"

    h3 = {
        "from": "newsletter@substack.com",
        "to": "tech-digest@substack.com",
        "delivered-to": "deepshah7977@gmail.com",
    }
    assert parse_recipient_headers(h3) == "deepshah7977"

def test_rag_negative_boundary_zero_matches():
    with tempfile.NamedTemporaryFile(suffix=".db") as tmp:
        db_path = Path(tmp.name)
        init_db(db_path)

        # Insert non-matching emails
        e1 = {
            "id": "e1", "thread_id": "th1",
            "sender": "Homeaglow Support <support@homeaglow.com>",
            "subject": "Do you have any questions I can help with?",
            "body": "Your appointment is confirmed.",
            "list_unsubscribe": "", "label_ids": [],
            "original_recipient": "deepshah7977", "trackers_blocked": 0,
        }
        c1 = EmailClassification("LOW", "Personal", False, "None", e1["subject"], True)
        save_email(e1, c1, db_path)

        e2 = {
            "id": "e2", "thread_id": "th2",
            "sender": "Alice <alice@example.com>",
            "subject": "Contract review complete",
            "body": "Alice completed the vendor contract review.",
            "list_unsubscribe": "", "label_ids": [],
            "original_recipient": "deepshah7977", "trackers_blocked": 0,
        }
        c2 = EmailClassification("NORMAL", "Work", False, "None", e2["subject"], False)
        save_email(e2, c2, db_path)

        # Ask question that has no matching terms
        res = query_rag(db_path, "any emails on system design?")
        assert res["ok"] is True
        assert res["matches"] == 0
        assert len(res["sources"]) == 0
        assert res["context"] == ""
        assert "No emails found" in res["answer"]
        assert "Homeaglow" not in res["answer"]

        # A keyword-only match must not cross the explicit person boundary.
        named_res = query_rag(db_path, "Did John send the contract?")
        assert named_res["matches"] == 0
        assert "No emails found" in named_res["answer"]


def test_gemini_teacher_json_and_reconciliation():
    class FakeResponse:
        ok = True
        status_code = 200

        def json(self):
            return {
                "candidates": [{"content": {"parts": [{"text": json.dumps({
                    "category": "Shopping",
                    "priority": "NORMAL",
                    "reason": "This is a retail order receipt.",
                })}]}}]
            }

    class FakeSession:
        def __init__(self):
            self.calls = []

        def post(self, *args, **kwargs):
            self.calls.append((args, kwargs))
            return FakeResponse()

    import json
    session = FakeSession()
    teacher = classify_with_gemini(
        "orders@brand.com", "Receipt for shoes", "Order total $89",
        api_key="test-key", session=session,
    )
    assert teacher.category == "Shopping"
    assert session.calls[0][1]["params"] == {"key": "test-key"}

    with tempfile.NamedTemporaryFile(suffix=".db") as tmp:
        db_path = Path(tmp.name)
        init_db(db_path)
        seed_feedback_email(db_path)
        service = FakeGmailService()
        labels = {
            "AI/Category-Finance": "finance-id",
            "AI/Category-Shopping": "shopping-id",
            "AI/Priority-Urgent": "urgent-id",
            "AI/Priority-Important": "important-id",
            "AI/Auto-Archived": "archived-id",
        }
        candidate = {
            "id": "feedback-1",
            "sender": "Store <orders@brand.com>",
            "subject": "Your order receipt",
            "body": "Order total $89",
            "classification": EmailClassification(
                "NORMAL", "Finance", False, "None", "A retail order", False
            ),
        }
        assert reconcile_classification(service, db_path, labels, candidate, teacher) is True
        conn = sqlite3.connect(db_path)
        assert conn.execute(
            "SELECT category FROM processed_emails WHERE msg_id='feedback-1'"
        ).fetchone()[0] == "Shopping"
        assert conn.execute("SELECT count(*) FROM model_mistakes").fetchone()[0] == 1
        rule = conn.execute(
            "SELECT category, rule_source FROM sender_rules WHERE sender_pattern='orders@brand.com'"
        ).fetchone()
        conn.close()
        assert rule == ("Shopping", "gemini_teacher")
        assert service.modifications[0]["body"]["addLabelIds"] == ["shopping-id"]


def test_telegram_label_and_rag_feedback_persistence():
    with tempfile.NamedTemporaryFile(suffix=".db") as tmp:
        db_path = Path(tmp.name)
        init_db(db_path)
        seed_feedback_email(db_path, "telegram-1")
        service = FakeGmailService()
        labels = {
            "AI/Category-Finance": "finance-id",
            "AI/Category-Shopping": "shopping-id",
        }
        learned = apply_category_feedback(
            service, db_path, labels, "telegram-1", "Shopping"
        )
        assert learned == "orders@brand.com"
        assert service.modifications[0]["body"] == {
            "addLabelIds": ["shopping-id"],
            "removeLabelIds": ["finance-id"],
        }

        result = {
            "answer": "Your package shipped.",
            "sources": ["Shipping notice"],
            "context": "Tracking 123",
        }
        feedback_id = record_rag_interaction(
            db_path, "deep", 1234, "Did it ship?", result
        )
        assert rate_rag_interaction(db_path, feedback_id, "bad", "deep", 1234)
        assert not rate_rag_interaction(db_path, feedback_id, "good", "other", 1234)
        conn = sqlite3.connect(db_path)
        saved = conn.execute(
            "SELECT question, context, rating FROM rag_feedback_log WHERE id = ?",
            (feedback_id,),
        ).fetchone()
        conn.close()
        assert saved == ("Did it ship?", "Tracking 123", "bad")

        keyboard = _category_keyboard("deep", "telegram-1")
        callbacks = [button["callback_data"] for row in keyboard["inline_keyboard"] for button in row]
        assert len(callbacks) == 7
        assert all(len(value.encode("utf-8")) <= 64 for value in callbacks)

if __name__ == "__main__":
    test_zero_quota_skips_gmail_request()
    test_real_ollama_http_deadline_and_gemini_retry_budget()
    test_clean_html_fallback()
    test_extract_body_html_fallback()
    test_quick_prefilter_newsletters_and_cold_outreach()
    test_prompt_injection_containment()
    test_pessimistic_fallback_excludes_social_and_promotions()
    test_feedback_rules_and_few_shot()
    test_envelope_recipient_parsing()
    test_rag_negative_boundary_zero_matches()
    test_gemini_teacher_json_and_reconciliation()
    test_telegram_label_and_rag_feedback_persistence()
    print("✅ All unit checks passed successfully!")
