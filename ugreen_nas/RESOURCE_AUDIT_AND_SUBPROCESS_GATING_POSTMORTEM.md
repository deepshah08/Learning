# 🛡️ Homelab Full-Stack Resource Audit & Subprocess Gating Post-Mortem

> **Domain**: Hardware Wear Prevention, Mechanical Storage Safeguards & Process Lifecycle Management  
> **Target Nodes**: UGREEN DXP2800 NAS (`192.168.1.80`) & Raspberry Pi 5 (`192.168.1.92`)  
> **Date**: 2026-09-12  
> **Status**: 🟢 **Hardened & Synchronized to Single Source of Truth**  

---

## 1. Executive Summary & Problem Analysis

Over a multi-day diagnostic period, two interconnected categories of operational friction were identified and systematically resolved across the hybrid homelab infrastructure:

1. **Unconstrained Mechanical Disk Scanning & Remote Subprocess Orphaning**:
   - Diagnostic search commands (`grep -rn ... /volume1` and `lsof +D /volume1`) initiated via SSH lacked remote OS-level execution timeouts.
   - When client-side tool steps were canceled locally, the remote SSH sessions orphaned child worker processes on the NAS.
   - Child processes continued recursive linear traversals across the 10TB Seagate IronWolf mechanical pool (`/volume1`), generating ~28% CPU load, sustained ~460 MB/s read bandwidth, and thermal spikes up to 79°C that engaged the high-RPM fan profile.
2. **Periodic Secondary Sync Misalignment**:
   - The Raspberry Pi 5's secondary Pi-hole list synchronization script (`/usr/local/bin/sync-pihole-to-nas.sh`) was targeting `/volume1` instead of the solid-state NVMe tier (`/volume2`).
   - The sync was scheduled at `*/30 * * * *` (48 times/day), generating ~880 MB/day of redundant database writes and waking mechanical drives every 30 minutes.
3. **Headless Pi 5 WayVNC Restart Churn**:
   - On the Raspberry Pi 5, `rpi-connect-wayvnc.service` was stuck in an unhandled 5-second crash loop (accumulating over 93,400 restarts) due to the absence of a Wayland display server on headless boot.

---

## 2. In-Depth Resource Footprint Audit

### A. UGREEN DXP2800 NAS (`192.168.1.80`)

| Subsystem | Metric / Configuration | Operational State |
| :--- | :--- | :--- |
| **CPU (Intel N100 4C/4T)** | Load Average: `0.73` P95 | 🟢 Idle, low-power C-states active |
| **RAM (8GB DDR5)** | 3.8 GB used / 3.8 GB available | 🟢 4× zRAM partitions holding 1.7GB compressed into ~500MB physical RAM |
| **NVMe SSD Tier (`/volume2`)** | 4TB WD_BLACK SN850X | 🟢 Houses all SQLite DBs, Docker runtimes, and Pi-hole data |
| **Mechanical Tier (`/volume1`)** | 10TB Seagate IronWolf CMR | 🟢 **0 reads / 0 writes (0 RPM idle state restored)** |
| **Chassis Cooling (`hwmonitor`)** | Fan PWM: 96 (~980 RPM) | 🟢 Idle quiet profile (<22 dB), HDD at 44°C |

#### Removals & Cleanups:
- **`com.ugreen.netdisk` (`cloud_serv`)**: Uninstalled via UGOS App Center. Reclaimed 0.5% continuous CPU and eliminated open file handles on `/volume1`.
- **`openclaw-gateway-1`**: Container uninstalled. Reclaimed 301 MB RAM.
- **Orphaned Containers (`adoring_pike`)**: Stopped and pruned.

---

### B. Raspberry Pi 5 (`192.168.1.92`)

| Subsystem | Metric / Configuration | Operational State |
| :--- | :--- | :--- |
| **CPU (Broadcom BCM2712)** | Temperature: **44.4°C – 46.6°C** | 🟢 Extremely cool, load avg <0.15 |
| **RAM (16GB LPDDR4X)** | 948 MB used / 15.2 GB available | 🟢 Massive headroom, zRAM at 0% usage |
| **Internal MicroSD (`/dev/mmcblk0`)** | 13 GB used / 100 GB available (12%) | 🟢 Minimal write amplification |
| **External SMR HDD (`/dev/sda`)** | 8TB Seagate Expansion USB 3.0 | 🟢 **Drive state: `standby` (0 RPM deep sleep)** |
| **Spindown Automation** | `/etc/udev/rules.d/69-smr-spindown.rules` | 🟢 `hdparm -S 180` (15-min auto-spindown verified) |
| **Filesystem Mount** | `/mnt/media-storage` | 🟢 `noatime,nofail` enforced in `/etc/fstab` |

#### Removals & Cleanups:
- **`rpi-connect-wayvnc.service`**: Stopped, disabled, and masked (`systemctl --user mask`). The 5-second restart loop was halted, ending log churn in `systemd-journald`.

---

## 3. Iterations, Bug Resolutions & Methodology

```text
┌───────────────────────────────────────────────────────────────────────────────────┐
│                      DIAGNOSTIC & SAFEGUARD EVOLUTION                             │
├───────────────────────────────────────────────────────────────────────────────────┤
│ 1. INCIDENT: Unconstrained grep on /volume1 caused 79°C CPU & 1,155 RPM Fan       │
│    ├── Root Cause: Missing hard timeout + remote subprocess orphaning over SSH    │
│    └── Fix: Explicit kill -9, immediate thermals drop to 60°C                     │
│                                                                                   │
│ 2. SYNC REDIRECTION: Pi 5 gravity.db sync targeted /volume1 (HDD)                 │
│    ├── Root Cause: Legacy path in /usr/local/bin/sync-pihole-to-nas.sh            │
│    └── Fix: Redirected to /volume2 (NVMe tier); verified SYNC_OK                  │
│                                                                                   │
│ 3. CADENCE OPTIMIZATION: Sync ran every 30 minutes (880MB/day writes)             │
│    ├── Root Cause: Over-aggressive cron schedule for static adblock lists         │
│    └── Fix: Adjusted to monthly (0 4 1 * *), cutting write volume >96%            │
│                                                                                   │
│ 4. SERVICE PRUNING: Unused background services kept disks warm                    │
│    ├── UGOS Cloud Drives (com.ugreen.netdisk) -> Uninstalled                      │
│    ├── OpenClaw AI Gateway -> Uninstalled                                         │
│    └── Pi 5 WayVNC -> Masked to /dev/null                                         │
└───────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Universal Invariants Codified in `AGENTS.md`

The following mandatory rules are now codified across all agent frameworks:

1. **Mechanical Pool Immunity & Absolute Path Exclusion**:
   - Bulk mechanical storage mounts (`/volume1` on NAS and `/mnt/media-storage` on Pi 5) are **strictly off-limits** for recursive inspection commands (`grep`, `find`, `du`, `lsof`, `rgrep`).
   - Searches must strictly target NVMe tiers (`/volume2`), system config roots (`/etc`, `/usr/local`), or specific files.
2. **Mandatory Hard Timeout Wrappers**:
   - All remote commands inspecting filesystem metadata or processes must execute behind an OS-level timeout wrapper (`timeout 5s <command>`).
3. **Zero Remote Orphaned Subprocesses**:
   - Bounding commands with `timeout 5s` at the remote kernel level ensures child processes are terminated even if the client SSH session drops or is canceled.
4. **Strict Storage Tiering Alignment**:
   - Recurring sync jobs, state files, and containers must bind-mount exclusively to the NVMe solid-state tier (`/volume2`) to allow mechanical HDDs to enter and remain in 0 RPM deep hibernation.
