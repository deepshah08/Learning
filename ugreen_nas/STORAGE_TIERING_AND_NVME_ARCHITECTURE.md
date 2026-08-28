# 📦 UGREEN DXP2800 Storage Tiering & Docker NVMe Engine: Single Source of Truth

> **Context**: Production storage tiering architecture separating high-IOPS stateless container engines from high-capacity cold media storage on the UGREEN DXP2800 NAS.  
> **Status**: 🟢 **Active & Verified**  
> **NVMe Tier (`/volume2`)**: 4TB WD_BLACK SN850X NVMe SSD (`/volume2/@docker` + `/volume2/docker`)  
> **CMR HDD Tier (`/volume1`)**: 10TB Seagate IronWolf CMR SATA HDD (`/volume1/data` + SMB Shares)  
> **Last Verified**: 2026-08-27 23:35 PDT

---

## 1. Storage Tiering & TBW Protection Matrix

```mermaid
flowchart TD
    subgraph NVMe["Volume 2: 4TB WD_BLACK SN850X NVMe SSD (7,000 MB/s & Silent)"]
        DockerRoot["/volume2/@docker\n• Docker Engine Base Images\n• Overlay2 Rootfs Containers\n• Ephemeral Temp Layers (23 GB)"]
        AppConfigs["/volume2/docker/\n• radarr.db, sonarr.db, tautulli.db\n• plex databases & metadata\n• vaultwarden vault (1.6 GB)"]
    end

    subgraph CMR["Volume 1: 10TB Seagate IronWolf CMR HDD (Cold Mass Storage)"]
        MediaFiles["/volume1/data/media/\n• Movies & TV Video Files (1.1 TB)"]
        Torrents["/volume1/data/torrents/\n• Incomplete & Complete Downloads"]
        PersonalShares["/volume1/personal_folder/ & /volume1/yellowstone/\n• macOS Finder SMB Archives"]
    end

    DockerRoot -->|"Lightning-Fast <500ms Container Starts"| AppConfigs
    AppConfigs -->|"Atomic Hardlink Mounts (0 TBW on SSD)"| MediaFiles
```

---

## 2. Resource Utilization & Space Audit

```text
┌────────────────────────────┬─────────────────────────────┬──────────────────────────────────┐
│ Storage Tier / Volume      │ Allocated Data              │ Space Used / Total Capacity      │
├────────────────────────────┼─────────────────────────────┼──────────────────────────────────┤
│ **NVMe SSD (`/volume2`)**  │ Docker Engine + App Configs │ **15 GB Used** / **3.7 TB Free** │
│ **CMR HDD (`/volume1`)**   │ Video Media + SMB Shares    │ **1.1 TB Used** / **8.1 TB Free** │
└────────────────────────────┴─────────────────────────────┴──────────────────────────────────┘
```

### Key Architectural Wins:
1. **Zero Mechanical Disk Thrashing:** All Docker image pulls, layer extractions, database journal commits (WAL), and container restarts run exclusively on NVMe in `<25ms`.
2. **SSD Endurance (TBW) Preservation:** Video torrent downloads and media files write directly to `/volume1/data`, completely bypassing the NVMe drive to protect flash write endurance.
3. **Atomic Hardlinks:** Sonarr/Radarr and qBittorrent create zero-byte instant hardlinks across `/volume1/data/torrents` and `/volume1/data/media` on the CMR filesystem.
