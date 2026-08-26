# 🖥️ Hardware Inventory & Systems Status — Single Source of Truth

> **Context**: Master inventory of all physical computing nodes, storage drives, network interfaces, and running software services across the home lab ecosystem.  
> **Last Verified**: 2026-08-25 22:08 PDT  
> **Status**: 🟢 **All Production Systems Healthy & Synchronized**  

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
│ Secondary Storage          │ 8TB Seagate Expansion (SMR) │ N/A                              │
│ SMR Drive Status           │ ⚠️ DISCONNECTED (Cold Standby│ N/A                              │
│ Network Interface          │ 2.5 Gigabit Ethernet (2.5GbE│ 1GbE / Wi-Fi 5                   │
│ Local IP Address           │ `192.168.1.80`              │ `192.168.1.92` (Static)          │
│ Tailscale Node Name        │ Subnet Routed (`.80`)       │ `pi5-media-nas` (`100.68.196.14`)│
│ Operating System           │ UGOS Pro (Debian 12 Kernel) │ Raspberry Pi OS (Debian 13)      │
└────────────────────────────┴─────────────────────────────┴──────────────────────────────────┘
```

---

## 💾 2. Storage Drive Architecture

### Drive 1: 10TB Seagate IronWolf CMR (`ST10000VN000`)
* **Location**: UGREEN NAS Bay 1 (`/volume1`)
* **Filesystem**: Btrfs (High-durability with checksumming and snapshot support)
* **Capacity**: ~9.1 TiB usable (~8.1 TiB free headroom)
* **Role**: Primary hot storage pool for Plex media, torrents, Docker container configs, Vaultwarden databases, and UGREEN Photos.

### Drive 2: 8TB Seagate Expansion SMR (`STKR8000400`)
* **Location**: External / Bay 2
* **Current Status**: 🛑 **DISCONNECTED / OFFLINE (As of Aug 25, 2026)**
* **Role**: Dedicated cold repository for scheduled weekly/monthly encrypted backups (Restic / Borg). Kept disconnected to prevent SMR write-amplification thrashing during daily random I/O.

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
| **UGREEN Photos AI** | `9999` | Native UGOS App | 🟢 **Production** | Hardware-accelerated AI face/scene recognition & mobile backup |
| **UGREEN Online Office**| `9999` | Native UGOS App | 🟢 **Production** | Collaborative OnlyOffice editor for Word, Excel, PowerPoint |

---

### B. Systems Hosted on Raspberry Pi 5 (`192.168.1.92`)

| Service | Port | Endpoint | Status | Verified Functionality |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Pi-hole v6 FTL**| `53`, `80`, `443`| [http://192.168.1.92/admin](http://192.168.1.92/admin)| 🟢 **Production** | Primary whole-home DNS ad-blocker & DHCP server |
| **Gravity-Sync Sender** | Cron (30m)| `/etc/cron.d/sync-pihole-nas` | 🟢 **Production** | Automated push of `gravity.db` & custom DNS to NAS |
| **Tailscale Subnet Router**| WireGuard | `100.68.196.14` | 🟢 **Production** | Subnet gateway advertising `192.168.1.0/24` to remote devices |
| **Ollama + ChromaDB** | `11434`, `8000`| Local Pipeline | 🟡 **Staged** | Local AI / RAG pipeline utilizing Pi 5's **16GB RAM** pool |
| **Legacy Media Stack** | Various | N/A | ⚪ **Decommissioned**| Removed to reclaim 5.07GB storage & eliminate memory pressure |

---

## 🌐 4. Client Ecosystem & Tailnet Devices

| Device | Owner / Role | OS | Connection Method |
| :--- | :--- | :--- | :--- |
| **MacBook Air** | Deep Shah (Dev / Control) | macOS | Local Wi-Fi / Tailscale (`100.78.122.75`) / SMB3 Mount |
| **Pixel 9 Pro XL** | Deep Shah (Primary Phone) | Android | Local Wi-Fi / Tailscale (`100.74.169.39`) / UGREENlink |
| **Pixel 1 (Sailfish)** | Dedicated Unlimited Uploader | Android | Local Wi-Fi / Google Photos Original Quality Waiver |
| **Galaxy Tab S10+** | Deep Shah (Tablet) | Android | Local Wi-Fi / Tailscale (`100.87.32.34`) / UGREENlink |
| **Pranali Devices** | Pranali (Co-Admin) | iOS / macOS | Local Wi-Fi / UGREEN Photos / Vaultwarden Family Vault |
