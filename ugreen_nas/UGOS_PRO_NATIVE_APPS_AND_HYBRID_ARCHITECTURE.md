# 🧭 UGOS Pro Native Applications & Hybrid Architecture Reference

> **Domain**: UGOS Pro Built-in Apps, Host Resource Profiles & Docker Co-existence  
> **Host Node**: UGREEN DXP2800 NAS (`192.168.1.80` | Intel N100, 8GB DDR5, 2.5GbE)  
> **Operating System**: UGOS Pro (Debian 12 Kernel)  
> **Status**: 🟢 **Active / Production Hybrid Model**  
> **Last Verified**: 2026-08-29  

---

## 📋 Table of Contents

1. [Architecture Overview & Hybrid Strategy](#-1-architecture-overview--hybrid-strategy)
2. [UGOS Pro Native Application Catalog](#-2-ugos-pro-native-application-catalog)
3. [Deep Comparison Matrices](#-3-deep-comparison-matrices)
   - [3.1 UG Theater & Downloads vs. Plex & The *Arr Stack](#31-ug-theater--downloads-vs-plex--the-arr-stack)
   - [3.2 UG Vault (File Safe) vs. Vaultwarden (Password Manager)](#32-ug-vault-file-safe-vs-vaultwarden-password-manager)
   - [3.3 UG Photos & AI Console vs. Immich](#33-ug-photos--ai-console-vs-immich)
   - [3.4 UG Office (OnlyOffice) & Sync & Backup](#34-ug-office-onlyoffice--sync--backup)
4. [Host Resource Profile & Background Footprint](#-4-host-resource-profile--background-footprint)
5. [Operational Management & Runbook](#-5-operational-management--runbook)
6. [Cross-References](#-6-cross-references)

---

## 🏗️ 1. Architecture Overview & Hybrid Strategy

The UGREEN DXP2800 NAS runs a **hybrid architecture** combining native UGOS Pro system applications with high-performance, containerized Docker microservices.

| Native UGOS Pro Services | Hardened Container Stack (Docker Engine) |
| :--- | :--- |
| • Storage Manager (SMART, IHM, Btrfs) | • Plex Media Server (QuickSync 4K HW) |
| • UG Photos (Pixel 9 Pro XL & Pranali) | • *Arr Automation (Sonarr/Radarr/Prowl) |
| • AI Console (Facial & Scene Vectors) | • qBittorrent (TCP-Only, Ratio 1.0) |
| • UG Sync & Backup (Mobile ingestion) | • Bazarr (EN + HI Subtitle automation) |
| • UG Office (In-browser Doc Viewer) | • Overseerr (Netflix-style Requests) |
| • UG Vault (Encrypted File Safe) | • Vaultwarden (Passkeys / TOTP / Auth) |
| • UG Theater (Native Video Playback) | • Pi-hole v6 (Local Ad-blocking DNS) |
| • NetDisk (Cloud Drive Sync) | • Tautulli (Stream Analytics & Logs) |

### Strategic Co-existence Rationale:
1. **Hardware & Firmware Integration**: Native UGOS Pro apps handle direct hardware telemetry (Storage Manager, SMART diagnostics, Seagate IronWolf Health Management, Btrfs data scrubbing, and encrypted disk volumes).
2. **Mobile & Family Ergonomics**: Native apps provide zero-friction mobile auto-backup for the Pixel 9 Pro XL, native facial recognition clustering for family photos, in-browser document editing, and fallback media playback for multi-user households.
3. **Power-User Automation**: Docker containers handle high-throughput media ingestion, indexer aggregation, 0-byte atomic hardlinking, Intel QuickSync GPU transcoding, whole-home DNS filtering, and cross-platform password/passkey management.

---

## 📦 2. UGOS Pro Native Application Catalog

All native packages reside under `/volume1/@appstore/` with dedicated PostgreSQL instances and systemd service targets:

| Package Identifier | User-Facing Name | Binary / Service | Primary Role |
| :--- | :--- | :--- | :--- |
| `com.ugreen.photo` | **UG Photos** | `photo_serv` | Photo timeline, mobile backup target, album sharing |
| `com.ugreen.aiconsole` | **AI Console & Model Mgr** | `aiconsole_serv` | Local NPU/CPU facial recognition, pet/scene classification |
| `com.ugreen.syncbackup` | **Sync & Backup** | `syncspace`, `syncbackup_serv` | Continuous folder sync (Pixel 9 Pro XL & PC), Time Machine target |
| `com.ugreen.videomgr` | **Theater (Video Center)** | `video_serv` | Native video scraping, TMDB poster wall, web/app playback |
| `com.ugreen.downloadmgr` | **Download Center** | `download_serv`, `aria2c` | Direct URL, magnet, and `.torrent` manual downloader |
| `com.ugreen.office` | **Document / Office** | `docservice`, `converter` | OnlyOffice document server for in-browser doc/sheet editing |
| `com.ugreen.vault` | **Encrypted Space (Vault)** | `com.ugreen.vault` | AES-256 encrypted file directory protected by master PIN |
| `com.ugreen.netdisk` | **Cloud Drive (NetDisk)** | `com.ugreen.netdisk` | 2-way sync with Google Drive, OneDrive, and Dropbox |

---

## 🔍 3. Deep Comparison Matrices

### 3.1 UG Theater & Downloads vs. Plex & The *Arr Stack

| Dimension | UG Native (Theater + Downloads) | Automated Stack (Plex + *Arr) |
| :--- | :--- | :--- |
| **Ingestion Trigger** | Manual magnet/torrent pasting | Automated via Overseerr request |
| **Indexer Querying** | None (Must search manually) | Prowlarr multi-indexer aggregator |
| **Release Quality Filter** | None (Manual selection) | Radarr/Sonarr Quality Profiles |
| **Download Engine** | Aria2 (`download_serv`) | qBittorrent (TCP-only, hardened) |
| **Storage Efficiency** | Flat file storage (no hardlinks) | 0-Byte Atomic Hardlinks & Renaming |
| **Subtitle Automation** | Basic single-file fetch | Bazarr (Dual EN + HI automated sync) |
| **Transcoding Engine** | Client-side software decode | Intel QuickSync iGPU (`/dev/dri`) |
| **Client Ecosystem** | UGREEN App / DLNA Casting | Apple TV, Smart TVs, iOS, Plexamp |
| **Swarm & NAT Safety** | Default unhardened Aria2 | Ratio 1.0 Auto-Pause, 300 Max Conns |

---

### 3.2 UG Vault (File Safe) vs. Vaultwarden (Password Manager)

> [!IMPORTANT]
> **UGOS Vault and Vaultwarden operate in distinct security domains:**
>
> 1. **UGOS Encrypted Space (`com.ugreen.vault`)** = **Encrypted File Locker**  
>    Encrypts local disk folders with AES-256 for private PDFs, tax files, contracts, and identity scans. Accessible via secondary PIN.
> 2. **Vaultwarden** = **Password & Credential Manager**  
>    Self-hosted Bitwarden server for web logins, passkeys, 2FA/TOTP authenticator codes, credit cards, and browser autofill.

| Dimension | UGOS Vault (Built-in NAS App) | Vaultwarden (Docker Container) |
| :--- | :--- | :--- |
| **Stored Content** | 📁 Files (PDFs, scans, contracts) | 🔑 Logins, Passwords, 2FA, Passkeys |
| **Access Protocol** | UGREEN App / Web Desktop | Bitwarden Browser Extension & Mobile |
| **Browser Autofill** | ❌ No | ✅ Yes (Automatic web form fill) |
| **2FA / TOTP Generator** | ❌ No | ✅ Yes (RFC 6238 6-digit tokens) |
| **Passkey / FIDO2 Auth** | ❌ No | ✅ Yes (WebAuthn / Passkeys) |
| **Data Encryption Target** | Local NAS Btrfs Volume | SQLite Encrypted Cipher Database |

---

### 3.3 UG Photos & AI Console vs. Immich

| Feature | UG Photos + AI Console (Native) | Immich (Containerized) |
| :--- | :--- | :--- |
| **Mobile Sync Target** | ✅ UGREEN NAS App (Pixel 9 Pro XL) | ✅ Immich Mobile App |
| **Facial Recognition** | ✅ Local AI model (com.aiconsole) | ✅ Machine Learning Facial Vectors |
| **Semantic Search** | ⚠️ Basic scene tags (Pets, Food) | ✅ CLIP Natural Language Search |
| **Live Photos Support** | ⚠️ Basic Motion Playback | ✅ Native HEIC + MOV Live Playback |
| **Multi-User Isolation** | Account-isolated shares | Partner Libraries & Granular Sharing |
| **Database Backend** | Proprietary UG PostgreSQL | PostgreSQL with `pgvector` extension |

---

### 3.4 UG Office (OnlyOffice) & Sync & Backup

- **UG Office (`com.ugreen.office`)**:
  - Runs OnlyOffice `docservice` and `converter` binaries.
  - Allows direct in-browser viewing and collaborative editing of Word (`.docx`), Excel (`.xlsx`), and PowerPoint (`.pptx`) files stored on the NAS without opening desktop software.
- **Sync & Backup (`com.ugreen.syncbackup`)**:
  - Runs dual `syncspace` daemon instances.
  - Handles continuous two-way sync between client devices (Pixel 9 Pro XL, macOS, Windows) and NAS folders.
  - Manages Apple Time Machine backup shares.

---

## 📊 4. Host Resource Profile & Background Footprint

Live telemetry on UGREEN DXP2800 (Intel N100, 8GB DDR5):

| Subsystem | Active Processes | RAM Usage | Storage Footprint |
| :--- | :--- | :--- | :--- |
| **Docker Engine + Containers** | dockerd, 11 containers | ~1.8 GiB | 16 GB (`/volume2`) |
| **UG Office (OnlyOffice)** | docservice, converter | ~170 MiB | ~1.5 GB (`@appstore`) |
| **UG Photos & AI Console** | photo_serv, aiconsole | ~80 MiB | ~500 MB (`@appstore`) |
| **UG Sync & Backup** | syncspace (2x), serv | ~85 MiB | ~150 MB (`@appstore`) |
| **UG Theater & Downloads** | video_serv, downloadmgr | ~100 MiB | ~100 MB (`@appstore`) |
| **System Core & OS Cache** | Kernel, systemd, Btrfs | ~1.1 GiB | Root Filesystem |
| **Total Allocated / Available** | Load Average: 0.35 P95 | **3.3G / 7.5G** | **4.2 GiB Free RAM** |

---

## 🛠️ 5. Operational Management & Runbook

### Service Lifecycle:
- Native UGOS Pro applications should be configured and toggled through the **UGOS Web Portal (`http://192.168.1.80`) -> App Center -> Installed**.
- Docker containers are managed via compose in `/volume2/docker/`.

### Storage Tiering Alignment:
- Hot application configs and databases live on the NVMe tier (`/volume2`).
- Cold media libraries, photo dumps, document archives, and torrent complete states live on the CMR HDD tier (`/volume1`).

---

## 🔗 6. Cross-References

- [`MEDIA_STACK_HANDOFF.md`](MEDIA_STACK_HANDOFF.md) — Strict SLA/SLO contract and operational runbooks for Plex and *Arr automation.
- [`STORAGE_TIERING_AND_NVME_ARCHITECTURE.md`](STORAGE_TIERING_AND_NVME_ARCHITECTURE.md) — NVMe TBW protection and Btrfs storage pool layout.
- [`HARDWARE_AND_SYSTEMS_INVENTORY.md`](../HARDWARE_AND_SYSTEMS_INVENTORY.md) — Single Source of Truth physical hardware specs.
