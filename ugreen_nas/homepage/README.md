# 📊 Homepage Dashboard (UGREEN DXP2800) — Single Source of Truth

> **Context**: Unified homelab control center and service status dashboard for Deep and Pranali.  
> **Host**: UGREEN DXP2800 (`192.168.1.80`)  
> **Status**: 🟢 **Operational & Production Verified**  
> **Dashboard URL**: [http://192.168.1.80:3000](http://192.168.1.80:3000)  

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

## 2. Docker Compose Configuration

```yaml
services:
  homepage:
    image: ghcr.io/gethomepage/homepage:latest
    container_name: homepage
    environment:
      - PUID=1000
      - PGID=10
      - TZ=America/Los_Angeles
    ports:
      - "3000:3000"
    volumes:
      - /volume1/docker/homepage/config:/app/config
      - /var/run/docker.sock:/var/run/docker.sock:ro
    restart: unless-stopped
```
