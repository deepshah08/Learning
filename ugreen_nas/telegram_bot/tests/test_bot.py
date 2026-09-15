import os
import sys
from unittest.mock import patch

# Ensure parent directory is in python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bot import is_authorized

def test_is_authorized_empty_list():
    """Test that any user is authorized when allowed_user_ids is empty."""
    with patch('bot.config.allowed_user_ids', []):
        assert is_authorized(12345) == True
        assert is_authorized(67890) == True

def test_is_authorized_allowed_user():
    """Test that a user in allowed_user_ids is authorized."""
    with patch('bot.config.allowed_user_ids', [12345, 11111]):
        assert is_authorized(12345) == True

def test_is_authorized_denied_user():
    """Test that a user not in allowed_user_ids is denied."""
    with patch('bot.config.allowed_user_ids', [12345, 11111]):
        assert is_authorized(67890) == False
