# Homelab Friendly Domain Routing & Media Queue Resolution Investigation

> Companion: durable architecture at [./homelab_friendly_routing_and_media_knowledge.md](./homelab_friendly_routing_and_media_knowledge.md)  
> Date: 2026-11-09 | Status: Resolved | Target: UGREEN DXP2800 (`192.168.1.80`), Raspberry Pi 5 (`192.168.1.92`)

---

## 1. Trigger

The user was setting up a TV with Plex and inquired about signing in and discovering media. Following this, the user requested an easy way to access their homelab homepage and services (Radarr, Sonarr, Overseerr, etc.) via human-readable domain names instead of raw IP addresses and ports, while also reporting that a newly queued movie (*3 Idiots*, 2009) appeared in Radarr but was stalled and not downloading.

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                               SESSION OBJECTIVES & CHALLENGES                          │
├──────────────────────────┬─────────────────────────────────────────────────────────────┤
│ Media Ingestion Stalled  │ "3 Idiots" monitored in Radarr but queue stayed 0; no grab. │
│ URL Usability Gap        │ Services bound to raw IP (192.168.1.80) & disparate ports.  │
│ Port 80 OS Conflict      │ UGOS Pro host nginx binds 0.0.0.0:80/443 (HTTP 307 to :9999)│
│ Dual Pi-hole HA Drift    │ Local DNS needed 1:1 sync across Pi 5 and NAS containers.   │
│ Host Header Rejection    │ Homepage threw 403 when accessed via custom domain names.   │
└──────────────────────────┴─────────────────────────────────────────────────────────────┘
```

---

## 2. Investigation Path

### Track A: Stalled Media Ingestion (*3 Idiots*)

| # | Hypothesis / Approach | What We Found | Outcome |
|---|----------------------|---------------|---------|
| 1 | Prowlarr/Indexers failed or returned 0 results | API release query (`/api/v3/release?movieId=3`) returned 79 distinct releases across TPB and YTS. | Refuted |
| 2 | Radarr automated search was never triggered | Triggered `MoviesSearch` command via API; command succeeded but queue remained at 0 items. | Refuted |
| 3 | Quality profile rejected available releases | Radarr release inspection showed: `Bluray-1080p is not wanted in profile`. The movie was configured with Quality Profile 5 (`Ultra-HD` / 2160p only). Since *3 Idiots* is a 2009 title with only 1080p BluRay/WEBRip masters, all 79 releases were disqualified. | **Confirmed Root Cause** |

**Remediation**:
- Modified movie profile to Quality Profile 4 (`HD-1080p`).
- Re-evaluated indexer reports: instantly yielded 8 approved releases.
- Automated search triggered grab of *3 Idiots 2009 1080p BluRay x264 Hindi AAC -Ozlem* (2.56 GB, 129 seeders).
- Ingested via qBittorrent at 25.8 MB/s, hardlinked into `/volume1/data/media/movies/3 Idiots (2009)/`, and confirmed live in Plex library with 9.4 rating.

---

### Track B: Friendly Homelab Domain Routing (`.nas`)

| # | Hypothesis / Approach | What We Found | Outcome |
|---|----------------------|---------------|---------|
| 1 | Bind Caddy reverse proxy to port 80 on UGREEN NAS | `ss -tlnp` revealed UGOS Pro's native host `nginx` (PID 3714/2626) already listening on `0.0.0.0:80` and `0.0.0.0:443`, redirecting to port 9999. Mutating host nginx violates zero-host-mutation rules. | Refuted (Rejected Path) |
| 2 | Direct Pi-hole Local DNS resolution to NAS IP | Added `address=/<name>.nas/192.168.1.80` via dnsmasq config. Resolves domain names to NAS across entire LAN without host OS changes. | **Confirmed Working** |
| 3 | Pi-hole v6 FTL dynamic reload via CLI | Running `pihole reloaddns` did not reload `/etc/dnsmasq.d` configuration files under Pi-hole v6 FTL without service restart. `systemctl restart pihole-FTL` on Pi 5 activated the entries. | Addressed |
| 4 | Secondary Pi-hole parity on UGREEN NAS | Secondary Pi-hole container had `etc_dnsmasq_d = false` in `/etc/pihole/pihole.toml`. Mounting `/etc/dnsmasq.d` without toggling this flag caused NXDOMAIN on failover. Set `etc_dnsmasq_d = true` and restarted container to achieve 1:1 parity. | **Confirmed Working** |
| 5 | Homepage 403 Forbidden upon domain access | Next.js host header protection in Homepage blocked non-listed hosts. Inspected `HOMEPAGE_ALLOWED_HOSTS` and found only IP and `.local` domains. Appended `*.nas,home.nas:3000,home.nas`. | **Confirmed Working** |

---

## 3. Verification Evidence

### DNS Resolution (Both Nodes Synchronized)
```bash
for domain in home.nas movies.nas radarr.nas sonarr.nas torrents.nas plex.nas; do
    echo "$domain -> Pi5: $(dig @192.168.1.92 $domain +short) | NAS: $(dig @192.168.1.80 $domain +short)"
done
```
Output:
```text
home.nas -> Pi5: 192.168.1.80 | NAS: 192.168.1.80
movies.nas -> Pi5: 192.168.1.80 | NAS: 192.168.1.80
radarr.nas -> Pi5: 192.168.1.80 | NAS: 192.168.1.80
sonarr.nas -> Pi5: 192.168.1.80 | NAS: 192.168.1.80
torrents.nas -> Pi5: 192.168.1.80 | NAS: 192.168.1.80
plex.nas -> Pi5: 192.168.1.80 | NAS: 192.168.1.80
```

### HTTP Service Responses via Friendly Domains
```text
http://home.nas:3000                 -> HTTP 200 OK
http://movies.nas:5055               -> HTTP 307 (Redirect to /login)
http://radarr.nas:7878               -> HTTP 200 OK
http://sonarr.nas:8989               -> HTTP 200 OK
http://torrents.nas:8080             -> HTTP 200 OK
http://plex.nas:32400/web/index.html -> HTTP 200 OK
```

### Media Pipeline Lifecycle
```text
[2026-11-10T02:47:22] grabbed                -> 3 Idiots 2009 1080p BluRay x264 Hindi AAC -Ozlem
[2026-11-10T02:49:00] downloadFolderImported -> /data/media/movies/3 Idiots (2009)/...
[2026-11-10T02:52:16] plexSectionScan        -> Matched: 3 Idiots (2009), 171m, Rating: 9.4
```
