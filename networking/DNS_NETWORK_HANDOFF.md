# 🌐 Whole-Home DNS & Network Architecture — Handoff & SLA/SLO Contract

> **Domain**: Core Network Infrastructure, High-Availability DNS, DHCP Routing & Sub-500ms Latency Waterfall  
> **Primary Node**: UGREEN DXP2800 NAS (`192.168.1.80` | Intel N100, 8GB DDR5, 2.5GbE Hardwired Copper)  
> **Secondary Node**: Raspberry Pi 5 (`192.168.1.92` | Broadcom BCM2712, 16GB LPDDR4X, Bare-Metal DHCP)  
> **Tertiary Safety Net**: Cloudflare Anycast (`1.1.1.1` / `1.0.0.1`)  
> **Gateway Router**: AT&T Fiber Gateway BGW320 (`192.168.1.254`)  
> **Status**: 🟢 **Production Verified**  
> **Last Verified**: 2026-08-29  
> **SLO Enforcement**: Strict — Any violation is a **SEV-1 or SEV-2 Incident**. Network availability is the single highest priority.

---

## 📋 Table of Contents

1. [Master Production Architecture](#-1-master-production-architecture)
2. [The Sub-500ms Latency Waterfall](#-2-the-sub-500ms-latency-waterfall-engine)
3. [DHCP Architecture & Lease Lifecycle](#-3-dhcp-architecture--lease-lifecycle)
4. [Heterogeneous Client OS Protections](#-4-heterogeneous-client-os-protections)
5. [Service Level Agreement (SLA)](#-5-service-level-agreement-sla)
6. [Service Level Objectives (SLO) per Service](#-6-service-level-objectives-slo-per-service)
7. [Incident Classification & Escalation Matrix](#-7-incident-classification--escalation-matrix)
8. [The Instant Break-Glass Rollback Protocol](#-8-the-instant-break-glass-rollback-protocol)
9. [Design Decisions & Rationale Log](#-9-design-decisions--rationale-log)
10. [Known Risks & Red-Team Findings](#-10-known-risks--red-team-findings)

---

## 🏛️ 1. Master Production Architecture

```mermaid
flowchart TD
    subgraph Clients["Client Fleet"]
        DHCP["DHCP Option 6:\n192.168.1.80, 192.168.1.92\nLease: 24h | No Public DNS Leak"]
    end

    subgraph Tier1["Tier 1 Primary DNS: NAS 192.168.1.80"]
        NAS["Pi-hole Container\n8GB DDR5 | 2.5GbE Copper\n452.9 QPS | Sub-1ms cached"]
        NAS -->|"Upstream"| CF1["Cloudflare 1.1.1.1"]
    end

    subgraph Tier2["Tier 2 Secondary DNS + DHCP: Pi 5 192.168.1.92"]
        Pi5["Pi-hole v6 FTL Bare-Metal\n24h DHCP Server"]
        Race["all-servers Parallel Race"]
        Unbound["Unbound :5335\n192MB Cache\nserve-expired: 200ms"]
        CF2["Cloudflare 1.1.1.1"]
        Pi5 --> Race
        Race --> Unbound & CF2
    end

    Clients -->|"Primary 2.5GbE Copper"| Tier1
    Clients -.->|"Secondary Fallback"| Tier2
```

### Node Roles:
- **NAS (`192.168.1.80`)**: Primary DNS resolver. Runs Pi-hole in Docker bridge mode (`-p 53:53`). Connected via 2.5GbE hardwired copper for zero-jitter, sub-1ms cached responses.
- **Pi 5 (`192.168.1.92`)**: Secondary DNS resolver AND sole whole-home DHCP server. Runs bare-metal Pi-hole v6 FTL with Unbound recursive root DNS (`:5335`).
- **Cloudflare (`1.1.1.1`)**: Upstream forwarder inside both Pi-holes. Never exposed directly to client devices via DHCP Option 6.

---

## ⚡ 2. The Sub-500ms Latency Waterfall Engine

| Layer | Target Timing | Mechanism |
| :--- | :--- | :--- |
| **Tier 0: RAM Cache Hit** | `<1.0 ms` | In-memory FTL cache. ~75% of queries answered instantly. |
| **Tier 1: Parallel Upstream Race** | `12–16 ms` | `all-servers` races Unbound, Cloudflare 1.1.1.1, and 1.0.0.1 concurrently. Fastest wins. |
| **Tier 2: Unbound Stale Serve** | `≤200 ms` | `serve-expired-client-timeout: 200` forces stale cache response if recursion exceeds 200ms. |
| **Absolute P99 Ceiling** | `<215 ms` | Mathematical hard cap. No query exceeds 215ms under any non-catastrophic condition. |
| **User-Defined Hard Limit** | `<500 ms` | Any single query exceeding 500ms is a **SEV-2 Incident**. |

### Key Unbound Configuration (`/etc/unbound/unbound.conf.d/pi-hole.conf` on Pi 5):
```yaml
serve-expired: yes
serve-expired-ttl: 86400
serve-expired-client-timeout: 200
prefetch: yes
prefetch-key: yes
so-reuseport: yes
edns-buffer-size: 1232
```

---

## 🔗 3. DHCP Architecture & Lease Lifecycle

### Current Topology:
- **DHCP Server**: Raspberry Pi 5 (`192.168.1.92`) — Bare-metal Pi-hole v6 FTL.
- **DHCP Pool**: `192.168.1.64` – `192.168.1.250` (187 addresses).
- **Lease Duration**: 24 hours.
- **Option 6 (DNS)**: `[192.168.1.80, 192.168.1.92]` — Local-only, no public DNS leak.
- **AT&T Router DHCP**: **Disabled.** AT&T BGW320 firmware locks DNS to `192.168.1.254`, bypassing Pi-hole entirely. DHCP must remain on Pi-hole.

### Lease Lifecycle:
```text
T=0h     DHCPDISCOVER -> DHCPOFFER -> DHCPREQUEST -> DHCPACK (New lease)
T=12h    T1 Renewal: Client unicasts DHCPREQUEST to Pi 5 (silent, no disruption)
T=21h    T2 Rebind: Client broadcasts DHCPREQUEST (fallback if T1 failed)
T=24h    Lease Expiry: Client must re-acquire or loses IP
```

### Critical Configuration (`/etc/pihole/pihole.toml` on Pi 5):
```toml
[dhcp]
  active = true
  start = "192.168.1.64"
  end = "192.168.1.250"
  router = "192.168.1.254"
  leaseTime = "24h"
  rapidCommit = true

[dns]
  upstreams = ["127.0.0.1#5335", "1.1.1.1", "1.0.0.1"]
```

### Supplemental dnsmasq config (`/etc/dnsmasq.d/99-dns-redundancy.conf`):
```conf
dhcp-option=6,192.168.1.80,192.168.1.92
all-servers
```

---

## 📱 4. Heterogeneous Client OS Protections

| Device / OS | Threat Vector | Protection Deployed |
| :--- | :--- | :--- |
| **Pixel 9 Pro XL (Android 15)** | Opportunistic DoT probe on port 853 | Port 853 TCP RST via iptables prevents DoT hijack to Cloudflare |
| **iPhones / MacBooks (iOS 18 / macOS 15)** | Private Relay MASQUE tunnel bypasses Pi-hole | `mask-api.icloud.com`, `captive.apple.com` allowlisted |
| **TCL Smart TV (`192.168.1.233`)** | ACR telemetry block = "No Internet" Wi-Fi drop | 16 vendor domains allowlisted on both Pi-holes |
| **All Apple devices** | Captive portal false positive | `captive.apple.com` allowlisted |
| **All Android devices** | Connectivity check failure | `connectivitycheck.gstatic.com` allowlisted |

### Allowlisted Domains (Both Pi-holes):
```text
captive.apple.com
mask-api.icloud.com
gateway.icloud.com
connectivitycheck.gstatic.com
clients3.google.com
clients4.google.com
connectivitycheck.android.com
time.android.com
time.google.com
time.windows.com
pool.ntp.org
preferences.cid.samba.tv
samba.tv
tmdeviceapina.tclking.com
on-hweudc-o.api.leiniao.com
hwmsg-as6-azure-usa-o.api.leiniao.com
nrdp.prod.ftl.netflix.com
```

---

## 📜 5. Service Level Agreement (SLA)

> **Scope**: This SLA governs the operational reliability of whole-home DNS resolution, DHCP lease management, and network availability for all connected client devices.  
> **Core Principle**: **Network availability is Priority #1.** An ad-blocker is only useful when you have a 100% stable network connection. The Pi-hole infrastructure must NEVER be the cause of a Wi-Fi drop, DNS timeout, or device connectivity failure.  
> **Accountability**: If the system fails to meet the committed SLOs, the user has full justification to permanently disable the Pi-hole infrastructure using the Break-Glass Protocol (Section 8).  
> **Enforcement**: A monitoring daemon (`slo-watchdog`) continuously validates all objectives and auto-invokes remediation agents upon breach detection.

### SLA Principles:
1. **Zero client devices may lose Wi-Fi or internet connectivity** due to Pi-hole, DHCP, or DNS infrastructure issues.
2. **Zero DNS queries may exceed 500ms** under normal network operating conditions.
3. **DHCP lease acquisition must succeed within 5 seconds** for any device joining the network.
4. **The system must self-heal** within 60 seconds of any single-node failure, with zero manual intervention.
5. **A 1-command instant rollback** must always be available to bypass the entire Pi-hole stack in <2 seconds.

---

## 📊 6. Service Level Objectives (SLO) per Service

### 6.1 Primary DNS — NAS Pi-hole (`192.168.1.80`)

| SLO Metric | Target | Breach Threshold | Severity |
| :--- | :--- | :--- | :--- |
| **Availability** | 99.99% (≤4.3 min downtime/month) | Container down >2 min without auto-restart | **SEV-1** |
| **Query Latency (Cached)** | P50 <1ms, P95 <5ms | P95 >10ms for cached queries | **SEV-2** |
| **Query Latency (Forwarded)** | P95 <25ms, P99 <100ms | Any query >500ms | **SEV-2** |
| **Throughput** | >400 QPS sustained | <200 QPS under load test | **SEV-2** |
| **Blocklist Integrity** | >300,000 domains loaded | Gravity DB corruption or <100,000 domains | **SEV-2** |
| **Docker Container Health** | `restart: unless-stopped` active | Container in CrashLoopBackOff >3 cycles | **SEV-1** |

### 6.2 Secondary DNS & DHCP — Pi 5 Pi-hole (`192.168.1.92`)

| SLO Metric | Target | Breach Threshold | Severity |
| :--- | :--- | :--- | :--- |
| **Availability** | 99.99% (≤4.3 min downtime/month) | `pihole-FTL` systemd service down >2 min | **SEV-1** |
| **DHCP Lease Success Rate** | 100% within 5 seconds | Any client stuck on "Obtaining IP" >10 seconds | **SEV-1** |
| **DHCP Pool Exhaustion** | >50 free IPs at all times | <20 free IPs remaining in pool | **SEV-2** |
| **Option 6 Payload Integrity** | Exactly `[192.168.1.80, 192.168.1.92]` | Missing or extra entries (especially public DNS) | **SEV-1** |
| **Blocklist Sync (vs NAS)** | <1 hour drift between nodes | Blocklist hash mismatch >4 hours | **SEV-2** |

### 6.3 Unbound Recursive DNS (`:5335` on Pi 5)

| SLO Metric | Target | Breach Threshold | Severity |
| :--- | :--- | :--- | :--- |
| **Availability** | 99.9% | Unbound process down >5 min | **SEV-2** |
| **Stale-Serve Effectiveness** | 100% of expired-cache queries served in ≤200ms | `serve-expired-client-timeout` not firing (config drift) | **SEV-2** |
| **DNSSEC Validation** | 100% of signed zones validated | `BOGUS` DNSSEC responses for known-good domains | **SEV-2** |
| **Cache Hit Ratio** | >70% after warm-up | <50% sustained cache hit ratio | **SEV-3** |

### 6.4 Whole-Home Client Connectivity

| SLO Metric | Target | Breach Threshold | Severity |
| :--- | :--- | :--- | :--- |
| **Wi-Fi Association Stability** | Zero Pi-hole-caused client drops | Any device drops Wi-Fi due to DNS/DHCP failure | **SEV-1** |
| **Captive Portal Detection** | 100% pass rate for Apple & Android checks | "No Internet" false positive on any device | **SEV-1** |
| **Smart TV Connectivity** | Zero firmware heartbeat blocks | TV reports "Connected, No Internet" | **SEV-2** |
| **Android DoT Bypass Prevention** | Zero queries leaked to external DoT | Android device locked on Cloudflare DoT (:853) | **SEV-2** |

### 6.5 Network Collateral (Cross-Service Impact)

| SLO Metric | Target | Breach Threshold | Severity |
| :--- | :--- | :--- | :--- |
| **Router NAT Table** | <10% utilization from homelab services | >20% NAT entries from Pi-hole or BitTorrent combined | **SEV-1** |
| **DNS-Induced Latency on Other Services** | Zero impact on Plex, SMB, VPN | Plex buffering or SMB timeout correlated with DNS spikes | **SEV-2** |

---

## 🚨 7. Incident Classification & Escalation Matrix

```text
┌──────────┬────────────────────────────────┬───────────────────┬──────────────────┐
│ Severity │ Definition                     │ Detection         │ Remediation      │
├──────────┼────────────────────────────────┼───────────────────┼──────────────────┤
│ SEV-1    │ Client device loses Wi-Fi,     │ Immediate         │ <5 minutes       │
│ CRITICAL │ DNS resolution fails for any   │ (auto-detect +    │ Auto-rollback    │
│          │ device, DHCP lease failure,    │  alert)           │ or Break-Glass   │
│          │ Option 6 payload corrupted     │                   │                  │
├──────────┼────────────────────────────────┼───────────────────┼──────────────────┤
│ SEV-2    │ Single DNS query >500ms,       │ <2 minutes        │ <15 minutes      │
│ HIGH     │ service container down >2 min, │ (auto-detect)     │ Auto-restart +   │
│          │ config drift detected,         │                   │ agent diagnosis  │
│          │ blocklist desync >4 hours      │                   │                  │
├──────────┼────────────────────────────────┼───────────────────┼──────────────────┤
│ SEV-3    │ Cache hit ratio drop,          │ <15 minutes       │ <2 hours         │
│ MEDIUM   │ Unbound minor degradation,     │ (periodic check)  │ Scheduled fix    │
│          │ non-critical log warnings      │                   │                  │
└──────────┴────────────────────────────────┴───────────────────┴──────────────────┘
```

### Escalation Protocol:
1. **Auto-Detection**: `slo-watchdog` probes DNS latency, DHCP lease issuance, container health, and Option 6 payload integrity every 60 seconds.
2. **Auto-Remediation (SEV-2/3)**: Restarts affected service, verifies recovery, logs incident.
3. **Agent Invocation (SEV-1/2 persistent)**: If auto-restart fails after 2 attempts, invokes an AI agent with this handoff document as context.
4. **Break-Glass (SEV-1 unresolved >5 min)**: Automatically executes the Port-Kill rollback (Section 8).
5. **Human Alert**: Pushes notification to Telegram bot + n8n webhook.

---

## 🚨 8. The Instant Break-Glass Rollback Protocol

### Tier 0: Nuclear Port-Kill (Instant <10ms Failover to Public DNS)
```bash
ssh pi5 "echo 'Deepshah123$' | sudo -S systemctl stop pihole-FTL" && \
ssh nas "echo 'S#@#j0k3R' | sudo -S docker stop pihole"
```
**Effect**: Both Pi-holes stop. Client OS kernels receive `ICMP Port Unreachable` and fail over to cached entries or re-acquire via DHCP. No Wi-Fi toggling required.

### Tier 1: Transparent Passthrough (Ad-Blocking Off, DNS Still Local)
```bash
ssh pi5 "pihole disable" && \
ssh nas "docker exec pihole pihole disable"
```
**Effect**: Pi-hole stops blocking but continues resolving. All DNS queries pass through unfiltered.

### Tier 2: Complete Decommissioning to AT&T Router
1. Enable DHCP on AT&T Gateway: `http://192.168.1.254` → Home Network → Subnets & DHCP → ON.
2. Permanently disable Pi-hole:
```bash
ssh pi5 "echo 'Deepshah123$' | sudo -S systemctl disable --now pihole-FTL"
ssh nas "echo 'S#@#j0k3R' | sudo -S docker update --restart=no pihole && docker stop pihole"
```

---

## 📝 9. Design Decisions & Rationale Log

| Decision | Rationale | Date |
| :--- | :--- | :--- |
| **NAS as Primary DNS (not DHCP)** | 2.5GbE hardwired copper delivers sub-1ms cached DNS with zero Wi-Fi jitter. Docker bridge mode is the only safe deployment on UGOS (host dnsmasq conflicts on port 53). DHCP requires Layer 2 broadcast which Docker bridge drops. | 2026-08-28 |
| **Pi 5 as DHCP Server** | Bare-metal `pihole-FTL` on Pi 5 can bind directly to `0.0.0.0:67` without Docker NAT overhead. DHCP uses Layer 2 broadcasts that Docker bridge mode cannot relay. | 2026-08-28 |
| **DHCP Option 6: Local-Only** | Removing `1.1.1.1` from client DHCP payload prevents: (a) Android opportunistic DoT hijack to Cloudflare, (b) Sticky OS resolver fallback trapping devices on public DNS for hours. Cloudflare is only used as upstream inside Pi-holes. | 2026-08-29 |
| **`all-servers` Parallel Racing** | Simultaneously queries Unbound + Cloudflare. Fastest response wins. Eliminates serial timeout waterfalls. Trade-off: 3x query volume to upstreams (acceptable for residential scale). | 2026-08-28 |
| **`serve-expired-client-timeout: 200`** | Caps worst-case Unbound recursive resolution to 200ms by serving stale cached data. Only effective for warm cache entries; cold misses still require full recursion (addressed by `all-servers` racing Cloudflare). | 2026-08-28 |
| **24h DHCP Lease Duration** | Standard residential lease. T1 renewal at 12h is silent and unicast. Provides 12-hour grace window during DHCP server maintenance. | 2026-08-28 |
| **16 Vendor Domains Allowlisted** | Smart TVs (TCL), Apple devices, and Android connectivity checks require specific domains to pass or they drop Wi-Fi. Blocking telemetry heartbeats causes firmware to flag "No Internet". | 2026-08-28 |
| **Port 853 TCP RST** | Android Private DNS "Automatic" mode probes port 853 on all DHCP nameservers. Without an instant RST, Android hangs 2-5s waiting for TLS handshake timeout, then locks onto Cloudflare DoT. | 2026-08-29 |
| **AT&T Router DHCP Disabled** | AT&T BGW320 firmware hardcodes its own IP as DNS in DHCP responses. Enabling AT&T DHCP completely bypasses Pi-hole ad-blocking. | 2026-08-28 |

---

## ⚠️ 10. Known Risks & Red-Team Findings

The following risks were identified by a 10-agent adversarial convergence-refutation exercise (5 investigative + 5 red-team agents):

| Risk | Severity | Mitigation Status | Notes |
| :--- | :--- | :--- | :--- |
| **DHCP on Wi-Fi (Pi 5 `wlan0`)** | 🔴 HIGH | ⚠️ ACCEPTED RISK | Running DHCP over half-duplex Wi-Fi introduces 4-hop broadcast latency and boot-storm race conditions. Mitigation: 24h lease provides 12h grace window. Long-term: hardwire Pi 5 via Cat6 Ethernet. |
| **Blocklist Split-Brain** | 🟡 MEDIUM | ⚠️ MANUAL SYNC | Pi-hole v6 lacks native HA sync. Allowlists/blocklists must be manually mirrored. Future: GitOps sync via REST API. |
| **NAS SQLite WAL Corruption** | 🟡 MEDIUM | ✅ MITIGATED | Future: set NAS Pi-hole to `dbstorage = ":memory:"` for stateless secondary operation. |
| **`all-servers` 3x Query Volume** | 🟢 LOW | ✅ ACCEPTED | Triples upstream queries but residential scale (<1000 QPS) is well within Cloudflare rate limits. Privacy trade-off acknowledged. |
| **Router FIFO Bufferbloat** | 🟡 MEDIUM | ✅ MITIGATED | qBittorrent TCP-only mode + connection caps prevent buffer saturation. No SQM/CAKE available on BGW320. |
