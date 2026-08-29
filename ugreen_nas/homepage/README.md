# 📊 Homepage Dashboard (UGREEN DXP2800) — Single Source of Truth

> **Context**: Unified homelab control center and service status dashboard for Deep and Pranali.  
> **Host**: UGREEN DXP2800 (`192.168.1.80`)  
> **Status**: 🟢 **Operational & Production Verified (HTTP 200 OK / All Widgets Green)**  
> **Dashboard URL**: [http://192.168.1.80:3000](http://192.168.1.80:3000)  
> **Theme**: Pure AMOLED / OLED Solid Black (`#000000`)  
> **Layout**: Vertical Columns (`style: column`)  
> **Last Verified**: 2026-08-28 17:46 PDT

---

## 1. Integrated Service Catalog

```text
├── Media (Column 1)
│   ├── Plex (Port 32400)
│   ├── Overseerr (Port 5055)
│   ├── Tautulli (Port 8181)
│   └── Bazarr (Port 6767)
├── Downloads & Automation (Column 2)
│   ├── qBittorrent (Port 8080 - Live speed widgets)
│   ├── Radarr (Port 7878 - Live queue widget)
│   ├── Sonarr (Port 8989 - Live queue widget)
│   └── Prowlarr (Port 9696)
├── Network & Security (Column 3)
│   ├── Primary Pi-hole (192.168.1.92)
│   ├── Secondary Pi-hole (192.168.1.80:8089)
│   └── Vaultwarden (Port 8085)
└── UGREEN Native Storage (Column 4)
    ├── UGOS Control Panel (Port 9999)
    ├── UGREEN Photos (Native AI face/scene recognition)
    └── UGREEN Online Office (OnlyOffice editor)
```

---

## 2. Docker Compose Configuration (NVMe Tiered with Disk Monitors)

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
      - /volume1:/volume1:ro
      - /volume2:/volume2:ro
    restart: unless-stopped
```

---

## 3. Storage & API Widget Configuration

### `/volume2/docker/homepage/config/widgets.yaml`:
```yaml
- logo:
    type: logo
- search:
    provider: google
    target: _blank
- resources:
    cpu: true
    memory: true
    disk:
      - /volume1
      - /volume2
```

### `/volume2/docker/homepage/config/custom.css` (Pure Solid Black & Clean Locked UI):
```css
body {
  background-color: #000000 !important;
}

#footer,
.footer,
div[id*="footer"] {
  display: none !important;
  visibility: hidden !important;
  opacity: 0 !important;
  pointer-events: none !important;
}
```
