# 📸 Project 04: Immich Photo Staging & Sync (Raspberry Pi 5)

> **Context**: Photo ingestion and staging orchestrator configuring Docker bindings and NAS sync pipelines for media vaults.  
> **Status**: 🟢 **Production / Tested** (Note: Native UGOS AI handles primary NAS photo library).  
> **Host**: Raspberry Pi 5 (`192.168.1.92`)  
> **Repository**: [`deepshah08/raspberry-pi-5-ecosystem/projects/04-immich`](https://github.com/deepshah08/raspberry-pi-5-ecosystem/tree/main/projects/04-immich)  

---

## 1. Key Components

- **Configuration (`immich_config.py` & `config.py`)**: Manages upload and database directory bindings across local Pi and NAS mounts (`/mnt/nas/media_vault`).
- **Path Validator (`validate_config.py`)**: Confirms target mount availability and directory health before container startup.

## 2. Verified Functionality & Test Suite

- `projects/04-immich/tests/test_immich.py`: Validates binding dictionary schema and configuration validation routines.
- **Test Results**: 2/2 passing tests.
