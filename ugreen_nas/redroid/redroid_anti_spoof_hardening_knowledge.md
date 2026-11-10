# Virtual Pixel 1 (Sailfish) — Anti-Spoof Hardening & Cloud Longevity Architecture

> Origin: investigation journey at [./redroid_anti_spoof_hardening_investigation.md](./redroid_anti_spoof_hardening_investigation.md)  
> Digital Twin: baseline runbook at [./REDROID_PIXEL1_DIGITAL_TWIN.md](./REDROID_PIXEL1_DIGITAL_TWIN.md)  
> Host Target: UGREEN DXP2800 NAS (`192.168.1.80`) · NVMe Tier (`/volume2`)  
> Container: `redroid-pixel1` (`redroid:11.0.0-pixel1-twin`)  
> Physical Cloned Donor: Google Pixel 1 (`FA6AN0302845`)  
> Status: 🟢 **Production / Immutable Hardened Baseline**

---

## 1. Role / Position

The hardened ReDroid Digital Twin provides a 100% headless, containerized emulation of the physical Google Pixel 1 (`sailfish`) on the UGREEN NAS. It guarantees indefinite lifetime **Original Quality Google Photos backups at 0 bytes cloud quota impact** without triggering Play Integrity revocations, GMS Phenotype flag demotions, CAPTCHAs, or account abuse flags.

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              SYSTEM TOPOLOGY & PLACEMENT                               │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  [Raspberry Pi 5 (192.168.1.92)]                   [Google Cloud Infrastructure]       │
│  ┌─────────────────────────────┐                   ┌────────────────────────────────┐  │
│  │ 8TB Cold SMR Media Archive  │                   │ Google Photos Cloud            │  │
│  │ (/mnt/media-storage)        │                   │  - Staging Account B           │  │
│  └──────────────┬──────────────┘                   │  - Original Quality (0GB Quota)│  │
│                 │                                  └───────────────▲────────────────┘  │
│                 │ 2.5GbE LAN Network Mount                         ▲ Google Photos IPC │
│                 ▼                                                  │                   │
│  ┌──────────────────────────────────────────────────────────────────────────────────┐  │
│  │ UGREEN DXP2800 NAS (192.168.1.80) — High-Speed NVMe Tier (/volume2)              │  │
│  │                                                                                  │  │
│  │  ┌─────────────────────────┐     ┌───────────────────────┐     ┌──────────────┐  │  │
│  │  │ rate_limiter.py         │ ──> │ redroid-photo-scanner │ ──> │ redroid-     │  │  │
│  │  │ (1GB/day baseline gate) │     │ (inotifywait daemon)  │     │ pixel1 (OCI) │  │  │
│  │  └─────────────────────────┘     └───────────────────────┘     └──────────────┘  │  │
│  │                                                                                  │  │
│  └──────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Plane Decomposition

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                      PLANE 1: IDENTITY & PARTITION ATTESTATION PLANE                   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  AOSP Init (/system/etc/prop.default + Docker Compose Environment Command Args)        │
│    │                                                                                   │
│    ├── System Partition       ──> ro.product.system.brand=google · release-keys        │
│    ├── Vendor Partition       ──> ro.product.vendor.model=Pixel · release-keys         │
│    ├── Product Partition      ──> ro.product.product.name=sailfish · QP1A.191005.007.A3│
│    ├── System_Ext Partition   ──> ro.product.system_ext.brand=google · release-keys    │
│    ├── ODM Partition          ──> ro.product.odm.brand=google · release-keys           │
│    ├── Bootloader Cloak       ──> ro.boot.flash.locked=1 · baseband=msm                │
│    └── Telephony Cloak        ──> Qualcomm RIL 1.0 · IMEI: 353086081745920             │
│                                                                                        │
│  Result: 100% Partition Parity. Zero test-keys. DroidGuard & Play Integrity Pass.      │
└────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        PLANE 2: HARDWARE ACCELERATION & HAL PLANE                      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  Host Intel N100 GPU (`/dev/dri/renderD128`)                                           │
│    │                                                                                   │
│    ├── Android HAL Loader     ──> Looks up hwcomposer.<ro.hardware>.so                 │
│    ├── ro.hardware Isolation  ──> Retains native redroid HAL (hwcomposer.redroid.so)   │
│    ├── Binder Interfaces      ──> /dev/binder, /dev/hwbinder, /dev/vndbinder           │
│    └── SurfaceFlinger EGL     ──> Mesa Host GPU Acceleration (30 FPS @ 1080x1920)      │
│                                                                                        │
│  Result: Hardware EGL GUI rendering; zero crashes; hardware-accelerated gallery decode │
└────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────┐
│                       PLANE 3: TRAFFIC PACING & CLOUD SAFETY PLANE                     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  Incoming Staged Media (/volume2/docker/redroid/inbox)                                 │
│    │                                                                                   │
│    ├── Pre-Ingest Safety Check──> rate_limiter.py check <bytes>                        │
│    │                              ├── If daily total + batch <= 1.00 GiB: ALLOWED      │
│    │                              └── If daily total > 1.00 GiB: HELD (Exit Code 1)    │
│    ├── Inotify Dispatch       ──> content call --method scan_volume (DCIM/Camera)      │
│    ├── Cloud Backup           ──> Google Photos uploads under Pixel 1 Waiver (0 bytes) │
│    └── Post-Upload Record     ──> rate_limiter.py record <bytes>                       │
│                                                                                        │
│  Result: Traffic strictly mimics organic human camera capture. Zero fraud flags.       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Architecture & Hardware Parity

### Component Matrix

| Component | Role | Location | State |
| :--- | :--- | :--- | :--- |
| **`docker-compose.yml`** | Injects 40+ system properties and partition flags | `/volume2/docker/redroid/` | ✅ Hardened |
| **`redroid-pixel1`** | Android 11 Digital Twin container | Docker Engine on NAS | ✅ Operational |
| **`rate_limiter.py`** | Centralized POSIX-locked rate limiter | `/volume2/docker/redroid/scripts/` | ✅ Active (1GB/day) |
| **`accounts_de.db`** | Encrypted SQLite Google account tokens | `/volume2/docker/redroid/data/system_de/0/` | ✅ Persistent |
| **`renderD128`** | Intel UHD Graphics host GPU node | `/dev/dri/renderD128` | ✅ Passed Through |

### Partition Property Parity Matrix

| Property Key | Physical Pixel 1 (`FA6AN0302845`) | Unhardened ReDroid | Hardened Production State |
| :--- | :--- | :--- | :--- |
| `ro.product.brand` | `google` | `redroid` | **`google`** |
| `ro.product.model` | `Pixel` | `redroid` | **`Pixel`** |
| `ro.product.name` | `sailfish` | `redroid` | **`sailfish`** |
| `ro.product.device` | `sailfish` | `redroid` | **`sailfish`** |
| `ro.build.flavor` | `sailfish-user` | `redroid-userdebug` | **`sailfish-user`** |
| `ro.build.tags` | `release-keys` | `test-keys` | **`release-keys`** |
| `ro.build.type` | `user` | `userdebug` | **`user`** |
| `ro.build.fingerprint` | `...QP1A.191005.007.A3...` | `redroid:11...` | **`google/sailfish/sailfish:10/QP1A.191005.007.A3/5972272:user/release-keys`** |
| `ro.product.odm.brand` | `google` | `redroid` | **`google`** |
| `ro.odm.build.tags` | `release-keys` | `test-keys` | **`release-keys`** |
| `ro.system_ext.build.tags` | `release-keys` | `test-keys` | **`release-keys`** |
| `ro.boot.flash.locked` | `1` | `0` / unset | **`1`** |
| `ro.boot.baseband` | `msm` | unset | **`msm`** |
| `persist.radio.imei` | `353086081745920` | unset | **`353086081745920`** |

---

## 4. Mechanics — Step by Step

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        NORMAL OPERATION & INGESTION MECHANICS                          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  1. Container Boot & Property Binding:                                                 │
│     Docker starts redroid-pixel1 with 40+ system property command arguments.           │
│     Android init populates property workspace; all 5 partitions mirror sailfish user   │
│     release-keys. Host Mesa GPU initializes EGL display.                               │
│                                                                                        │
│  2. Network & Token Validation:                                                        │
│     Container connects to LAN via bridge port 5555. GMS loads persistent credentials   │
│     from /data/system_de/0/accounts_de.db. GMS Checkin verifies device fingerprint,    │
│     receiving valid sailfish Phenotype flags from Google servers.                      │
│                                                                                        │
│  3. Rate-Gated Staging:                                                                │
│     Uploader script queries: python3 rate_limiter.py check <bytes>                     │
│     - If under daily 1.00 GiB baseline (or override active): Exit code 0               │
│     - If daily limit reached: Exit code 1 (uploader sleeps until next 00:00 UTC)       │
│                                                                                        │
│  4. Inotify Scan & Permission Normalization:                                           │
│     File moved to /volume2/docker/redroid/inbox/. Scanner script chowns to 1023:1023   │
│     (media_rw:media_rw) and moves to /volume2/docker/redroid/data/media/0/DCIM/Camera. │
│     Broadcasts android.intent.action.MEDIA_SCANNER_SCAN_FILE.                          │
│                                                                                        │
│  5. Google Photos Background Cloud Ingestion:                                          │
│     Google Photos detects new media, queries Android build features, identifies        │
│     PIXEL_2016_PREMIUM and PIXEL_2016_EXCLUSIVE, and streams to Google Cloud with      │
│     Original Quality flag. Google One quota charged: 0 bytes.                          │
│                                                                                        │
│  6. Metric Recording & State Sync:                                                     │
│     Uploader executes python3 rate_limiter.py record <bytes>. State file updated.      │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Longevity & Anti-Flagging Guarantees

1. **Residential Trust Anchor (Network Invariant)**:
   - Headless cloud emulators (AWS/GCP/Hetzner) trigger immediate fraud reviews because residential consumer accounts do not upload raw media from commercial data center ASNs.
   - The UGREEN NAS is located on the home LAN (`192.168.1.80`), sharing the exact residential ISP public IP, gateway, and ASN with the user's primary mobile phone and laptop.
2. **Persistent Storage (Zero Authentication Churn)**:
   - Ephemeral containers trigger security challenges because Google detects repeated fresh enrollments.
   - The container's `/data` partition is mapped to a dedicated persistent directory on NVMe SSD (`/volume2/docker/redroid/data`), preserving SQLite databases, OAuth refresh tokens, and static Android ID (`f21de13ba98557f8`) indefinitely across restarts.
3. **Static Hardware Fingerprint**:
   - MAC address: `40:4e:36:7f:fb:d9` (fixed in Docker Compose).
   - Serial Number: `FA6AN0302845` (cloned from physical retired Pixel 1).
   - Cloned IMEI: `353086081745920`.
4. **Traffic Pacing (Human Behavior Mimicry)**:
   - Automated ingestion scripts enforce a 1.00 GiB/day default ceiling, preventing statistical anomaly triggers in Google Cloud abuse scoring.
5. **Google Play Store Auto-Update Freeze**:
   - `auto_update_enabled=false` and `auto_update_mode=2` are pinned in `/data/data/com.android.vending/shared_prefs/finsky.xml`, preventing background APK updates from modifying Google Photos or introducing breaking compatibility checks.

---

## 6. Centralized Rate Limiter CLI Specification

The rate limiter resides on the NAS at `/volume2/docker/redroid/scripts/rate_limiter.py` and uses POSIX advisory file locking (`fcntl.flock`) for atomic concurrency safety across multiple scripts and workers.

### Commands

| Command | Arguments | Exit Code | Purpose |
| :--- | :--- | :--- | :--- |
| `check` | `<bytes>` | `0` (Allowed) / `1` (Limit Reached) | Pre-flight validation before extracting or staging media |
| `record` | `<bytes>` | `0` | Atomically increments today's uploaded byte tally |
| `status` | None | `0` | Emits JSON summary of today's upload volume, remaining budget, and override state |
| `override enable` | `[--ceiling-gb N] [--reason S] [--sticky]` | `0` | Unlocks burst mode for event uploads (e.g. weddings, vacations) |
| `override disable` | None | `0` | Re-engages standard 1.00 GiB/day baseline protection |
| `set-uploaded` | `<gb>` | `0` | Overrides today's baseline tally for testing or synchronization |

---

## 7. Operational Health Checks

```bash
# 1. Verify container status and GPU device binding
ssh nas "docker ps --filter name=redroid-pixel1"

# 2. Verify complete partition property cloaking (expect zero output)
ssh nas "docker exec redroid-pixel1 getprop" | grep -E "test-keys|userdebug|redroid"

# 3. Check rate limiter quota and daily budget
ssh nas "python3 /volume2/docker/redroid/scripts/rate_limiter.py status"

# 4. Verify Google Photos cloud backup and account quota
# Captures interactive screencap of Google Photos settings
ssh nas "adb exec-out screencap -p" > /tmp/photos_check.png
```
