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
