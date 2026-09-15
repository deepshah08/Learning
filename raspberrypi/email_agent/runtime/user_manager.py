"""
user_manager.py
Pi-loop Email Intelligence Agent — Multi-User Registry & Fair-Share Scheduler
Manages multi-tenant configuration (up to 10+ users) with isolated databases,
credentials, Telegram notification routes, and round-robin fair-share scheduling.
"""

import argparse
import json
import logging
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

BASE_DIR = Path(__file__).parent
CONF_DIR = BASE_DIR / "config"
DATA_DIR = BASE_DIR / "data"
CREDS_DIR = BASE_DIR / "credentials"

CONF_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)
CREDS_DIR.mkdir(parents=True, exist_ok=True)

USERS_FILE = CONF_DIR / "users.json"

logger = logging.getLogger(__name__)


@dataclass
class UserConfig:
    id: str                  # unique username/slug (e.g. deep, pranali)
    name: str                # display name
    email: str               # primary email
    enabled: bool = True     # whether this user is actively scheduled
    telegram_chat_id: str = "" # Telegram chat ID for personalized alerts
    max_emails_per_run: int = 15 # Fair-share quota per cycle
    priority_level: int = 1  # 1 = Normal, 2 = High Priority


def load_users_registry() -> list[UserConfig]:
    """Load user registry from config/users.json or create default."""
    if not USERS_FILE.exists():
        # Auto-create default user 'deep' from existing setup
        default_user = UserConfig(
            id="deep",
            name="Deep",
            email="sl4ught3rcl4y@gmail.com",
            enabled=True,
            telegram_chat_id="955908960",
            max_emails_per_run=15,
            priority_level=1,
        )
        save_users_registry([default_user])
        return [default_user]

    try:
        data = json.loads(USERS_FILE.read_text())
        return [UserConfig(**u) for u in data.get("users", [])]
    except Exception as e:
        logger.error(f"Failed to read {USERS_FILE}: {e}")
        return []


def save_users_registry(users: list[UserConfig]):
    """Persist user registry to config/users.json."""
    data = {"users": [asdict(u) for u in users]}
    USERS_FILE.write_text(json.dumps(data, indent=2))


def get_active_users() -> list[UserConfig]:
    """Return all enabled users, sorted by priority."""
    users = load_users_registry()
    active = [u for u in users if u.enabled]
    active.sort(key=lambda u: u.priority_level, reverse=True)
    return active


def get_user_by_chat_id(chat_id: str | int) -> UserConfig | None:
    """Look up an active user configuration matching a Telegram chat_id."""
    active = get_active_users()
    target_str = str(chat_id).strip()
    for u in active:
        if u.telegram_chat_id and str(u.telegram_chat_id).strip() == target_str:
            return u
    return None



def add_user(id: str, name: str, email: str, telegram_chat_id: str = "", max_emails: int = 15):
    """Add a new user to the registry."""
    id = id.lower().strip()
    users = load_users_registry()
    for u in users:
        if u.id == id:
            print(f"❌ User '{id}' already exists.")
            return False

    new_user = UserConfig(
        id=id,
        name=name.strip(),
        email=email.strip(),
        enabled=True,
        telegram_chat_id=telegram_chat_id.strip(),
        max_emails_per_run=max_emails,
        priority_level=1,
    )
    users.append(new_user)
    save_users_registry(users)
    print(f"✅ User '{name}' ({id}) added successfully!")
    print(f"Next steps for {name}:")
    print(f"  1. Run auth: python auth_setup.py --user {id}")
    print(f"  2. Copy token: scp credentials/{id}_token.json pi5:~/email-agent/credentials/")
    return True


def remove_user(id: str):
    """Remove user from registry."""
    id = id.lower().strip()
    users = load_users_registry()
    initial_len = len(users)
    users = [u for u in users if u.id != id]
    if len(users) == initial_len:
        print(f"❌ User '{id}' not found.")
        return False

    save_users_registry(users)
    print(f"✅ User '{id}' removed.")
    return True


def toggle_user(id: str, enable: bool):
    """Enable or pause a user."""
    id = id.lower().strip()
    users = load_users_registry()
    found = False
    for u in users:
        if u.id == id:
            u.enabled = enable
            found = True
            break
    if not found:
        print(f"❌ User '{id}' not found.")
        return False

    save_users_registry(users)
    status = "enabled" if enable else "paused"
    print(f"✅ User '{id}' is now {status}.")
    return True


def list_users():
    """Print a clean ASCII table of all users."""
    users = load_users_registry()
    if not users:
        print("No users registered.")
        return

    print(f"\n{'ID':<12} {'NAME':<15} {'EMAIL':<30} {'STATUS':<10} {'TELEGRAM ID':<15} {'QUOTA'}")
    print("-" * 95)
    for u in users:
        status = "Active" if u.enabled else "Paused"
        tg = u.telegram_chat_id if u.telegram_chat_id else "(none)"
        print(f"{u.id:<12} {u.name:<15} {u.email:<30} {status:<10} {tg:<15} {u.max_emails_per_run}/run")
    print()


def main():
    parser = argparse.ArgumentParser(description="Pi-loop Email Intelligence User Manager")
    subparsers = parser.add_subparsers(dest="command")

    # list
    subparsers.add_parser("list", help="List all users")

    # add
    add_parser = subparsers.add_parser("add", help="Add a new user")
    add_parser.add_argument("--id", required=True, help="User slug (e.g. pranali)")
    add_parser.add_argument("--name", required=True, help="Display name (e.g. Pranali)")
    add_parser.add_argument("--email", required=True, help="Gmail address")
    add_parser.add_argument("--telegram-id", default="", help="Telegram chat ID for alerts")
    add_parser.add_argument("--max-emails", type=int, default=15, help="Batch quota per cycle")

    # enable / disable
    en_parser = subparsers.add_parser("enable", help="Enable user")
    en_parser.add_argument("id", help="User slug")

    dis_parser = subparsers.add_parser("disable", help="Disable user")
    dis_parser.add_argument("id", help="User slug")

    # remove
    rm_parser = subparsers.add_parser("remove", help="Remove user")
    rm_parser.add_argument("id", help="User slug")

    args = parser.parse_args()

    if args.command == "list" or not args.command:
        list_users()
    elif args.command == "add":
        add_user(args.id, args.name, args.email, args.telegram_id, args.max_emails)
    elif args.command == "enable":
        toggle_user(args.id, True)
    elif args.command == "disable":
        toggle_user(args.id, False)
    elif args.command == "remove":
        remove_user(args.id)


if __name__ == "__main__":
    main()
