import sqlite3
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from vector_store import (
    init_vector_tables,
    upsert_email_embedding,
    batch_index_unembedded,
    EMBEDDING_DIM,
)

@pytest.fixture
def temp_db():
    with tempfile.NamedTemporaryFile(suffix=".db") as tmp:
        db_path = Path(tmp.name)
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
        conn.commit()
        conn.close()
        yield db_path

def dummy_compute_embedding(text: str, timeout_sec: float = 10.0):
    return [0.1] * EMBEDDING_DIM

def test_upsert_email_embedding_with_and_without_conn(temp_db):
    with patch("vector_store.compute_embedding", side_effect=dummy_compute_embedding):
        # Without passing connection
        res1 = upsert_email_embedding(temp_db, "m1", "Subject 1", "sender1@example.com", "Summary 1")
        assert res1 is True

        # With passed connection
        conn = sqlite3.connect(temp_db)
        res2 = upsert_email_embedding(
            temp_db, "m2", "Subject 2", "sender2@example.com", "Summary 2", conn=conn
        )
        assert res2 is True
        conn.close()

    conn = sqlite3.connect(temp_db)
    cursor = conn.execute("SELECT msg_id FROM email_embeddings ORDER BY msg_id")
    rows = [r[0] for r in cursor.fetchall()]
    conn.close()
    assert rows == ["m1", "m2"]

def test_batch_index_unembedded_reuses_connection(temp_db):
    conn = sqlite3.connect(temp_db)
    conn.execute("""
        INSERT INTO processed_emails (msg_id, subject, sender, summary)
        VALUES ('msg_1', 'Sub1', 'sen1@test.com', 'Sum1'),
               ('msg_2', 'Sub2', 'sen2@test.com', 'Sum2')
    """)
    conn.commit()
    conn.close()

    with patch("vector_store.compute_embedding", side_effect=dummy_compute_embedding):
        with patch("sqlite3.connect", wraps=sqlite3.connect) as mock_connect:
            indexed = batch_index_unembedded(temp_db, limit=10)
            assert indexed == 2
            # Connection to db_path should be created only once inside batch_index_unembedded
            db_connect_calls = [
                call for call in mock_connect.call_args_list if call.args and call.args[0] == temp_db
            ]
            assert len(db_connect_calls) == 1
