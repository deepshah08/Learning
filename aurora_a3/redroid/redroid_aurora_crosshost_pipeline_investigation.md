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
