# 🎬 Plex & *Arr Stack (Raspberry Pi 5) — Legacy Archive

> [!NOTE]  
> **Status: Migrated to UGREEN DXP2800**  
> The 8-service media stack has been promoted to the **UGREEN DXP2800 NAS** for Intel QuickSync hardware transcoding and zero-copy atomic hardlinks on the 10TB IronWolf CMR volume.  
> See the active production Single Source of Truth at: [ugreen_nas/arr_stack/README.md](../../ugreen_nas/arr_stack/README.md).

---

## 1. Historical Architecture (Pi 5)
* **Host**: Raspberry Pi 5 (16GB RAM)
* **Replaced Services**: Plex, Prowlarr, Radarr, Sonarr, qBittorrent, Bazarr, Overseerr, Tautulli.
* **Pi 5 Re-allocation**: Pi 5 is now dedicated to whole-home DNS filtering (**Pi-hole v6**), high availability, and network services.