"""
test_user_manager.py
Unit tests for user_manager.py module covering registry loading/saving,
active user filtering, priority sorting, Telegram chat ID lookup,
user management (add, remove, toggle, list), and CLI interface.
"""

import json
import sys
from pathlib import Path
import pytest

BASE_DIR = Path(__file__).parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

import user_manager
from user_manager import (
    UserConfig,
    load_users_registry,
    save_users_registry,
    get_active_users,
    get_user_by_chat_id,
    add_user,
    remove_user,
    toggle_user,
    list_users,
    main,
)


@pytest.fixture
def users_file(tmp_path, monkeypatch):
    file_path = tmp_path / "users.json"
    monkeypatch.setattr(user_manager, "USERS_FILE", file_path)
    return file_path


def test_load_users_registry_auto_create_default(users_file):
    assert not users_file.exists()
    users = load_users_registry()
    assert users_file.exists()
    assert len(users) == 1
    default_user = users[0]
    assert default_user.id == "deep"
    assert default_user.name == "Deep"
    assert default_user.email == "sl4ught3rcl4y@gmail.com"
    assert default_user.telegram_chat_id == "955908960"
    assert default_user.enabled is True


def test_load_users_registry_existing_file(users_file):
    data = {
        "users": [
            {
                "id": "alice",
                "name": "Alice",
                "email": "alice@example.com",
                "enabled": True,
                "telegram_chat_id": "111",
                "max_emails_per_run": 10,
                "priority_level": 1,
            },
            {
                "id": "bob",
                "name": "Bob",
                "email": "bob@example.com",
                "enabled": False,
                "telegram_chat_id": "222",
                "max_emails_per_run": 20,
                "priority_level": 2,
            },
        ]
    }
    users_file.write_text(json.dumps(data))

    users = load_users_registry()
    assert len(users) == 2
    assert users[0].id == "alice"
    assert users[0].enabled is True
    assert users[1].id == "bob"
    assert users[1].enabled is False


def test_load_users_registry_corrupt_file(users_file):
    users_file.write_text("{corrupt json content")
    users = load_users_registry()
    assert users == []


def test_save_users_registry(users_file):
    user1 = UserConfig(
        id="user1",
        name="User One",
        email="user1@example.com",
        enabled=True,
        telegram_chat_id="100",
        max_emails_per_run=15,
        priority_level=1,
    )
    save_users_registry([user1])

    assert users_file.exists()
    data = json.loads(users_file.read_text())
    assert "users" in data
    assert len(data["users"]) == 1
    assert data["users"][0]["id"] == "user1"
    assert data["users"][0]["email"] == "user1@example.com"


def test_get_active_users_filtering_and_sorting(users_file):
    u1 = UserConfig(id="u1", name="Normal", email="u1@ex.com", enabled=True, priority_level=1)
    u2 = UserConfig(id="u2", name="HighPrio", email="u2@ex.com", enabled=True, priority_level=2)
    u3 = UserConfig(id="u3", name="Disabled", email="u3@ex.com", enabled=False, priority_level=2)
    save_users_registry([u1, u2, u3])

    active = get_active_users()
    assert len(active) == 2
    # Should be sorted by priority level descending (u2 then u1)
    assert active[0].id == "u2"
    assert active[1].id == "u1"


def test_get_user_by_chat_id(users_file):
    u1 = UserConfig(id="u1", name="U1", email="u1@ex.com", enabled=True, telegram_chat_id="12345")
    u2 = UserConfig(id="u2", name="U2", email="u2@ex.com", enabled=False, telegram_chat_id="67890")
    save_users_registry([u1, u2])

    # Test string and int matching
    found_str = get_user_by_chat_id("12345")
    assert found_str is not None
    assert found_str.id == "u1"

    found_int = get_user_by_chat_id(12345)
    assert found_int is not None
    assert found_int.id == "u1"

    # Disabled user should return None
    assert get_user_by_chat_id("67890") is None

    # Non-existent chat_id returns None
    assert get_user_by_chat_id("99999") is None


def test_add_user_success_and_duplicate(users_file):
    # Auto-creates default registry first
    res1 = add_user(id="alice", name="Alice", email="alice@example.com", telegram_chat_id="111", max_emails=20)
    assert res1 is True

    users = load_users_registry()
    alice = next((u for u in users if u.id == "alice"), None)
    assert alice is not None
    assert alice.name == "Alice"
    assert alice.email == "alice@example.com"
    assert alice.telegram_chat_id == "111"
    assert alice.max_emails_per_run == 20

    # Attempt adding duplicate with different casing/whitespace
    res2 = add_user(id=" ALICE ", name="Alice Dup", email="alice2@example.com")
    assert res2 is False


def test_remove_user(users_file):
    add_user(id="bob", name="Bob", email="bob@example.com")
    assert remove_user("bob") is True
    assert remove_user("bob") is False


def test_toggle_user(users_file):
    add_user(id="charlie", name="Charlie", email="charlie@example.com")
    assert toggle_user("charlie", enable=False) is True

    users = load_users_registry()
    charlie = next((u for u in users if u.id == "charlie"), None)
    assert charlie is not None
    assert charlie.enabled is False

    assert toggle_user("charlie", enable=True) is True
    charlie_reenabled = next((u for u in load_users_registry() if u.id == "charlie"), None)
    assert charlie_reenabled.enabled is True

    assert toggle_user("nonexistent", enable=True) is False


def test_list_users(users_file, capsys):
    # Test empty registry
    save_users_registry([])
    list_users()
    captured = capsys.readouterr()
    assert "No users registered." in captured.out

    # Test populated registry
    add_user(id="dave", name="Dave", email="dave@example.com", telegram_chat_id="555")
    list_users()
    captured = capsys.readouterr()
    assert "ID" in captured.out
    assert "dave" in captured.out
    assert "Dave" in captured.out
    assert "dave@example.com" in captured.out
    assert "555" in captured.out


def test_main_cli_subcommands(users_file, monkeypatch, capsys):
    # Test add subcommand
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "user_manager.py",
            "add",
            "--id",
            "cliuser",
            "--name",
            "CLI User",
            "--email",
            "cli@example.com",
            "--telegram-id",
            "777",
            "--max-emails",
            "25",
        ],
    )
    main()
    assert any(u.id == "cliuser" for u in load_users_registry())

    # Test list subcommand
    monkeypatch.setattr(sys, "argv", ["user_manager.py", "list"])
    main()
    captured = capsys.readouterr()
    assert "cliuser" in captured.out

    # Test disable subcommand
    monkeypatch.setattr(sys, "argv", ["user_manager.py", "disable", "cliuser"])
    main()
    cli_user = next(u for u in load_users_registry() if u.id == "cliuser")
    assert cli_user.enabled is False

    # Test enable subcommand
    monkeypatch.setattr(sys, "argv", ["user_manager.py", "enable", "cliuser"])
    main()
    cli_user = next(u for u in load_users_registry() if u.id == "cliuser")
    assert cli_user.enabled is True

    # Test remove subcommand
    monkeypatch.setattr(sys, "argv", ["user_manager.py", "remove", "cliuser"])
    main()
    assert not any(u.id == "cliuser" for u in load_users_registry())
