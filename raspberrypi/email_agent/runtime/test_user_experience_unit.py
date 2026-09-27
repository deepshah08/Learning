from pathlib import Path
from unittest.mock import patch

from test_user_experience import run_personas, render_report, PERSONAS


def test_run_personas_without_judge():
    dummy_db = Path("/tmp/dummy.db")
    mock_rag = lambda db, q: {"matches": 1, "answer": f"Answer for {q}", "context": f"Context for {q}"}

    with patch("test_user_experience.query_rag", side_effect=mock_rag):
        entries = run_personas(dummy_db, use_gemini_judge=False)
        assert len(entries) == len(PERSONAS)
        for entry in entries:
            assert "scores" not in entry
            assert "judge_error" not in entry


def test_run_personas_with_judge_success():
    dummy_db = Path("/tmp/dummy.db")
    mock_rag = lambda db, q: {"matches": 1, "answer": f"Answer for {q}", "context": f"Context for {q}"}
    def mock_judge(q, a, c):
        return {
            "faithfulness": 80.0,
            "relevance": 90.0,
            "completeness": 85.0,
            "finding": f"Good for {q}"
        }

    with patch("test_user_experience.query_rag", side_effect=mock_rag), \
         patch("test_user_experience.judge_answer", side_effect=mock_judge):
        entries = run_personas(dummy_db, use_gemini_judge=True)
        assert len(entries) == len(PERSONAS)
        for entry in entries:
            assert "scores" in entry
            assert entry["scores"]["faithfulness"] == 80.0
            assert "judge_error" not in entry


def test_run_personas_with_judge_errors():
    dummy_db = Path("/tmp/dummy.db")
    mock_rag = lambda db, q: {"matches": 1, "answer": f"Answer for {q}", "context": f"Context for {q}"}
    def mock_judge(q, a, c):
        if "urgent" in q:
            raise RuntimeError("API quota exceeded")
        return {
            "faithfulness": 100.0,
            "relevance": 100.0,
            "completeness": 100.0,
            "finding": "Perfect"
        }

    with patch("test_user_experience.query_rag", side_effect=mock_rag), \
         patch("test_user_experience.judge_answer", side_effect=mock_judge):
        entries = run_personas(dummy_db, use_gemini_judge=True)
        assert len(entries) == len(PERSONAS)
        urgent_entry = next(e for e in entries if "urgent" in e["question"])
        assert "judge_error" in urgent_entry
        assert urgent_entry["judge_error"] == "API quota exceeded"

        other_entry = next(e for e in entries if "urgent" not in e["question"])
        assert "scores" in other_entry


def test_render_report():
    entries = [
        {
            "persona": "TestPersona",
            "question": "test query?",
            "matches": 1,
            "boundary_ok": True,
            "answer": "test answer",
            "scores": {
                "faithfulness": 90.0,
                "relevance": 95.0,
                "completeness": 80.0,
                "finding": "Looks solid"
            }
        }
    ]
    report = render_report(entries)
    assert "# Pi-loop Executive Persona Report" in report
    assert "Average faithfulness: 90.0%" in report
    assert "Judge: faithfulness=90% relevance=95% completeness=80% — Looks solid" in report
