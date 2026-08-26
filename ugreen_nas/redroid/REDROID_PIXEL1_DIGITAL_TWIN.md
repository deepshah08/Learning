# 📱 Virtual Pixel 1 (Sailfish) — Redroid Digital Twin on UGREEN NAS

> **Status**: 🟢 **Production / Operational**  
> **Host Target**: UGREEN DXP2800 NAS (`192.168.1.80`)  
> **Deployment Architecture**: Containerized OCI (Docker Engine 29.4)  
> **Last Verified**: 2026-08-25 23:45 PDT  

---

## 🎯 Architectural Purpose

To replicate the physical Google Pixel 1 (`sailfish`) hardware environment headlessly within an isolated Linux container on the UGREEN NAS. This unlocks lifetime unlimited Google Photos backups in Original Quality (0 bytes storage quota charged) while allowing the aging, battery-degraded physical Pixel 1 hardware to be retired permanently.

---

## 📊 Live Resource Telemetry & Performance Footprint

| Metric / Dimension | Baseline Host State | Redroid Container (`redroid-pixel1`) | Inotify Daemon (`photo-scanner`) | Total Stack Footprint |
| :--- | :--- | :--- | :--- | :--- |
| **CPU Utilization (Idle)** | ~1.5% | **0.81%** (4-Core Intel N100) | **0.00%** | **~0.81%** |
| **RAM Usage** | 3.2 GiB (OS + Arr stack) | **1.18 GiB** (15.76% of 8GB pool) | **9.3 MiB** | **~1.19 GiB** |
| **GPU Acceleration** | Intel Gen12 UHD 24EU | Hardware Host Passthrough (`/dev/dri/renderD128`) | N/A | Hardware Mesa EGL |
| **Network I/O** | 2.5 GbE Interface | Direct Bridged Host Network (Port `5555` ADB) | Local IPC | <20 MB (sync bursts) |
| **Storage Consumption** | 10TB Btrfs Pool | Container Rootfs: **2.4 GB** \| `/data`: Persistent Volume | Memory-mapped | Isolated in `/volume1/docker/redroid/` |

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
│  /volume1/docker/redroid/inbox/                             │
│             │                                               │
│             │ (Inotify Watcher Trigger — close_write)       │
│             ▼                                               │
│  [redroid-photo-scanner.service]                            │
│   └── Issues: content call --method scan_volume             │
│             │                                               │
│             ▼                                               │
│  [Docker: redroid-pixel1 Container]                         │
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
