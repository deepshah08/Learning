# 🔬 Investigation: ReDroid Pixel 1 Cross-Host Migration & Pipeline Architecture

> **Date**: 2026-11-12  
> **Status**: Resolved / Verified  
> **Hosts**: UGREEN DXP2800 NAS (`192.168.1.80`), OrigiMagic Aurora A3 (`192.168.1.111`)  
> **Author**: Antigravity Assistant  

---

## 1. Initial State & Problem Statement

The user reported an unexpected shutdown notification from the UGREEN NAS mobile application and inquired whether the compute-rich OrigiMagic Aurora A3 could be leveraged to offload media ingestion, indexing, and the ReDroid container stack.

### Diagnostic Findings:
1. **Host Shutdown Myth Debunked**: Live inspection of `/var/log/syslog` and `uptime` on the NAS revealed the NAS had not shut down that day. The unread notification originated from an unacknowledged WebSocket dispatch recorded at 23:36:52 MST on Nov 11, corresponding to a kernel reset from Nov 10 at 23:07 MST during the ingestion of `Wedding-001.mp4` (10.5 GB).
2. **NAS Memory Constraint**: The NAS's Intel N100 (4C/4T) with 8 GB DDR5 RAM had only ~2.2 GiB available memory while running UGOS Pro, Pi-hole DNS, and *Arr stacks. During large video processing, memory exhaustion tripped the Intel TCO hardware watchdog.
3. **Swap & NVMe Health**: Verified that the NAS swap is strictly memory-compressed `zram` (3.75 GB) and eMMC fallback (`mmcblk0p5`). The 4TB WD_BLACK SN850X NVMe had zero swap configured and exhibited only 1.60 TB lifetime writes out of 2,400 TBW (0.067% wear).
4. **Network & Ingress Bottlenecks**: Aurora communicates over Wi-Fi 6E (`-51 dBm`, ~52–75 MB/s). However, Google Photos cloud ingress is throttled server-side to 50–100 Mbps (~8.3 minutes for 5 GB). Local transfer takes only ~66 seconds (<12% of total runtime).

---

## 2. Hypothesis & Architectural Strategy

- **Hypothesis**: Offloading ReDroid to Aurora A3 (AMD Ryzen 7 8745HS, 16 threads, 16 GB DDR5) will eliminate NAS memory panics, reduce NAS RAM utilization by >1.5 GiB, and accelerate media processing.
- **RAM-Disk Zero-Wear Staging**: Staging media directly into `/dev/shm` (POSIX tmpfs) on Aurora avoids any write amplification on Aurora's NVMe SSD during transit.
- **64-bit Signed Truncation Patch**: The patched `libcutils.so` eliminates the 2.0 GiB ceiling in `ashmem_get_size_region`, enabling seamless ingestion of files > 2.0 GiB.

---

## 3. Implementation Steps & Verification

### Step 1: Aurora Kernel & Device Preparation
- Mounted `/dev/binderfs` allocating `binder`, `hwbinder`, and `vndbinder` devices (major 234) with `0666` permissions.
- Created and enabled persistent systemd unit `/etc/systemd/system/binderfs.service`.
- Verified AMD Radeon 780M GPU node `/dev/dri/renderD128` (gid `render`).

### Step 2: Container Image & State Migration
- Exported `redroid:11.0.0-pixel1-patched` from NAS NVMe and imported into Aurora's Docker engine.
- Streamed `/volume2/docker/redroid/data` over SSH tar pipeline to `/opt/redroid/data` on Aurora.
- Preserved Android UIDs (`1023:1023`, `10131:10131`).
- Deployed `/opt/redroid/docker-compose.yml` with Sailfish properties and launched container.

### Step 3: Binary Disassembly Verification of 64-bit libcutils.so
- Disassembled `ashmem_get_size_region` in `/system/lib64/libcutils.so` from `0xba90` to `0xbbe0`.
- Verified instruction at `0xbb24`:
  ```assembly
  bb21:  cmp    rax,rbx
  bb24:  jmp    bbcd <ashmem_get_size_region@@Base+0x13d>
  bb29:  nop
  bb2a:  call   fd40 <abort@plt>
  ```
  The signed 32-bit `abort@plt` branch is unconditionally bypassed, returning the full 64-bit `st_size` in `rbx`.

### Step 4: Cross-Host Pipeline Implementation
- Developed `/opt/redroid/scripts/pipeline_processor.py` orchestrating:
  `Disk (NAS /volume2) -> Page Cache -> SSH Stream -> RAM Disk (/dev/shm) -> Integrity/SHA256 -> ReDroid DCIM -> Cloud Upload -> SQLite WAL Consensus -> Cleanup`.
- Set default POSIX ACLs (`setfacl`) on `/opt/redroid/data/data/...` to ensure host Python scripts have persistent read/write access.
- Enabled `redroid-photo-scanner.service` and `redroid-daily-uploader.timer` on Aurora.

### Step 5: Live End-to-End Verification
- **Test 1**: Local Aurora staging of `test_aurora_sync.jpg` verified cloud sync in <20s (`cloud_media_key: AF1QipMDnoXaLpUkPhCD-D8-UJRvZN4lmQbbx-UgXG2O`).
- **Test 2**: Live cross-host test of `test_pipeline_crosshost.jpg` placed in NAS inbox:
  - Streamed to Aurora `/dev/shm` in 0.25s.
  - Validated integrity & SHA-256 (`c621cd2defc3f6d8...`).
  - Ingested into DCIM and uploaded to cloud.
  - Verified `SYNCED` consensus via `verify_backup.py` (`cloud_media_key: AF1QipNR2mnJQvqZ82C0J-IA-DvFqBmIbcR52zB5BSuA`).
  - Automatically evicted from NAS inbox and RAM disk staging.

### Step 6: NAS Decommissioning
- Stopped and disabled `redroid-photo-scanner.service` and `redroid-daily-uploader.*` on NAS.
- Removed container `redroid-pixel1` on NAS.
- NAS available RAM increased to **4.5 GiB** (used RAM dropped to 3.0 GiB, load average 0.22).


---

## 4. Phase 2 Evolution: Account Migration, Hardened Batch Architecture & Zero-Wear Ingestion (Nov 14–15, 2026)

### Incident & Transition Drivers:
1. **Account Migration Request**: User requested transitioning the backup target from `sl4ught3rcl4y@gmail.com` (Account 0) to personal account `humananimal.ds@gmail.com` (Account 1, Deep Shah).
2. **Cross-Account Contamination Prevention**: Preventing local camera roll purging from deleting or trashing Fenil's wedding photos on `sl4ught3r`'s cloud library.
3. **Hardware Safety Audit**: Identifying and eliminating NAS NVMe (`/volume2`) wear caused by candidate inbox staging.
4. **SSH Handshake Latency & Bottleneck Review**: Uncovering ~1,000 separate SSH connection handshakes per 5 GB batch and replacing with persistent OpenSSH multiplexing.
5. **Local SSD Bloat Prevention**: Eliminating permanent accumulation of uploaded files in Aurora's DCIM via post-consensus batch eviction.

### Implementation & Verification Milestones:
- **Zero-Contamination Account Switch**:
  - Purged 2,797 wedding photos from local `/opt/redroid/data/media/0/DCIM/Camera` before activating Account 1.
  - Verified remote cloud library on `sl4ught3r` remained 100% intact (0 tombstones, 0 remote trash). Confirmed 60 GB cold master archive (`wedding_archive_DF.tar`) on Raspberry Pi 5 SMR pool (`/mnt/media-storage`).
  - Activated `humananimal.ds@gmail.com` in `photos.backup.backup_prefs.xml` (`backup_prefs_account_id=1`).
  - Verified visual Google Photos state: `☁ Complete` with green checkmark badge, unlimited Pixel 1 storage waiver banner confirmed active.
- **NAS NVMe Zero-Wear Enforcement**:
  - Completely purged legacy `/volume2/docker/redroid/inbox` on NAS NVMe.
  - Converted the pipeline to stream strictly read-only from the 10TB Seagate IronWolf CMR mechanical HDD (`/volume1`), achieving infinite read endurance with zero NAS SSD wear.
  - Removed dangerous `remove_nas_file()` function; NAS host connection is 100% read-only.
- **OpenSSH ControlMaster Multiplexing**:
  - Configured persistent master sockets in `~/.ssh/controlmasters/` on Aurora (`ControlMaster auto`, `ControlPersist 1h`).
  - Reduced command execution latency from ~500ms down to `<15ms` per call.
- **Batch Streaming & Parallel Upload Pipeline**:
  - Replaced per-file sequential lockstep with continuous single-session `tar` stream: `ssh nas "tar -C / -cf - --verbatim-files-from -T -"` piped to `tar -xf - -C /dev/shm/redroid_staging --transform=s,.*/,,`.
  - Streamed 5.0 GB batches in ~45 seconds across LAN (~110 MB/s).
  - Deep validation: verified magic bytes/trailers (JPEG `FF D8 ... FF D9`, PNG `89PNG`) and `ffprobe` for video containers, catching corrupted motion photo trailers and AppleDouble metadata files.
  - Deployed batch into ReDroid DCIM, enabling Google Photos' internal multi-threaded HTTP client to upload in parallel.
- **Selective Post-Consensus Eviction**:
  - Verified batch consensus in `gphotos1.db` (`state == 1` and `quota_charged_bytes == 0`).
  - Selectively evicted verified files from Aurora SSD, freeing ~5.0 GB daily and keeping DCIM lean.
- **Structured Observability & SOT Sync**:
  - Implemented `pipeline_events` and `batch_history` tables in `/opt/redroid/config/media_sync_inventory.db`.
  - Integrated WAL checkpointing (`PRAGMA wal_checkpoint(TRUNCATE)`) and automated DB snapshot streaming to NAS `/volume1/docker/redroid_backup/media_sync_inventory.db`.
- **First Production Batch Results (Nov 14, 2026)**:
  - Total files uploaded and verified: **311 files**.
  - Total data uploaded: **5,095.04 MB** (~4.976 GB / 5,342,540,604 bytes).
  - Quota charged: **`0 bytes`** across all 311 items.
  - Corrupted files: 0.

- **Morning Production Batch & ModernMediaScanner Hardening (Nov 15, 2026)**:
  - **Pixel Motion Photo (`.MP.jpg`) Integrity Patch**: Identified that Google Pixel Motion Photos append an MP4 micro-video track to the tail of the JPEG, causing conventional EOI trailer checks (`0xFF 0xD9`) to fail. Patched `verify_media_integrity()` to search the tail buffer for `b"ftyp"` embedded micro-containers, preventing false rejections.
  - **AOSP ModernMediaScanner Fallback Trap**: Discovered that calling `content call --method scan_volume --uri content://media --arg external_primary` on Android 10/11 defaults unmapped volume arguments to internal storage (`/`), initiating a recursive filesystem traversal into `/sys/kernel/slab/` and `/sys/kernel/debug/` that blocks `ModernMediaScanner`'s worker thread.
  - **Chunked In-Container Broadcast Fix**: Replaced `scan_volume` with a chunked (100 files/exec) in-container shell loop broadcasting `android.intent.action.MEDIA_SCANNER_SCAN_FILE`, reducing indexing latency to $<2$ seconds.
  - **Batch 1 (`batch_1794768931_de9e58`)**: Streamed 557 candidates (5,120 MB) over LAN in 94.82s (54 MB/s); deployed and verified 438 items (4,492.77 MB) with 0 quota charged.
  - **Batch 2 (`batch_1794770142_fc61b3`)**: Ingested remaining 112 Motion Photo items (626.00 MB); verified consensus and evicted all 112 items.
  - **Total Data Uploaded Today**: **5,368,147,420 bytes (~5.00 GB)** across 550 verified items.
  - **Quota Charged**: **`0 bytes`** (100% covered under Pixel 1 original quality unlimited tier).
  - **Twice-Daily Automated Schedule**: Configured `redroid-daily-uploader.timer` to fire morning (08:00 AM PST / 16:00 UTC) and night (08:00 PM PST / 04:00 UTC next day), strictly adhering to the 10.0 GB/day limit.

---

## 5. Phase 3: Autonomous EXIF & Metadata Synthesis Engine & Glitch Remediation (Nov 15, 2026)

### Incident & Problem Analysis:
1. **The Metadata Glitch**:
   - Following the morning ingestion runs, the user noticed that 172 photos in Google Photos appeared under "Nov 13" and "Nov 14" instead of their true historical dates.
   - Files affected included Snapchat downloads (`Snapchat-838539229.jpg`), WhatsApp media, and chat dump exports (`photo_14@09-07-2023_21-11-38.jpg`).
2. **Root Cause Identification**:
   - Binary inspection of NAS source files with `PIL.Image.getexif()` confirmed zero embedded EXIF tags.
   - When Google Photos encounters an image without `DateTimeOriginal`, it falls back strictly to the Android filesystem `mtime` (which matched the exact moment the file was extracted to disk during staging).
3. **Architecture Evaluation: In-Flight vs. 900 GB Bulk Pre-processing**:
   - The user proposed pre-processing and staging ~900 GB of media on Aurora's NVMe drive to fix EXIF headers in bulk.
   - **Empirical Benchmark**: Measured `piexif.insert()` execution time on Aurora: **`0.086 ms` per file** (<0.05 seconds of CPU time and <15 MB RAM for an entire 500-file batch).
   - **Trade-off Gate**: Aurora's root filesystem had 806 GB available. Staging 900 GB would exhaust disk capacity (>95%), trigger Docker volume crashes, incur unnecessary NVMe flash wear, and yield zero upload acceleration due to Google's 10 GB/day rate limit.
   - **Decision**: Implemented zero-wear in-flight EXIF synthesis in POSIX RAM (`/dev/shm`) during standard batch streaming.

### Implementation & Hardening:
- **Autonomous EXIF Synthesis**:
  - Provisioned `/opt/redroid/venv` with `Pillow` and `piexif`.
  - Added `infer_media_timestamp(fn, nas_path)` and `inject_or_synthesize_metadata(file_path, fn, nas_path)` to `/opt/redroid/scripts/pipeline_processor.py`.
  - Infers capture dates from chat export filenames (`DD-MM-YYYY_HH-MM-SS`), ISO timestamps (`YYYY-MM-DD HH.MM.SS`), parent directory paths (`/YYYY/MM/`), or NAS filesystem timestamps.
  - Losslessly injects `piexif.ExifIFD.DateTimeOriginal`, `piexif.ExifIFD.DateTimeDigitized`, and `piexif.ImageIFD.DateTime`, syncing file `mtime` via `os.utime()`.
- **In-Container MediaStore Shell Quoting**:
  - Replaced Python string tokenization in `trigger_cloud_backup` with `find /storage/emulated/0/DCIM/Camera/ -maxdepth 1 -type f ! -name '.*' -exec am broadcast ... \;` to eliminate word-splitting bugs on filenames with spaces and parentheses.
- **Service & Timer Alignment**:
  - Updated `/opt/redroid/scripts/daily-batch-uploader.sh` to execute via `/opt/redroid/venv/bin/python3`.
  - Verified `redroid-daily-uploader.timer` active for twice-daily runs (08:00 AM & 08:00 PM PST).

### 171-File Remediation & Verification:
- **Safe Reset & Deduplication**:
  - The user trashed the 171 malformed photos in Google Photos (preserving 1 genuine Pixel 9 photo).
  - Reset all 171 candidate rows in `local_inventory` to `PENDING` and purged their keys from `cloud_inventory` and `uploaded_manifest.txt`.
- **Live Re-Ingestion**:
  - Streamed, synthesized EXIF metadata, and deployed all 171 items to ReDroid DCIM.
  - **100% Consensus Achieved**: All 171 items verified in `gphotos1.db` (`state = 1`, `quota_charged_bytes = 0`).
  - **Verified True Cloud Dates**:
    - `photo_2024-06-18 19.44.04.jpeg` $\to$ **`2024-06-18 19:44:04`** (Quota: 0 bytes)
    - `photo_14@09-07-2023_21-11-38.jpg` $\to$ **`2023-07-09 21:11:38`** (Quota: 0 bytes)
    - `photo_10@09-07-2023_18-24-16.jpg` $\to$ **`2023-07-09 18:24:16`** (Quota: 0 bytes)
    - `Snapchat-838539229.jpg` $\to$ **`2023-07-09 12:00:00`** (Quota: 0 bytes)
    - `Snapchat-455855546.jpg` $\to$ **`2023-07-30 09:16:45`** (Quota: 0 bytes)
  - All 171 staging files cleanly evicted from DCIM (0 remaining files). SOT database WAL checkpointed and mirrored to NAS.
