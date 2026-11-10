# 🔀 Caddy Reverse Proxy — UGREEN DXP2800

> **Purpose**: Maps friendly `.nas` hostnames to all homelab services. No port numbers needed.
> **Host**: UGREEN DXP2800 (`192.168.1.80`)
> **Listens on**: Port `80` (HTTP only — local network, no HTTPS needed)
> **Config on NAS**: `/volume2/docker/caddy/Caddyfile`

---

## URL Map

| Friendly URL | Service | Old URL |
|---|---|---|
| `http://home.nas` | Homepage Dashboard | `192.168.1.80:3000` |
| `http://movies.nas` | Overseerr / Seerr | `192.168.1.80:5055` |
| `http://radarr.nas` | Radarr (Movies) | `192.168.1.80:7878` |
| `http://sonarr.nas` | Sonarr (TV) | `192.168.1.80:8989` |
| `http://prowlarr.nas` | Prowlarr (Indexers) | `192.168.1.80:9696` |
| `http://bazarr.nas` | Bazarr (Subtitles) | `192.168.1.80:6767` |
| `http://torrents.nas` | qBittorrent | `192.168.1.80:8080` |
| `http://tautulli.nas` | Tautulli (Stats) | `192.168.1.80:8181` |
| `http://pihole.nas` | Secondary Pi-hole | `192.168.1.80:8089` |
| `http://plex.nas` | Plex Media Server | `192.168.1.80:32400` |

---

## 🚀 Deployment Steps

### 1. SSH into the NAS
```bash
ssh deep@192.168.1.80
```

### 2. Create the config directory on NVMe and copy the Caddyfile
```bash
mkdir -p /volume2/docker/caddy/{data,config}
# Copy Caddyfile from your Mac (run on Mac):
scp ~/Desktop/DATA\ ORG/Learning/ugreen_nas/caddy/Caddyfile deep@192.168.1.80:/volume2/docker/caddy/Caddyfile
```

### 3. Deploy Caddy
```bash
# On the NAS — copy the compose file first (run on Mac):
scp ~/Desktop/DATA\ ORG/Learning/ugreen_nas/caddy/docker-compose.yml deep@192.168.1.80:/volume2/docker/caddy/docker-compose.yml

# Then on the NAS:
cd /volume2/docker/caddy
docker compose up -d
docker logs caddy --tail 20
```

### 4. Verify Caddy is up
```bash
# On NAS:
curl -I http://localhost/  # Should get response (even 404 is fine — means Caddy is alive)
docker ps | grep caddy
```

---

## 🌐 Pi-hole DNS Records (do this once)

Add these in **Pi-hole Admin → Local DNS → DNS Records** on both Pi-hole instances:

| Domain | IP |
|--------|----|
| `home.nas` | `192.168.1.80` |
| `movies.nas` | `192.168.1.80` |
| `radarr.nas` | `192.168.1.80` |
| `sonarr.nas` | `192.168.1.80` |
| `prowlarr.nas` | `192.168.1.80` |
| `bazarr.nas` | `192.168.1.80` |
| `torrents.nas` | `192.168.1.80` |
| `tautulli.nas` | `192.168.1.80` |
| `pihole.nas` | `192.168.1.80` |
| `plex.nas` | `192.168.1.80` |

> Primary Pi-hole: http://192.168.1.92/admin
> Secondary Pi-hole: http://192.168.1.80:8089/admin

---

## ⚠️ Troubleshooting

**Port 80 conflict?**
UGOS Pro should not use port 80, but verify with:
```bash
ss -tlnp | grep ':80 '
```
If something else is on port 80, change Caddy's host port in `docker-compose.yml` to e.g. `8888:80` and add DNS CNAME records pointing to `192.168.1.80:8888`.

**Homepage returning 403?**
Caddy's hostname will appear in requests. If Homepage blocks it, add `home.nas` to `HOMEPAGE_ALLOWED_HOSTS` in the homepage docker-compose env var.

**Reload config without restart:**
```bash
docker exec caddy caddy reload --config /etc/caddy/Caddyfile
```

**Add a new service:**
Append to Caddyfile:
```
http://newservice.nas {
    reverse_proxy localhost:PORT
}
```
Then reload: `docker exec caddy caddy reload --config /etc/caddy/Caddyfile`
