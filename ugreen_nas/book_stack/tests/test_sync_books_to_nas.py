import os
import sys
import pytest
from pathlib import Path

# Ensure parent directory is in python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sync_books_to_nas import find_books

def test_find_books_valid_extensions(tmp_path):
    """Test that valid extensions are found."""
    (tmp_path / "book1.epub").touch()
    (tmp_path / "book2.pdf").touch()
    (tmp_path / "book3.mobi").touch()

    books = find_books(tmp_path)
    assert len(books) == 3
    assert tmp_path / "book1.epub" in books
    assert tmp_path / "book2.pdf" in books
    assert tmp_path / "book3.mobi" in books

def test_find_books_ignores_invalid_extensions(tmp_path):
    """Test that invalid extensions are ignored."""
    (tmp_path / "book1.epub").touch()
    (tmp_path / "notes.txt").touch()
    (tmp_path / "cover.jpg").touch()

    books = find_books(tmp_path)
    assert len(books) == 1
    assert tmp_path / "book1.epub" in books

def test_find_books_ignores_hidden_files(tmp_path):
    """Test that hidden files (starting with .) are ignored."""
    (tmp_path / "book1.epub").touch()
    (tmp_path / ".hidden_book.epub").touch()
    (tmp_path / ".DS_Store").touch()

    books = find_books(tmp_path)
    assert len(books) == 1
    assert tmp_path / "book1.epub" in books

def test_find_books_case_insensitive_extensions(tmp_path):
    """Test that extensions are case-insensitive."""
    (tmp_path / "book1.EPUB").touch()
    (tmp_path / "book2.Pdf").touch()
    (tmp_path / "book3.MOBI").touch()

    books = find_books(tmp_path)
    assert len(books) == 3
    assert tmp_path / "book1.EPUB" in books
    assert tmp_path / "book2.Pdf" in books
    assert tmp_path / "book3.MOBI" in books

def test_find_books_recursive(tmp_path):
    """Test that files in subdirectories are found."""
    sub_dir1 = tmp_path / "sub1"
    sub_dir1.mkdir()
    sub_dir2 = tmp_path / "sub2"
    sub_dir2.mkdir()
    nested_dir = sub_dir1 / "nested"
    nested_dir.mkdir()

    (tmp_path / "book1.epub").touch()
    (sub_dir1 / "book2.pdf").touch()
    (sub_dir2 / "book3.mobi").touch()
    (nested_dir / "book4.azw3").touch()

    books = find_books(tmp_path)
    assert len(books) == 4
    assert tmp_path / "book1.epub" in books
    assert sub_dir1 / "book2.pdf" in books
    assert sub_dir2 / "book3.mobi" in books
    assert nested_dir / "book4.azw3" in books

def test_find_books_sorted(tmp_path):
    """Test that the returned list of books is sorted."""
    (tmp_path / "c_book.epub").touch()
    (tmp_path / "a_book.epub").touch()
    (tmp_path / "b_book.epub").touch()

    books = find_books(tmp_path)
    assert len(books) == 3
    assert books[0] == tmp_path / "a_book.epub"
    assert books[1] == tmp_path / "b_book.epub"
    assert books[2] == tmp_path / "c_book.epub"
