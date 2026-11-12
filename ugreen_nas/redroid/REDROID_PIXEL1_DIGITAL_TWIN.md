# 📱 Virtual Pixel 1 (Sailfish) — Redroid Digital Twin (Archived / Migrated to Aurora A3)

> **Status**: 🔄 **MIGRATED TO AURORA A3** (`192.168.1.111`)  
> **Original Host**: UGREEN DXP2800 NAS (`192.168.1.80`)  
> **Current Authoritative Runbook**: [Learning/aurora_a3/redroid/REDROID_PIXEL1_DIGITAL_TWIN.md](../../aurora_a3/redroid/REDROID_PIXEL1_DIGITAL_TWIN.md)  
> **Migration Date**: 2026-11-12  
> **NAS State**: ReDroid container decommissioned to reclaim 1.5+ GiB RAM. NAS operates strictly as low-latency NVMe ingestion inbox drop-point (`/volume2/docker/redroid/inbox`).

---

## 🎯 Architectural Purpose & Migration Context

To replicate the physical Google Pixel 1 (`sailfish`) hardware environment headlessly within an isolated Linux container. This unlocks lifetime unlimited Google Photos backups in Original Quality (0 bytes storage quota charged) while allowing the aging, battery-degraded physical Pixel 1 hardware to be retired permanently.

On 2026-11-12, the entire ReDroid container, patched 64-bit `libcutils.so` runtime, and 2,819 synced items were migrated to the **OrigiMagic Aurora A3 (`192.168.1.111`)** to eliminate memory pressure and hardware watchdog resets on the NAS. See the Aurora runbook for live operations.

---

## 📊 Live Resource Telemetry & Performance Footprint

| Metric / Dimension | Baseline Host State | Redroid Container (`redroid-pixel1`) | Inotify Daemon (`photo-scanner`) | Total Stack Footprint |
| :--- | :--- | :--- | :--- | :--- |
| **CPU Utilization (Idle)** | ~1.5% | **0.81%** (4-Core Intel N100) | **0.00%** | **~0.81%** |
| **RAM Usage** | 3.2 GiB (OS + Arr stack) | **1.18 GiB** (15.76% of 8GB pool) | **9.3 MiB** | **~1.19 GiB** |
| **GPU Acceleration** | Intel Gen12 UHD 24EU | Hardware Host Passthrough (`/dev/dri/renderD128`) | N/A | Hardware Mesa EGL |
| **Network I/O** | 2.5 GbE Interface | Direct Bridged Host Network (Port `5555` ADB) | Local IPC | <20 MB (sync bursts) |
| **Storage Consumption** | 4TB NVMe SSD Tier (`/volume2`) | Container Rootfs: **2.4 GB** \| `/data`: Persistent Volume | Memory-mapped | Isolated in `/volume2/docker/redroid/` |

---

## 🏗️ Hardware Identity & Build Properties

```properties
ro.product.brand=google
ro.product.manufacturer=Google
ro.product.model=Pixel
ro.product.name=sailfish
ro.product.device=sailfish
ro.product.board=sailfish
ro.board.platform=msm8996
ro.build.flavor=sailfish-user
ro.build.tags=release-keys
ro.build.type=user
ro.build.fingerprint=google/sailfish/sailfish:10/QP1A.191005.007.A3/5972272:user/release-keys
```

### Injected Feature Manifests
`/system/etc/sysconfig/pixel_2016_exclusive.xml`:
```xml
<?xml version="1.0" encoding="utf-8"?>
<config>
    <feature name="com.google.android.feature.PIXEL_2016_PREMIUM" />
    <feature name="com.google.android.feature.PIXEL_2016_EXCLUSIVE" />
    <feature name="com.google.android.apps.photos.NEXUS_PRELOAD" />
    <feature name="com.google.android.apps.photos.PIXEL_2016_PRELOAD" />
</config>
```

---

## 🔄 End-to-End Operational Pipeline

```text
[Mobile Phone / Camera / Mac]
          │
          │ (Auto-push via FolderSync over SMB3 / Syncthing)
          ▼
┌─────────────────────────────────────────────────────────────┐
│ 🗄️ UGREEN NAS (Intel N100 — 192.168.1.80)                  │
│                                                             │
│  /volume2/docker/redroid/inbox/ (High-Speed NVMe Tier)      │
│             │                                               │
│             │ (Inotify Watcher Trigger — close_write)       │
│             ▼                                               │
│  [redroid-photo-scanner.service]                            │
│   └── Issues: content call --method scan_volume             │
│             │                                               │
│             ▼                                               │
│  [Docker: redroid-pixel1 Container on /volume2]             │
│   ├── /sdcard/DCIM/Camera/ (Internal Android Gallery)       │
│   └── Google Photos App (Authenticated to Staging Account B)│
└─────────────┬───────────────────────────────────────────────┘
              │
              │ (Uploads under Pixel 1 Original Quality Waiver: 0 GB Quota)
              ▼
┌─────────────────────────────────────────────────────────────┐
│ ☁️ Google Cloud Infrastructure                              │
│   Account B (0 GB charged)                                  │
│       │                                                     │
│       │ (Native Google Partner Sharing with Auto-Save ON)   │
│       ▼                                                     │
│   Account A (Deep's Primary Master Google Account)          │
│       • High-resolution original photos in main feed        │
│       • Zero risk to Account A security or login context    │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛡️ Isolation & Safety Directives
1. **Zero Host Mutation:** No kernel swapping, custom base package removals, or OS-level reconfigurations were performed on either host node.
2. **Dedicated Staging Account (Account B):** Primary Account A never directly connects or authenticates to the virtual container. All cloud transfers execute via Google's native Partner Sharing API.
3. **Master Archive Integrity:** The authoritative Single Source of Truth for all high-resolution media remains on the **10TB CMR IronWolf Btrfs pool** on the NAS (`/volume1/personal_folder/Photos`).

---

## ⚙️ Automated Ingestion & Daily Batch Worker Architecture

### 1. Inotify Media Scanner (`redroid-photo-scanner.service`)
- **Path**: `/volume2/docker/redroid/scripts/inotify-media-scanner.sh`
- **Mechanism**: Watches `/volume2/docker/redroid/inbox` for new writes/moves. Debounces for 3 seconds, sets permissions to `media_rw:media_rw` (`1023:1023`), moves files into `/volume2/docker/redroid/data/media/0/DCIM/Camera`, and broadcasts explicit `android.intent.action.MEDIA_SCANNER_SCAN_FILE` intents for every file to bypass Android 11 scoped storage scan limitations.

### 2. Daily Batch Ingest Worker (`redroid-daily-uploader.service` & `.timer`)
- **Worker Script**: `/volume2/docker/redroid/scripts/daily-batch-uploader.sh`
- **Manifest**: Tracks processed files in `/volume2/docker/redroid/scripts/uploaded_manifest.txt` to guarantee zero duplicate processing.
- **Budget**: Stages batches up to ~1 GiB per run across `/volume1/@home/Deep Shah/{Photos,MobileBackup,Yellowstone,Grad Photoshoot,GOPro}` into the NVMe inbox tier.
- **Schedule**: Automatically fires at **03:30 AM** daily via systemd timer (`redroid-daily-uploader.timer`).
- **Manual Trigger**: `echo '<nas_password>' | sudo -S systemctl start redroid-daily-uploader.service`.

### 3. Production Verification & Quota Telemetry (Verified 2026-11-10)
- **Ingestion Test**: 125 RAW/DSLR and GoPro files totaling **>2.2 GB** staged and ingested.
- **Google Photos Telemetry**:
  - Upload Status: `Backup complete`
  - Upload Quality: `Original quality` (grandfathered Pixel 1 waiver confirmed)
  - Quota Impact: **0 bytes charged** (Storage remained constant at `552.31 MB of 5 TB`).
  - Partner Sharing: Invitation dispatched to `deepshah7977@gmail.com` with `All photos` and `All time` active.
