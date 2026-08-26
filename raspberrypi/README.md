# 🖥️ Raspberry Pi 5: System & Hardware Single Source of Truth

> **Context**: Hardware profile, network management, OS stability tuning, known hardware quirks, and full portfolio of implemented and tested software services on the Raspberry Pi 5 server.  
> **Host**: `raspberrypi` (`192.168.1.92` / Tailscale `100.68.196.14`)  
> **Hardware**: Raspberry Pi 5 Model B (Broadcom BCM2712, 16GB RAM)  
> **OS**: Debian GNU/Linux 13 (Trixie/Bookworm aarch64, Kernel 6.18)  
> **Status**: 🟢 **Production (24/7 Active & Synchronized)**  
> **Repository**: [`deepshah08/raspberry-pi-5-ecosystem`](https://github.com/deepshah08/raspberry-pi-5-ecosystem)  

---

## 1. Network Profile & Access Endpoints

| Parameter | Value | Details |
| :--- | :--- | :--- |
| **Wi-Fi SSID** | `Rimjhim` | Password: `Restlessinsect` |
| **LAN IPv4** | `192.168.1.92` | Static / Reserved on Home Subnet |
| **Tailscale IPv4** | `100.68.196.14` | Node Name: `pi5-media-nas` |
| **Default Gateway** | `192.168.1.254` | AT&T Fiber Gateway BGW210/320 |
| **SSH User** | `deepshah08` | Primary administrator (`sudo` enabled) |
| **Root Storage** | 117GB MicroSD | ~11GB used (10%), ~101GB available |
| **System RAM** | 16GB LPDDR4X | Dedicated to core network, RAG, and automation services |
| **GPU / Video Decode**| `/dev/dri/renderD128` | Broadcom VideoCore VII DRM |

---

## 2. Stability Hardening & Sleep Prevention (Permanently Configured)

### 1. Wi-Fi Power Management (Disabled Globally)
- **Problem**: Raspberry Pi OS defaults to 802.11 power saving (`power_save = on`). After several hours of inactivity, the Broadcom Wi-Fi module went to sleep and dropped ARP response packets, causing the Pi to appear offline despite a solid green power LED.
- **Permanent Solution**: Configured `/etc/NetworkManager/conf.d/disable-wifi-powersave.conf`:
  ```ini
  [connection]
  wifi.powersave = 2
  ```
  *(Value `2` enforces `NM_SETTING_WIRELESS_POWERSAVE_DISABLE` across all Wi-Fi profiles).*
- **Verified via CLI**: `sudo iw dev wlan0 get power_save` ➔ `Power save: off`.

### 2. Kernel IP Forwarding (Active & Persistent)
- **Problem**: Docker containers, Subnet Routing (`192.168.1.0/24`), and Tailscale Exit Node functions require packet forwarding between network adapters.
- **Permanent Solution**: Configured `/etc/sysctl.d/99-tailscale.conf`:
  ```ini
  net.ipv4.ip_forward = 1
  net.ipv6.conf.all.forwarding = 1
  ```
- **Verified via CLI**: `cat /proc/sys/net/ipv4/ip_forward` ➔ `1`.

---

## 3. Proven Bug Resolutions & Engineering Log

### Incident 001: Wi-Fi Password Update & NetworkManager Stale Profile
- **What Happened**: Wi-Fi password was changed on the home router. Running `sudo nmcli dev wifi connect "Rimjhim" password "..."` threw a `property is missing` error.
- **Root Cause**: NetworkManager already had a saved connection profile named `"Rimjhim"` with the old credentials, causing conflict.
- **Solution**: Delete the stale profile and reconnect:
  ```bash
  sudo nmcli connection delete "Rimjhim"
  sudo nmcli device wifi connect "Rimjhim" password "Restlessinsect"
  ```

### Incident 002: Offloading Media Stack to UGREEN DXP2800
- **What Happened**: Software transcoding 4K HDR media on ARM saturated the Broadcom BCM2712 CPU at 100%.
- **Solution**: Promoted Plex and *Arr stack to UGREEN DXP2800 with Intel QuickSync GPU passthrough. Pi 5 is dedicated to Pi-hole v6 DNS ad-blocking, local AI/RAG pipelines, workflow automation, and security monitoring.

---

## 4. Pi 5 Projects Portfolio & Documentation Index

All 16 active Pi 5 projects have been implemented, tested (68/68 passing automated pytest tests), and documented:

| Project | Domain | Key Files / Ports | Documentation |
| :--- | :--- | :--- | :--- |
| **01. Offline Socratic Tutor** | Education / RAG | `graph_engine.py`, `agent.py` | [offline_tutor/README.md](offline_tutor/README.md) |
| **02. Git-Backed Second Brain** | PKM / Search | `ingest.py`, `search.py` | [second_brain/README.md](second_brain/README.md) |
| **03. WhisperX Meeting Indexer** | Audio / Search | `transcribe.py`, `indexer.py` | [whisper_indexer/README.md](whisper_indexer/README.md) |
| **04. Immich Photo Staging** | Photos / Cloud | `immich_config.py` | [immich/README.md](immich/README.md) |
| **05. Jellyfin Media Server** | Media Streaming | Port `8096` | [jellyfin/README.md](jellyfin/README.md) |
| **06. Voice Clone TTS Sandbox** | Audio / ML | `voice_clone.py` | [voice_clone/README.md](voice_clone/README.md) |
| **07. Backup Engine & Pixel Guard** | Storage / DR | `pixel1_sync_guard.py` | [backup_engine/README.md](backup_engine/README.md) |
| **08. TripDrop Staging Portal** | Transfers | Port `8088` (`server.py`) | [trip_drop/README.md](trip_drop/README.md) |
| **09. Stirling-PDF Utility** | Productivity | Port `8083` | [stirling_pdf/README.md](stirling_pdf/README.md) |
| **10. Intrusion Monitor** | Security | `monitor.py` (Scapy) | [intrusion_monitor/README.md](intrusion_monitor/README.md) |
| **11. Dead Man's Switch** | Cryptography | `daemon.py` ({521}$ Shamir) | [deadmans_switch/README.md](deadmans_switch/README.md) |
| **12. Pi-hole v6 Primary DNS** | Network | Ports `53`, `80`, `443` | [pihole/README.md](pihole/README.md) |
| **13. n8n Workflow Automation** | Automation | Port `5678` | [n8n/README.md](n8n/README.md) |
| **14. Market Sentiment Tracker** | Finance / RAG | `sentiment_analyzer.py` | [market_sentiment/README.md](market_sentiment/README.md) |
| **15. Financial Pipeline** | Analytics | `portfolio_tracker.py` | [financial_pipeline/README.md](financial_pipeline/README.md) |
| **16. Morning Briefing Generator**| Productivity | `main.py` (Daily Digest) | [morning_briefing/README.md](morning_briefing/README.md) |
