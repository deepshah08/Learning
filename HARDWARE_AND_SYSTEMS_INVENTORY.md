# 🖥️ Hardware Inventory & Systems Status — Single Source of Truth

> **Context**: Master inventory of all physical computing nodes, storage drives, network interfaces, and running software services across the home lab ecosystem.  
> **Last Verified**: 2026-08-28 10:05 PDT  
> **Status**: 🟢 **All Production Systems Healthy & Synchronized (100% High-Availability Architecture)**  

---

## 🏗️ 1. Physical Hardware Inventory

| Specification | Node 1: UGREEN DXP2800 NAS | Node 2: Raspberry Pi 5 (16GB) | Node 3: GEEKOM IT13 Max |
| :--- | :--- | :--- | :--- |
| **Processor (CPU)** | Intel N100 (4C/4T, ≤3.4GHz) | Broadcom BCM2712 (4C @ 2.4GHz) | Intel Core Ultra 9 185H (16C/22T) |
| **GPU / Transcoding** | Intel UHD 24EU QuickSync | VideoCore VII (Display only) | Intel Arc 8 Xe-Cores iGPU + NPU |
| **System Memory (RAM)** | 8 GB DDR5 | 16 GB LPDDR4X | 16 GB DDR5 |
| **Primary Storage** | 10TB Seagate IronWolf (CMR) | 128GB MicroSD (101GB Free / 10%) | 1TB Gen4 NVMe PCIe SSD |
| **High-Speed Solid-State Tier** | 4TB WD_BLACK SN850X (NVMe) | N/A | 1TB Gen4 NVMe PCIe SSD |
| **Attached Secondary Storage** | N/A (Decoupled to Pi 5) | 8TB Seagate Expansion (SMR) | N/A |
| **Physical M.2 / RAM Layout** | M.2 Slots: Inside HDD Trays | Bottom Hatch: SODIMM RAM Slot | Dual M.2 PCIe / SODIMM DDR5 Slots |
| **SMR Drive Status** | N/A (Decoupled to Pi 5) | 🟢 MOUNTED (`/mnt/media-storage`) | N/A |
| **Network Interface** | 2.5 Gigabit Ethernet (2.5GbE) | 1GbE (`eth0` default) + Wi-Fi 5 | Wi-Fi 6E/7 + 2.5GbE LAN |
| **Local IP Address** | `192.168.1.80` | `192.168.1.116` (`eth0`) / `.92` | `192.168.1.155` (`it13_max.lan`) |
| **Tailscale Node Name** | Subnet Routed (`.80`) | `pi5-media-nas` (`100.68.196.14`)| `it13-max-compute` (Planned) |
| **Operating System** | UGOS Pro (Debian 12 Kernel) | Raspberry Pi OS (Debian 13) | Ubuntu Server 24.04 / Win11 Pro |
| **SSH Session Pipeline** | ControlMaster (<25ms pipe) | ControlMaster (<25ms pipe) | ControlMaster (<25ms pipe) |

---

## 💾 2. Storage Drive Architecture

### Drive 1: 10TB Seagate IronWolf CMR (`ST10000VN000`)
* **Location**: UGREEN NAS Bay 1 (`/volume1`)
* **Filesystem**: Btrfs (~9.1 TiB usable, ~8.1 TiB Free)
* **Role**: Bulk cold media tier (Plex Movies, TV Shows, raw photo archives, Time Machine backups). Configured for deep sleep / 0 RPM hibernation without USB polling interference.

### Drive 2: 4TB WD_BLACK SN850X NVMe PCIe 4.0 SSD (`WDS400T2X0E`)
* **Location**: Internal M.2 Slot 1 (`/volume2` - 3.7 TiB Free)
* **Endurance Rating**: **2,400 TBW** (33.2 GB written = 0.0013% used; ~6,575-year lifespan)
* **Role**: High-speed 24/7 Hot Application Tier (`/volume2/@docker` + `/volume2/docker`). Hosts Docker engine, SQLite databases (Pi-hole, *Arr, Vaultwarden, Plex metadata), Redroid Pixel 1 twin, and snapshot archives.

### Drive 3: 8TB Seagate Expansion SMR (`STKR8000400` / `ST8000DM004`)
* **Location**: Connected to Raspberry Pi 5 USB 3.0 port (`/dev/sda2`)
* **Filesystem**: exFAT (7.3 TiB usable, 6.3 TiB Free, 14% used)
* **Mount Point (Pi 5)**: `/mnt/media-storage`
* **Mount Configuration (Pi 5)**: `UUID=6217-BF12 /mnt/media-storage exfat rw,nofail,noatime,uid=1000,gid=1000,errors=remount-ro 0 0` in `/etc/fstab`
* **Spindown Policy**: 🟢 **15-Minute Standby Spindown** enforced by `/etc/udev/rules.d/69-smr-spindown.rules` (`hdparm -S 180`). Drive rests at 0 RPM (<0.5W, ~26°C–28°C) during idle periods to prevent bearing thermal breakdown.
* **Network Export (Pi 5)**: Containerized Samba (SMB3) service (`crazymax/samba`, Zero Host Mutation) binding to `192.168.1.116:445` and `192.168.1.92:445`. Restricted to LAN subnet and NAS IP.
* **NAS Client Mount**: 🟢 **ACTIVE / MOUNTED** at `/mnt/smr-archive` via `/sbin/mount.cifs` and symlinked at `/volume1/data/smr-archive`.
* **NAS Persistent Automation**: Managed via systemd service `pi5-smr-mount.service` with root credentials file `/etc/samba/pi5-smr.cred`.
* **Archival Synchronization**: Automated via `/volume2/docker/backups/sync_to_smr_archive.sh` with `--bwlimit=60000` (60MB/s) sequential I/O throttling to protect SMR write performance.
* **Decoupling Benefit**: Offloads all SMR drive latency, write cliffs, and USB polling from the UGREEN NAS, allowing the NAS to operate purely with NVMe + CMR SATA while the 16GB RAM Pi 5 handles cold media ingestion, secondary backups, and offline RAG pipelines.

### Drive 4: 1TB PCIe 4.0 NVMe SSD (Internal)
* **Location**: GEEKOM IT13 Max internal M.2 NVMe slot (`/dev/nvme0n1`)
* **Filesystem**: NTFS (Factory Win11) -> Target: ext4 / btrfs (Ubuntu Server)
* **Role**: High-speed dedicated AI model weight storage (Ollama, OpenVINO, Faster-Whisper), Docker root runtime, and local execution caches.

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
| **Calibre-Web** | `8083` | [http://192.168.1.80:8083](http://192.168.1.80:8083) | 🟢 **Production** | Digital Bookshelf, in-browser reader, and OPDS wireless catalog |
| **Shelfmark** | `8084` | [http://192.168.1.80:8084](http://192.168.1.80:8084) | 🟢 **Production** | Book search, multi-source request hub (Prowlarr/Torrents, Anna's Archive, LibGen) |
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
| **Cold SMR Media Archive** | Filesystem | `/mnt/media-storage` | 🟢 **Production** | 8TB Seagate Expansion SMR mounted read-only (`ro,nofail,noatime`) |

---

### C. Systems Hosted on GEEKOM IT13 Max (`192.168.1.155`)

| Service | Port | Endpoint | Status | Verified Functionality |
| :--- | :--- | :--- | :--- | :--- |
| **Remote Desktop (RDP)** | `3389` | `192.168.1.155:3389` | 🟢 **Active** | Native Windows 11 Pro RDP server verified from Mac |
| **OpenSSH Management** | `22` | `ssh deep@192.168.1.155` | 🟡 **Provisioning** | Port 22 OpenSSH server daemon (ControlMaster target) |
| **Ollama Local LLM (Target)** | `11434` | `http://192.168.1.155:11434` | 📋 **Planned** | Intel Arc 8 Xe-core iGPU offload via OpenVINO / oneAPI |
| **Faster-Whisper STT (Target)**| `8090` | `http://192.168.1.155:8090` | 📋 **Planned** | Dedicated real-time speech-to-text offloading Pi 5 |
| **Immich ML Offload (Target)** | `3003` | `http://192.168.1.155:3003` | 📋 **Planned** | CLIP & facial recognition engine offloading NAS N100 |

---

## ⚖️ 4. Decoupled Architecture & Independent Scaling

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        3-TIER INDEPENDENT ASYMMETRIC SCALING MODEL                     │
├────────────────────────────┬─────────────────────────────┬─────────────────────────────┤
│ Node 1: UGREEN NAS (.80)   │ Node 2: Raspberry Pi 5 (.92)│ Node 3: GEEKOM IT13 Max(.155│
├────────────────────────────┼─────────────────────────────┼─────────────────────────────┤
│ • Pure Storage Tiering:    │ • Network & DNS Authority:  │ • Dedicated Compute & AI:   │
│   - NVMe (/volume2): Docker│   - Pi-hole v6 Primary FTL  │   - Core Ultra 9 185H (16C) │
│   - CMR SATA (/volume1):   │   - Unbound Root Recursive  │   - Arc 8 Xe-Cores iGPU     │
│     Mass Media (0 RPM)     │   - Authoritative DHCP Opt 6│   - 16GB DDR5 + 1TB NVMe    │
│ • Zero USB polling wakeups │ • Strict SLO Protection:    │ • Zero Throttle AI:         │
│ • QuickSync Transcoding    │   - Nice=15 / CPUQuota=50%  │   - Ollama / OpenVINO       │
│ • 2.5GbE Dedicated LAN     │   - Decoupled from heavy AI │   - Faster-Whisper real-time│
│ • High-Availability DNS #2 │ • Attached 8TB SMR Archive  │   - Immich ML offloader     │
└────────────────────────────┴─────────────────────────────┴─────────────────────────────┘
```

### Key Scaling Principles:
1. **SLO & Network Blast-Radius Shielding**: Whole-home DNS/DHCP on the Raspberry Pi 5 is completely insulated from CPU starvation. Heavy inference (Whisper, LLMs) is decoupled onto the IT13 Max.
2. **Actuator & Spindown Isolation**: The UGREEN NAS is completely freed from external USB disk controllers. The 10TB Seagate IronWolf CMR drive stays in 0 RPM deep hibernation undisturbed.
3. **Compute Specialization**:
   - **Pi 5 (16GB RAM)**: Network gatekeeper, recursive DNS, lightweight background orchestration, and cold SMR archiving.
   - **NAS (Intel N100 + QuickSync)**: Low-latency NVMe transactions, 4K QuickSync hardware media streaming, and native file sharing.
   - **IT13 Max (Intel Core Ultra 9 185H + Arc)**: Unthrottled local AI inference, OpenVINO acceleration, continuous container workloads, and automated builds.

---

## 🛠️ 5. Portable Diagnostic & RF Tooling Inventory

| Device | Model & UID | Firmware | Primary Storage | Role & Interface | Documentation Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Flipper Zero** | `Epriesol` (UID: `58688D0127E18000`, HW Ver 15) | Release 1.4.3 (Radio: 1.20.0 light) | 32GB MicroSD (FAT32, ~29.7 GiB, 1-bit SPI) | Sub-GHz, NFC (Mifare), RFID (125kHz), IR universal remotes, BadUSB audits (`/dev/cu.usbmodemflip_Epriesol1`) | [flipper_zero/README.md](hardware_and_diagnostics/flipper_zero/README.md) |


