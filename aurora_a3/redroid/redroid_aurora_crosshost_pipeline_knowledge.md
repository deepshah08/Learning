# 🧠 Knowledge: Cross-Host ReDroid Pipeline & Large-File Media Architecture

> **Domain**: Containerized Android Virtualization, Cross-Host Automation & Cloud Ingestion  
> **Target Node**: OrigiMagic Aurora A3 (`192.168.1.111`), UGREEN DXP2800 NAS (`192.168.1.80`)  
> **Status**: Production Reference  
> **Active Backup Account**: `humananimal.ds@gmail.com` (Deep Shah, Account 1)  

---

## 1. Architectural Summary

This document formalizes the production design, operational contracts, and database synchronization patterns for offloading Google Photos virtualization and media ingestion from a storage-focused NAS to an asynchronous, compute-dense worker node.

```mermaid
sequenceDiagram
    autonumber
    participant NAS_HDD as NAS CMR HDD (/volume1)
    participant SSH_CM as OpenSSH ControlMaster
    participant AuroraRAM as Aurora /dev/shm (POSIX RAM)
    participant Worker as pipeline_processor.py
    participant ReDroid as redroid-pixel1 (DCIM)
    participant Cloud as Google Photos Cloud
    participant SQLite as gphotos1.db & inventory.db
    participant NAS_BK as NAS SOT Snapshot (/volume1)

    Worker->>SQLite: Pre-flight check & cloud deduplication (0-quota skip)
    Worker->>SSH_CM: Stream batch manifest over persistent SSH socket
    SSH_CM->>NAS_HDD: Read-only sequential tar stream (cat/tar)
    NAS_HDD-->>AuroraRAM: Buffer batch in /dev/shm (zero SSD writes)
    Worker->>Worker: Deep validation (magic bytes & ffprobe)
    Worker->>ReDroid: Deploy validated batch to DCIM/Camera/
    Worker->>ReDroid: Broadcast MediaStore volume scan & JobScheduler
    ReDroid->>Cloud: Parallel multi-threaded HTTP upload (Pixel 1 0-quota)
    Worker->>SQLite: Monitor batch consensus in gphotos1.db
    SQLite-->>Worker: Batch verified (state=1, quota=0)
    Worker->>ReDroid: Selectively evict verified files from Aurora SSD
    Worker->>SQLite: Record batch history & pipeline_events
    Worker->>NAS_BK: Flush WAL & sync DB snapshot to NAS
```

---

## 2. Key Operational Principles

### 1. OpenSSH ControlMaster Multiplexing (<15ms Latency)
To eliminate repeated SSH connection overhead (TCP 3-way handshakes, TLS/KEX cipher renegotiation, and PAM authentication loops that cost ~500ms per file), Aurora maintains persistent master sockets in `~/.ssh/controlmasters/` (`ControlMaster auto`, `ControlPersist 1h`). Ad-hoc commands and candidate queries execute over local Unix domain sockets in `<15ms`.

### 2. Zero NAS NVMe Wear & Mechanical CMR Streaming
The legacy `/volume2/docker/redroid/inbox` on the NAS NVMe has been **completely eliminated**. NAS media is read strictly read-only from the 10TB Seagate IronWolf CMR mechanical drive (`/volume1`), which possesses infinite read endurance without flash cell degradation. The NAS host connection is 100% read-only; zero files are deleted or modified on the NAS.

### 3. Continuous Single-Session Batch Streaming
Candidate media is assembled into daily batches constrained mathematically to $\le 5.00\text{ GiB}$. The entire batch streams in a single continuous `tar` pipe over persistent SSH directly into Aurora's POSIX RAM disk (`/dev/shm`), achieving wire-speed LAN throughput (~110–115 MB/s) in ~45 seconds.

### 4. Multi-Table SQLite WAL Consensus
The verification engine cross-references internal Google Photos SQLite tables in read-only WAL mode to prevent false positives:
1. `backup_item_status`: `state = 1` and `media_key_on_upload IS NOT NULL`.
2. `MediaTombstone`: Zero matches against `remoteMediaKey` and `dedupKey`.
3. `remote_media`: `trash_timestamp IS NULL` or `0`, and `quota_charged_bytes == 0` (Pixel 1 waiver).
4. `media`: `is_deleted = 0`.
5. `permanent_failure_reason == 0`.

### 5. Selective Post-Consensus Batch Eviction
To prevent host SSD bloat, files staged in `/opt/redroid/data/media/0/DCIM/Camera/` are automatically evicted **only after** `gphotos1.db` consensus confirms `state == 1` and `quota_charged_bytes == 0`. Any unverified or failed files remain safely on disk for the subsequent run.

### 6. Structured Observability & Eventual Consistency SOT Sync
- **Local Event Logging**: Every lifecycle event (candidate collection, tar transfer, integrity failure, consensus progress, and eviction) is recorded in `pipeline_events` and `batch_history` within `/opt/redroid/config/media_sync_inventory.db`.
- **NAS SOT Snapshot**: At the end of each batch run, Aurora checkpoints the SQLite WAL (`PRAGMA wal_checkpoint(TRUNCATE)`) and streams a consistent snapshot to the NAS at `/volume1/docker/redroid_backup/media_sync_inventory.db`, ensuring permanent disaster recovery resilience.

### 7. Android MediaStore In-Container Chunked Broadcast
- **AOSP ModernMediaScanner Root Fallback Trap**: Calling `content call --method scan_volume --uri content://media --arg external_primary` on Android 10/11 defaults unmapped volume arguments to internal storage (`/`), initiating a recursive filesystem traversal into `/sys/kernel/slab/` and `/sys/kernel/debug/` that blocks `ModernMediaScanner`'s worker thread.
- **Chunked In-Container Broadcast Solution**: Files deployed into `/storage/emulated/0/DCIM/Camera/` are broadcast in chunks of 100 via a single in-container shell loop:
  ```bash
  for f in "$@"; do [ -f "$f" ] && am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d "file://$f" >/dev/null 2>&1; done
  ```
  This eliminates multi-process Python `subprocess` overhead while ensuring MediaStore and Google Photos index newly staged media in $<2$ seconds.

---

## 3. Production Benchmark & Telemetry (5.0 GB Batch Baseline)

| Telemetry Metric | Aurora A3 (`192.168.1.111`) | UGREEN DXP2800 NAS (`192.168.1.80`) |
| :--- | :--- | :--- |
| **CPU Load Average** | `0.93` (8C/16T Ryzen 7 8745HS, <6% CPU) | `0.15` (4C/4T Intel N100, 98% idle) |
| **RAM Utilization** | 3.1 GiB used / 11 GiB available | 3.4 GiB used / 4.2 GiB available |
| **Swap Activity** | 2.7 MiB (zero swap wear on SSD) | 1.1 GiB (static, no churn) |
| **Storage Usage** | 806 GB available (10% used) | 7.5 TB available on `/volume1` (19%) |
| **NVMe Flash Writes** | Zero NVMe staging (POSIX RAM `/dev/shm`) | Zero writes to `/volume2` (inbox deleted) |
| **Batch Completion** | 550 files / 5,118.77 MB (5.00 GB) | 100% SOT SQLite snapshot mirrored (20 MB) |
| **Google Cloud Status**| 550 / 550 verified (`state=1`, `quota=0`) | Quota charged: **0 bytes** |

---

## 4. Command Reference & Runbook

### Service Management (Aurora):
```bash
# View live batch uploader logs:
tail -f /opt/redroid/scripts/batch-uploader.log

# Check status of twice-daily batch timer (08:00 AM & 08:00 PM PST):
systemctl status redroid-daily-uploader.timer

# Check rate limiter quota and balance (10 GB/day baseline):
python3 /opt/redroid/scripts/rate_limiter.py status

# Run inventory deduplication stats:
python3 /opt/redroid/scripts/media_inventory_manager.py stats
```

### Manual Trigger & Burst Override:
```bash
# Execute immediate batch processing:
python3 /opt/redroid/scripts/pipeline_processor.py

# Execute manual burst with custom ceiling (e.g. 10 GB):
python3 /opt/redroid/scripts/pipeline_processor.py --burst 10

# Dry-run candidate discovery without staging or uploading:
python3 /opt/redroid/scripts/pipeline_processor.py --dry-run
```
