# 🌐 Whole-Home 2.5GbE Hardwired DHCP Server & SRE Watchdog

> **Context**: High-performance, low-latency, authoritative whole-home DHCP server running in a containerized environment on the UGREEN DXP2800 NAS, coupled with the Project #31 automated SLO Watchdog Daemon.  
> **Host**: UGREEN DXP2800 NAS (`192.168.1.80` Static | 2.5GbE Hardwired Copper)  
> **Role**: Primary Authoritative DHCP Server + Real-Time SRE Watchdog Sentry  
> **Status**: 🟢 **Production Verified**  
> **Last Verified**: 2026-09-01  

---

## 🏛️ 1. Architecture & Endpoints

| Service | Container Name | Network Mode | Ports Bound | Role / Scope |
| :--- | :--- | :--- | :--- | :--- |
| **Primary DHCP** | `nas_dhcp_server` | `host` | `67/udp` | Primary Split-Scope Pool (`192.168.1.64` – `192.168.1.189`) |
| **SLO Watchdog** | `nas_slo_watchdog` | `host` | None (Outbound Sockets) | Continuous 60s probe of Primary/Secondary DNS & failover logging |

---

## ⚙️ 2. Configuration & Parameter Matrix

### Path: `/volume2/docker/dhcp_server/dnsmasq.conf`
```conf
# DHCP-only Mode: Port 0 completely disables DNS server (zero port 53 conflict with UGOS)
port=0

# Bind to physical 2.5GbE hardwired interface
interface=eth0
bind-interfaces

# DHCP Authoritative Primary Server Configuration
dhcp-authoritative
dhcp-range=192.168.1.64,192.168.1.189,255.255.255.0,24h
dhcp-option=option:router,192.168.1.254
dhcp-option=6,192.168.1.80,192.168.1.92
dhcp-leasefile=/data/dhcp.leases

# Static IP Reservations (Shared with Secondary Node)
dhcp-host=6c:1f:f7:b5:6d:ed,192.168.1.80,DeepDXP2800
dhcp-host=88:a2:9e:a6:ab:c6,192.168.1.92,raspberrypi
dhcp-host=0c:79:55:f9:0d:94,192.168.1.233,TCL-RokuTV
dhcp-host=96:16:6d:8e:4e:c2,192.168.1.98,Pixel9ProXL
```

### Path: `/volume2/docker/dhcp_server/docker-compose.yml`
```yaml
services:
  dhcp-server:
    build: .
    container_name: nas_dhcp_server
    restart: unless-stopped
    network_mode: host
    cap_add:
      - NET_ADMIN
      - NET_BIND_SERVICE
      - NET_RAW
    volumes:
      - ./dnsmasq.conf:/etc/dnsmasq.conf:ro
      - ./data:/data

  slo-watchdog:
    image: alpine:3.20
    container_name: nas_slo_watchdog
    restart: unless-stopped
    network_mode: host
    volumes:
      - ./slo_watchdog.py:/app/slo_watchdog.py:ro
      - ./data:/data
    command: ["sh", "-c", "apk add --no-cache python3 bind-tools >/dev/null && python3 /app/slo_watchdog.py"]
```

---

## 🔍 3. Known Bugs, Quirks & Resolved Solutions

- **Issue**: Docker bridge port mapping (`-p 67:67/udp`) failed to receive client `DHCPDISCOVER` broadcasts.
  - **Root Cause**: Linux bridge networks do not forward Layer 2 Ethernet broadcast frames (`FF:FF:FF:FF:FF:FF`) across subnets.
  - **Fix Applied**: Deployed container in `network_mode: host` with `port=0` (DHCP-only). Disables DNS listener on port 53 completely, avoiding collision with UGOS host `dnsmasq`.
- **Issue**: Elevated CPU temperature (63°C) and fan noise caused by watchdog polling.
  - **Root Cause**: Watchdog was spawning external `dig` process forks every 30s, keeping Intel N100 out of C-state package sleep.
  - **Fix Applied**: Rewrote watchdog to use pure in-memory asynchronous Python UDP sockets (`0.00% CPU`, 0 process forks). CPU temperature dropped to 56°C and fan throttled to silent minimum.

---

## 🛠️ 4. Operational Runbook

```bash
# Check container status
docker ps --filter name=nas_

# View live DHCP leases
cat /volume2/docker/dhcp_server/data/dhcp.leases

# View real-time DHCP lease transactions
docker logs nas_dhcp_server --tail 30 -f

# View SLO Watchdog status & incidents
cat /volume2/docker/dhcp_server/data/incidents.jsonl
```

---

## 🔗 5. References & Cross-Links
- **Master Handoff & Contract**: [`Learning/networking/DNS_NETWORK_HANDOFF.md`](../../networking/DNS_NETWORK_HANDOFF.md)
- **Incident Post-Mortem**: [`Learning/networking/INCIDENT_2026_08_31_DHCP_OUTAGE_RCA.md`](../../networking/INCIDENT_2026_08_31_DHCP_OUTAGE_RCA.md)
- **Secondary Node Runbook**: [`Learning/raspberrypi/pihole/README.md`](../../raspberrypi/pihole/README.md)
