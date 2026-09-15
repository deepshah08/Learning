"""
background_evaluator.py
Autonomous Post-Batch Background Verification & Drift Detection Daemon.
Runs after every 6-hour email batch to verify invariants, audit category drift,
and catch biases or rule conflicts before they impact user trust.
"""

import logging
import sqlite3
from collections import Counter
from pathlib import Path
from typing import Dict, Any, List

logger = logging.getLogger(__name__)


def run_post_batch_evaluations(db_path: Path, sample_size: int = 100) -> Dict[str, Any]:
    """
    Run automated post-batch verification suite on the SQLite database:
    1. Invariant: 0 URGENT or IMPORTANT emails auto-archived.
    2. Invariant: Valid categories and priorities across all records.
    3. Drift & Bias: Category distribution skew detector.
    4. Rule Conflict: Cross-reference recent emails against active sender_rules.
    """
    report = {
        "ok": True,
        "sample_size": 0,
        "invariant_violations": [],
        "drift_warnings": [],
        "rule_conflicts": [],
        "category_distribution": {},
        "health_score": 100.0,
    }

    if not db_path.exists():
        report["ok"] = False
        report["error"] = "Database not found"
        return report

    conn = sqlite3.connect(db_path, timeout=10.0)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    # 1. Invariant Check: Auto-archive on Urgent/Important
    violations = c.execute("""
        SELECT msg_id, sender, subject, priority, category
        FROM processed_emails
        WHERE auto_archived = 1 AND priority IN ('URGENT', 'IMPORTANT')
    """).fetchall()

    for v in violations:
        msg = f"CRITICAL: Priority '{v['priority']}' email auto-archived: '{v['subject'][:40]}' from {v['sender'][:30]}"
        report["invariant_violations"].append(msg)
        logger.error(f"[INVARIANT VIOLATION] {msg}")

    # 2. Invariant Check: Null or invalid fields
    invalid_rows = c.execute("""
        SELECT msg_id, subject
        FROM processed_emails
        WHERE priority IS NULL OR category IS NULL OR priority = '' OR category = ''
    """).fetchall()
    for inv in invalid_rows:
        msg = f"Invalid schema state: msg_id {inv['msg_id']} has empty priority or category"
        report["invariant_violations"].append(msg)

    # 3. Category Distribution Drift & Bias Detection
    recent = c.execute("""
        SELECT category, priority, auto_archived
        FROM processed_emails
        ORDER BY processed_at DESC LIMIT ?
    """, (sample_size,)).fetchall()

    report["sample_size"] = len(recent)
    if recent:
        cat_counts = Counter(r["category"] for r in recent)
        total = len(recent)
        report["category_distribution"] = {k: f"{(v / total) * 100:.1f}% ({v})" for k, v in cat_counts.items()}

        # Alert if single category skews beyond 65% on large samples
        if total >= 25:
            for cat, cnt in cat_counts.items():
                ratio = cnt / total
                if ratio > 0.65:
                    warn = f"Distribution Skew: Category '{cat}' represents {ratio*100:.1f}% of recent emails (>65% threshold)"
                    report["drift_warnings"].append(warn)
                    logger.warning(f"[DRIFT DETECTED] {warn}")

    # 4. Learned Rule Conflict Audit
    rules = c.execute("""
        SELECT sender_pattern, category, priority, auto_archive, updated_at
        FROM sender_rules
    """).fetchall()

    for rule in rules:
        pat = rule["sender_pattern"].lower()
        rule_cat = rule["category"]
        conflicts = c.execute("""
            SELECT msg_id, sender, subject, category
            FROM processed_emails
            WHERE LOWER(sender) LIKE ?
              AND category != ?
              AND datetime(processed_at) >= datetime(?)
              AND status != 'corrected'
            ORDER BY processed_at DESC LIMIT 5
        """, (f"%{pat}%", rule_cat, rule["updated_at"])).fetchall()

        for conf in conflicts:
            c_msg = f"Rule Conflict: Sender {conf['sender'][:35]} classified as '{conf['category']}' but sender_rule dictates '{rule_cat}'"
            report["rule_conflicts"].append(c_msg)
            logger.warning(f"[RULE CONFLICT] {c_msg}")

    conn.close()

    # Calculate overall health score
    deductions = (
        len(report["invariant_violations"]) * 25 +
        len(report["drift_warnings"]) * 10 +
        len(report["rule_conflicts"]) * 5
    )
    report["health_score"] = max(0.0, 100.0 - deductions)
    report["ok"] = len(report["invariant_violations"]) == 0 and report["health_score"] >= 70.0

    return report


def dispatch_eval_alert_if_needed(report: Dict[str, Any], chat_id: str | int):
    """Notify user via Telegram if invariants or critical drifts are detected."""
    if report["ok"]:
        return

    try:
        from notifier import send_telegram_direct
        lines = [f"⚠️ Email Intelligence Guardrail Alert (Score: {report['health_score']:.0f}%)\n"]

        if report["invariant_violations"]:
            lines.append("🔴 Safety Invariant Violations:")
            for iv in report["invariant_violations"][:3]:
                lines.append(f"  • {iv}")
            lines.append("")

        if report["drift_warnings"]:
            lines.append("🟡 Model Drift Warnings:")
            for dw in report["drift_warnings"][:2]:
                lines.append(f"  • {dw}")
            lines.append("")

        if report["rule_conflicts"]:
            lines.append("🟠 Learned Rule Conflicts:")
            for rc in report["rule_conflicts"][:2]:
                lines.append(f"  • {rc}")

        send_telegram_direct(chat_id, "\n".join(lines))
    except Exception as e:
        logger.debug(f"Failed to dispatch eval alert: {e}")
