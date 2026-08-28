# 📊 Homepage Dashboard (UGREEN DXP2800) — Single Source of Truth

> **Context**: Unified homelab control center and service status dashboard for Deep and Pranali.  
> **Host**: UGREEN DXP2800 (`192.168.1.80`)  
> **Status**: 🟢 **Operational & Production Verified (HTTP 200 OK)**  
> **Dashboard URL**: [http://192.168.1.80:3000](http://192.168.1.80:3000)  
> **Last Verified**: 2026-08-28 15:24 PDT

---

## 1. Integrated Service Catalog

```text
├── Media
│   ├── Plex (Port 32400)
│   ├── Overseerr (Port 5055)
│   ├── Tautulli (Port 8181)
│   └── Bazarr (Port 6767)
├── Downloads & Automation
│   ├── qBittorrent (Port 8080 - Live speed widgets)
│   ├── Radarr (Port 7878 - Live queue widget)
│   ├── Sonarr (Port 8989 - Live queue widget)
│   └── Prowlarr (Port 9696)
├── Network & Security
│   ├── Primary Pi-hole (192.168.1.92)
│   ├── Secondary Pi-hole (192.168.1.80:8089)
│   └── Vaultwarden (Port 8085)
└── UGREEN Native Storage
    ├── UGOS Control Panel (Port 9999)
    ├── UGREEN Photos (Native AI face/scene recognition)
    └── UGREEN Online Office (OnlyOffice editor)
```

---

## 2. Docker Compose Configuration (NVMe Tiered)

```yaml
services:
  homepage:
    image: ghcr.io/gethomepage/homepage:latest
    container_name: homepage
    environment:
      - PUID=1000
      - PGID=10
      - TZ=America/Los_Angeles
      - HOMEPAGE_ALLOWED_HOSTS=192.168.1.80:3000,192.168.1.80,localhost:3000,localhost,127.0.0.1:3000,127.0.0.1,pi5-media-nas,deepdxp2800,*.local
    ports:
      - "3000:3000"
    volumes:
      - /volume2/docker/homepage/config:/app/config
      - /var/run/docker.sock:/var/run/docker.sock:ro
    restart: unless-stopped
```

---

## 3. Host Validation Troubleshooting Runbook

In Homepage v0.9+, strict host header validation is enforced to prevent DNS rebinding attacks:
* If you see `{"error":"Host validation failed. See logs for more details."}`, ensure `HOMEPAGE_ALLOWED_HOSTS` contains the host/port you are accessing (e.g. `192.168.1.80:3000,192.168.1.80`).
