# 🖥️ Hardware Inventory & Systems Status — Single Source of Truth

> **Context**: Master inventory of all physical computing nodes, storage drives, network interfaces, and running software services across the home lab ecosystem.  
> **Last Verified**: 2026-08-28 10:05 PDT  
> **Status**: 🟢 **All Production Systems Healthy & Synchronized (100% High-Availability Architecture)**  

---

## 🏗️ 1. Physical Hardware Inventory

```text
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   PHYSICAL HARDWARE NODES                                   │
├────────────────────────────┬─────────────────────────────┬──────────────────────────────────┤
│ Specification              │ Node 1: UGREEN DXP2800 NAS  │ Node 2: Raspberry Pi 5 (16GB)   │
├────────────────────────────┼─────────────────────────────┼──────────────────────────────────┤
│ Processor (CPU)            │ Intel N100 (4C/4T, ≤3.4GHz) │ Broadcom BCM2712 (4C @ 2.4GHz)   │
│ GPU / Transcoding          │ Intel UHD 24EU QuickSync    │ VideoCore VII (Display only)     │
│ System Memory (RAM)        │ 8 GB DDR5                   │ 16 GB LPDDR4X                    │
│ Primary Storage            │ 10TB Seagate IronWolf (CMR) │ 128GB MicroSD (101GB Free / 10%) │
│ High-Speed Solid-State Tier│ 4TB WD_BLACK SN850X (NVMe)  │ N/A                              │
│ Secondary Storage          │ 8TB Seagate Expansion (SMR) │ N/A                              │
│ Physical M.2 / RAM Layout  │ M.2 Slots: Inside HDD Trays │ Bottom Hatch: SODIMM RAM Slot    │
│ SMR Drive Status           │ ⚠️ DISCONNECTED (Cold Standby│ N/A                              │
│ Network Interface          │ 2.5 Gigabit Ethernet (2.5GbE│ 1GbE / 5GHz Wi-Fi (BSSID Locked) │
│ Local IP Address           │ `192.168.1.80`              │ `192.168.1.92` (Static)          │
│ Tailscale Node Name        │ Subnet Routed (`.80`)       │ `pi5-media-nas` (`100.68.196.14`)│
│ Operating System           │ UGOS Pro (Debian 12 Kernel) │ Raspberry Pi OS (Debian 13)      │
│ SSH Session Pipeline       │ ControlMaster (<25ms pipe)  │ ControlMaster (<25ms pipe)       │
└────────────────────────────┴─────────────────────────────┴──────────────────────────────────┘
```

---

## 💾 2. Storage Drive Architecture

### Drive 1: 10TB Seagate IronWolf CMR (`ST10000VN000`)
* **Location**: UGREEN NAS Bay 1 (`/volume1`)
* **Filesystem**: Btrfs (~9.1 TiB usable, ~8.1 TiB Free)
* **Role**: Bulk cold media tier (Plex Movies, TV Shows, raw photo archives, Time Machine backups). Configured for deep sleep / 0 RPM hibernation.

### Drive 2: 4TB WD_BLACK SN850X NVMe PCIe 4.0 SSD (`WDS400T2X0E`)
* **Location**: Internal M.2 Slot 1 (`/volume2` - 3.7 TiB Free)
* **Endurance Rating**: **2,400 TBW** (33.2 GB written = 0.0013% used; ~6,575-year lifespan)
* **Role**: High-speed 24/7 Hot Application Tier (`/volume2/@docker` + `/volume2/docker`). Hosts Docker engine, SQLite databases (Pi-hole, *Arr, Vaultwarden, Plex metadata), Redroid Pixel 1 twin, and snapshot archives.

### Drive 3: 8TB Seagate Expansion SMR (`STKR8000400`)
* **Location**: External USB 3.0
* **Current Status**: 🛑 **DISCONNECTED / COLD ARCHIVAL**
* **Power Management Policy**: Configured with automated **15-minute spindown (`hdparm -S 180 -B 127`)** via udev rule (`98-smr-spindown.rules`).
* **Role**: Dedicated cold repository for scheduled weekly/monthly encrypted backups (Restic / Borg).

---

## 🚀 3. Live Services Status by Host

### A. Systems Hosted on UGREEN DXP2800 (`192.168.1.80`)

| Service | Port | Endpoint | Status | Verified Functionality |
| :--- | :--- | :--- | :--- | :--- |
| **Plex Media Server** | `32400` | [http://192.168.1.80:32400/web](http://192.168.1.80:32400/web) | 🟢 **Production** | Hardware transcoding via Intel QuickSync (`/dev/dri/renderD128`) |
| **Prowlarr** | `9696` | [http://192.168.1.80:9696](http://192.168.1.80:9696) | 🟢 **Production** | Indexer hub auto-syncing 1337x, Nyaa, TPB, YTS to Radarr/Sonarr |
| **Radarr** | `7878` | [http://192.168.1.80:7878](http://192.168.1.80:7878) | 🟢 **Production** | Movies automation with Hindi (+500) & Dual Audio (+400) scoring |
| **Sonarr** | `8989` | [http://192.168.1.80:8989](http://192.168.1.80:8989) | 🟢 **Production** | TV Shows automation with Hindi & Dual Audio scoring rules |
| **qBittorrent** | `8080` | [http://192.168.1.80:8080](http://192.168.1.80:8080) | 🟢 **Production** | Direct SATA I/O (Port `6881` P2P, default user `admin`) |
| **Bazarr** | `6767` | [http://192.168.1.80:6767](http://192.168.1.80:6767) | 🟢 **Production** | Subtitle automation and multi-language synchronization |
| **Overseerr** | `5055` | [http://192.168.1.80:5055](http://192.168.1.80:5055) | 🟢 **Production** | Media discovery & user request portal |
| **Tautulli** | `8181` | [http://192.168.1.80:8181](http://192.168.1.80:8181) | 🟢 **Production** | Stream telemetry & Intel GPU hardware transcode verification |
| **Secondary Pi-hole** | `53`, `8089`| [http://192.168.1.80:8089/admin](http://192.168.1.80:8089/admin)| 🟢 **Production** | High-availability failover DNS (309,418 blocked domains) |
| **Vaultwarden** | `8085`, `3012`| [http://192.168.1.80:8085](http://192.168.1.80:8085) | 🟢 **Production** | Encrypted Bitwarden password manager for Deep & Pranali |
| **Homepage Dashboard**| `3000` | [http://192.168.1.80:3000](http://192.168.1.80:3000) | 🟢 **Production** | Unified single-pane homelab dashboard with live widgets |
| **macOS SMB3 Sharing** | `445` | `smb://192.168.1.80` | 🟢 **Production** | High-speed Finder drag-and-drop (`personal_folder`, `data`, `DP`) |
| **OpenClaw AI Gateway** | `18799`| [http://192.168.1.80:18799](http://192.168.1.80:18799)| ⏸️ **Standby** | Multi-channel AI agent & personal automation gateway (Paused) |
| **UGREEN Photos AI** | `9999` | Native UGOS App | 🟢 **Production** | Hardware-accelerated AI face/scene recognition & mobile backup |
| **UGREEN Online Office**| `9999` | Native UGOS App | 🟢 **Production** | Collaborative OnlyOffice editor for Word, Excel, PowerPoint |

---

### B. Systems Hosted on Raspberry Pi 5 (`192.168.1.92`)

| Service | Port | Endpoint | Status | Verified Functionality |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Pi-hole v6 FTL**| `53`, `80`, `443`| [http://192.168.1.92/admin](http://192.168.1.92/admin)| 🟢 **Production** | Primary whole-home DNS ad-blocker & 24h DHCP server |
| **Unbound Recursive DNS** | `5335` (Local) | `127.0.0.1#5335` | 🟢 **Production** | 192MB In-Memory recursive root DNS with DNSSEC validation |
| **Tailscale Subnet Router**| WireGuard | `100.68.196.14` | 🟢 **Production** | Subnet gateway advertising `192.168.1.0/24` to remote devices |
| **Headless Jules Agent Worker**| Daemon | `projects/18-agent-worker` | 🟢 **Production** | Autonomous 24/7 background PR review & pytest worker |
| **TripDrop Staging Portal**| `8088` | [http://192.168.1.92:8088](http://192.168.1.92:8088) | 🟢 **Production** | FastAPI chunked drag-and-drop ingestion with mDNS |
| **Stirling-PDF Suite** | `8083` | [http://192.168.1.92:8083](http://192.168.1.92:8083) | 🟢 **Production** | Dockerized offline PDF transformation and OCR suite |
| **n8n Automation Engine** | `5678` | [http://192.168.1.92:5678](http://192.168.1.92:5678) | 🟢 **Production** | Self-hosted workflow automation & alert webhooks |
| **Dead Man's Switch** | Daemon | `projects/11-deadmans-switch` | 🟢 **Production** | Shamir's Secret Sharing ($M_{521}$) contingency key vault |
