# 🛡️ Unbound Recursive DNS Server & Root DNSSEC Validator (Raspberry Pi 5)

> **Context**: Private, in-memory recursive root DNS resolver validating DNSSEC signatures and answering Pi-hole v6 FTL queries on loopback port `5335`.  
> **Status**: 🟢 **Production / Active (24/7)**  
> **Host**: Raspberry Pi 5 (`192.168.1.92`) | Port: `127.0.0.1#5335`  
> **Upstream Mode**: Zero Third-Party DNS Upstreams (Direct Root Anchors)  

---

## 1. Architecture Overview

```mermaid
flowchart TD
    Client["LAN Clients (Phones / Laptops / TVs)"] -->|Port 53 DNS| Pihole["Pi-hole v6 FTL (192.168.1.92:53)"]
    Pihole -->|Adlist Filtering (309,418 domains)| BlockCheck{"Is Domain in Blocklist?"}
    BlockCheck -->|Yes| Blocked["Return 0.0.0.0 (Ad/Tracker Blocked)"]
    BlockCheck -->|No| Unbound["Unbound Root Resolver (127.0.0.1:5335)"]
    
    Unbound -->|Iterative Query 1| RootDNS["Root Nameservers (.)"]
    RootDNS -->|Referral| TLD["TLD Nameservers (.com / .org)"]
    TLD -->|Referral| AuthDNS["Authoritative Nameservers"]
    AuthDNS -->|DNSSEC Verified Answer| Unbound
    Unbound -->|Cached Validated IP| Pihole
    Pihole -->|Response| Client
```

---

## 2. Key Technical Configurations

- **Configuration File**: `/etc/unbound/unbound.conf.d/pi-hole.conf`
- **Socket**: `interface: 127.0.0.1`, `port: 5335` (isolated to loopback, no external port exposure).
- **Privacy & Hardening**:
  - `harden-dnssec-stripped: yes`
  - `harden-glue: yes`
  - `edns-buffer-size: 1232`
  - `prefetch: yes`
  - `qname-minimisation: yes`
  - Private subnet boundary filters (`192.168.0.0/16`, `10.0.0.0/8`, `172.16.0.0/12`, `fd00::/8`).

---

## 3. Verified Validation Runbook

```bash
# 1. Verify Unbound Service Status
sudo systemctl status unbound

# 2. Test DNSSEC Rejection on Bogus Signature (Must return SERVFAIL)
dig @127.0.0.1 -p 5335 sigfail.verteiltesysteme.net

# 3. Test DNSSEC Acceptance on Valid Signature (Must return NOERROR + IP)
dig @127.0.0.1 -p 5335 sigok.verteiltesysteme.net +short

# 4. Test End-to-End Resolution through Pi-hole (Port 53)
dig @127.0.0.1 -p 53 google.com +short
dig @127.0.0.1 -p 53 doubleclick.net +short  # returns 0.0.0.0
```
