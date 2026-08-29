# 📊 Homepage Dashboard (UGREEN DXP2800) — Single Source of Truth

> **Context**: Unified homelab control center and service status dashboard for Deep and Pranali.  
> **Host**: UGREEN DXP2800 (`192.168.1.80`)  
> **Status**: 🟢 **Operational & Production Verified (HTTP 200 OK)**  
> **Dashboard URL**: [http://192.168.1.80:3000](http://192.168.1.80:3000)  
> **Theme**: Pure AMOLED / OLED Solid Black (`#000000`)  
> **Layout**: Vertical Columns (`style: column`)  
> **Last Verified**: 2026-08-28 17:42 PDT

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

## 2. Configuration (`settings.yaml` & `custom.css`)

### `/volume2/docker/homepage/config/settings.yaml`:
```yaml
title: Deep & Pranali HomeLab
theme: dark
color: slate
layout:
  Media:
    style: column
  Downloads & Automation:
    style: column
  Network & Security:
    style: column
  UGREEN Native Storage:
    style: column

allowHosts:
  - "192.168.1.80:3000"
  - "192.168.1.80"
  - "localhost:3000"
  - "localhost"
  - "127.0.0.1:3000"
  - "127.0.0.1"
```

### `/volume2/docker/homepage/config/custom.css` (Pure Solid Black):
```css
body {
  background-color: #000000 !important;
}
```

---

## 3. Quick-Toggle Layout Runbook (Columns vs. Rows)

* **To switch to Horizontal Rows Layout:**
  ```bash
  ssh nas "sed -i 's/style: column/style: row\n    columns: 4/g' /volume2/docker/homepage/config/settings.yaml && docker restart homepage"
  ```

* **To switch to Vertical Columns Layout:**
  ```bash
  ssh nas "sed -i '/columns: 4/d; s/style: row/style: column/g' /volume2/docker/homepage/config/settings.yaml && docker restart homepage"
  ```
