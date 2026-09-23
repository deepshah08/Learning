# 🚀 UGOS Pro Native Feature Catalog & DXP2800 Optimization Master Guide

> **Target Node**: UGREEN DXP2800 NAS (`192.168.1.80` | Intel N100, 8GB DDR5, 2.5GbE)  
> **Operating System**: UGOS Pro `1.19.1.0126` (Debian 12 Bookworm Kernel)  
> **Offline Knowledge Base Mirror**: 531 cached official articles in [`knowledge_cache/`](knowledge_cache/README.md)  
> **Status**: 🟢 **Active / Verified Ground Truth**  
> **Last Updated**: 2026-09-19  

---

## 📋 Executive Summary & Live Hardware Ground Truth

Live diagnostic telemetry gathered directly from `192.168.1.80` confirms the physical setup and storage configuration:

| Subsystem / Metric | Live Physical Hardware Reality | Technical Notes & Ground Truth |
| :--- | :--- | :--- |
| **Processor (CPU)** | **Intel N100** (4 Cores / 4 Threads, up to 3.4 GHz) | 6W TDP, 24EU Intel UHD Graphics with Intel QuickSync (`/dev/dri`) |
| **System Memory (RAM)** | **8 GB DDR5** (Single SODIMM slot) | Expandable up to 16GB/32GB DDR5 via bottom hatch; ~3.9 GB available |
| **Mechanical Storage (`/volume1`)** | **10TB Seagate IronWolf CMR (`ST10000VN000`)** | **IronWolf CMR (Not Pro)**: 9.1 TiB usable Btrfs (~7.5 TiB free, 18% used). AgileArray, RV sensors, Seagate IHM health diagnostics |
| **Solid-State Storage (`/volume2`)** | **4TB WD_BLACK SN850X NVMe PCIe 4.0 SSD** | **Dedicated Storage Pool 2**: 3.6 TiB usable Btrfs (~20 GB used, 1% used). 2,400 TBW endurance rating; zero HDD wakeups |
| **OS System Drive** | **32 GB eMMC (`mmcblk0`)** | Internal eMMC hosting Debian 12 Bookworm rootfs, boot, and overlay |
| **Network Interface** | **2.5 Gigabit Ethernet (2.5GbE)** | `eth0` running at full duplex, providing ~280 MB/s line speed |
| **Secondary Cold Archive** | **8TB Seagate Expansion SMR** | Attached to Pi 5 (`192.168.1.92`), mounted to NAS via SMB at `/mnt/smr-archive` |

### 🔍 Drive Model Clarification: Seagate IronWolf vs. IronWolf Pro
* **Detected Drive**: Model string `ST10000VN000-3AK101` in Bay 1.
* **Distinction**: This is the standard **Seagate IronWolf CMR** drive, not the **IronWolf Pro** (`ST10000NE000` / `ST10000NT000`).
* **Comparison**:
  - Both share identical 10TB capacity, Conventional Magnetic Recording (CMR), 256MB cache, built-in Rotational Vibration (RV) sensors, and native Seagate IronWolf Health Management (IHM) integration.
  - The standard IronWolf carries a 3-year warranty and a 180 TB/year workload rating (perfect for personal media/family storage), whereas the Pro carries a 5-year warranty and a 300 TB/year rating.

---

## 🏛️ Storage Tiering Architecture: Dedicated Volume 2 vs. SSD Cache

UGOS Pro supports using M.2 NVMe drives in two distinct operating modes:
1. **SSD Cache** (Read-only or Read-Write cache attached to Storage Pool 1).
2. **Dedicated Storage Pool / Volume 2** (Current Setup: `/volume2`).

```
┌───────────────────────────────────────┬────────────────────────────────┐
│                 UGREEN DXP2800 HARDWARE STORAGE TIERS                  │
├───────────────────────────────────────┼────────────────────────────────┤
│ HOT TIER: 4TB NVMe SSD (/volume2)     │ COLD TIER: 10TB HDD (/volume1) │
├───────────────────────────────────────┼────────────────────────────────┤
│ - Docker Container Runtimes           │ - Plex Media Library (Movies)  │
│ - SQLite Databases (Pi-hole, Arr)     │ - Family Photos & Raw Dumps    │
│ - AI Vector Indexes & Embeddings      │ - Automated Phone/PC Backups   │
│ - SAN Manager High-Speed iSCSI LUNs   │ - Document Archives & ISOs     │
│ - Zero Disk Churn on Mechanical Bay   │ - 0 RPM Deep Sleep Hibernation │
└───────────────────────────────────────┴────────────────────────────────┘
```

### Why Dedicated Volume 2 is Superior for Your Setup:
1. **Zero Mechanical Churn & Deep 0 RPM Sleep**: As documented in [Why Drives Stay Awake](knowledge_cache/articles/876_why_ugreen_nas_drives_stay_awake_and_what_causes_them_to_spi.md), enabling an SSD Read-Write cache requires continuous write-back flushes from NVMe to HDD, preventing the 10TB mechanical drive from ever spinning down. With Volume 2, hot 24/7 services run entirely on NVMe, allowing Bay 1 to sleep silently.
2. **TBW Endurance & Lifespan Protection**: Large sequential writes (e.g. 4K movie downloads or torrent streaming) would chew through SSD write endurance in cache mode without providing real-world performance gains ([SSD Cache Benefits Analysis](knowledge_cache/articles/807_why_is_there_no_significant_performance_improvement_after_ad.md)).
3. **Usable Capacity Expansion**: SSD Cache adds zero usable storage space. Volume 2 grants 3.6 TiB of blazing-fast random I/O storage.

---

## 💎 Hidden & High-Value UGOS Pro Features to Unlock

Beyond basic file sharing and Plex, UGOS Pro includes powerful enterprise-grade and consumer features that are often overlooked:

### 1. 🛡️ Btrfs Point-in-Time Snapshots & Instant Ransomware Rollback
* **What it is**: Instantaneous, zero-copy snapshots of any shared folder on your Btrfs volumes ([Snapshot User Guide](knowledge_cache/articles/654_snapshot_user_guide.md)).
* **Why it matters**: Protects against accidental deletion, file corruption, or ransomware encryption. Snapshots take milliseconds to generate and use almost zero additional storage initially.
* **Key Capabilities**:
  - Supports up to 1,024 historical snapshot points.
  - Automated scheduling: Hourly, daily, or weekly snapshots with custom retention policies.
  - Snapshot Replication: Replicate snapshots across storage pools (e.g. from `/volume1` to `/volume2` or external backup).
  - Invisible `@snapshot` folder in SMB shares for instant file self-restoration in macOS Finder and Windows Explorer.
* **How to enable**: Open **App Center** > Install **Snapshot** > Configure shared folder schedule.

### 2. ⚡ SAN Manager (iSCSI Block Storage) over 2.5GbE
* **What it is**: Virtualizes NAS storage into raw block-level virtual disks (LUNs) that mount on your Mac or PC as if they were internal physical NVMe/SATA drives ([SAN Manager Guide](knowledge_cache/articles/706_san_manager.md) & [macOS iSCSI Guide](knowledge_cache/articles/725_mounting_ugreen_nas_iscsi_virtual_disk_on_macos.md)).
* **Why it matters**: Unlike standard SMB network shares, applications that refuse to work on network drives (e.g. Final Cut Pro video projects, Steam game libraries, Logic Pro sound libraries, Lightroom catalogs) treat iSCSI LUNs as local internal disks.
* **Performance**: Over the DXP2800's 2.5GbE port, you achieve ~280 MB/s read/write speeds directly off your 4TB NVMe SSD tier.

### 3. 🔐 Cloud Drives with Zero-Knowledge Client-Side Encryption
* **What it is**: Native multi-cloud sync engine supporting Google Drive, OneDrive, Dropbox, Baidu, Aliyun, **Amazon S3 Buckets**, and **Backblaze B2 Object Storage** ([Cloud Drives Guide](knowledge_cache/articles/376_cloud_drives_guide.md), [Amazon S3](knowledge_cache/articles/861_how_to_mount_an_amazon_s3_bucket.md), [Backblaze B2](knowledge_cache/articles/883_how_to_mount_backblaze_b2_object_storage.md)).
* **Hidden Superpower — End-to-End Encryption**: UGOS Pro has built-in **Client-Side File Encryption** ([Cloud Drive File Encryption](knowledge_cache/articles/932_cloud_drive_file_encryption.md)). Files are encrypted with AES before being transmitted to the cloud provider. Even if Google, Microsoft, or AWS inspect the cloud bucket, file names and contents are completely unintelligible garble.

### 4. 🎬 Theater Cloud Direct Playback & Auto Intro/Outro Skip
* **What it is**: UGOS Pro's built-in Theater app has video analysis capabilities ([Theater User Guide](knowledge_cache/articles/929_theater_user_guide.md)).
* **Hidden Gems**:
  - **Auto Skip Intro & Outro**: Intelligently analyzes video waveforms across series episodes to detect repeated opening/closing credits and automatically skips them during playback ([Skip Intro/Outro Guide](knowledge_cache/articles/821_how_to_set_videos_to_automatically_skip_intro_and_outro.md)).
  - **Direct Cloud Streaming**: Mount a Google Drive or OneDrive account into Theater, and stream movies directly through TMDB poster wall without downloading the files to the NAS hard drive ([Cloud Direct Playback](knowledge_cache/articles/805_how_to_use_the_cloud_drive_direct_playback_in_theater.md)).
  - **Offline Caching**: Download full movies to your mobile device or tablet within the UGREEN app for offline viewing on flights without needing Plex Pass ([Offline Caching](knowledge_cache/articles/864_theater_offline_caching_and_data_free_playback.md)).
  - **Audio Passthrough & Dolby Atmos**: Bitstream TrueHD, DTS:X, and Dolby Atmos audio directly to AV receivers via HDMI or optical ([Audio Passthrough](knowledge_cache/articles/880_how_to_enable_audio_passthrough_and_dolby_atmos.md)).

### 5. 🚗 Music with Apple CarPlay Integration & Synced Lyrics
* **What it is**: Built-in lossless audio player supporting FLAC, ALAC, DSD, WAV, and MP3 ([Music Guide](knowledge_cache/articles/279_music.md)).
* **Hidden Gem**: Supports native **Apple CarPlay**! By enabling Background App Refresh on your iPhone, you can browse your NAS music library and stream lossless audio directly through your car dashboard display while driving ([CarPlay Music Guide](knowledge_cache/articles/914_how_to_play_ugreen_nas_music_through_carplay.md)).

### 6. 🧹 Hash-Based File Deduplication & Duplicate Photo Merge
* **What it is**: Low-level scanning engines that identify duplicate files across all shared folders ([File Deduplication](knowledge_cache/articles/158_quickly_clean_up_duplicate_files_with_file_deduplication.md) and [Similar Photo Cleanup](knowledge_cache/articles/834_how_to_clean_up_similar_and_duplicate_photos.md)).
* **Capabilities**:
  - **Exact Match (SHA Hash)**: Compares cryptographic file fingerprints rather than just names or sizes to detect exact duplicates.
  - **Smart Merge in Photos**: Automatically identifies the "Kept" master file, merges album tags and favorites, and safely purges redundant duplicates.

### 7. 💻 Virtual Machine Manager (KVM/QEMU) with Hardware Passthrough
* **What it is**: Built-in hypervisor to run Windows, Linux (Ubuntu, Debian), or Home Assistant OS virtual machines directly on the NAS ([VM User Guide](knowledge_cache/articles/909_virtual_machine_user_guide.md)).
* **Hidden Capabilities**:
  - **Hardware Passthrough**: Pass physical USB ports, storage controllers, or GPU devices directly to the VM ([Hardware Passthrough](knowledge_cache/articles/911_ugreen_nas_hardware_passthrough.md)).
  - **Web VNC Share Links**: Generate password-protected web browser links to access a VM's desktop remotely without installing VNC clients ([VM Share Links](knowledge_cache/articles/332_virtual_machine_share_link_feature.md)).
  - **VM Snapshots**: Snapshot entire VM memory and disk states for testing updates ([VM Snapshots](knowledge_cache/articles/331_virtual_machine_snapshot_feature.md)).

### 8. 📹 Surveillance Center (NVR)
* **What it is**: Turns the DXP2800 into a private Network Video Recorder for security cameras ([Surveillance Center](knowledge_cache/articles/866_surveillance_center_user_guide.md)).
* **Capabilities**: Supports ONVIF and RTSP IP camera protocols, multi-channel continuous/event recording, scheduled motion detection alerts, and timeline playback.

### 9. 📚 Comics & Manga Reader
* **What it is**: Native comic and graphic novel reader supporting `.cbz`, `.cbr`, `.pdf`, and `.zip` archives ([Comics User Guide](knowledge_cache/articles/768_comics_user_guide.md)).
* **Features**: Automatically recognizes series and chapters ([Chapter Recognition](knowledge_cache/articles/937_how_does_the_comics_app_identify_comic_files_and_chapters.md)), optimizes page-turning rendering, and tracks reading progress across mobile and desktop.

### 10. 📝 Personal Cloud Notes & OnlyOffice Collaboration
* **Notes**: Native markdown-compatible rich text note-taking app with inline image attachments, tag-based organization, and private user encryption ([Notes User Guide](knowledge_cache/articles/894_how_to_use_the_notes_app.md)).
* **Online Office**: Full OnlyOffice Document Server integration allowing multi-user real-time collaborative editing of `.docx`, `.xlsx`, and `.pptx` directly inside the web browser without Microsoft Office licenses ([Online Office](knowledge_cache/articles/337_online_office.md)).

---

## 🤖 Deep Dive: Model Manager (`com.ugreen.aiconsole`) & Photos Intelligence

You noted that you enabled the **Model Manager**. Inspecting the live configuration on the NAS (`/volume1/@appstore/com.ugreen.aiconsole/config/console_config.json`) reveals an advanced local AI stack running on **OpenVINO 2024/2025** and **ONNX Runtime** hardware-accelerated by the Intel N100:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   UGREEN AI CONSOLE & MODEL MANAGER                    │
├────────────────────────────────────────────────────────────────────────┤
│  LOCAL HARDWARE MODELS (OpenVINO + ONNX Runtime on Intel N100)         │
│  ├─ Face & People Clustering     (UGREEN_FACE / save_head)             │
│  ├─ Pet Classification           (UGREEN_PET)                          │
│  ├─ Scene Recognition            (UGREEN_SCENE)                        │
│  ├─ Multimodal Semantic Search   (UGREEN_ITM: Image-to-Text CLIP)      │
│  ├─ Natural Language Labeling    (UGREEN_ITM_NLP & ITM_LABEL)          │
│  ├─ Document & ID Card OCR       (UGREEN_OCR & UGREEN_CREDENTIAL)      │
│  ├─ Blur & Quality Scoring       (UGREEN_BLUR)                         │
│  ├─ Similar & Burst Clustering   (UGREEN_SIMILAR)                      │
│  └─ Continual User Fine-Tuning   (UGREEN_OLL / off_line_learning)      │
├────────────────────────────────────────────────────────────────────────┤
│  CLOUD LLM GATEWAY (Custom API Keys Supported)                         │
│  ├─ OpenAI     (gpt-4o, gpt-5.x, etc.)                                 │
│  ├─ DeepSeek   (deepseek-v4-pro, deepseek-v4-flash, R1)                │
│  ├─ Qwen / Alibaba DashScope                                           │
│  └─ Kimi / Moonshot & MiniMax                                          │
├────────────────────────────────────────────────────────────────────────┤
│  SYSTEM CONTROL AI AGENT & MCP SERVER (`ai_mcp_serv`)                  │
│  ├─ Power Settings & Fan Speed Control                                 │
│  ├─ Photo Album & Video Playback Control                               │
│  └─ Container & Image Inspection                                       │
└────────────────────────────────────────────────────────────────────────┘
```

### 🔍 Live Model Inventory on Your DXP2800 (`aiconsole.db`)

Direct SQLite inspection of `model_config` on `/volume1/@appstore/com.ugreen.aiconsole/db/aiconsole.db` reveals your exact active AI models:

| Model Code | Purpose / Feature | Installed Version | Size | Live Status |
| :--- | :--- | :--- | :--- | :--- |
| `image_recognition` | Scene & Multimodal Search (CLIP) | `v2.1.4` | **1.06 GB** | 🟢 **Active / Downloaded** |
| `face_recognition` | Facial Detection & People Clustering | `v2.1.3` | **214 MB** | 🟢 **Active / Downloaded** |
| `model_training` | Custom Category User Training | `v2.1.0` | **78 MB** | 🟢 **Active / Downloaded** |
| `ocr_text` | Text & Document OCR in Photos | `v2.1.2` | **68 MB** | 🟢 **Active / Downloaded** |
| `nsfw` | Sensitive Content Filter | `v2.1.0` | **64 MB** | 🟢 **Active / Downloaded** |
| `imgfeature_extract` | Similar & Duplicate Photo Matching | `v2.1.0` | **36 MB** | 🟢 **Active / Downloaded** |
| `pets_detect` | Pet Detection (Cats & Dogs) | `v2.1.0` | **97 MB** | ⚪ **Available (Not Downloaded Yet)** |
| `monitor_face_rec` | Surveillance Face Recognition | `v1.0.3` | **69 MB** | ⚪ **Available (Not Downloaded Yet)** |
| `monitor_obj_detect`| Surveillance Object Detection | `v1.0.3` | **9.3 MB** | ⚪ **Available (Not Downloaded Yet)** |

> [!IMPORTANT]
> **Live Schedule Finding**: In `system_setting`, `smart_learning` is currently set to `{"switch": false}`.  
> This means AI indexing processes photos continuously as they arrive. Setting an off-peak window (`01:00 AM – 06:00 AM`) in Model Manager settings will eliminate any daytime CPU competition with Plex.

### 🔌 Built-in Model Context Protocol (MCP) Server

UGOS Pro runs an official **Model Context Protocol (MCP) Server** daemon (`ai_mcp_serv`) on port `11540`:
* **Endpoint**: `http://127.0.0.1:11540/mcp`
* **Protocol Version**: `2024-11-05`
* **Server Identity**: `Model Manager NAS MCP Server v1.0.0`
* **Exposed System Tools (18 Discovered Tools)**:
  - `search_photos`: Natural language semantic search using CLIP embeddings & OCR keywords.
  - `get_album_list` & `create_album`: Programmatic photo album querying and auto-generation.
  - `get_system_info`: Detailed system metrics across categories (`system`, `device`, `cpu`, `ram`, `storage`, `network`, `uglink`, `fan_speed`).
  - `configure_memory_compression`: Real-time control of Linux ZRAM / ZSWAP memory compression.
  - `control_cooling_fan_speed` & `adjust_led_brightness`: Hardware cooling fan and LED brightness controls.
  - `configure_nas_power_settings` & `set_power_efficiency_mode`: Power profile and hibernation management.
  - `docker_search_container` & `docker_search_image`: Local and remote container inspection.
  - `music_search_control`, `music_play_control`, `music_settings_control`: Lossless music playback engine.
  - `video_search_control` & `video_play_control`: Theater streaming and media control.
* **Authentication Architecture**:
  - The MCP server authenticates requests via `X-Ugreen-Token` session tokens generated by UGOS Pro.

### Making the Most of the Local AI Features:

1. **Enable Pet Recognition**:
   - In **Model Manager**, locate `Pet recognition` (`pets_detect`) and click download (97 MB). This enables automatic pet clustering for dogs and cats in the Photos app.
2. **Enable Multimodal Natural Language Search (Image-Text Matching)**:
   - In Photos > Settings > AI Settings, ensure **Search by keyword / Semantic Search** is toggled on.
   - This activates `UGREEN_ITM` and `UGREEN_ITM_NLP` powered by your 1.06GB `image_recognition` model. You can search for concepts rather than tags: e.g., typing *"dog playing in snow"*, *"birthday candle"*, or *"red convertible car"* will find matching photos even if you never tagged them.
3. **Train Custom Categories with Your Own Sample Photos**:
   - As detailed in [Custom Category Model Training](knowledge_cache/articles/874_how_to_create_a_custom_category_with_model_training.md), your active `model_training` package allows custom AI classifiers.
   - Upload 5–10 sample photos of a specific object or theme (e.g. your specific car model, a specific hobby craft, or personal items), and the NAS will train a custom classifier to automatically group all matching photos across your library!
4. **Automate Document & Receipt Organization with OCR**:
   - Your active `ocr_text` model automatically identifies receipts, utility bills, business cards, passports, and ID cards, grouping them into a dedicated document album.
5. **Schedule AI Recognition to Run During Off-Peak Hours**:
   - In the Model Manager / Photos AI settings, toggle on **Smart Learning Schedule** (e.g., `01:00 AM – 06:00 AM`). This prevents photo indexing from consuming CPU during the day.
6. **Clean Up Burst Shots & Redundant Photos**:
   - Navigate to Photos > **Similar & Duplicate**. Run a scan to merge true duplicates with 1 click using `imgfeature_extract`.

---

## 🛡️ Production Docker Infrastructure, Zero-Lock Backups & Log Hygiene

The hot application tier on `/volume2` (NVMe) runs 14 mission-critical containerized services. To ensure maximum stability, zero data corruption, and disk endurance, the following optimizations are deployed:

### 1. 🔄 Automated Daily Zero-Lock SQLite Snapshots & SMR Archival
* **Core Script**: `/volume2/docker/backups/create_daily_docker_snapshot.sh`
* **Python Helper**: `/volume2/docker/backups/snapshot_sqlite_helper.py`
* **Zero-Lock Atomic Architecture**: Uses Python 3's native `sqlite3.backup()` API to open all databases in read-only mode (`mode=ro`). The backup engine performs atomic, consistent point-in-time snapshots page-by-page without taking exclusive table locks or interrupting live containers:
  - `vaultwarden` (`/volume2/docker/vaultwarden/data/db.sqlite3`)
  - `pihole_ftl` (`/volume2/docker/pihole/etc-pihole/pihole-FTL.db`)
  - `pihole_gravity` (`/volume2/docker/pihole/etc-pihole/gravity.db`)
  - `sonarr` (`/volume2/docker/arr_stack/sonarr/sonarr.db`)
  - `radarr` (`/volume2/docker/arr_stack/radarr/radarr.db`)
  - `prowlarr` (`/volume2/docker/arr_stack/prowlarr/prowlarr.db`)
  - `bazarr` (`/volume2/docker/arr_stack/bazarr/db/bazarr.db`)
  - `tautulli` (`/volume2/docker/arr_stack/tautulli/tautulli.db`)
  - `seerr` (`/volume2/docker/arr_stack/overseerr/db/db.sqlite3`)
  - `calibre_web_app` (`/volume2/docker/book_stack/calibre-web-automated/config/app.db`)
  - `calibre_web_cwa` (`/volume2/docker/book_stack/calibre-web-automated/config/cwa.db`)
  - `shelfmark_users` (`/volume2/docker/book_stack/shelfmark/config/users.db`)
* **Configuration Packaging**: Packages all Docker Compose files, XML configs, DNS redundancy files, and application settings into a lean ~65MB gzip archive (`docker_state_backup_YYYYMMDD_HHMMSS.tar.gz`), replacing the old uncompressed 701MB bloat.
* **7-Day Rolling Retention**: Automatically purges snapshots and logs older than 7 days from the NVMe tier to preserve disk capacity.
* **Resilient SMR Mirroring (`sync_to_smr_archive.sh`)**:
  - Automatically probes Pi 5 on `192.168.1.92:445` (and fallback `192.168.1.116:445`).
  - Employs user-space `smbclient` sequential streaming directly to `//192.168.1.92/smr-archive/Archival_Backups/Docker_Snapshots`.
  - Zero requirement for root/sudo CIFS kernel mounts on the NAS host.
  - Skips already-synced snapshots and writes sequentially to prevent SMR drive write-cliffs.
* **Persistent Systemd User Automation**:
  - Service: `~/.config/systemd/user/docker-backup.service`
  - Timer: `~/.config/systemd/user/docker-backup.timer`
  - Schedule: Daily at `03:30 AM` with 300s randomized jitter.
  - Persistence: Enforced via `loginctl enable-linger 'Deep Shah'`, ensuring 24/7 background execution across reboots and logouts.

### 2. 📝 Strict Container Log Rotation Policy
To prevent container log bloat from exhausting NVMe storage over time, strict `json-file` log caps are enforced across all compose stacks:
```yaml
logging:
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "3"
```
* **Enforced Across**: `arr_stack/docker-compose.yml`, `book_stack/docker-compose.yml`, `homepage/docker-compose.yml`, `vaultwarden/docker-compose.yml`, `pihole/docker-compose.yml`.
* **Guaranteed Maximum Log Footprint**: Capped at exactly 30MB per container (3 rotated files × 10MB).

### 3. 🧹 Storage Optimization & Docker Hygiene
* **Builder Cache Pruned**: Purged 288MB of stale Docker build cache.
* **Unused Images Pruned**: Removed 7 unneeded images (`redroid:12.0.0-latest`, `python:3.10-slim`, `debian:12-slim`, `alpine/git`, `strm/dnsmasq`, `hello-world`, `linuxserver/plex:latest`), reclaiming ~2.9GB of NVMe storage.
* **Current Storage Footprint**:
  - Total Docker Images: 8.9 GB (Reclaimable: **0B / 0%**).
  - Total Container Layers: 222 MB (Reclaimable: **71B / 0%**).
  - Build Cache: **0B**.

### 4. ⚡ BitTorrent Protocol & NAT Protection Compliance
* **Host Path**: `/volume2/docker/arr_stack/qbittorrent/qBittorrent/qBittorrent.conf`
* **Injected Directives**:
  - `Session\BTProtocol=1`: Forces TCP-only transport (eliminates connectionless uTP UDP NAT state explosions in router conntrack tables).
  - `Session\GlobalMaxRatio=1.0`: Enforces strict 1:1 seed ratio.
  - `Session\GlobalMaxRatioAction=0`: Automatically pauses torrents upon reaching 1:1 ratio to prevent mechanical HDD random read churn.

---

## ⚡ Live Telemetry, Thermals & Health Verification

Live host probes gathered over OpenSSH ControlMaster confirm 100% production health:

```
┌────────────────────────────────────────────────────────────────────────┐
│               DXP2800 PRODUCTION HEALTH & TELEMETRY                    │
├────────────────────────────────────────────────────────────────────────┤
│ • System Uptime     : 2 days, 11 hours (Load Average: 0.30, 0.23, 0.19)│
│ • System Memory     : 7.5 GiB total | 3.5 GiB used | 4.1 GiB available │
│ • Package Thermal   : 59 °C (x86_pkg_temp) | ACPI Board: 27 °C         │
│ • NVMe SSD Health   : 40 °C | 0% Wear | 0 Errors | 404.5 GB Written    │
│ • Mechanical Drive  : Active/Idle | 0 RPM Hibernation Capable          │
│ • DNS Query Latency : 0 msec (192.168.1.80#53) | 0 msec (.92#53)       │
│ • Production Ports  : 13/13 Endpoints HTTP 200 Sub-50ms Response       │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🧭 Complete Application Guide & Knowledge Base Directory

The full 531-article official documentation has been organized into clear categories under [`knowledge_cache/`](knowledge_cache/README.md). Below is an index to high-value sections:

| Category | Articles Count | Key Guides & Reference Links |
| :--- | :--- | :--- |
| **Storage & RAID** | 30+ articles | [SSD Cache Types](knowledge_cache/articles/430_ssd_cache_types_supported_by_ugreen_nas.md) • [Btrfs Snapshots](knowledge_cache/articles/654_snapshot_user_guide.md) • [Drive Sleep Causes](knowledge_cache/articles/876_why_ugreen_nas_drives_stay_awake_and_what_causes_them_to_spi.md) • [RAID Levels](knowledge_cache/articles/132_how_to_choose_the_right_raid_level_for_your_needs.md) |
| **Photos & AI** | 20+ articles | [Model Management](knowledge_cache/articles/831_model_management_dxp_series.md) • [Custom Category Training](knowledge_cache/articles/874_how_to_create_a_custom_category_with_model_training.md) • [Duplicate Cleanup](knowledge_cache/articles/834_how_to_clean_up_similar_and_duplicate_photos.md) • [Shared Albums](knowledge_cache/articles/904_how_to_share_libraries_and_albums_with_family_members.md) |
| **Media & Theater** | 50+ articles | [Theater Overview](knowledge_cache/articles/929_theater_user_guide.md) • [Skip Intro/Outro](knowledge_cache/articles/821_how_to_set_videos_to_automatically_skip_intro_and_outro.md) • [Dolby Atmos](knowledge_cache/articles/880_how_to_enable_audio_passthrough_and_dolby_atmos.md) • [CarPlay Music](knowledge_cache/articles/914_how_to_play_ugreen_nas_music_through_carplay.md) • [Comics Guide](knowledge_cache/articles/768_comics_user_guide.md) |
| **Cloud & Sync** | 25+ articles | [Cloud Encryption](knowledge_cache/articles/932_cloud_drive_file_encryption.md) • [Amazon S3 Mount](knowledge_cache/articles/861_how_to_mount_an_amazon_s3_bucket.md) • [Backblaze B2](knowledge_cache/articles/883_how_to_mount_backblaze_b2_object_storage.md) • [Time Machine](knowledge_cache/articles/350_backup_mac_files_to_ugreen_nas_using_time_machine.md) |
| **SAN & Virtualization** | 35+ articles | [SAN Manager (iSCSI)](knowledge_cache/articles/706_san_manager.md) • [macOS iSCSI](knowledge_cache/articles/725_mounting_ugreen_nas_iscsi_virtual_disk_on_macos.md) • [VM Guide](knowledge_cache/articles/909_virtual_machine_user_guide.md) • [VM Passthrough](knowledge_cache/articles/911_ugreen_nas_hardware_passthrough.md) |
| **Control & Hardware**| 110+ articles| [Link Aggregation](knowledge_cache/articles/324_how_to_set_up_link_aggregation_on_ugreen_nas_to_improve_tran.md) • [UPS / NUT Server](knowledge_cache/articles/708_how_to_enable_ups_and_configure_the_nut_server_feature_on_a_.md) • [Firewall & Whitelist](knowledge_cache/articles/353_how_to_configure_firewall_rules_to_improve_system_security.md) |

---

## 🛠️ Step-by-Step Optimization Checklist for Your DXP2800

### Automated & Implemented System Optimizations (Done)
- [x] **Zero-Lock Atomic SQLite Database Backups**: Implemented `/volume2/docker/backups/create_daily_docker_snapshot.sh` backing up all 12 SQLite databases in 1s without table locks.
- [x] **Automated SMR Archival Pipeline**: Synced to Pi 5 8TB SMR archive via user-space `smbclient` with sequential write throttling.
- [x] **Systemd User 24/7 Timer**: Scheduled daily at `03:30 AM` via `docker-backup.timer` with persistent user lingering.
- [x] **Docker Container Log Rotation**: Configured `max-size: 10m`, `max-file: 3` across all 5 compose stacks (capped at 30MB/container).
- [x] **BitTorrent TCP & Ratio Compliance**: Enforced `Session\BTProtocol=1`, `GlobalMaxRatio=1.0`, and auto-pause `GlobalMaxRatioAction=0`.
- [x] **Storage Reclamation**: Pruned 2.9GB of stale Docker images and builder cache, achieving 0B reclaimable.
- [x] **Offline Knowledge Base Sync**: Scraped and indexed all 531 UGREEN Knowledge Center articles under `knowledge_cache/`.

### Recommended Quick Web UI Toggles (10-Second Actions)
1. [ ] **Configure Hard Drive Specified Storage Pool Sleep**:
   - In UGOS Pro **Control Panel** > **Hardware & Power** > **Power Management** > **Hard Drive Hibernation**.
   - Select **Specified Storage Pool Sleep**: Configure **Storage Pool 1** (`/volume1` HDD) to enter sleep after **15 or 30 minutes** of inactivity, while keeping **Storage Pool 2** (`/volume2` NVMe) active 24/7.
2. [ ] **Download Pet Detection Model in Model Manager**:
   - In UGOS Pro Web UI (`http://192.168.1.80`) > **Model Manager**, find **Pet recognition** (`pets_detect`) and click **Download** (97 MB). This enables automatic pet clustering for dogs and cats in Photos.
3. [ ] **Configure Smart Learning Off-Peak Window**:
   - In **Model Manager** > **Settings** > **Smart Learning**, toggle **ON** and set the time window to **01:00 AM – 06:00 AM**. This prevents facial clustering and CLIP indexing from competing with daytime Plex transcoding.
4. [ ] **Set Up Automated Btrfs Snapshots on `/volume1`**:
   - Open App Center > Install **Snapshot**.
   - Create a daily snapshot schedule for your personal and family media shares with 14-day retention.
5. [ ] **Enable Skip Intro/Outro in Theater**:
   - In Theater > **Settings** > **Background Management**, enable episode waveform analysis to auto-skip intro/outro credits during playback.
6. [ ] **Test Native Apple CarPlay with UGREEN Music**:
   - Add a high-res FLAC album to your NAS Music folder, enable Background App Refresh on iPhone, and connect to CarPlay.

