"""
vector_store.py
Dense Vector Embeddings & Hybrid RAG Retrieval Engine for Pi-loop Email Intelligence.
Uses local Ollama all-minilm (384 dimensions) for semantic email retrieval.
"""

import json
import logging
import math
import re
import sqlite3
from pathlib import Path
from typing import List, Dict, Any, Optional

try:
    import requests
except ImportError:
    requests = None

logger = logging.getLogger(__name__)

EMBEDDING_MODEL = "all-minilm"
OLLAMA_EMBED_URL = "http://127.0.0.1:11434/api/embeddings"
EMBEDDING_DIM = 384


def init_vector_tables(conn: sqlite3.Connection):
    """Create email_embeddings table and indexes if they do not exist."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS email_embeddings (
            msg_id      TEXT PRIMARY KEY,
            embedding   TEXT,
            subject     TEXT,
            sender      TEXT,
            summary     TEXT,
            created_at  TEXT DEFAULT (datetime('now'))
        );
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_emb_created ON email_embeddings(created_at);")


def normalize_vector(vec: List[float]) -> List[float]:
    """Compute L2 unit norm so cosine similarity equals dot product."""
    norm = math.sqrt(sum(x * x for x in vec))
    if norm < 1e-9:
        return vec
    return [x / norm for x in vec]


def compute_embedding(text: str, timeout_sec: float = 10.0) -> Optional[List[float]]:
    """Generate 384-dimensional vector embedding via Ollama all-minilm."""
    if not requests:
        return None

    clean_text = text.replace("\n", " ").strip()[:800]
    if not clean_text:
        return None

    try:
        resp = requests.post(
            OLLAMA_EMBED_URL,
            json={"model": EMBEDDING_MODEL, "prompt": clean_text, "keep_alive": "15m"},
            timeout=timeout_sec,
        )
        if resp.status_code == 200:
            data = resp.json()
            vec = data.get("embedding", [])
            if len(vec) == EMBEDDING_DIM:
                return normalize_vector(vec)
        logger.warning(f"Embedding API returned status {resp.status_code}: {resp.text[:100]}")
    except Exception as e:
        logger.debug(f"Failed to generate embedding: {e}")

    return None


def upsert_email_embedding(
    db_path: Path,
    msg_id: str,
    subject: str,
    sender: str,
    summary: str,
    body_snippet: str = "",
) -> bool:
    """Compute embedding for an email and store in SQLite."""
    text_to_embed = f"Subject: {subject} | From: {sender} | Summary: {summary} | Context: {body_snippet[:300]}"
    vec = compute_embedding(text_to_embed)
    if not vec:
        return False

    conn = sqlite3.connect(db_path, timeout=10.0)
    init_vector_tables(conn)
    conn.execute("""
        INSERT OR REPLACE INTO email_embeddings (msg_id, embedding, subject, sender, summary, created_at)
        VALUES (?, ?, ?, ?, ?, datetime('now'))
    """, (msg_id, json.dumps(vec), subject, sender, summary))
    conn.commit()
    conn.close()
    return True


def batch_index_unembedded(db_path: Path, limit: int = 50) -> int:
    """Find processed emails without embeddings and generate them in batch."""
    conn = sqlite3.connect(db_path, timeout=15.0)
    init_vector_tables(conn)
    conn.row_factory = sqlite3.Row

    rows = conn.execute("""
        SELECT p.msg_id, p.subject, p.sender, p.summary
        FROM processed_emails p
        LEFT JOIN email_embeddings e ON p.msg_id = e.msg_id
        WHERE e.msg_id IS NULL
        ORDER BY p.processed_at DESC
        LIMIT ?
    """, (limit,)).fetchall()
    conn.close()

    if not rows:
        return 0

    count = 0
    for r in rows:
        ok = upsert_email_embedding(
            db_path,
            r["msg_id"],
            r["subject"] or "",
            r["sender"] or "",
            r["summary"] or "",
        )
        if ok:
            count += 1
    return count


def search_dense(db_path: Path, query: str, top_k: int = 6) -> List[Dict[str, Any]]:
    """Perform dense vector cosine similarity search."""
    q_vec = compute_embedding(query)
    if not q_vec:
        return []

    conn = sqlite3.connect(db_path, timeout=10.0)
    init_vector_tables(conn)
    conn.row_factory = sqlite3.Row

    rows = conn.execute("""
        SELECT e.msg_id, e.embedding, e.subject, e.sender, e.summary, p.processed_at, p.category, p.priority
        FROM email_embeddings e
        JOIN processed_emails p ON e.msg_id = p.msg_id
    """).fetchall()
    conn.close()

    if not rows:
        return []

    scored = []
    for r in rows:
        try:
            emb = json.loads(r["embedding"])
            # Vectors are pre-normalized, so dot product = cosine similarity
            sim = sum(a * b for a, b in zip(q_vec, emb))
            scored.append({
                "msg_id": r["msg_id"],
                "subject": r["subject"],
                "sender": r["sender"],
                "summary": r["summary"],
                "category": r["category"],
                "priority": r["priority"],
                "processed_at": r["processed_at"],
                "score": sim,
            })
        except Exception:
            continue

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:top_k]


def hybrid_search(db_path: Path, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
    """
    Hybrid Search combining:
    1. Dense semantic search (all-minilm cosine similarity)
    2. Sparse lexical search (SQLite FTS5 BM25)
    Fused using Reciprocal Rank Fusion (RRF).
    """
    dense_results = search_dense(db_path, query, top_k=10)

    # Sparse FTS5 search
    conn = sqlite3.connect(db_path, timeout=10.0)
    conn.row_factory = sqlite3.Row

    raw_terms = re.findall(r'\w+', query.lower())
    stop_words = {"the", "a", "an", "is", "in", "on", "of", "to", "for", "any", "email", "emails", "did", "what", "from"}
    terms = [t for t in raw_terms if len(t) > 2 and t not in stop_words]

    sparse_results = []
    if terms:
        fts_query = " OR ".join(f'"{t}"*' for t in terms)
        try:
            rows = conn.execute("""
                SELECT e.msg_id, e.sender, e.subject, e.summary, e.category, e.priority, e.processed_at
                FROM emails_fts f
                JOIN processed_emails e ON f.msg_id = e.msg_id
                WHERE emails_fts MATCH ?
                ORDER BY rank LIMIT 10
            """, (fts_query,)).fetchall()
            sparse_results = [dict(r) for r in rows]
        except Exception as e:
            logger.debug(f"FTS query error: {e}")
    conn.close()

    # Reciprocal Rank Fusion (RRF) with k=60
    K = 60
    rrf_scores = {}
    doc_map = {}

    for rank, doc in enumerate(dense_results):
        mid = doc["msg_id"]
        doc_map[mid] = doc
        rrf_scores[mid] = rrf_scores.get(mid, 0.0) + 1.0 / (K + rank + 1)

    for rank, doc in enumerate(sparse_results):
        mid = doc["msg_id"]
        if mid not in doc_map:
            doc_map[mid] = doc
        rrf_scores[mid] = rrf_scores.get(mid, 0.0) + 1.0 / (K + rank + 1)

    ranked_mids = sorted(rrf_scores.keys(), key=lambda x: rrf_scores[x], reverse=True)
    fused = []
    for mid in ranked_mids[:top_k]:
        item = doc_map[mid].copy()
        item["rrf_score"] = rrf_scores[mid]
        fused.append(item)

    return fused
