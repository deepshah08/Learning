import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sync_books_to_nas import get_existing_remote_titles, find_books, sync_books

@patch("sync_books_to_nas.subprocess.run")
def test_get_existing_remote_titles_success(mock_run):
    mock_res = MagicMock()
    mock_res.stdout = "Title One\nTitle Two\n\nTitle Three\n"
    mock_run.return_value = mock_res

    titles = get_existing_remote_titles()

    assert mock_run.called
    assert titles == {"title one", "title two", "title three"}

@patch("sync_books_to_nas.subprocess.run")
def test_get_existing_remote_titles_failure(mock_run):
    mock_run.side_effect = Exception("Mocked subprocess failure")

    titles = get_existing_remote_titles()

    assert mock_run.called
    assert titles == set()

def test_find_books(tmp_path):
    # Valid files
    (tmp_path / "book1.epub").touch()
    (tmp_path / "book2.pdf").touch()
    (tmp_path / "book3.MOBI").touch() # Test case-insensitivity

    # Invalid files / hidden files
    (tmp_path / "image.jpg").touch()
    (tmp_path / ".hidden_book.epub").touch()

    # Subdirectories
    sub_dir = tmp_path / "subfolder"
    sub_dir.mkdir()
    (sub_dir / "book4.azw3").touch()
    (sub_dir / "ignore.txt").touch()

    books = find_books(tmp_path)

    assert len(books) == 4
    # find_books returns sorted(books)
    expected = sorted([
        tmp_path / "book1.epub",
        tmp_path / "book2.pdf",
        tmp_path / "book3.MOBI",
        sub_dir / "book4.azw3"
    ])
    assert books == expected

@patch("sync_books_to_nas.sys.exit")
def test_sync_books_directory_not_exist(mock_exit, tmp_path):
    non_existent_dir = tmp_path / "does_not_exist"
    sync_books(non_existent_dir)
    mock_exit.assert_called_once_with(1)

@patch("sync_books_to_nas.get_existing_remote_titles")
@patch("sync_books_to_nas.subprocess.run")
def test_sync_books_dry_run(mock_run, mock_get_titles, tmp_path):
    mock_get_titles.return_value = set()
    (tmp_path / "book1.epub").touch()

    sync_books(tmp_path, dry_run=True)

    mock_run.assert_not_called()

@patch("sync_books_to_nas.get_existing_remote_titles")
@patch("sync_books_to_nas.subprocess.run")
@patch("sync_books_to_nas.time.sleep")
def test_sync_books_upload_success(mock_sleep, mock_run, mock_get_titles, tmp_path):
    mock_get_titles.return_value = set()
    (tmp_path / "book1.epub").touch()

    mock_res = MagicMock()
    mock_res.returncode = 0
    mock_run.return_value = mock_res

    sync_books(tmp_path, dry_run=False)

    mock_run.assert_called_once()
    mock_sleep.assert_called_once_with(2.0)

@patch("sync_books_to_nas.get_existing_remote_titles")
@patch("sync_books_to_nas.subprocess.run")
@patch("sync_books_to_nas.time.sleep")
def test_sync_books_upload_failure(mock_sleep, mock_run, mock_get_titles, tmp_path):
    mock_get_titles.return_value = set()
    (tmp_path / "book1.epub").touch()

    mock_res = MagicMock()
    mock_res.returncode = 1
    mock_res.stderr = "Error msg"
    mock_run.return_value = mock_res

    sync_books(tmp_path, dry_run=False)

    mock_run.assert_called_once()
    mock_sleep.assert_not_called()

@patch("sync_books_to_nas.get_existing_remote_titles")
@patch("sync_books_to_nas.subprocess.run")
def test_sync_books_skip_existing(mock_run, mock_get_titles, tmp_path):
    mock_get_titles.return_value = {"existing book title"}

    # Needs to be > 4 chars, and stem match
    (tmp_path / "Existing Book Title.epub").touch()
    (tmp_path / "New Book Title.epub").touch()

    sync_books(tmp_path, dry_run=True)

    # It shouldn't have tried to run subprocess since it's dry_run, but wait,
    # we want to verify it was skipped. We can verify uploaded count if it was returned,
    # but it's printed. Let's capture stdout or just rely on dry_run not doing anything.
    # Actually, let's verify subprocess.run isn't called even if dry_run=False
    sync_books(tmp_path, dry_run=False)

    # It should only call subprocess for the new book
    assert mock_run.call_count == 1
    args, _ = mock_run.call_args
    assert "New Book Title.epub" in args[0][2]

@patch("sync_books_to_nas.get_existing_remote_titles")
@patch("sync_books_to_nas.subprocess.run")
@patch("sync_books_to_nas.time.sleep")
def test_sync_books_limit(mock_sleep, mock_run, mock_get_titles, tmp_path):
    mock_get_titles.return_value = set()
    (tmp_path / "book1.epub").touch()
    (tmp_path / "book2.epub").touch()
    (tmp_path / "book3.epub").touch()

    mock_res = MagicMock()
    mock_res.returncode = 0
    mock_run.return_value = mock_res

    sync_books(tmp_path, dry_run=False, limit=2)

    assert mock_run.call_count == 2
