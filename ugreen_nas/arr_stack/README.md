# 🎬 Plex & *Arr Stack (UGREEN DXP2800) — Single Source of Truth

> **Target Device**: UGREEN DXP2800 (Intel N100, 8GB DDR5 RAM, 10TB IronWolf CMR Volume 1)  
> **Status**: 🟢 **Operational & Production Verified** (All 8 Services Healthy)  
> **Transcoding Engine**: Intel QuickSync Video (Hardware Transcoding via `/dev/dri` render group `105`)  
> **Storage Architecture**: Unified `/volume1/data` mount enabling true zero-copy atomic hardlinks  

---

## 1. Service Catalog & Endpoints

| Service | Port | LAN URL | Purpose |
| :--- | :--- | :--- | :--- |
| **Plex** | `32400` | [http://192.168.1.80:32400/web](http://192.168.1.80:32400/web) | Hardware-accelerated media streaming (Intel QuickSync `/dev/dri`) |
| **Prowlarr** | `9696` | [http://192.168.1.80:9696](http://192.168.1.80:9696) | Centralized Indexer Manager (1337x, Nyaa, TPB, YTS, LimeTorrents auto-synced) |
| **Radarr** | `7878` | [http://192.168.1.80:7878](http://192.168.1.80:7878) | Movies automation & quality scoring |
| **Sonarr** | `8989` | [http://192.168.1.80:8989](http://192.168.1.80:8989) | TV Shows automation & season tracking |
| **qBittorrent**| `8080` | [http://192.168.1.80:8080](http://192.168.1.80:8080) | Torrent client with direct SATA I/O (Default user: `admin`, port `6881`) |
| **Bazarr** | `6767` | [http://192.168.1.80:6767](http://192.168.1.80:6767) | Subtitle auto-sync and management |
| **Overseerr** | `5055` | [http://192.168.1.80:5055](http://192.168.1.80:5055) | Media discovery & request portal |
| **Tautulli** | `8181` | [http://192.168.1.80:8181](http://192.168.1.80:8181) | Plex stream analytics, monitoring, & QuickSync HW transcode verification |

---

## 2. Key Architecture & Migrated Tokens

### 1. Migrated Application Tokens & Integrations
* **Prowlarr API Key**: `eb674050f3e24beaa54b515dbb7a01ac`
* **Radarr API Key**: `30ad1ab196a04184b11289e39a695f20`
* **Sonarr API Key**: `7385f68a846a416d9964d08d1eccda12`
* **Tautulli MovieDB API Key**: `e9a6655bae34bf694a0f3e33338dc28e`
* **Overseerr API Key**: `MTc4NzI5MzM4ODAwMTZmODg3ZWJlLTU5NWItNDA5My1hOTczLThmZDAwYjExMmRlMQ==`

### 2. Intel QuickSync Hardware Acceleration
* **Host Nodes**: `/dev/dri/card0` (video group `44`), `/dev/dri/renderD128` (render group `105`).
* **Container Group Mapping**: Plex container configured with `group_add: ["105", "44"]` and `devices: - /dev/dri:/dev/dri` so the internal process has full hardware access to Intel QuickSync for 4K HDR tone mapping.

### 3. Zero-Copy Atomic Hardlinks
* **Unified Data Path**: Both downloaders and \*Arr apps share `/volume1/data:/data`.
* **Inodes Validation**: Verified that completed torrents in `/data/torrents/movies/` link directly to `/data/media/movies/` with **0 MB duplicate disk space** and instant migration.

### 4. Language Scoring Custom Formats
Applied across all Quality Profiles in both Radarr and Sonarr:
* **Hindi Audio**: `+500` (regex: `(?i)\b(hindi)\b`)
* **Dual Audio**: `+400` (regex: `(?i)(Dual.Audio|DualAudio|\[Dual\])`)
* **Hindi Dubbed**: `+300` (regex: `(?i)(Hindi.Dubbed|HindiDubbed)`)

---

## 3. Directory Layout on 10TB IronWolf (Volume 1)

```text
/volume1/
├── docker/
│   └── arr_stack/
│       ├── docker-compose.yml
│       ├── plex/
│       ├── qbittorrent/
│       ├── radarr/
│       ├── sonarr/
│       ├── prowlarr/
│       ├── bazarr/
│       ├── overseerr/
│       └── tautulli/
└── data/
    ├── torrents/
    │   ├── incomplete/
    │   ├── movies/
    │   └── tv/
    └── media/
        ├── movies/
        ├── tv/
        └── music/
```

---

## 4. Decommissioning & Legacy Status on Pi 5
* **Raspberry Pi 5 Cleanup**: All 8 media containers and 5.07GB of unused Docker images deleted from `192.168.1.92`.
* **Reclaimed Pi 5 Storage**: 101GB free space (10% utilization).
* **Dedicated Role**: Raspberry Pi 5 is 100% dedicated to **Pi-hole v6** whole-home DNS filtering and high availability.
