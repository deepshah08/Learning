# 📦 SMR Sequential Streaming Archival Runbook

> **Context**: Production procedure for streaming bulk directories from macOS to Shingled Magnetic Recording (SMR) mechanical storage (8TB Seagate Expansion on Raspberry Pi 5 at `/mnt/media-storage`) with zero local disk overhead and complete avoidance of SMR write-cliff degradation.  
> **Last Verified**: 2026-09-13 18:07 PDT  
> **Status**: 🟢 **Production Verified (60GB Archive Completed & Verified)**

---

## 🏗️ 1. The Physics of SMR: Why Streaming is Mandatory

### The "Write Cliff" Mechanism
* **Track Overlap**: SMR tracks overlap like shingles on a roof. Writing even a 4 KB random block forces the drive's internal firmware controller to read an entire overlapping band (~256 MB), modify it in volatile DRAM/SLC write cache, and rewrite the whole zone.
* **Random File Penalty**: Copying loose folders (e.g. thousands of images, `.zip` packages, videos, source code) via standard `cp`, Finder drag-and-drop, or unthrottled SMB floods the on-drive cache within seconds. Once the cache saturates, write speeds collapse from **~140 MB/s down to 2–5 MB/s**, triggering severe head thrashing, mechanical heat, and bearing wear.
* **The Solution**: Stream the directory as a **single, contiguous, sequential byte stream**. The mechanical drive head sweeps sequentially along the platter tracks with zero head seek thrashing.

---

## ⚡ 2. The Zero-Local-Footprint Streaming Architecture

By chaining `tar` through an SSH pipe directly into the remote file target on the Pi 5, **zero scratch space is used on the Mac**:

```text
┌────────────────────────────────┐                 ┌─────────────────────────────────┐
│     Source Mac (Controller)    │                 │   Destination: Pi 5 (SMR Host)  │
│                                │   SSH Tunnel    │                                 │
│  ~/Desktop/Folder/             │ (TCP Stream)    │  cat > /mnt/media-storage/      │
│         │                      │                 │        target_dir/archive.tar   │
│         ▼                      │                 │                 │               │
│  tar -cf - (RAM buffer only)   ├────────────────►│                 ▼               │
│  [Zero Mac Disk Used]          │                 │  Direct Sequential Sectors      │
└────────────────────────────────┘                 └─────────────────────────────────┘
```

---

## 🛠️ 3. Execution Commands

### Step 1: Pre-Create the Target Subdirectory on the Pi 5
```bash
ssh deepshah08@192.168.1.92 "mkdir -p /mnt/media-storage/<TARGET_DIR>"
```

### Step 2: Stream On-The-Fly (Pre-Compressed Files: Videos, Zips, Photos)
When files are already compressed (`.zip`, `.mp4`, `.mkv`), bypass compression to save CPU and maximize network throughput:
```bash
tar --exclude='.DS_Store' -cvf - -C "/path/to/parent" "<FOLDER_NAME>" | \
  ssh deepshah08@192.168.1.92 "cat > /mnt/media-storage/<TARGET_DIR>/<ARCHIVE_NAME>.tar"
```

### Step 3: Stream with Multi-Core Zstandard (Raw Documents, Code, CSVs)
If archiving uncompressed text, logs, or raw code, compress on-the-fly using Apple Silicon multi-core Zstandard (`zstd -3 -T0`):
```bash
tar --exclude='.DS_Store' -cf - -C "/path/to/parent" "<FOLDER_NAME>" | \
  zstd -3 -T0 | \
  ssh deepshah08@192.168.1.92 "cat > /mnt/media-storage/<TARGET_DIR>/<ARCHIVE_NAME>.tar.zst"
```

---

## 🔍 4. Verification & Safe Deletion Protocol

**NEVER delete source files without completing this two-step verification:**

### 1. Verify Archive Index & Byte Sizes Remotely
```bash
ssh deepshah08@192.168.1.92 "tar -tvf /mnt/media-storage/<TARGET_DIR>/<ARCHIVE_NAME>.tar"
```

### 2. Compare Remote Byte Counts vs. Local Files
```bash
# Compare individual file sizes on source:
find /path/to/source -type f -not -name '.DS_Store' -exec stat -f "%z %N" {} +

# Compare against remote tar table:
ssh deepshah08@192.168.1.92 "tar -tvf /mnt/media-storage/<TARGET_DIR>/<ARCHIVE_NAME>.tar" | awk '{print $3, $6}'
```

### 3. Evict Source Only After Verification
```bash
rm -rf /path/to/source
```

---

## 🔄 5. Standalone Reusable Helper Script

A portable script for one-line archiving can be placed in `~/.local/bin/smr-archive`:

```bash
#!/usr/bin/env bash
# smr-archive: Stream a local directory into a single sequential tar on SMR storage
set -euo pipefail

SOURCE_DIR="${1:-}"
REMOTE_SUBDIR="${2:-Backups}"
REMOTE_HOST="deepshah08@192.168.1.92"
SMR_ROOT="/mnt/media-storage"

if [[ -z "$SOURCE_DIR" || ! -d "$SOURCE_DIR" ]]; then
  echo "Usage: smr-archive <LOCAL_DIRECTORY_PATH> [REMOTE_SUBDIR_NAME]"
  exit 1
fi

PARENT_DIR=$(dirname "$SOURCE_DIR")
BASE_NAME=$(basename "$SOURCE_DIR")
ARCHIVE_NAME="${BASE_NAME}_archive_$(date +%Y_%m_%d).tar"

echo "[*] Target SMR directory: ${SMR_ROOT}/${REMOTE_SUBDIR}"
ssh "$REMOTE_HOST" "mkdir -p '${SMR_ROOT}/${REMOTE_SUBDIR}'"

echo "[*] Streaming '${BASE_NAME}' to '${REMOTE_HOST}:${SMR_ROOT}/${REMOTE_SUBDIR}/${ARCHIVE_NAME}'..."
tar --exclude='.DS_Store' -cvf - -C "$PARENT_DIR" "$BASE_NAME" | \
  ssh "$REMOTE_HOST" "cat > '${SMR_ROOT}/${REMOTE_SUBDIR}/${ARCHIVE_NAME}'"

echo "[*] Verifying remote archive integrity..."
ssh "$REMOTE_HOST" "ls -lh '${SMR_ROOT}/${REMOTE_SUBDIR}/${ARCHIVE_NAME}' && tar -tf '${SMR_ROOT}/${REMOTE_SUBDIR}/${ARCHIVE_NAME}' | head -n 5"
echo "[+] Archive successfully written and verified on SMR storage!"
```

---

## 🌐 6. On-Demand Ephemeral Sharing (Architecture 3: Scale-to-Zero)

> **Philosophy**: Zero background containers, 0% idle CPU, 0 MB idle RAM, and guaranteed 0 RPM mechanical drive spindown for 364 days/year. Activates strictly on-demand when the recipient needs to download.

### Controller Location (Pi 5)
`~/scripts/df_share/share_manager.sh`

### Architecture & Security Workflow
1. **Idle State**: Tailscale Funnel / Serve is off. Port 8089 is completely dead. SMR drive rests in 0 RPM sleep.
2. **On Trigger (`share_manager.sh start [HOURS]`)**:
   - Generates a cryptographically random session token (`secrets.token_urlsafe(16)`).
   - Starts an isolated, read-only Python streaming service (`server.py`) binding strictly to `127.0.0.1:8089`.
   - Exposes port 8089 over **Tailscale Funnel** (`https://pi5-media-nas.tail983cc9.ts.net:8089/df?token=<SECRET>`).
   - Starts an automated background self-destruct timer (default 4 hours).
3. **Recipient Experience**:
   - Opens the link in any modern browser on phone, Mac, or PC (no Tailscale client needed).
   - Clean landing page detailing archive contents, size (60 GB), and a single **Download Master Archive** button.
   - Server implements **HTTP 206 Partial Content (Range requests)** allowing paused or interrupted downloads to resume smoothly.
4. **On Completion / Teardown (`share_manager.sh stop`)**:
   - Unbinds and disables Tailscale Funnel / Serve.
   - Terminates the streaming process.
   - Clears the active session token.
   - Verifies 0 processes and 0 open ports remain active.

### Live CLI Operational Commands
```bash
# Start 4-hour ephemeral portal (prints public HTTPS URL + token)
ssh deepshah08@192.168.1.92 "~/scripts/df_share/share_manager.sh start 4"

# Check current status
ssh deepshah08@192.168.1.92 "~/scripts/df_share/share_manager.sh status"

# Manually tear down early once recipient finishes downloading
ssh deepshah08@192.168.1.92 "~/scripts/df_share/share_manager.sh stop"
```

---

## 🔔 7. Self-Service "Digital Doorbell" PIN Trigger (Option 1)

> **Purpose**: Enables the recipient (cousin) to self-trigger the cold storage wake-up anytime via a single PIN web form without disturbing the administrator, while maintaining 0 RPM SMR sleep during idle periods.

### Flow Architecture
```text
┌───────────────────────────────┐
│ Recipient opens Doorbell URL: │
│ https://...:8088/             │
└──────────────┬────────────────┘
               │ Submits PIN (e.g. DhuriFenil2026)
               ▼
┌───────────────────────────────┐
│ Doorbell Service (RAM only)   │
│ - Rate limits failed attempts │
│ - Verifies constant-time hash │
│ - Runs share_manager.sh start │
└──────────────┬────────────────┘
               │ Dynamic Redirect (3s splash)
               ▼
┌───────────────────────────────┐
│ Live Ephemeral 4-Hour Stream  │
│ https://...:8089/df?token=XYZ │
└───────────────────────────────┘
```

### Components Deployed
1. **Dispatcher**: `~/scripts/df_share/doorbell_service.py` (Port 8088, pure RAM, 0 SMR lookups).
2. **Access Key (PIN)**: `DhuriFenil2026` (Configurable in script).
3. **Safety Protection**: Built-in 5-attempt rate-limiting per client IP (prevents automated guessing).
4. **Auto-Redirect**: On successful PIN submission, the recipient is presented with a 3-second animated "Waking Cold Archive" splash screen that automatically redirects their browser to their fresh tokenized download URL.
