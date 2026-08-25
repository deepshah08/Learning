# 🔐 Vaultwarden (UGREEN DXP2800) — Single Source of Truth

> **Context**: Lightweight, end-to-end encrypted Bitwarden-compatible password manager for Deep and Pranali.  
> **Host**: UGREEN DXP2800 (`192.168.1.80`)  
> **Status**: 🟢 **Operational & Production Verified**  
> **Web UI**: [http://192.168.1.80:8085](http://192.168.1.80:8085)  
> **WebSocket Push**: Port `3012`  

---

## 1. Features & Configuration

1. **Private Vaults**: Deep and Pranali maintain distinct private encrypted password vaults.
2. **Shared Family Organization**: Shared collections for joint services (Wi-Fi passwords, streaming accounts, leases, utility bills).
3. **Clients Supported**: Bitwarden browser extensions (Chrome, Safari, Firefox), macOS Desktop app, iOS App, and Android App.

---

## 2. Docker Compose Configuration

```yaml
services:
  vaultwarden:
    image: vaultwarden/server:latest
    container_name: vaultwarden
    restart: unless-stopped
    environment:
      - WEBSOCKET_ENABLED=true
      - SIGNUPS_ALLOWED=true
      - INVITATIONS_ALLOWED=true
      - SHOW_PASSWORD_HINT=false
      - DOMAIN=http://192.168.1.80:8085
    volumes:
      - /volume1/docker/vaultwarden/data:/data
    ports:
      - "8085:80"
      - "3012:3012"
```
