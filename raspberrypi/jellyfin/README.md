# 🎬 Project 05: Jellyfin Media Server Profile (Raspberry Pi 5)

> **Context**: Lightweight ARM64 media streaming configuration with V4L2/DRM hardware acceleration hooks, serving as secondary streaming fallback to primary Plex on NAS.  
> **Status**: 🟢 **Operational / Tested**  
> **Host**: Raspberry Pi 5 (`192.168.1.92`) | Port: `8096`  
> **Repository**: [`deepshah08/raspberry-pi-5-ecosystem/projects/05-jellyfin`](https://github.com/deepshah08/raspberry-pi-5-ecosystem/tree/main/projects/05-jellyfin)  

---

## 1. Key Components

- **Compose Stack (`docker-compose.jellyfin.yml`)**: Mounts VideoCore VII DRM (`/dev/dri`) and NAS media paths (`/mnt/nas/media_vault`).
- **Setup Validator (`validate_setup.py`)**: Verifies hardware acceleration devices and volume bindings.

## 2. Verified Functionality & Test Suite

- `tests/test_jellyfin_config.py`: Validates docker compose syntax, required service definitions, and GPU device nodes.
- **Test Results**: 4/4 passing tests.
