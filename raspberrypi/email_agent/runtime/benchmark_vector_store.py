import time
import tempfile
import sqlite3
from pathlib import Path
from unittest.mock import patch

from vector_store import init_vector_tables, batch_index_unembedded, EMBEDDING_DIM

def setup_benchmark_db(db_path: Path, num_emails: int = 100):
    conn = sqlite3.connect(db_path)
    init_vector_tables(conn)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS processed_emails (
            msg_id TEXT PRIMARY KEY,
            subject TEXT,
            sender TEXT,
            summary TEXT,
            body TEXT,
            category TEXT,
            priority TEXT,
            processed_at TEXT DEFAULT (datetime('now'))
        );
    """)
    rows = [
        (
            f"msg_{i}",
            f"Subject {i}",
            f"sender_{i}@example.com",
            f"Summary for email {i}",
            f"Body text for email {i}",
            "INBOX",
            "NORMAL"
        )
        for i in range(num_emails)
    ]
    conn.executemany("""
        INSERT INTO processed_emails (msg_id, subject, sender, summary, body, category, priority)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, rows)
    conn.commit()
    conn.close()

def dummy_compute_embedding(text: str, timeout_sec: float = 10.0):
    return [0.1] * EMBEDDING_DIM

def run_benchmark(num_emails: int = 100, runs: int = 5):
    durations = []
    for _ in range(runs):
        with tempfile.NamedTemporaryFile(suffix=".db") as tmp:
            db_path = Path(tmp.name)
            setup_benchmark_db(db_path, num_emails=num_emails)

            with patch("vector_store.compute_embedding", side_effect=dummy_compute_embedding):
                t0 = time.perf_counter()
                indexed = batch_index_unembedded(db_path, limit=num_emails)
                t1 = time.perf_counter()

            assert indexed == num_emails, f"Expected {num_emails} indexed, got {indexed}"
            durations.append(t1 - t0)

    avg_time = sum(durations) / len(durations)
    print(f"Benchmark: {num_emails} emails, {runs} runs.")
    print(f"Durations: {[round(d * 1000, 2) for d in durations]} ms")
    print(f"Average time: {avg_time * 1000:.2f} ms")
    return avg_time

if __name__ == "__main__":
    run_benchmark()
