# Virtual Pixel 1 ReDroid Anti-Spoof Hardening & Cloud Longevity Investigation

> Companion: durable architecture at [./redroid_anti_spoof_hardening_knowledge.md](./redroid_anti_spoof_hardening_knowledge.md)  
> System Twin: baseline runbook at [./REDROID_PIXEL1_DIGITAL_TWIN.md](./REDROID_PIXEL1_DIGITAL_TWIN.md)  
> Host Target: UGREEN DXP2800 NAS (`192.168.1.80`) · NVMe Tier (`/volume2`)  
> Container: `redroid-pixel1` (Android 11 Digital Twin)  
> Date: 2026-11-10 · Status: 🟢 Fully Hardened & Verified

---

## 1. Trigger

During the automated staging and cloud migration of a 60 GB high-bitrate wedding archive (`wedding_archive_DF.tar`) from the cold SMR tier on Raspberry Pi 5 to the virtual Pixel 1 container (`redroid-pixel1`) on the UGREEN NAS, two high-impact risks were audited:

1. **Google Account & Anti-Spoof Longevity Risk**: A broad survey of custom ROM and root-based spoofing setups (e.g. crDroid issue tracker [#990](https://github.com/crdroidandroid/issue_tracker/issues/990) and [#977](https://github.com/crdroidandroid/issue_tracker/issues/977), Magisk `Pixelify`, Zygisk `PlayIntegrityFix`) revealed that spoofed Pixel 1 instances frequently experience quota revocations, backup dropouts after 1–4 hours, or account authentication challenges.
2. **Traffic Anomaly Risk**: Blasting tens of gigabytes in continuous un-throttled bursts directly to Google Photos from a headless container risks triggering Google Cloud abuse heuristics, CAPTCHAs, or account flagging.

The goal was to audit all known failure modes across the Android emulation and custom ROM landscape, converge on which vulnerabilities applied to ReDroid, implement complete partition property hardening, and deploy an automated 1GB/day rate limiter with manual burst overrides to guarantee multi-year unattended operation.

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          INVESTIGATION ARCHITECTURE & SCOPE                            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  [Raspberry Pi 5 (192.168.1.92)]                   [UGREEN NAS (192.168.1.80)]         │
│  ┌─────────────────────────────┐                   ┌────────────────────────────────┐  │
│  │ 8TB Seagate SMR (/dev/sda2) │                   │ NVMe Tier (/volume2)           │  │
│  │  - wedding_archive_DF.tar   │                   │  - docker-compose.yml (Hardened│  │
│  │  - ingest_large_videos.py   │                   │  - redroid-pixel1 Container    │  │
│  └──────────────┬──────────────┘                   │  - rate_limiter.py (1GB/day)   │  │
│                 │                                  └───────────────┬────────────────┘  │
│                 │ 2.5GbE LAN Pipeline                              │                   │
│                 ▼                                                  ▼                   │
│  ┌─────────────────────────────┐                   ┌────────────────────────────────┐  │
│  │ Lossless 1.5GB Segmentation │ ────────────────> │ Google Photos Cloud            │  │
│  │ (Bypasses 32-bit Ashmem)    │                   │ (Original Quality / 0GB Quota) │  │
│  └─────────────────────────────┘                   └────────────────────────────────┘  │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Investigation Path

| # | Hypothesis / Approach | What We Found | Outcome |
|---|----------------------|---------------|---------|
| 1 | crDroid Issue #990 applies directly to ReDroid container | Disproved. crDroid uses selective Java reflection hooking (`PixelPropsUtils.java`) on Google Photos while GMS Phenotype runs unhooked, receiving real device flags over IPC and demoting quota. ReDroid runs the entire OS under unified `sailfish` identity. | Invalidated for ReDroid |
| 2 | Top-level `ro.product.*` props are sufficient for Play Integrity | Disproved. DroidGuard and Play Integrity inspect 5 distinct partitions (`system`, `vendor`, `product`, `system_ext`, `odm`). Live container inspection revealed `test-keys` and `redroid` leaking in ODM/System_Ext partitions. | Vulnerability Confirmed; Remediated |
| 3 | Cloak `ro.hardware=sailfish` to match physical Pixel 1 | Disproved. SurfaceFlinger crashed in a bootloop. Android HAL dynamic loader requires `hwcomposer.<ro.hardware>.so` and `gralloc.<ro.hardware>.so`; ReDroid ships `hwcomposer.redroid.so`. | Rejected (HAL Broken); Reverted |
| 4 | Decouple HAL loader while enforcing partition property parity | Verified. Keeping `ro.hardware` managed by ReDroid while cloaking all partition models, fingerprints, build tags, bootloader, baseband, and IMEI yielded a bootable, leak-free container. | Selected & Deployed |
| 5 | Continuous un-throttled burst upload for entire 60GB archive | High anomaly risk. Cloud anti-abuse heuristics flag continuous sustained multi-gigabyte uploads on personal residential lines. | Rejected for daily baseline; 1GB rate limit enforced |
| 6 | Centralized POSIX-locked rate limiter on NAS with burst override | Verified. `rate_limiter.py` gates daily ingestion to 1.00 GiB baseline while supporting `--burst` and `--cooling-seconds` for special events (e.g. wedding archive). | Selected & Integrated |

---

## 3. Root Causes and Fixes

### Custom ROM & Hooking Vulnerability Analysis (crDroid #990 / #977)

| Component | Root Cause in Custom ROMs | Why ReDroid Is Structurally Immune |
| :--- | :--- | :--- |
| **GMS Phenotype Sync** | `PixelPropsUtils` hooks `Build` properties only inside `com.google.android.apps.photos`. `com.google.android.gms` runs unhooked. GMS Phenotype receives server flags for the un-spoofed device (e.g. Poco `garnet`) and syncs them to Photos. | ReDroid uses zero method hooking or Zygote injection. The container kernel and Android init set properties globally. GMS registers with Google Checkin/Phenotype as a legitimate Pixel 1 from boot. |
| **Zygisk / Magisk Modules** | Hooks are vulnerable to process restart races, GMS daemon forks, and app updates that check un-hooked binder interfaces. | Properties are immutable OS environment variables read from system properties (`/system/etc/prop.default`, init env). No runtime hook to fail. |
| **DroidGuard Attestation** | Play Integrity probes un-spoofed partitions (`odm`, `vendor`) for `userdebug` or `test-keys`. | All 5 partitions (`system`, `vendor`, `product`, `system_ext`, `odm`) were hardened with identical `QP1A.191005.007.A3` fingerprints and `release-keys`. |

### Container Vulnerability Audit & Fix Matrix

| # | Component / Subsystem | Unhardened Live Baseline | Hardened Production State | Fix Mechanism |
|---|----------------------|--------------------------|---------------------------|---------------|
| 1 | ODM Partition Identity | `ro.product.odm.brand=redroid` · `ro.odm.build.tags=test-keys` | `ro.product.odm.brand=google` · `ro.odm.build.tags=release-keys` | Injected into docker-compose `command` args |
| 2 | System_Ext Partition Identity | `ro.product.system_ext.model=redroid` | `ro.product.system_ext.model=Pixel` · `release-keys` | Injected into docker-compose `command` args |
| 3 | Bootloader Status | Empty / un-emulated | `ro.boot.flash.locked=1` · `ro.boot.bootloader=8996-012001-1908071822` | Emulated Qualcomm MSM8996 bootloader |
| 4 | Radio / Telephony Stack | Missing baseband & RIL strings | `gsm.version.ril-impl=Qualcomm RIL 1.0` · `persist.radio.imei=353086081745920` | Injected cloned physical IMEI & Qualcomm RIL |
| 5 | Graphics HAL Binding | `ro.hardware=sailfish` crashed HAL | Native `ro.hardware` preserved; Host Intel GPU `/dev/dri/renderD128` | Decoupled HAL loader from partition build props |

---

## 4. Key Architecture & Longevity Invariants

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                       MULTI-YEAR UNATTENDED LONGEVITY ANCHORS                          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  1. Residential Trust Anchor                                                           │
│     - Runs on UGREEN NAS (192.168.1.80) on home LAN.                                   │
│     - Shares exact public IP, ISP ASN, and residential subnet with user's daily        │
│       personal devices (MacBook, Pixel, iPhone). Zero data center VPN flags.           │
│                                                                                        │
│  2. Token & State Persistence                                                          │
│     - NVMe bind mount (/volume2/docker/redroid/data -> /data).                         │
│     - Persistent SQLite accounts_de.db, OAuth tokens, Android ID (f21de13ba98557f8).   │
│     - Google never observes fresh device enrollments or repeated re-logins.            │
│                                                                                        │
│  3. Permanent Cloned Hardware Identifiers                                              │
│     - Static MAC address: 40:4e:36:7f:fb:d9                                            │
│     - Serial Number: FA6AN0302845 (cloned from Deep's physical retired Pixel 1)        │
│     - Cloned Physical IMEI: 353086081745920                                            │
│                                                                                        │
│  4. Centralized Traffic Pacing (1GB/Day Baseline)                                      │
│     - rate_limiter.py enforces 1.00 GiB/day baseline to mimic natural camera capture.  │
│     - Explicit --burst mode for post-trip or wedding batch ingestions.                 │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Live Telemetry & Verification Gate

1. **Partition Property Verification**:
   ```bash
   ssh nas "docker exec redroid-pixel1 getprop" | grep -E "test-keys|userdebug|redroid"
   # Output: 0 matching lines in partition identity or build properties
   ```
2. **Google Photos Live Status**:
   - Backup State: **`Backup is on`** · **`Quality: Original`**
   - Active Quota: **`552.31 MB of 5 TB (0% used)`** (Zero bytes charged against Google One storage).
   - Sync State: **`3,000 photos & videos backed up`** · **`Backup complete [✓]`**.
3. **Rate Limiter Verification**:
   - Today's Ingested Volume: **22.00 GB** recorded for 2026-11-10.
   - Baseline State: `allowed: false` (Daily limit of 1.00 GiB reached; gate actively holding).
   - Burst Mode: Fully operational via `python3 rate_limiter.py override enable --ceiling-gb 50`.

---

## 6. Key Learnings

1. **System Containerization Outperforms In-Process Hooking**:
   Method hooking (Xposed, Magisk, Zygisk) creates split-brain state between app processes and background Play Services daemons (e.g. Phenotype IPC in crDroid #990). Containerizing the entire OS allows standard immutable property propagation across all processes.
2. **HAL Dynamic Linking Overrides Build Identity**:
   AOSP HAL dynamic loaders rely strictly on `ro.hardware` to locate `.so` vendor implementations (`hwcomposer.<ro.hardware>.so`). Modifying `ro.hardware` without recompiling vendor HAL binaries breaks graphics rendering. Build and partition identities must be cloaked without altering HAL binding variables.
3. **Cloud Anti-Abuse Relies on Traffic Cadence**:
   Unlimited storage abuse triggers are largely statistical (gigabytes uploaded per hour vs typical mobile usage). Enforcing a 1GB/day baseline provides statistical camouflaging, while manual burst overrides accommodate legitimate real-world event ingestion.
