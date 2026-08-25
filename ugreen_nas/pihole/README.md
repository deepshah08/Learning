# 🛡️ High-Availability Dual Pi-hole (UGREEN NAS Secondary Node) — Single Source of Truth

> **Context**: High-Availability redundant DNS ad-blocking paired with primary Pi-hole on Raspberry Pi 5.  
> **Host**: UGREEN DXP2800 (`192.168.1.80`)  
> **Status**: 🟢 **Production Active** (100% DNS Redundancy Verified)  
> **Sync Engine**: Gravity-Sync daemon running on Pi 5 (30-minute automated synchronization)

---

## 1. Network Profile & Endpoints

| Parameter | Value | Details |
| :--- | :--- | :--- |
| **Primary DNS Node** | `192.168.1.92:53` | Raspberry Pi 5 (Pi-hole v6 FTL) |
| **Secondary DNS Node** | `192.168.1.80:53` | UGREEN DXP2800 (Docker Pi-hole) |
| **Secondary Web Admin** | [http://192.168.1.80:8089/admin](http://192.168.1.80:8089/admin) | Password: `S#@#j0k3R` |
| **Upstream DNS** | `1.1.1.1`, `1.0.0.1` | Cloudflare DNS-over-HTTPS fallback |
| **Sync Interval** | Every 30 minutes | Replicates blocklists, whitelists, regex, custom DNS |

---

## 2. Zero-Outage Architecture

```mermaid
flowchart TD
    subgraph Household["Household Clients (Laptops, Phones, Smart TVs)"]
        Client["Client Device"]
    end

    subgraph Primary["Primary DNS (Raspberry Pi 5)"]
        Pi5["Pi-hole v6 FTL\n192.168.1.92:53"]
    end

    subgraph Secondary["Secondary DNS (UGREEN DXP2800)"]
        NAS["Docker Pi-hole\n192.168.1.80:53"]
    end

    Client -->|Primary Query| Pi5
    Client -.->|Failover / Backup Query (0ms outage)| NAS
    Pi5 <==|Automated Gravity-Sync (30m)| NAS
```

---

## 3. Automated Gravity-Sync Mechanism

The Raspberry Pi 5 maintains a cron script at `/usr/local/bin/sync-pihole-to-nas.sh` that securely pushes `gravity.db` to the NAS and reloads lists:

```bash
#!/bin/bash
set -e
# Replicate gravity.db to UGREEN NAS Secondary Pi-hole
ssh -o BatchMode=yes -o StrictHostKeyChecking=accept-new -i /home/deepshah08/.ssh/id_ed25519 "Deep Shah"@192.168.1.80 "echo S#@#j0k3R | sudo -S tee /volume1/docker/pihole/etc-pihole/gravity.db > /dev/null" < /etc/pihole/gravity.db
ssh -o BatchMode=yes -o StrictHostKeyChecking=accept-new -i /home/deepshah08/.ssh/id_ed25519 "Deep Shah"@192.168.1.80 "docker exec pihole pihole reloadlists"
```

---

## 4. Verification Commands

```bash
# Verify DNS query on Secondary node
dig @192.168.1.80 google.com +short

# Verify Ad-block on Secondary node (returns 0.0.0.0)
dig @192.168.1.80 googleads.g.doubleclick.net +short
```
