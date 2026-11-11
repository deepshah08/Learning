#!/usr/bin/env python3
"""
Centralized Rate Limiter for Google Photos ReDroid Ingestion Pipeline
Enforces 1GB/day baseline to mimic organic mobile camera behavior and avoid Google fraud heuristics.
Supports manual override for post-trip / event bursts.
"""
import os
import sys
import json
import time
import fcntl
import argparse
from datetime import datetime

STATE_FILE = "/volume2/docker/redroid/scripts/rate_limit_state.json"
LOCK_FILE = "/volume2/docker/redroid/scripts/rate_limit.lock"
DEFAULT_DAILY_LIMIT_BYTES = 1024 * 1024 * 1024  # 1.00 GiB

def get_today_str():
    return datetime.now().strftime("%Y-%m-%d")

def acquire_lock():
    os.makedirs(os.path.dirname(LOCK_FILE), exist_ok=True)
    fd = os.open(LOCK_FILE, os.O_CREAT | os.O_RDWR)
    fcntl.flock(fd, fcntl.LOCK_EX)
    return fd

def release_lock(fd):
    fcntl.flock(fd, fcntl.LOCK_UN)
    os.close(fd)

def load_state():
    today = get_today_str()
    data = {}
    mutated = False
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                data = json.load(f)
        except Exception:
            data = {}
            mutated = True

    # Reset counter if a new day has rolled over
    if data.get("date") != today:
        data["date"] = today
        data["uploaded_today_bytes"] = 0
        if not data.get("override_sticky", False):
            data["override_active"] = False
            data["override_reason"] = None
            data["override_ceiling_bytes"] = None
        mutated = True

    data.setdefault("date", today)
    data.setdefault("daily_limit_bytes", DEFAULT_DAILY_LIMIT_BYTES)
    data.setdefault("uploaded_today_bytes", 0)
    data.setdefault("override_active", False)
    data.setdefault("override_ceiling_bytes", None)
    data.setdefault("override_reason", None)
    data.setdefault("override_sticky", False)
    data.setdefault("last_upload_time", None)
    return data, mutated

def save_state(data):
    temp_file = STATE_FILE + ".tmp"
    with open(temp_file, "w") as f:
        json.dump(data, f, indent=2)
        f.flush()
        os.fsync(f.fileno())
    os.replace(temp_file, STATE_FILE)

def cmd_check(args):
    bytes_to_add = int(args.bytes)
    if bytes_to_add < 0:
        sys.stderr.write("Error: bytes must be a non-negative integer.\n")
        sys.exit(2)

    lock_fd = acquire_lock()
    try:
        data, mutated = load_state()
        if mutated:
            save_state(data)
        uploaded = data["uploaded_today_bytes"]
        daily_limit = data["daily_limit_bytes"]
        override_active = data["override_active"]
        ceiling = data["override_ceiling_bytes"]

        if override_active:
            effective_limit = ceiling if ceiling is not None else float("inf")
            limit_type = f"Override ({data.get('override_reason') or 'Manual Burst'})"
        else:
            effective_limit = daily_limit
            limit_type = "Standard 1GB/day baseline"

        projected = uploaded + bytes_to_add
        allowed = (projected <= effective_limit)
        remaining = max(0, effective_limit - uploaded) if effective_limit != float("inf") else -1

        result = {
            "allowed": allowed,
            "bytes_requested": bytes_to_add,
            "uploaded_today_mb": round(uploaded / (1024 * 1024), 2),
            "effective_limit_mb": round(effective_limit / (1024 * 1024), 2) if effective_limit != float("inf") else "unlimited",
            "remaining_mb": round(remaining / (1024 * 1024), 2) if remaining != -1 else "unlimited",
            "limit_type": limit_type,
            "override_active": override_active
        }
        print(json.dumps(result, indent=2))
        sys.exit(0 if allowed else 1)
    finally:
        release_lock(lock_fd)

def cmd_record(args):
    bytes_added = int(args.bytes)
    if bytes_added < 0:
        sys.stderr.write("Error: bytes must be a non-negative integer.\n")
        sys.exit(2)

    lock_fd = acquire_lock()
    try:
        data, _ = load_state()
        data["uploaded_today_bytes"] += bytes_added
        data["last_upload_time"] = datetime.now().isoformat()
        save_state(data)
        print(json.dumps({
            "status": "recorded",
            "bytes_added": bytes_added,
            "uploaded_today_mb": round(data["uploaded_today_bytes"] / (1024 * 1024), 2)
        }, indent=2))
        sys.exit(0)
    finally:
        release_lock(lock_fd)

def cmd_status(args):
    lock_fd = acquire_lock()
    try:
        data, mutated = load_state()
        if mutated:
            save_state(data)
        uploaded = data["uploaded_today_bytes"]
        daily_limit = data["daily_limit_bytes"]
        override_active = data["override_active"]
        ceiling = data["override_ceiling_bytes"]

        effective_limit = ceiling if (override_active and ceiling is not None) else (daily_limit if not override_active else None)
        remaining = max(0, effective_limit - uploaded) if effective_limit is not None else "unlimited"

        summary = {
            "date": data["date"],
            "uploaded_today_mb": round(uploaded / (1024 * 1024), 2),
            "uploaded_today_gb": round(uploaded / (1024 * 1024 * 1024), 3),
            "daily_limit_gb": round(daily_limit / (1024 * 1024 * 1024), 2),
            "remaining_mb": round(remaining / (1024 * 1024), 2) if remaining != "unlimited" else "unlimited",
            "override_active": override_active,
            "override_reason": data.get("override_reason"),
            "override_ceiling_gb": round(ceiling / (1024 * 1024 * 1024), 2) if ceiling else None,
            "last_upload_time": data.get("last_upload_time")
        }
        print(json.dumps(summary, indent=2))
        sys.exit(0)
    finally:
        release_lock(lock_fd)

def cmd_override(args):
    lock_fd = acquire_lock()
    try:
        data, _ = load_state()
        if args.action == "enable":
            data["override_active"] = True
            data["override_reason"] = args.reason or "Manual user burst invocation"
            data["override_sticky"] = bool(args.sticky)
            if args.ceiling_gb:
                data["override_ceiling_bytes"] = int(float(args.ceiling_gb) * 1024 * 1024 * 1024)
            else:
                data["override_ceiling_bytes"] = None
            save_state(data)
            print(f"Rate limiter override ENABLED: {data['override_reason']} (Ceiling: {args.ceiling_gb or 'Unlimited'} GB)")
        elif args.action == "disable":
            data["override_active"] = False
            data["override_reason"] = None
            data["override_ceiling_bytes"] = None
            data["override_sticky"] = False
            save_state(data)
            print("Rate limiter override DISABLED. Returned to standard 1GB/day baseline.")
        sys.exit(0)
    finally:
        release_lock(lock_fd)

def cmd_set_uploaded(args):
    lock_fd = acquire_lock()
    try:
        data, _ = load_state()
        data["uploaded_today_bytes"] = int(float(args.gb) * 1024 * 1024 * 1024)
        save_state(data)
        print(f"Set uploaded today to {args.gb} GB ({data['uploaded_today_bytes']} bytes).")
        sys.exit(0)
    finally:
        release_lock(lock_fd)

def main():
    parser = argparse.ArgumentParser(description="ReDroid Google Photos Upload Rate Limiter")
    subparsers = parser.add_subparsers(dest="command", required=True)

    check_parser = subparsers.add_parser("check", help="Check if bytes can be uploaded under limit")
    check_parser.add_argument("bytes", type=int, help="Byte size of media item to check")

    record_parser = subparsers.add_parser("record", help="Record uploaded bytes")
    record_parser.add_argument("bytes", type=int, help="Byte size of uploaded media item")

    status_parser = subparsers.add_parser("status", help="Get current daily upload and quota status")

    override_parser = subparsers.add_parser("override", help="Enable or disable manual burst override")
    override_parser.add_argument("action", choices=["enable", "disable"])
    override_parser.add_argument("--ceiling-gb", type=float, default=None, help="Burst quota ceiling in GB (e.g. 15)")
    override_parser.add_argument("--reason", type=str, default="Trip/Event Burst", help="Reason for override")
    override_parser.add_argument("--sticky", action="store_true", help="Persist override past midnight")

    set_parser = subparsers.add_parser("set-uploaded", help="Set today's uploaded bytes for initial synchronization")
    set_parser.add_argument("gb", type=float, help="Gigabytes uploaded today")

    args = parser.parse_args()

    if args.command == "check":
        cmd_check(args)
    elif args.command == "record":
        cmd_record(args)
    elif args.command == "status":
        cmd_status(args)
    elif args.command == "override":
        cmd_override(args)
    elif args.command == "set-uploaded":
        cmd_set_uploaded(args)

if __name__ == "__main__":
    main()
