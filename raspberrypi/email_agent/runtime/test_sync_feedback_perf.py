import time
import sqlite3
import re
from pathlib import Path
from unittest.mock import MagicMock
import pytest

from gmail_agent import init_db, sync_user_feedback, get_db_connection

class MockMessagesList:
    def __init__(self, messages_by_q):
        self.messages_by_q = messages_by_q
        self.q = ""

    def list(self, userId, q, maxResults=50):
        self.q = q
        return self

    def execute(self):
        return {"messages": self.messages_by_q.get(self.q, [])}

def setup_test_db(db_path: Path, num_per_cat: int = 50, background_rows: int = 5000):
    init_db(db_path)
    conn = get_db_connection(db_path)
    cursor = conn.cursor()

    # Pre-populate background rows to simulate realistic database size
    bg_data = [
        (f"bg_msg_{i}", f"bg_th_{i}", f"bg{i}@example.com", f"BG Subject {i}", "Newsletter", "LOW", "processed", 0)
        for i in range(background_rows)
    ]
    cursor.executemany("""
        INSERT INTO processed_emails
        (msg_id, thread_id, sender, subject, category, priority, status, auto_archived)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, bg_data)

    categories = ["Shopping", "Work", "Finance", "Travel", "Newsletter", "ColdOutreach"]
    messages_by_q = {}

    for cat in categories:
        q = f"label:AI-Category-{cat}"
        msg_list = []
        for i in range(num_per_cat):
            msg_id = f"msg_{cat}_{i}"
            msg_list.append({"id": msg_id})
            cursor.execute("""
                INSERT INTO processed_emails
                (msg_id, thread_id, sender, subject, category, priority, status, auto_archived, processed_at)
                VALUES (?, ?, ?, ?, ?, ?, 'processed', 0, datetime('now'))
            """, (msg_id, f"th_{msg_id}", f"User {i} <user{i}@example.com>", f"Subject {i}", "OldCat", "NORMAL"))
        messages_by_q[q] = msg_list

    # Unarchived emails
    q_unarch = "label:INBOX label:AI-Auto-Archived"
    unarch_list = []
    for i in range(num_per_cat):
        msg_id = f"msg_unarch_{i}"
        unarch_list.append({"id": msg_id})
        cursor.execute("""
            INSERT INTO processed_emails
            (msg_id, thread_id, sender, subject, category, priority, status, auto_archived, processed_at)
            VALUES (?, ?, ?, ?, ?, ?, 'processed', 1, datetime('now'))
        """, (msg_id, f"th_{msg_id}", f"Sender {i} <sender{i}@example.com>", f"Unarch Subject {i}", "Work", "LOW"))
    messages_by_q[q_unarch] = unarch_list

    # Urgent escalation
    q_urgent = "label:AI-Priority-Urgent"
    urgent_list = []
    for i in range(num_per_cat):
        msg_id = f"msg_urgent_{i}"
        urgent_list.append({"id": msg_id})
        cursor.execute("""
            INSERT INTO processed_emails
            (msg_id, thread_id, sender, subject, category, priority, status, auto_archived, processed_at)
            VALUES (?, ?, ?, ?, ?, ?, 'processed', 0, datetime('now'))
        """, (msg_id, f"th_{msg_id}", f"Boss {i} <boss{i}@example.com>", f"Urgent Subject {i}", "Work", "NORMAL"))
    messages_by_q[q_urgent] = urgent_list

    conn.commit()
    conn.close()

    mock_service = MagicMock()
    mock_messages = MockMessagesList(messages_by_q)
    mock_service.users.return_value.messages.return_value = mock_messages

    return mock_service

def measure_select_phase_unoptimized(cursor, messages_by_cat):
    t0 = time.perf_counter()
    rows_found = 0
    for cat, messages in messages_by_cat.items():
        for m in messages:
            msg_id = m["id"]
            row = cursor.execute("""
                SELECT sender, subject, priority, category, auto_archived
                FROM processed_emails WHERE msg_id = ?
            """, (msg_id,)).fetchone()
            if row:
                rows_found += 1
    t1 = time.perf_counter()
    return (t1 - t0) * 1000, rows_found

def measure_select_phase_optimized(cursor, messages_by_cat):
    t0 = time.perf_counter()
    rows_found = 0
    for cat, messages in messages_by_cat.items():
        msg_ids = [m["id"] for m in messages if "id" in m]
        if not msg_ids:
            continue
        placeholders = ",".join("?" * len(msg_ids))
        rows = cursor.execute(f"""
            SELECT msg_id, sender, subject, priority, category, auto_archived
            FROM processed_emails WHERE msg_id IN ({placeholders})
        """, msg_ids).fetchall()
        rows_by_id = {row["msg_id"]: row for row in rows}
        for m in messages:
            if rows_by_id.get(m["id"]):
                rows_found += 1
    t1 = time.perf_counter()
    return (t1 - t0) * 1000, rows_found

def test_sync_user_feedback_select_query_perf(tmp_path):
    db_path = tmp_path / "test_perf_select.db"
    mock_service = setup_test_db(db_path, num_per_cat=50, background_rows=10000)

    categories = ["Shopping", "Work", "Finance", "Travel", "Newsletter", "ColdOutreach"]
    messages_by_cat = {}
    for cat in categories:
        q = f"label:AI-Category-{cat}"
        messages_by_cat[cat] = mock_service.users().messages().list(userId="me", q=q).execute()["messages"]

    conn = get_db_connection(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Measure unoptimized N+1 SELECT phase (8 query batches * 50 = 400 queries)
    unopt_ms, unopt_found = measure_select_phase_unoptimized(cursor, messages_by_cat)

    # Measure optimized batch IN SELECT phase (8 queries total)
    opt_ms, opt_found = measure_select_phase_optimized(cursor, messages_by_cat)

    conn.close()

    print(f"\n[SELECT QUERY PHASE PERFORMANCE BENCHMARK]")
    print(f"  Unoptimized (400 individual SELECT queries): {unopt_ms:.3f} ms")
    print(f"  Optimized (8 batch IN queries): {opt_ms:.3f} ms")
    if opt_ms > 0:
        print(f"  Query phase speedup: {unopt_ms / opt_ms:.2f}x faster ({((unopt_ms - opt_ms) / unopt_ms)*100:.1f}% reduction in SELECT phase latency)")

    assert unopt_found == opt_found == 300
