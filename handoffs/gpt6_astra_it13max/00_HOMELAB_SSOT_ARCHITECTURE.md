# 🌐 Homelab Architecture & Systems Single Source of Truth (SSOT)

> **Audience**: `oGPT-6-astra`  
> **Master Purpose**: Full ground-truth architectural baseline of physical nodes, storage tiers, network routing, and running microservices across the private infrastructure.

---

## 🏗️ 1. Physical Node Matrix

| Specification | Node 1: UGREEN DXP2800 NAS | Node 2: Raspberry Pi 5 | Node 3: GEEKOM IT13 Max | Node 4: Pixel 1 (Phys + Twin) |
| :--- | :--- | :--- | :--- | :--- |
| **IP Address** | `192.168.1.80` (Wired 2.5GbE) | `192.168.1.92` (`wlan0`) / `.116` | `192.168.1.155` (Wi-Fi 7 / 2.5GbE) | `192.168.1.X` / Port `5555` Twin |
| **Processor (CPU)**| Intel N100 (4C/4T, ≤3.4GHz) | Broadcom BCM2712 (4C @ 2.4GHz)| Intel Core Ultra 9 185H (16C/22T)| Qualcomm Snapdragon 821 |
| **Hardware Accel** | Intel UHD 24EU QuickSync | VideoCore VII (Display only) | Intel Arc 8 Xe-Cores iGPU + NPU | Adreno 530 GPU |
| **RAM** | 8 GB DDR5 (Single SODIMM) | 16 GB LPDDR4X (Soldered) | 16 GB DDR5 5600MHz (Dual Slot)| 4 GB LPDDR4 |
| **Operating System**| UGOS Pro (Debian 12 kernel) | Raspberry Pi OS (Debian 13) | Ubuntu Server 24.04 LTS | Android 10 (LineageOS / Stock)|
| **Primary Tier** | 10TB Seagate IronWolf (CMR) | 128GB MicroSD Card | 1TB Gen4 NVMe SSD (`WPBSN4M8`) | 32GB Internal Flash |
| **Solid-State Tier**| 4TB WD_BLACK SN850X NVMe | N/A | 1TB Gen4 NVMe SSD | N/A |
| **Cold SMR Archive**| CIFS Mount from Pi 5 | 8TB Seagate Expansion SMR | N/A | N/A |
| **Role** | Hot Apps, Databases, Storage | DNS, DHCP, Cold Orchestration | **Dedicated Heavy Compute & AI**| **Unlimited Google Photos Backup**|

---

## 🗄️ 2. Storage Tiering & Preservation Directives
1. **Hot NVMe Tier (`/volume2` on NAS — 4TB WD_BLACK SN850X)**:
   - Reserved exclusively for random I/O: SQLite databases, Docker runtimes, active state files, and fast metadata.
   - Rated at 2,400 TBW endurance.
2. **Cold Mechanical CMR Tier (`/volume1` on NAS — 10TB Seagate IronWolf)**:
   - Houses bulk media (Plex movies, TV shows, raw photo dumps, time-machine backups).
   - Configured for deep sleep / 0 RPM hibernation when idle. Strictly protected from recursive metadata scanners (`find`, `grep`, `du`).
3. **Cold SMR Tier (`/mnt/media-storage` on Pi 5 — 8TB Seagate Expansion)**:
   - Attached to the Pi 5 to completely isolate slow SMR write cliffs and USB polling latency from the NAS.
   - Managed via a 15-minute aggressive spindown rule (`hdparm -S 180`).
4. **Zero-Copy Containerization Mandate**:
   - Never copy bulk media across volumes. Always use read-only bind mounts (`-v /volume1/path:/target:ro`).

---

## 🛡️ 3. Core Network & DNS Hierarchy
1. **High-Availability DNS Failover**:
   - **Primary Node**: Pi-hole v6 FTL on Raspberry Pi 5 (`192.168.1.92:53`) backed by an in-memory root recursive resolver (**Unbound** at `127.0.0.1:5335`).
   - **Secondary Node**: Standby Pi-hole on UGREEN NAS (`192.168.1.80:53`) running in bridge mode (binding `192.168.1.80:53:53` to avoid host `dnsmasq` conflict).
2. **Authoritative DHCP (Option 6)**:
   - Broadcast exclusively with local DNS: `dhcp-option=6,192.168.1.80,192.168.1.92`.
   - **Strict Rule**: NEVER inject public DNS (`1.1.1.1`, `8.8.8.8`) into client Option 6 to prevent Android DoT hijacking (port 853) and OS-level ad-blocking bypass.
3. **Static Reservations**:
   - Pi 5: `192.168.1.92`
   - UGREEN NAS: `192.168.1.80`
   - IT13 Max: `192.168.1.155` (MAC: `f8:cf:52:eb:88:e0`)
4. **BitTorrent Conntrack Protection**:
   - In `qbittorrent`, TCP-only transport is enforced (`Session\BittorrentProtocol=1`) to eliminate connectionless uTP UDP NAT table explosions on the router. 1:1 seed ratio auto-pauses downloads.

---

## 📱 4. Pixel 1 Unlimited Backup Pipeline & Redroid Digital Twin
- **Physical Pixel 1 Hardware**: Connected to LAN, runs Syncthing in the background. Ingests photos from user iPhones and cameras, then uploads original-quality uncompressed photos to Google Photos under Google's lifetime unlimited tier.
- **Virtual Redroid Pixel 1 Twin (`redroid-pixel1`)**: Hosted on the UGREEN NAS NVMe tier (`/volume2`), exposing Android ADB on port `5555`. Serves as an always-on cloud synchronization gateway and backup verification container.
- **Decoupled Photo Architecture**: Uses read-only bind mounts directly from `/volume1/DP` to eliminate duplicate writes.

---

## 🚀 5. Active Production Services by Node

### A. UGREEN DXP2800 NAS (`192.168.1.80`)
- **Plex Media Server (`32400`)**: Hardware-accelerated 4K HDR transcoding via Intel UHD QuickSync (`/dev/dri/renderD128`).
- ***Arr Automation Suite**:
  - `Prowlarr` (`9696`): Indexer aggregator.
  - `Radarr` (`7878`): Movie automation with custom Hindi & Dual-Audio scoring.
  - `Sonarr` (`8989`): TV Show automation.
  - `qBittorrent` (`8080` / `6881`): High-throughput torrent engine.
  - `Bazarr` (`6767`): Subtitle synchronization.
  - `Overseerr` (`5055`): Media discovery & request portal.
  - `Tautulli` (`8181`): Stream telemetry.
- **Vaultwarden (`8085` / `3012`)**: Self-hosted Bitwarden password manager with WebSocket sync.
- **Homepage (`3000`)**: Homelab single-pane-of-glass status dashboard.
- **Calibre-Web (`8083`) & Shelfmark (`8084`)**: Digital library and multi-source book requesting hub.
- **Secondary Pi-hole (`8089`)**: High-availability DNS backup node.

### B. Raspberry Pi 5 (`192.168.1.92`)
- **Primary Pi-hole v6 FTL (`53`, `80`, `443`)**: Whole-home ad-blocking & DHCP server (`Nice=-10`, `OOMScoreAdjust=-1000`).
- **Unbound Recursive DNS (`5335`)**: Local root DNS resolver with DNSSEC anchor validation.
- **Tailscale Subnet Router**: WireGuard mesh gateway advertising `192.168.1.0/24`.
- **Headless Jules Agent Worker**: Autonomous 24/7 GitHub PR review daemon.
- **n8n Automation Engine (`5678`)**: Low-code workflow automation orchestrator.
- **Stirling-PDF (`8083`)**: Offline document transformation & OCR utility.
- **TripDrop (`8088`)**: High-speed chunked file upload portal.
- **Dead Man's Switch**: Shamir's Secret Sharing ($M_{521}$) contingency key vault.
- **Monorepo Extended Swarm**: 100 fully merged, containerized homelab microservices (Projects 01–100 in `deepshah08/raspberry-pi-5-ecosystem`).
