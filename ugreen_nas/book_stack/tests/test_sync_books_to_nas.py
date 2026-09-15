import pytest
from unittest.mock import patch, MagicMock
from ugreen_nas.book_stack.sync_books_to_nas import get_existing_remote_titles

def test_get_existing_remote_titles_success():
    with patch("ugreen_nas.book_stack.sync_books_to_nas.subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(stdout="Book One\n Book Two \n\n")

        titles = get_existing_remote_titles()

        assert titles == {"book one", "book two"}
        mock_run.assert_called_once()

def test_get_existing_remote_titles_exception(capsys):
    with patch("ugreen_nas.book_stack.sync_books_to_nas.subprocess.run") as mock_run:
        mock_run.side_effect = Exception("ssh timeout")

        titles = get_existing_remote_titles()

        assert titles == set()
        mock_run.assert_called_once()

        captured = capsys.readouterr()
        assert "[!] Warning: Could not fetch existing titles from NAS: ssh timeout" in captured.out
