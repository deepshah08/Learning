import time
from pathlib import Path
from unittest.mock import patch

from test_user_experience import run_personas

def mock_query_rag(db_path, question):
    return {
        "matches": 1,
        "answer": f"Mock answer for {question}",
        "context": f"Mock context for {question}"
    }

def mock_judge_answer(question, answer, context):
    time.sleep(0.2)  # Simulate 200ms Gemini API call latency
    return {
        "faithfulness": 90.0,
        "relevance": 95.0,
        "completeness": 85.0,
        "finding": "Good response"
    }

def main():
    db_path = Path("/tmp/dummy_db.db")
    with patch("test_user_experience.query_rag", side_effect=mock_query_rag), \
         patch("test_user_experience.judge_answer", side_effect=mock_judge_answer):

        start = time.monotonic()
        entries = run_personas(db_path, use_gemini_judge=True)
        duration = time.monotonic() - start

        print(f"Executed run_personas for {len(entries)} personas in {duration:.4f} seconds")
        print(f"Scored entries count: {sum(1 for e in entries if 'scores' in e)}")

if __name__ == "__main__":
    main()
