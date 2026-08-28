# 🛡️ Unbound Recursive Root DNS Server & Performance Memory Cache

> **Context**: High-performance, in-memory recursive root DNS resolver and cryptographic DNSSEC validator answering Pi-hole v6 FTL queries on loopback port `5335`. Engineered for zero third-party logging, multi-threaded Pi 5 execution, and burst resilience during heavy cloud syncs.  
> **Status**: 🟢 **Production Grade / Active (24/7)**  
> **Host**: Raspberry Pi 5 (`192.168.1.92`) | Socket: `127.0.0.1#5335`  
> **Dedicated RAM Cache Pool**: **192 MB** (`msg-cache: 64MB` + `rrset-cache: 128MB`)  
> **Upstream Topology**: Direct Root Iteration + Pi-hole Cloudflare (`1.1.1.1/1.0.0.1`) Fallback  
> **Last Verified**: 2026-08-27 23:24 PDT

---

## 1. Architectural Overview & Resolution Flow

```mermaid
flowchart TD
    Client["LAN Clients (Phones / Laptops / TVs / Backups)"] -->|Port 53 DNS| Pihole["Pi-hole v6 FTL (192.168.1.92:53)\n(5,000 Q/min Rate Limit)"]
    
    Pihole -->|Adlist Filtering| BlockCheck{"Is Domain Blocked?\n(309,418 domains)"}
    BlockCheck -->|Yes| Blocked["Return 0.0.0.0 (Ad/Tracker Blocked)"]
    BlockCheck -->|No| Unbound["Unbound Root Resolver (127.0.0.1:5335)\n⚡ 192MB Dedicated RAM Pool\n⚡ 2-Core Multi-Threading"]
    
    Unbound -->|In-Memory Cache Hit (<0.2ms)| CacheHit["Instant RAM Answer"]
    Unbound -->|Cache Miss| RootDNS["Root Nameservers (.)"]
    RootDNS -->|Referral| TLD["TLD Nameservers (.com / .org)"]
    TLD -->|Referral| AuthDNS["Authoritative Nameservers"]
    AuthDNS -->|DNSSEC Verified Answer| Unbound
    
    Unbound -->|Store in 192MB Cache & Return| Pihole
    Pihole -->|Cached Sub-millisecond Response| Client
    
    Pihole -.->|"If Root Iteration Stalls >200ms"| Cloudflare["Fallback 1: Cloudflare 1.1.1.1\nFallback 2: Cloudflare 1.0.0.1"]
```

---

## 2. High-Capacity Memory & Performance Specifications

To leverage the Raspberry Pi 5’s **16 GB RAM** and **4-Core Cortex-A76 CPU**, Unbound is tuned to permanently eliminate rate-limiting and buffer exhaustion during heavy photo backups and streaming bursts:

```ini
# /etc/unbound/unbound.conf.d/pi-hole.conf

server:
    verbosity: 1
    interface: 127.0.0.1
    port: 5335
    do-ip4: yes
    do-udp: yes
    do-tcp: yes
    do-ip6: no
    prefer-ip6: no

    # 1. Multi-Core Threading & Memory Slabs
    num-threads: 2
    msg-cache-slabs: 2
    rrset-cache-slabs: 2
    infra-cache-slabs: 2
    key-cache-slabs: 2

    # 2. Dedicated 192MB In-Memory Cache (Zero Disk I/O)
    msg-cache-size: 64m
    rrset-cache-size: 128m
    infra-cache-numhosts: 10000

    # 3. Resiliency & Serve-Expired Fallback
    serve-expired: yes
    serve-expired-ttl: 86400
    serve-expired-client-timeout: 200

    # 4. Proactive Background Refreshing
    prefetch: yes
    prefetch-key: yes

    # 5. Socket Buffer Capacity (Absorbs Burst Upload Floods)
    so-rcvbuf: 4m
    so-sndbuf: 4m
    edns-buffer-size: 1232

    # 6. Security & DNSSEC Validation
    harden-glue: yes
    harden-dnssec-stripped: yes
    use-caps-for-id: no

    # 7. Private Subnet Protection
    private-address: 192.168.0.0/16
    private-address: 169.254.0.0/16
    private-address: 172.16.0.0/12
    private-address: 10.0.0.0/8
    private-address: fd00::/8
    private-address: fe80::/10
```

---

## 3. Why This Eliminates Sync / Backup Bottlenecks

1. **192MB RAM Cache Pool:**
   * Stores hundreds of thousands of active DNS records in volatile RAM.
   * Repeat queries for sync endpoints (e.g. `photos.googleapis.com`, `upload.video.google.com`, `pXX-content.icloud.com`) resolve in **`<0.2ms`** without network calls.
2. **`serve-expired: yes` (Network Hiccup Immunity):**
   * If a root server is momentarily unreachable during a backup, Unbound **immediately returns the cached expired record in `<0.1ms`** while refreshing in the background.
3. **4MB Socket Buffers (`so-rcvbuf` / `so-sndbuf`):**
   * Prevents kernel UDP socket drops during high-volume parallel connections.
4. **Zero Loopback Rate Limits:**
   * Unbound enforces **0 rate limits on `127.0.0.1`**, allowing unlimited queries from the local Pi-hole instance.

---

## 4. Live Verification & Health Runbook

```bash
# 1. Check Unbound Service Status & Multi-Threading (Tasks: 2)
ssh pi5 "systemctl status unbound --no-pager"

# 2. Test DNSSEC Enforcement (Must return SERVFAIL on spoofed signatures)
ssh pi5 "dig @127.0.0.1 -p 5335 sigfail.verteiltesysteme.net"

# 3. Test DNSSEC Acceptance (Must return NOERROR + Valid IP)
ssh pi5 "dig @127.0.0.1 -p 5335 sigok.verteiltesysteme.net +short"

# 4. Check Unbound Live Cache Stats (Verify 0 rate-limits & 0 timeouts)
ssh pi5 "unbound-control stats_noreset | grep -E 'total.num.queries|cache.hits|queries_ip_ratelimited|timed_out'"
```
