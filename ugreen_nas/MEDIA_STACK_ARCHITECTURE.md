# 🎬 Complete *Arr, Plex & Media Automation Stack — Single Source of Truth

> **Host**: UGREEN DXP2800 (`192.168.1.80`)  
> **Status**: 🟢 **100% Operational & Production Verified**  
> **Last Verified**: 2026-08-28 18:42 PDT  
> **Storage Tier**: 10TB Seagate IronWolf CMR HDD (`/volume1/data`) for media & 4TB WD_BLACK SN850X NVMe (`/volume2`) for Docker/Databases.

---

## 🗺️ Master Service Catalog & API Endpoints

| Service | Port | Internal Docker URL | Auth / API Key | Storage Path |
|---|---|---|---|---|
| **Plex Media Server** | `32400` | `http://192.168.1.80:32400` | `26cEskkHTxWVGTJA8paY` | `/data/media` |
| **Overseerr** | `5055` | `http://overseerr:5055` | `MTc4NzI5MzM4OD...` | SQLite on NVMe |
| **Radarr (Movies)** | `7878` | `http://radarr:7878` | `30ad1ab196a04184b11289e39a695f20` | `/data/media/movies` |
| **Sonarr (TV Shows)** | `8989` | `http://sonarr:8989` | `7385f68a846a416d9964d08d1eccda12` | `/data/media/tv` |
| **Prowlarr (Indexers)** | `9696` | `http://prowlarr:9696` | `eb674050f3e24beaa54b515dbb7a01ac` | `deepshah08` / `Deepshah123$` |
| **qBittorrent** | `8080` | `http://qbittorrent:8080` | `admin` / `Deepshah123$` | `/data/torrents` |
| **Tautulli** | `8181` | `http://tautulli:8181` | `f2645a632bde4efb822a9a9c43c562da` | Config on NVMe |

---

## 📁 Storage Hierarchy on CMR HDD (`/volume1/data`)

```text
/volume1/data/
├── torrents/                  <-- Ingestion Tier (qBittorrent writes)
│   ├── incomplete/
│   ├── movies/
│   └── tv/
└── media/                     <-- Playback Tier (Atomic Hardlinks for Plex)
    ├── movies/                <-- 13 Organized Titles
    │   ├── Dhurandhar (2025)/
    │   ├── Dhurandhar The Revenge (2026)/
    │   ├── Ek Chalis Ki Last Local (2007)/
    │   ├── Fractured (2019)/
    │   ├── Geostorm (2017)/
    │   ├── Hereditary (2018)/
    │   ├── Kaalakaandi (2018)/
    │   ├── Motor City (2026)/
    │   ├── Nishaanchi (2025)/
    │   ├── Nishaanchi 2 (2025)/
    │   ├── Obsession (2026)/
    │   ├── Oye Lucky! Lucky Oye! (2008)/
    │   └── Paan Singh Tomar (2012)/
    └── tv/                    <-- 7 TV Series
        ├── A Year on Planet Earth/
        ├── Adarsh Baal Vidyalaya/
        ├── Delhi Crime/
        ├── Musafir Cafe/
        ├── Planet Earth/
        ├── Saare Jahan Se Accha/
        └── Sapne vs Everyone/
```

---

## ⚡ Hardlink Mechanics
Because `/volume1/data` is mounted across all containers under `/data`:
1. qBittorrent downloads to `/data/torrents/movies/`.
2. Radarr creates a 0-byte atomic hardlink at `/data/media/movies/`.
3. Plex streams the file with 0 duplicate disk space and 0 SSD wear.
