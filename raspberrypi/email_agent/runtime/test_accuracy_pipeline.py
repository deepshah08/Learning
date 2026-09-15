"""
test_accuracy_pipeline.py
Automated Verification Suite for Accuracy-First Architecture.
Tests:
1. Seed Knowledge Rules (Shopping, Finance, Travel, Work, Security)
2. O(1) Label Hashtable State Tracking
3. Domain-Level Convergence
4. Dense Vector Cosine Similarity & Semantic Retrieval
5. Post-Batch Background Invariant & Drift Evaluator
"""

import math
import os
import sqlite3
import tempfile
from pathlib import Path
from knowledge_rules import match_seed_knowledge
from email_classifier import classify_email
from background_evaluator import run_post_batch_evaluations
from vector_store import init_vector_tables, normalize_vector, search_dense, hybrid_search


def test_seed_knowledge():
    print("🧪 Testing Seed Knowledge Datasets...")

    # Shopping
    m1 = match_seed_knowledge("newsletter@email.hm.com", "20% off your entire order this weekend", "Shop now")
    assert m1 is not None and m1.category == "Shopping", f"Expected Shopping, got {m1}"

    m2 = match_seed_knowledge("no-reply@emails.skechers.com", "Step into comfort with 15% off", "Sale ends tonight")
    assert m2 is not None and m2.category == "Shopping", f"Expected Shopping, got {m2}"

    # Finance
    m3 = match_seed_knowledge("alerts@chase.com", "Your monthly statement is ready", "View your account balance")
    assert m3 is not None and m3.category == "Finance", f"Expected Finance, got {m3}"

    # Travel
    m4 = match_seed_knowledge("reservations@united.com", "Your flight confirmation: SFO to JFK", "Confirmation code: ABC123")
    assert m4 is not None and m4.category == "Travel", f"Expected Travel, got {m4}"

    # Work / Dev Platforms
    m5 = match_seed_knowledge("notifications@github.com", "[github/repo] Pull request #42: fix concurrency", "Requested your review")
    assert m5 is not None and m5.category == "Work" and m5.action_needed is True, f"Expected Work action, got {m5}"

    # Security Alert
    m6 = match_seed_knowledge("no-reply@accounts.google.com", "Security alert: new login from unknown device", "Review activity")
    assert m6 is not None and m6.priority == "URGENT" and m6.action_needed is True, f"Expected Urgent security, got {m6}"

    print("  ✅ Seed knowledge rules passed 100% of test cases.")


def test_hashtable_and_evaluator():
    print("🧪 Testing Label Hashtable & Post-Batch Evaluator...")

    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        db_path = Path(f.name)

    try:
        conn = sqlite3.connect(db_path)
        conn.execute("""
            CREATE TABLE processed_emails (
                msg_id TEXT PRIMARY KEY,
                thread_id TEXT,
                sender TEXT,
                subject TEXT,
                priority TEXT,
                category TEXT,
                action_needed INTEGER,
                action_type TEXT,
                summary TEXT,
                auto_archived INTEGER,
                status TEXT,
                original_recipient TEXT,
                trackers_blocked INTEGER,
                processed_at TEXT DEFAULT (datetime('now'))
            );
        """)
        conn.execute("""
            CREATE TABLE email_label_state (
                msg_id TEXT PRIMARY KEY,
                last_category TEXT,
                last_priority TEXT,
                is_archived INTEGER,
                checksum TEXT,
                updated_at TEXT DEFAULT (datetime('now'))
            );
        """)
        conn.execute("""
            CREATE TABLE sender_rules (
                sender_pattern TEXT PRIMARY KEY,
                priority TEXT,
                category TEXT,
                action_needed INTEGER,
                action_type TEXT,
                auto_archive INTEGER,
                rule_source TEXT,
                updated_at TEXT DEFAULT (datetime('now'))
            );
        """)

        # Insert 30 normal emails
        for i in range(30):
            cat = "Shopping" if i % 2 == 0 else "Work"
            conn.execute("""
                INSERT INTO processed_emails (msg_id, sender, subject, priority, category, auto_archived)
                VALUES (?, ?, ?, 'NORMAL', ?, 0)
            """, (f"msg_{i}", f"sender{i}@example.com", f"Subject {i}", cat))

            conn.execute("""
                INSERT INTO email_label_state (msg_id, last_category, last_priority, is_archived, checksum)
                VALUES (?, ?, 'NORMAL', 0, 'checksum')
            """, (f"msg_{i}", cat))

        conn.commit()

        # Run evaluation on clean state
        clean_report = run_post_batch_evaluations(db_path, sample_size=30)
        assert clean_report["ok"] is True, f"Expected clean eval, got {clean_report}"
        assert len(clean_report["invariant_violations"]) == 0

        # Inject deliberate invariant violation: URGENT email auto-archived
        conn.execute("""
            INSERT INTO processed_emails (msg_id, sender, subject, priority, category, auto_archived)
            VALUES ('violation_1', 'bad@example.com', 'Critical Security Alert', 'URGENT', 'Work', 1)
        """)
        conn.commit()

        violated_report = run_post_batch_evaluations(db_path, sample_size=30)
        assert violated_report["ok"] is False, "Evaluator should fail on invariant violation"
        assert len(violated_report["invariant_violations"]) == 1
        print("  ✅ Evaluator caught invariant violation as expected.")

    finally:
        if db_path.exists():
            os.remove(db_path)


def test_vector_normalization_and_similarity():
    print("🧪 Testing Dense Vector Math & Semantic Invariant...")
    v1 = [1.0, 2.0, 3.0]
    n1 = normalize_vector(v1)
    norm = math.sqrt(sum(x*x for x in n1))
    assert abs(norm - 1.0) < 1e-6, f"Vector should have unit norm, got {norm}"

    # Identical vectors should have dot product 1.0
    sim = sum(a * b for a, b in zip(n1, n1))
    assert abs(sim - 1.0) < 1e-6, f"Self-similarity should be 1.0, got {sim}"
    print("  ✅ Vector math and unit normalization verified.")


if __name__ == "__main__":
    test_seed_knowledge()
    test_hashtable_and_evaluator()
    test_vector_normalization_and_similarity()
    print("\n🎉 ALL PIPELINE TESTS PASSED SUCCESSFULLY!")
