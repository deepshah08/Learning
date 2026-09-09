#!/usr/bin/env python3
"""
Sync local ebooks and text documents to the Calibre-Web-Automated ingest pipeline on UGREEN NAS.
"""

import os
import sys
import argparse
import subprocess
import time
from pathlib import Path

EXTENSIONS = {".epub", ".pdf", ".mobi", ".azw3", ".azw", ".djvu", ".cbz", ".cbr", ".fb2"}
REMOTE_INGEST = "nas:/volume1/data/books/ingest/"

def get_existing_remote_titles():
    """Query Calibre metadata.db on NAS to see what is already imported."""
    cmd = [
        "ssh", "nas",
        'sqlite3 /volume1/data/books/library/metadata.db "SELECT title FROM books;" 2>/dev/null || true'
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        titles = set(line.strip().lower() for line in res.stdout.splitlines() if line.strip())
        return titles
    except Exception as e:
        print(f"[!] Warning: Could not fetch existing titles from NAS: {e}")
        return set()

def find_books(directory: Path):
    books = []
    for root, _, files in os.walk(directory):
        for f in files:
            p = Path(root) / f
            if p.suffix.lower() in EXTENSIONS and not f.startswith("."):
                books.append(p)
    return sorted(books)

def sync_books(directory: Path, dry_run: bool = False, limit: int = None):
    if not directory.exists():
        print(f"Error: Directory {directory} does not exist.")
        sys.exit(1)

    print(f"\n🔍 Scanning {directory} for textual books and documents...")
    books = find_books(directory)
    print(f"📚 Found {len(books)} eligible books.")

    existing_titles = get_existing_remote_titles()
    print(f"🗄️  NAS Calibre currently contains {len(existing_titles)} books: {', '.join(sorted(existing_titles))}\n")

    uploaded = 0
    skipped = 0

    for i, book in enumerate(books, 1):
        filename = book.name
        stem_lower = book.stem.lower()

        # Check if already present in titles
        is_imported = any(title in stem_lower or stem_lower in title for title in existing_titles if len(title) > 4)
        if is_imported:
            print(f"[{i}/{len(books)}] ⏭️  Skipping (Already on NAS): {filename}")
            skipped += 1
            continue

        size_mb = book.stat().st_size / (1024 * 1024)
        print(f"[{i}/{len(books)}] 🚀 {'[DRY RUN] Would sync' if dry_run else 'Syncing'} ({size_mb:.1f} MB): {filename}")

        if not dry_run:
            cmd = ["scp", "-O", str(book), REMOTE_INGEST]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0:
                uploaded += 1
                time.sleep(2.0)
            else:
                print(f"    ❌ Failed to upload: {res.stderr.strip()}")
        else:
            uploaded += 1

        if limit and uploaded >= limit:
            print(f"\nReached batch limit of {limit} books.")
            break

    print(f"\n✨ Sync completed! Uploaded: {uploaded}, Skipped: {skipped}, Total Scanned: {len(books)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync local books to NAS Calibre-Web-Automated ingest.")
    parser.add_argument("dir", nargs="?", default="/Users/deep/Desktop/Books", help="Local directory containing books")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without uploading")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of books to sync in one run")
    args = parser.parse_args()

    sync_books(Path(args.dir), dry_run=args.dry_run, limit=args.limit)
