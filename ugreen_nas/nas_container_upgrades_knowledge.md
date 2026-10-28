# UGREEN NAS Container Upgrade Orchestration & I/O Isolation

> Origin: investigation journey at [./nas_container_upgrades_investigation.md](./nas_container_upgrades_investigation.md)
> Scope: Operational standards and upgrade wave architecture for UGREEN DXP2800 NAS.

---

## 1. Role / Position

The UGREEN DXP2800 NAS (`192.168.1.80`) is the storage backbone and secondary DNS authority
in the homelab ecosystem. It runs an asymmetric storage model with dual tiers:
* **NVMe SSD Tier (`/volume2`)**: 4TB WD_BLACK SN850X for Docker engine, databases, and caches.
* **Mechanical CMR HDD Tier (`/volume1`)**: 10TB Seagate IronWolf for bulk media storage.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   UGREEN NAS STORAGE & COMPUTE ENVELOPE                │
├───────────────────────────────────┬────────────────────────────────────┤
│ Intel N100 SoC (4 Cores / 4 Th.)  │ 8 GB DDR5 RAM (Single SODIMM)      │
├───────────────────────────────────┼────────────────────────────────────┤
│ Tier 1: NVMe SSD (/volume2)       │ Hot DBs, Docker roots, SQLite      │
│ Tier 2: Mechanical CMR (/volume1) │ Cold media, 0 RPM hibernation tar. │
└───────────────────────────────────┴────────────────────────────────────┘
```

---

## 2. Upgrade Waves & Sequential Orchestration

Mass container recreation causes simultaneous library scans across `/volume1`, inducing
mechanical thrashing and host daemon starvation. Upgrades MUST follow sequential waves:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                      CONTAINER UPGRADE WAVE PROTOCOL                   │
├─────────┬──────────────────────┬───────────────────────────────────────┤
│ Wave 1  │ Core Infrastructure  │ pihole, vaultwarden, homepage         │
│         │ (NVMe only, zero HDD)│ Verify DNS resolution and web auth    │
├─────────┼──────────────────────┼───────────────────────────────────────┤
│ Wave 2  │ Network & Ingestion  │ qbittorrent, prowlarr, seerr          │
│         │ (Low seek overhead)  │ Allow torrent state check to finish   │
├─────────┼──────────────────────┼───────────────────────────────────────┤
│ Wave 3  │ Media Cataloggers    │ radarr, sonarr, bazarr (1 by 1)       │
│         │ (Heavy HDD metadata) │ Wait for library rescan to complete   │
├─────────┼──────────────────────┼───────────────────────────────────────┤
│ Wave 4  │ Media Core           │ plex, calibre-web, shelfmark          │
│         │ (Deep video/book IO) │ Verify hardware transcode QuickSync   │
└─────────┴──────────────────────┴───────────────────────────────────────┘
```

### Wave Execution Protocol:
1. **Never combine Wave 3 and Wave 4.** Radarr/Sonarr and Plex must never scan `/volume1` at the same time.
2. **Verify settle time before advancing.** Check `iostat` or container CPU/disk metrics before triggering the next wave:
   ```bash
   docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.BlockIO}}"
   ```
3. **Monitor swap pressure.** If swap usage exceeds 1.5GB, pause upgrades until memory buffers flush.

---

## 3. Host System Maintenance Invariants

| Component | Standard | Enforcement Rule |
|-----------|----------|------------------|
| Base OS Packages | UGOS Pro Managed | `sudo apt-get upgrade` is strictly blocked by vendor policy. Never attempt to bypass or force base Debian package upgrades. |
| Firmware Updates | Native Web UI | All OS, kernel, udev, and systemd updates must be performed exclusively via the native UGOS Pro Web UI under System ➔ Firmware Update. |
| SSH Service | Fallback Management | UGOS SSH daemon runs on port 22. If locked or unresponsive, initiate an ACPI short-press shutdown via front power button. |
| SMR CIFS Mount | Network Decoupled | `pi5-smr-mount.service` targets Pi 5 at `//192.168.1.92/smr-archive` with credentials in `/etc/samba/pi5-smr.cred`. |
