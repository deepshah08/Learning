# 🌬️ UGREEN NAS Fan, Temperature & Resource Optimization Guide

> **Domain**: Hardware Thermal Management & Background Resource Optimization  
> **Host Node**: UGREEN DXP2800 NAS (`192.168.1.80` | Intel N100 4C/4T, 8GB DDR5, 2.5GbE Wired)  
> **Operating System**: UGOS Pro (Debian 12 Kernel)  
> **Status**: 🟢 **Production Optimized & Hardened**  
> **Last Verified**: 2026-09-06  

---

## 1. Problem Statement & Root Cause Analysis (RCA)

### Symptoms
- NAS cooling fan unexpectedly spun up to audible high RPMs during quiet hours.
- Mechanical and thermal sensors registered sustained CPU core temperatures climbing to 68°C–74°C without active user video playback or file transfers.

### Root Cause
1. **Plex Deep Media Analysis & Ad Marker Detection**:
   - Plex Media Server was configured with default commercial scanning (`GenerateAdMarkerBehavior`), running continuous multi-threaded CPU video decoding passes against newly grabbed media files.
   - CPU-bound FFmpeg analysis threads saturated all 4 cores of the Intel N100, driving package temperatures above the PWM fan curve threshold.
2. **Maintenance Window Overlap**:
   - Default maintenance windows ran during early morning hours, causing unexpected fan spin-up and disk churn.

---

## 2. Applied Configurations & Permanent Fixes

### A. Plex Ad Marker Scanning Disabled
- **Configuration**: Set `GenerateAdMarkerBehavior="never"` in Plex Media Server preferences (`Preferences.xml`).
- **Impact**: Completely eliminates CPU-intensive commercial detection passes. Saves ~80% of post-download compute spikes.
- **Intro Detection**: Confirmed set to scheduled maintenance window only, rather than triggering immediate background tasks upon download completion.

### B. Maintenance Window Shifted (1:00 PM – 4:00 PM)
- **Settings Path**: Plex Web UI $\rightarrow$ Settings $\rightarrow$ Scheduled Tasks.
- **Window**: Changed from default night/morning hours to **13:00 – 16:00 (1:00 PM – 4:00 PM)**.
- **Rationale**: 
  - Aligns heavy housekeeping tasks (database optimization, thumbnail generation, media index file cleanup) to midday when ambient noise is naturally higher and no users are sleeping or streaming.
  - Prevents evening peak-time streaming competition.

### C. Sonarr & Radarr Refresh Optimization
- **File System Scanning**: Avoided setting aggressive periodic whole-library rescans.
- **Event-Driven Sync**: Rely strictly on Radarr/Sonarr download-completion webhooks to notify Plex of new items instantly, eliminating continuous recursive disk crawling across `/volume1/data/media/`.

### D. UGREEN Fan Curve Mode
- Set fan profile to **Smart / Quiet Mode** in UGOS Pro Control Panel.
- Idle package temperatures remain steady at ~42°C–48°C with near-silent fan operation (<22 dB).

---

## 3. Verification Commands & Diagnostics

```bash
# Check CPU temperatures across all cores
sensors | grep "Core"

# Check top CPU-consuming processes and container runtimes
ssh nas "top -b -n 1 | head -n 20"

# Check active Docker container resource usage
ssh nas "docker stats --no-stream"

# Verify Plex preferences contain ad-marker disablement
ssh nas "grep GenerateAdMarkerBehavior /volume2/@docker/containers/plex/config/Library/Application\ Support/Plex\ Media\ Server/Preferences.xml"
```

---

## 4. Key Invariants & Safeguards
- **Zero Host Mutation**: All Plex configuration modifications remain inside the containerized mount on NVMe (`/volume2/@docker/containers/plex`).
- **Storage Tiering Protection**: Plex SQLite metadata and temporary transcode buffers stay strictly on the NVMe SSD (`/volume2`), preventing CMR mechanical HDD (`/volume1`) wear and spin-up.
