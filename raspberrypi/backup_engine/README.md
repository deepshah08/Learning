# 💾 Project 07: Backup Engine & Pixel 1 Sync Guard (Raspberry Pi 5)

> **Context**: Disaster recovery engine coordinating encrypted Backblaze B2 backups (Restic) and Pixel 1 Unlimited Google Photos sync staging guard.  
> **Status**: 🟢 **Production / Tested**  
> **Host**: Raspberry Pi 5 (`192.168.1.92`)  
> **Repository**: [`deepshah08/raspberry-pi-5-ecosystem/projects/07-backup-engine`](https://github.com/deepshah08/raspberry-pi-5-ecosystem/tree/main/projects/07-backup-engine)  

---

## 1. Key Components

- **Pixel Sync Guard (`pixel1_sync_guard.py`)**: Compares local MD5 checksums of staging photos against Pixel 1 remote storage via ADB. Safely purges staged photos older than 3 days only after verifying successful transfer.
- **B2 Restic Script (`backup_to_b2.sh`)**: Encrypted snapshot repository pushing critical homelab configs to Backblaze B2 with automated retention pruning (`7 daily, 4 weekly, 12 monthly`).

## 2. Verified Functionality & Test Suite

- `projects/07-backup-engine/tests/test_backup_engine.py`: Validates MD5 hash generation and retention purge safety rules.
- **Test Results**: 2/2 passing tests.
