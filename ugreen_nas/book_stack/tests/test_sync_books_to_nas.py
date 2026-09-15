import os
import sys
import pytest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sync_books_to_nas import get_existing_remote_titles


def test_get_existing_remote_titles_success():
    with patch('sync_books_to_nas.subprocess.run') as mock_run:
        mock_result = MagicMock()
        mock_result.stdout = "Title One\nTitle Two\n  Title Three  \n"
        mock_run.return_value = mock_result

        titles = get_existing_remote_titles()

        assert titles == {"title one", "title two", "title three"}
        mock_run.assert_called_once()
        cmd_called = mock_run.call_args[0][0]
        assert "ssh" in cmd_called
        assert "nas" in cmd_called
        assert "sqlite3" in cmd_called[2]


def test_get_existing_remote_titles_empty():
    with patch('sync_books_to_nas.subprocess.run') as mock_run:
        mock_result = MagicMock()
        mock_result.stdout = ""
        mock_run.return_value = mock_result

        titles = get_existing_remote_titles()

        assert titles == set()


def test_get_existing_remote_titles_exception():
    with patch('sync_books_to_nas.subprocess.run') as mock_run:
        mock_run.side_effect = Exception("Connection failed")

        titles = get_existing_remote_titles()

        assert titles == set()


def test_get_existing_remote_titles_timeout():
    with patch('sync_books_to_nas.subprocess.run') as mock_run:
        import subprocess
        mock_run.side_effect = subprocess.TimeoutExpired(cmd="ssh", timeout=10)

        titles = get_existing_remote_titles()

        assert titles == set()
