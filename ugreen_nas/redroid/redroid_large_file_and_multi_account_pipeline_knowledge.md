# Virtual Pixel 1 (Sailfish) — Large-File Pipeline & Multi-Account Architecture

> Origin: investigation journey at [./redroid_large_file_and_multi_account_pipeline_investigation.md](./redroid_large_file_and_multi_account_pipeline_investigation.md)  
> Prior Architecture: anti-spoof hardening at [./redroid_anti_spoof_hardening_knowledge.md](./redroid_anti_spoof_hardening_knowledge.md)  
> Digital Twin: baseline runbook at [./REDROID_PIXEL1_DIGITAL_TWIN.md](./REDROID_PIXEL1_DIGITAL_TWIN.md)  
> Host Target: UGREEN DXP2800 NAS (`192.168.1.80`) · NVMe Tier (`/volume2`)  
> Worker Node: Raspberry Pi 5 (`192.168.1.92`) · SMR Archive (`/mnt/media-storage/DF`)  
> Status: 🟢 **Production / Durable System Architecture**

---

## 1. Role / Position

The hardened Large-File & Multi-Account ReDroid Pipeline enables high-throughput, unattended media synchronization into Google Photos Cloud at Original Quality with zero storage quota consumption. It resolves the legacy Android 32-bit ashmem inode ceiling ($2.0\text{ GiB}$ limit), protects storage tiers from I/O thrashing, eliminates inotify race conditions via two-phase atomic staging, and provides serialized multi-account switching under a single containerized Pixel 1 digital twin.

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              SYSTEM COMPONENT TOPOLOGY                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  [Raspberry Pi 5 Worker (192.168.1.92)]          [UGREEN DXP2800 NAS (192.168.1.80)]   │
│  ┌───────────────────────────────────┐           ┌──────────────────────────────────┐  │
│  │ 8TB Seagate Expansion SMR Drive   │           │ 4TB WD_BLACK SN850X NVMe Tier    │  │
│  │  - Master TAR Archives            │           │  - /volume2/docker/redroid/      │  │
│  └─────────────────┬─────────────────┘           │    - inbox_staging/ (Two-Phase)  │  │
│                    │ Read-Only                   │    - inbox/ (Debounced Watch)    │  │
│                    ▼                             │    - data/media/0/DCIM/ (Target) │  │
│  ┌───────────────────────────────────┐           │    - scripts/ (Control Plane)    │  │
│  │ Pi 5 RAM Disk (/dev/shm)          │           └─────────────────▲────────────────┘  │
│  │  - Zero-Wear TAR Extraction       │                             │                   │
│  │  - ffmpeg -c copy Keyframe Slices │ ────────────────────────────┘ 2.5GbE Streaming  │
│  └───────────────────────────────────┘                                                 │
│                                                                                        │
│  [ReDroid Container (redroid-pixel1)]            [Google Cloud Infrastructure]         │
│  ┌───────────────────────────────────┐           ┌──────────────────────────────────┐  │
│  │ Android 10 Sailfish Digital Twin  │           │ Google Photos Cloud Backend      │  │
│  │  - libcutils.so (64-bit patch)    │ ────────> │  - Lifetime Unlimited Original   │  │
│  │  - Google Photos App (User 0)     │           │  - 0 Bytes Charged to Quota      │  │
│  │  - SQLite WAL (gphotos0.db)       │           │  - 10GB Per-File Hard Limit      │  │
│  └───────────────────────────────────┘           └──────────────────────────────────┘  │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Plane Decomposition

The architecture separates concerns into three decoupled operational planes:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                       PLANE 1: DATA INGESTION & STORAGE PLANE                          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  Pi 5 RAM Disk (/dev/shm) ──> NAS inbox_staging/ ──> Atomic mv ──> NAS inbox/          │
│                                                                          │             │
│  Google Photos Cloud <── ReDroid DCIM/ <── Zero-Copy mv <── inotifywait (close_write)  │
│                                                                                        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                       PLANE 2: RATE LIMITING & ACCOUNT MUTEX PLANE                     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  CLI Request ──> rate_limiter.py ──> Acquire rate_limit.lock (POSIX fcntl)             │
│                        │                                                               │
│                        ├── Date Check (Midnight Reset)                                 │
│                        ├── Check Quota (1.00 GiB Default / Dynamic Burst Ceiling)      │
│                        └── Acquire account.lock (Mutex: Deep vs Pranali)               │
│                                                                                        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                    PLANE 3: OBSERVABILITY & SQLite VERIFICATION PLANE                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  verify_backup.py ──> SQLite Read-Only URI (?mode=ro) ──> gphotos0.db-wal              │
│                             │                                                          │
│                             ├── Exponential Backoff Retry (Max 5 attempts, step 1.0s)  │
│                             ├── Instant Permanent Failure Abort (code > 0)             │
│                             └── Polling Loop (wait <file> --timeout <sec>)             │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Key Facts About Each Plane:
- **Plane 1 (Data)**: Enforces zero-copy moves within the Btrfs NVMe tier (`mv -f`), writes event directories with Android UID `1023:1023` (775), and prevents partial file reads via atomic two-phase staging (`inbox_staging` $\to$ `inbox`).
- **Plane 2 (Rate & Mutex)**: Governs daily cloud traffic to 1.00 GiB baseline to simulate authentic mobile capture habits, supports dynamic manual burst overrides up to 1 TB, and serializes multi-account uploads via `account.lock`.
- **Plane 3 (Observability)**: Eliminates heavy ADB screencaps and UI automation by inspecting Google Photos internal SQLite database (`gphotos0.db`) in non-blocking WAL mode with exponential lock backoff.

---

## 3. Architecture

### 3.1 Component Footprint Matrix

| Component | Role | Host / Path | Touched? |
| :--- | :--- | :--- | :---: |
| `libcutils.so` (Patched) | 64-bit ashmem inode patch bypassing 2GB SIGABRT | Container: `/system/lib64/libcutils.so` | ✅ Patched |
| `inotify-media-scanner.sh` | Debounced inbox watcher & Android MediaStore scan trigger | NAS: `/volume2/docker/redroid/scripts/` | ✅ Hardened |
| `rate_limiter.py` | Centralized POSIX-locked rate limiter & burst manager | NAS: `/volume2/docker/redroid/scripts/` | ✅ Hardened |
| `verify_backup.py` | Headless SQLite WAL cloud verification service | NAS: `/volume2/docker/redroid/scripts/` | ✅ Hardened |
| `daily-batch-uploader.sh` | Automated background batch uploader with catalog queue | NAS: `/volume2/docker/redroid/scripts/` | ✅ Hardened |
| `batch_worker_fenil.sh` | High-volume batch extractor leveraging `/dev/shm` RAM | Pi 5: `/mnt/media-storage/DF/` | ✅ Hardened |
| `ingest_large_videos.py` | Lossless keyframe stream-copy segmentation pipeline | Pi 5: `/mnt/media-storage/DF/` | ✅ Hardened |
| `account.lock` | POSIX mutex file lock serializing multi-account uploads | NAS: `/volume2/docker/redroid/config/account.lock` | ✅ Created |
| `source_catalog.txt` | Static queue on NVMe replacing mechanical HDD live crawls | NAS: `/volume2/docker/redroid/config/source_catalog.txt` | ✅ Created |

### 3.2 Script Inventory & File Roles

| File Path | Lines | Core Responsibility |
| :--- | :---: | :--- |
| `/volume2/docker/redroid/scripts/inotify-media-scanner.sh` | 85 | Monitors `inbox/`, performs 3s debouncing, executes zero-copy `mv` to `DCIM/`, fixes UID 1023 permissions, broadcasts `android.intent.action.MEDIA_SCANNER_SCAN_FILE`. |
| `/volume2/docker/redroid/scripts/rate_limiter.py` | 195 | Manages `rate_limit_state.json` with POSIX `fcntl` locking, handles midnight rollover, zero-write status queries, and manual burst overrides. |
| `/volume2/docker/redroid/scripts/verify_backup.py` | 135 | Queries `local_media` and `backup_item_status` in `gphotos0.db`, implements exponential backoff on WAL locks, detects permanent failure codes. |
| `/volume2/docker/redroid/scripts/daily-batch-uploader.sh` | 110 | Reads media queues from NVMe `source_catalog.txt`, checks rate limit headroom, stages via two-phase copy, logs to `batch-uploader.log`. |
| `/mnt/media-storage/DF/batch_worker_fenil.sh` | 130 | Manages TAR batch extraction in Pi 5 `/dev/shm`, streams via SSH, triggers atomic staging, verifies uploads using `verify_backup.py`. |
| `/mnt/media-storage/DF/ingest_large_videos.py` | 210 | Performs lossless `ffmpeg -c copy` slicing on keyframe boundaries for >10GB files, tracks checkpoints in `fenil_processed_batches.txt`. |

---

## 4. Mechanics — Step by Step

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        END-TO-END INGESTION LIFECYCLE                                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  [1. Extraction & Ingestion Pre-Check]                                                 │
│      ├── Worker checks rate limit: python3 rate_limiter.py check <bytes>               │
│      └── Worker extracts TAR batch into Pi 5 RAM disk (/dev/shm/staging_flat)          │
│                                                                                        │
│  [2. Two-Phase Staging over 2.5GbE LAN]                                                │
│      ├── Stream files to NAS: /volume2/docker/redroid/inbox_staging/<Album>/           │
│      └── Atomic Move: mv /inbox_staging/<Album>/* /inbox/<Album>/                      │
│                                                                                        │
│  [3. Debounced Inotify Scan]                                                           │
│      ├── inotifywait captures close_write, moved_to events                             │
│      ├── Sleep 3s to debounce batch writes                                             │
│      ├── Case-insensitive extension match (jpg, png, heic, dng, mp4, mov)              │
│      ├── Zero-copy mv into target: /volume2/docker/redroid/data/media/0/DCIM/<Album>/  │
│      └── Ensure permissions: chown 1023:1023 & chmod 775 on target directory           │
│                                                                                        │
│  [4. Android MediaStore Broadcast]                                                     │
│      └── docker exec redroid-pixel1 am broadcast -a ...MEDIA_SCANNER_SCAN_FILE -d ...  │
│                                                                                        │
│  [5. Google Photos Cloud Upload]                                                       │
│      ├── Photos app discovers new media rows via MediaStore                            │
│      ├── Opens file descriptor via ContentResolver (libcutils bypasses 2GB limit)      │
│      └── Uploads bytes to Google Photos Cloud at Original Quality (0 Quota)            │
│                                                                                        │
│  [6. SQLite WAL Verification & Commitment]                                             │
│      ├── Worker polls: python3 verify_backup.py wait <sample_file> --timeout 600       │
│      ├── Verifies state = 1 (SYNCED) and non-null media_key_on_upload in gphotos0.db   │
│      ├── Commits rate limiter bytes: python3 rate_limiter.py record <bytes>            │
│      └── Records processed item in state checkpoint; cleans /dev/shm RAM disk          │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Large File Decision Matrix (<10GB vs >10GB)

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          LARGE FILE INGESTION DECISION LOGIC                           │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  Input Video File                                                                      │
│    │                                                                                   │
│    ├── If Size > 10GB (Google Cloud Limit)                                             │
│    │     └── Lossless Keyframe Slicing: ffmpeg -c copy (Balanced parts < 10GB)         │
│    │                                                                                   │
│    └── If Size <= 10GB                                                                 │
│          └── Ingest Complete Uncut Directly (libcutils 64-bit patch handles > 2GB)     │
│                                                                                        │
│  Result: 100% Bit-for-bit quality preservation; zero server rejects; zero re-encoding  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Video File Size Decision Matrix

| File Size Range | Processing Strategy | Technical Mechanism | Quota / Quality Impact |
| :--- | :--- | :--- | :--- |
| **$< 2.0\text{ GiB}$** ($< 2,147,483,647\text{ B}$) | **Standard Ingestion** | Native Android 10 ashmem handling; direct move into DCIM. | Original Quality · 0 Quota |
| **$2.0\text{ GiB} - 10.0\text{ GB}$** | **Uncut Ingestion** | Patched `libcutils.so` bypasses 32-bit truncation; uploads as single continuous video. | Original Quality · 0 Quota |
| **$> 10.0\text{ GB}$** (e.g. 24.35 GB Sangeet) | **Lossless Keyframe Slicing** | `ffmpeg -ss <start> -to <end> -c copy` on keyframe boundaries into parts $< 10.0\text{ GB}$. | 100% Bit-for-bit · Zero Transcoding |

---

## 6. Multi-Account Mutex & Switching Architecture

To service multiple family accounts on the single Pixel 1 twin without resource duplication:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        MULTI-ACCOUNT MUTEX SERIALIZATION                               │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│     [Deep Ingestion Worker]                     [Pranali Ingestion Worker]             │
│                │                                             │                         │
│                ▼                                             ▼                         │
│        Request account.lock                          Request account.lock              │
│                │                                             │                         │
│       ┌────────┬────────┐                           ┌────────┬────────┐                │
│       │ Lock Available? │                           │ Lock Available? │                │
│       └────────┬────────┘                           └────────┬────────┘                │
│          YES   │                                       NO    │ (Wait / Retry)          │
│                ▼                                             ▼                         │
│        Acquire account.lock                          Blocked until release             │
│        Set Active Account (A)                                │                         │
│        Execute Ingestion Batch                               │                         │
│        Release account.lock ─────────────────────────────────┘                         │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Operational Rules for Multi-Account Setup:
1. **Single Android Profile (`User 0`)**: Both accounts authenticate inside Google Photos under standard Android multi-account management.
2. **Dedicated Staging Paths**:
   - Deep: `/volume2/docker/redroid/inbox/`
   - Pranali: `/volume2/docker/redroid/inbox_pranali/`
3. **Dedicated Rate Limit Trackers**:
   - Deep: `/volume2/docker/redroid/scripts/rate_limit_state.json`
   - Pranali: `/volume2/docker/redroid/scripts/rate_limit_pranali.json`
4. **Mutex File Lock**: `/volume2/docker/redroid/config/account.lock` prevents concurrent ingestion, ensuring Google Photos only ever uploads to one account at a time.

---

## 7. Configuration & CLI Reference

### 7.1 `rate_limiter.py` CLI Commands

```bash
# 1. Inspect rate limiter status (Zero-write query)
python3 /volume2/docker/redroid/scripts/rate_limiter.py status

# 2. Check if a payload fits within today's remaining quota
python3 /volume2/docker/redroid/scripts/rate_limiter.py check <bytes>

# 3. Commit uploaded bytes to state file
python3 /volume2/docker/redroid/scripts/rate_limiter.py record <bytes>

# 4. Enable temporary burst override (e.g. 1000 GB for event migration)
python3 /volume2/docker/redroid/scripts/rate_limiter.py override enable --ceiling-gb 1000 --reason "Wedding Archive Upload"

# 5. Disable burst override and restore 1.00 GiB baseline
python3 /volume2/docker/redroid/scripts/rate_limiter.py override disable
```

### 7.2 `verify_backup.py` CLI Commands

```bash
# 1. Query consensus backup status for an individual file (JSON output)
# Checks backup_item_status, remote_media, MediaTombstone, and media tables
python3 /volume2/docker/redroid/scripts/verify_backup.py check "Haldi.mp4"

# 2. Block until file reaches true consensus SYNCED state (Exit code 0) or times out
python3 /volume2/docker/redroid/scripts/verify_backup.py wait "Haldi.mp4" --timeout 600

# 3. Self-healing reset for a stuck or tombstoned file (purges tombstones & re-queues)
python3 /volume2/docker/redroid/scripts/verify_backup.py reset "Dhuri & Fenil Full Movie-001.mp4"

# 4. Comprehensive multi-table audit of entire library (detects ghost syncs & tombstones)
python3 /volume2/docker/redroid/scripts/verify_backup.py audit

# 5. Print cloud sync summary across entire library
python3 /volume2/docker/redroid/scripts/verify_backup.py summary
```

---

## 8. Failure Modes Observed & Recovery Matrix

| Failure Mode | Data Plane Impact | Observability Plane Impact | Root Mechanism | Recovery Procedure |
| :--- | :--- | :--- | :--- | :--- |
| **Ashmem 32-bit Crash** | `SIGABRT` crashes Photos app immediately. | Zero sync progress; container restarts if fatal. | Signed integer overflow in `libcutils.so::ashmem_get_size_region()`. | Apply 2-byte patch (`jmp; nop`) to `libcutils.so` binary. |
| **Inotify Race Condition** | Scanner moves 0-byte or partially written file. | Duplicate truncated assets in cloud (e.g. 2-min clips). | Direct writing into active `inbox` directory during write stream. | Enforce two-phase staging: write to `inbox_staging/`, then `mv` to `inbox/`. |
| **Ghost Sync (Stale Cache)** | Local files skipped during re-sync without being uploaded. | `verify_backup.py` falsely reports `SYNCED` (`state = 1`). | Remote deletions from web UI purge cloud media, but Android app leaves local `backup_item_status` untouched. | Multi-Table Consensus in `verify_backup.py` (checks `MediaTombstone`, `remote_media.trash_timestamp`). |
| **`MediaTombstone` Barrier** | Android MediaStore scanner refuses to index file into `local_media`. | File shows `NOT_FOUND` or `STATE_None` indefinitely. | Cloud-initiated deletion writes tombstone into `MediaTombstone` table, suppressing future ingestion. | Run `verify_backup.py reset <filename>` to purge tombstones and re-trigger MediaStore scan. |
| **SQLite WAL Lockout** | Cloud upload proceeds unaffected in Android. | `verify_backup.py` hangs or throws `OperationalError: database locked`. | Background WAL checkpoint locks database file exclusively. | Exponential backoff retry in `verify_backup.py` (up to 5 attempts). |
| **SMR Drive Thrashing** | Extraction write speed drops to $< 2\text{ MB/s}$. | Batch worker hits 600s verification timeout. | Shingled magnetic track rewriting during simultaneous tar unpacks. | Redirect extraction paths to `/dev/shm` RAM disk on Pi 5. |
| **Mechanical HDD Spinup** | Unnecessary mechanical disk wear and acoustic noise. | Unintended latency on NAS filesystem queries. | Recursive `find` executed across `/volume1` bulk storage pool. | Query static NVMe catalog (`source_catalog.txt`); never crawl `/volume1`. |
| **Cloud 10GB Server Error** | Upload stalls at 100% and fails with permanent error. | `bis.permanent_failure_reason > 0` recorded in `gphotos0.db`. | Google Photos cloud API rejects single video containers $> 10\text{ GB}$. | Split container with `ffmpeg -c copy` on keyframes into parts $< 10\text{ GB}$. |

---

## 9. Concrete Incident Replay

### Incident: 2.17 GiB Wedding Movie Upload Crash & Partial Ingestion Races

#### Before Hardening:
- **Crash Behavior**: Attempting to upload `Dhuri_Fenil_Full_Movie_Uncut_Test.mp4` (`2,329,301,153 bytes`) triggered immediate `SIGABRT` in `libcutils.so`. Photos app process died; backup stopped indefinitely.
- **Race Condition**: Staging scripts copied directly to `inbox/`; scanner triggered on `IN_CREATE`, moving half-written videos into DCIM and uploading 3 truncated duplicate files to the cloud.
- **Mechanical Churn**: Daily uploader ran `find /volume1` every 24 hours, waking the 10TB Seagate IronWolf drive from 0 RPM deep hibernation daily.

#### After Hardening:
- **Ashmem 64-bit Micro-Patch**: Applied 2-byte patch to `libcutils.so`. Uploaded `Dhuri_Fenil_Full_Movie_Uncut_Test.mp4` (2.17 GiB) and `GoPro_4GB_Test.mp4` (4.34 GiB) completely uncut with **0 bytes quota charged**.
- **Atomic Two-Phase Staging**: All assets staged via `inbox_staging/` and debounced for 3s. Zero truncated duplicates created.
- **Storage Tier Isolation**: Bulk files read from static NVMe catalog (`source_catalog.txt`); mechanical HDD remained in continuous 0 RPM sleep.
- **Cloud Verification**: 100% of 2,797 photos and 33 ceremony videos verified `SYNCED` in `gphotos0.db` with valid cloud media keys.

### Incident 9.2: Post-Deletion Ghost Sync & MediaTombstone Suppression

#### Before Hardening:
- **Flaw**: After the operator deleted prior batch uploads on the web interface (`photos.google.com`), `verify_backup.py` inspected only `backup_item_status.state = 1`. Because Android retained stale records for deleted media keys, `verify_backup.py` falsely reported `SYNCED` (`is_synced: true`). Ingestion scripts skipped 7 critical video files (`Haldi`, `Reels`, `Trailers`) without uploading.
- **Suppression**: Attempting to force-reindex `Dhuri & Fenil Full Movie-001.mp4` by purging local rows failed because Google Photos wrote a tombstone into `MediaTombstone` upon remote deletion, instructing the MediaStore scanner to reject the file.

#### After Hardening:
- **Multi-Table Consensus Verifier**: Re-engineered `verify_backup.py` to cross-reference `backup_item_status`, `local_media`, `remote_media`, `MediaTombstone`, and `media`. An asset is verified `SYNCED` if and only if its media key is live, has no tombstones, and is not trashed in the cloud.
- **Self-Healing Reset Tooling**: Added `verify_backup.py reset <filename>` to automatically purge `MediaTombstone`, reset `local_media` backup markers, touch the camera file, and trigger Job 1052. All 14 wedding video assets verified 100% synced with fresh cloud media keys.
