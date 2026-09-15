"""
auth_setup.py
One-time OAuth2 authentication helper.
Run this ONCE from any machine with a browser to generate token.json.
Supports multi-user profiles (--user deep, --user pranali).

Usage:
    python auth_setup.py
    python auth_setup.py --user pranali
"""

import argparse
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow

BASE_DIR   = Path(__file__).parent
CREDS_FILE = BASE_DIR / "credentials" / "credentials.json"

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.modify",
]

def main():
    parser = argparse.ArgumentParser(description="One-time OAuth Setup for Gmail Agent")
    parser.add_argument("--user", default="deep", help="User profile ID (e.g. deep, pranali)")
    args = parser.parse_args()

    user_id = args.user.lower().strip()
    token_file = BASE_DIR / "credentials" / f"{user_id}_token.json" if user_id != "deep" else BASE_DIR / "credentials" / "token.json"

    if not CREDS_FILE.exists():
        print(f"❌ ERROR: credentials.json not found at {CREDS_FILE}")
        print("Download it from Google Cloud Console:")
        print("  console.cloud.google.com → APIs & Services → Credentials")
        print("  → OAuth 2.0 Client IDs → Desktop app → Download JSON")
        print(f"  → Save as {CREDS_FILE}")
        return

    print(f"🔑 Authorizing Gmail account for user profile: [{user_id.capitalize()}]")
    print("Opening browser for Google OAuth consent...")
    print(f"Sign in with the Gmail account for [{user_id.capitalize()}] and click 'Allow'")
    print()

    flow = InstalledAppFlow.from_client_secrets_file(
        str(CREDS_FILE),
        SCOPES,
    )
    # access_type=offline + prompt=consent ensures we get a permanent refresh token
    creds = flow.run_local_server(
        port=0,
        access_type="offline",
        prompt="consent",
    )

    token_file.parent.mkdir(parents=True, exist_ok=True)
    token_file.write_text(creds.to_json())

    print()
    print(f"✅ Token saved to: {token_file}")
    print()
    print("Next step — copy to Pi 5:")
    print(f"  scp {token_file} pi5:~/email-agent/credentials/{token_file.name}")
    print()
    print("IMPORTANT: In Google Cloud Console, change the OAuth app publishing status from")
    print("'Testing' → 'In Production' (keeps you as only test user) to prevent 7-day token expiry.")


if __name__ == "__main__":
    main()
