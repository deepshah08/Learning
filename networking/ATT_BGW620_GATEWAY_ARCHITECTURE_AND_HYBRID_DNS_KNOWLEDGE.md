# AT&T BGW620 Gateway Architecture & Hybrid DNS System

> Origin: investigation journey at [./2026_10_23_ATT_BGW620_BRIDGE_DHCP_KILLSWITCH_INVESTIGATION.md](./2026_10_23_ATT_BGW620_BRIDGE_DHCP_KILLSWITCH_INVESTIGATION.md)  
> Operational contract at [./DNS_NETWORK_HANDOFF.md](./DNS_NETWORK_HANDOFF.md)  
> Hardware: AT&T Fiber BGW620-700 Gateway (`192.168.1.254`, Firmware `5.40.4`), Raspberry Pi 5 (`192.168.1.92`), UGREEN DXP2800 NAS (`192.168.1.80`)  
> Target Architecture: Decoupled "Zero Blast-Radius" Hybrid DNS & Gateway DHCP Model

---

## Role / Position

The AT&T BGW620-700 sits at the physical boundary between the AT&T WAN optical network and the local residential network. It provides Layer 1/2 physical termination, hardware Layer 2 Ethernet switching, tri-band Wi-Fi 7 wireless access, stateful NAT routing, and authoritative DHCP leasing (`192.168.1.0/24`).

The gateway is **NOT** responsible for local ad-blocking, local hostname resolution (`pi.hole`, local service records), or privacy-preserving recursive DNS. Those functions are decoupled and delegated to dedicated homelab nodes (Raspberry Pi 5 and UGREEN NAS) accessed directly at Layer 7 by configured endpoints.

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   PHYSICAL & LOGICAL TOPOLOGY OF HOMELAB NETWORK                       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   WAN Fiber Drop (AT&T Fiber 1Gbps Symmetric)                                          │
│         │                                                                              │
│         ▼                                                                              │
│   ┌──────────────────────────────────────────────────────────────────────────────────┐ │
│   │ AT&T BGW620-700 Gateway (192.168.1.254, Firmware 5.40.4)                         │ │
│   │ - Layer 3 Router, NAT, WAN Firewall                                              │ │
│   │ - Authoritative DHCP Server (Pool: 192.168.1.64 - 192.168.1.253)                 │ │
│   │ - Wi-Fi 7 Radios (Rimjhim 2.4G Ch11, 5G Ch149, 6G 320MHz)                        │ │
│   └───────────────┬──────────────────────────────────┬───────────────────────────────┘ │
│                   │ Physical Copper LAN-1            │ Physical Copper LAN-2           │
│                   ▼                                  ▼                                 │
│   ┌────────────────────────────────┐ ┌───────────────────────────────────────────────┐ │
│   │ Linksys Extender ("Uptop")     │ │ Raspberry Pi 5 (192.168.1.92, 1GbE eth0)      │ │
│   │ 3rd Floor AP (192.168.1.122)   │ │ - Primary Pi-hole v6 FTL (Sub-1ms DNS cache)  │ │
│   │ Hardware L2 Bridge to LAN-1    │ │ - Unbound Root Recursive DNS (127.0.0.1#5335) │ │
│   └────────────────────────────────┘ └───────────────────────┬───────────────────────┘ │
│                                                              │ 2.5GbE Copper           │
│                                                              ▼                         │
│                                      ┌───────────────────────────────────────────────┐ │
│                                      │ UGREEN DXP2800 NAS (192.168.1.80, 2.5GbE)     │ │
│                                      │ - Secondary Standby Pi-hole (Docker bridge)   │ │
│                                      │ - Docker Host, Storage, Media Stack           │ │
│                                      └───────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Plane Decomposition

The homelab network is partitioned into three parallel planes to achieve zero blast-radius isolation:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│           PLANE DECOMPOSITION: COUPLED OFF-GATEWAY VS. DECOUPLED HYBRID ARCH           │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ BEFORE: COUPLED OFF-GATEWAY DHCP (HIGH BLAST RADIUS)                                   │
│                                                                                        │
│   Client Broadcast ──► [BGW620 Wi-Fi Bridge] ──X (Dropped: 0.0.0.0)                    │
│                               │                                                        │
│                               ▼                                                        │
│                        [Pi 5 DHCP Server] ──► (Never reached) ──► WHOLE HOME OFFLINE   │
│                                                                                        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ AFTER: DECOUPLED ZERO BLAST-RADIUS HYBRID ARCHITECTURE                                 │
│                                                                                        │
│   1. CONTROL PLANE (DHCP & Layer 3 Routing):                                           │
│      All Clients ──► [BGW620 Native DHCP] ──► Instant IP + Gateway (100% Reliable)     │
│                                                                                        │
│   2. APPLICATION PLANE (DNS Resolution):                                               │
│      ├─ Whole-Home / IoT ──► [Gateway DNS 192.168.1.254] (Zero Blast Radius)           │
│      └─ Personal Fleet ────► [Pi-hole 192.168.1.92 / .80] (100% Ad-Blocking)           │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

> **The Whole Point in One Sentence**: The Gateway handles 100% of Layer 3 DHCP and network routing to eliminate Layer 2 Wi-Fi bridge discard deadlocks, while personal endpoints configure Layer 7 DNS directly to retain 100% ad-blocking with zero household blast radius.

### Key Facts About the Control Plane (DHCP & Routing):
- **Sole Source of Leases**: AT&T Gateway native `dhcpd` is authoritative. Pool is `192.168.1.64` to `192.168.1.253` with a 24-hour lease (`86400s`).
- **Zero Bridge Discards**: Because the gateway daemon listens on `0.0.0.0:67` on the local bridge, incoming wireless station `DHCPDISCOVER` packets are consumed locally without crossing the bridge anti-spoofing filter.
- **Default Route Guarantees**: Every client unconditionally receives Default Gateway `192.168.1.254` (`Option 3`) and Subnet Mask `255.255.255.0` (`Option 1`).

### Key Facts About the Data Plane (Physical & RF):
- **Copper Switching**: Hardware switch ASIC (`BCM53134`) handles inter-port Ethernet traffic at wire speed with sub-0.5ms latency.
- **RF Hardening**: 2.4 GHz is pinned to Channel 11 (20MHz) in pure WPA2-AES mode to support microcontrollers; 5 GHz is pinned to non-DFS Channel 149 (80MHz) to eliminate 60-second radar silences; 6 GHz is active on 320MHz for Wi-Fi 6E/7 flagships.

### Key Facts About the Application / DNS Plane:
- **Default Fleet**: Roommates, visiting guests, and IoT smart devices resolve DNS via Gateway upstream (`68.94.156.1`). They never interact with homelab containers and never suffer outages if homelab hosts reboot.
- **Developer Fleet**: Personal devices (MacBooks, Pixel 9 Pro XL, iPad) set static DNS to `192.168.1.92` (Pi 5) and `192.168.1.80` (NAS) with IPv6 set to "Link-local only". They enjoy 100% local ad-blocking and sub-2ms resolution.

---

## Architecture

### Component Inventory

| Component | Role in Architecture | Location / Platform | State in Hybrid Model |
| :--- | :--- | :--- | :---: |
| **AT&T BGW620-700** | L3 Router, NAT, WAN Firewall, Authoritative DHCP | `192.168.1.254` (Firmware `5.40.4`) | ✅ **Active & Hardened** |
| **WLAN Software Bridge (`br0`)** | Ingress frame bridge between Wi-Fi and switch fabric | BGW620 Kernel Driver | ❌ **Unchanged (Bypassed by local DHCP)** |
| **Switch ASIC (`BCM53134`)** | 4-port Gigabit Ethernet hardware switch | BGW620 Physical Board | ❌ **Unchanged (Wire speed)** |
| **Linksys Extender (`Uptop`)** | 3rd-floor AP wired to Gateway LAN-1 | `192.168.1.122` (LAN-1 Copper) | ❌ **Unchanged (Split SSID)** |
| **Raspberry Pi 5** | Primary Pi-hole v6 FTL + Unbound recursive DNS | `192.168.1.92` (Bare-metal Gigabit) | ✅ **Modified (DHCP Disabled)** |
| **UGREEN DXP2800 NAS** | Secondary Pi-hole DNS container | `192.168.1.80` (Docker 2.5GbE) | ✅ **Modified (Standby DHCP Disabled)** |
| **Personal Developer Fleet** | High-performance developer laptops/phones | Personal MacBooks, Pixel, iPad | ✅ **Configured (Manual DNS + Link-Local)** |
| **Household / IoT Fleet** | Smart home plugs, bulbs, roommate devices | Unmodified consumer devices | ❌ **Unchanged (Native DHCP/DNS)** |

---

## Master Configuration Matrix: AT&T BGW620 Gateway

The following matrix represents the live audited configuration state of the gateway reconciled against factory defaults and previous experimental states:

| Parameter & Endpoint | Factory Default | Previous Experimental State | Current Audited State | Performance & Availability Impact | Operating Rationale |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **DHCP Server**<br>`/cgi-bin/dhcpserver.ha` | **`On`**<br>(Pool `.64`–`.253`, 1d) | **`Off`**<br>(Handed off to Pi 5) | **`On`**<br>(Pool `.64`–`.253`, 1d) | 🔴 **CRITICAL AVAILABILITY**<br>Eliminates `0.0.0.0` bridge discards. Cold-boot devices and waking devices connect instantly. | 🟢 **KEEP `ON`**<br>*(Authoritative)* |
| **2.4 GHz Security**<br>`/cgi-bin/wconfig.ha` | **`Max Performance`**<br>(WPA3-Transition / PMF) | **`Max Interoperability`**<br>(Pure WPA2-AES, G/N) | **`Max Interoperability`**<br>(Pure WPA2-AES, G/N) | 🔴 **CRITICAL STABILITY**<br>Default PMF caused 1,890+ deauths that crashed all 3 AiDot plugs. Pure WPA2 is 100% stable. | 🛡️ **KEEP MODIFIED**<br>*(Mandatory for IoT)* |
| **2.4 GHz Channel**<br>`/cgi-bin/wconfig.ha` | **`Auto`**<br>(Dynamic 10/11) | **`11`**<br>(Fixed 20MHz) | **`11`**<br>(Fixed 20MHz) | 🟡 **HIGH AVAILABILITY**<br>Eliminates RF channel hopping and adjacent-channel interference with neighbor networks. | 🛡️ **KEEP MODIFIED**<br>*(Fixed Ch 11)* |
| **5 GHz Channel**<br>`/cgi-bin/wconfig.ha` | **`Auto`**<br>(Frequently selected DFS) | **`149`**<br>(Fixed UNII-3 non-DFS) | **`149`**<br>(Fixed UNII-3 non-DFS) | 🔴 **CRITICAL STABILITY**<br>Auto selects DFS radar frequencies. Radar detection forces 60s of complete radio silence (CAC). | 🛡️ **KEEP MODIFIED**<br>*(Fixed Ch 149)* |
| **5 GHz Bandwidth**<br>`/cgi-bin/wconfig.ha` | **`80MHz`** | **`80MHz`** | **`80MHz`** | 🟢 **HIGH PERFORMANCE**<br>Delivers up to 1.2 Gbps theoretical Wi-Fi 6 throughput with zero channel-bonding instability. | 🟢 **KEEP `80MHz`**<br>*(Factory Default)* |
| **6 GHz Radio**<br>`/cgi-bin/wconfig.ha` | **`On`**<br>(WPA3-Personal, 320MHz) | **`On`**<br>(WPA3-Personal, 320MHz) | **`On`**<br>(WPA3-Personal, 320MHz) | 🟢 **MAX SPEED**<br>Dedicated high-speed pipe for Pixel 9 Pro XL & M-series Macs without legacy device contention. | 🟢 **KEEP `ON`**<br>*(Factory Default)* |
| **IPv6 LAN**<br>`/cgi-bin/ip6lan.ha` | **`On`**<br>(Stateful/Stateless RDNSS) | **`Off`**<br>(Disabled to stop ad leaks) | **`Off`**<br>(Disabled) | 🟡 **TRADE-OFF**<br>Disabling stops AT&T from broadcasting unblocked DNS (`2600:...::1`). Requires Apple devices to set Link-local. | ⚖️ **KEEP `OFF`**<br>*(Ad-Block Isolation)* |
| **Reflexive ACL**<br>`/cgi-bin/dosprotect.ha` | **`On`** | **`Off`** | **`Off`** | ⚪ **LOW IMPACT**<br>Disabled to prevent dropping incoming broadcast replies without outbound state table. | 🟢 **KEEP `OFF`** |
| **LAN ICMP Echo Drop**<br>`/cgi-bin/dosprotect.ha` | **`On`** | **`Off`** | **`Off`** | 🟡 **DIAGNOSTIC BENEFIT**<br>Allows ping telemetry between Pi 5, NAS, and clients for latency monitoring. | 🛡️ **KEEP `OFF`**<br>*(Diagnostic Value)* |
| **Packet Filters**<br>`/cgi-bin/packetfilter.ha` | **`Enabled`** | **`Disabled`** | **`Disabled`** | ⚪ **LOW IMPACT**<br>Disabling strips CPU overhead on local broadcasts. Stateful NAT firewall protects WAN. | 🟢 **KEEP `OFF`** |
| **IP Passthrough**<br>`/cgi-bin/ippass.ha` | **`Off`** (`allocmode = normal`) | **`Off`** | **`Off`** | 🔴 **CRITICAL SECURITY**<br>Prevents exposing local homelab ports directly to the public internet WAN IP. | 🟢 **KEEP `OFF`**<br>*(Factory Default)* |
| **Home Network Security**<br>`/cgi-bin/securityoptions.ha` | **`Enabled`** | **`Enabled`** | **`Enabled`** | ⚪ **FIRMWARE LOCKED**<br>Hardcoded in firmware 5.40.4 base image; no local toggle exists. | 🟢 **KEEP AS IS** |
| **SSID Topology**<br>`Rimjhim` vs `Uptop` | Single Unified SSID | Split (`Rimjhim` 1st / `Uptop` 3rd) | Split (`Rimjhim` 1st / `Uptop` 3rd) | 🔴 **CRITICAL AVAILABILITY**<br>Prevents sticky macOS roaming from holding onto weak 3rd-floor AP at -80 dBm. | 🛡️ **KEEP SPLIT** |

---

## Mechanics — Step by Step

### Path 1: Client Cold Boot Association (`INIT` State)
1. **L2 Frame Emission**: Client associates with `Rimjhim` SSID. Client has no assigned IP address.
2. **Broadcast Discovery**: Client transmits UDP broadcast `0.0.0.0:68` $\to$ `255.255.255.255:67` (`DHCPDISCOVER`).
3. **Gateway Kernel Ingress**: The BGW620 wireless driver hands the frame to interface `br0`.
4. **Local Consumption**: Because `dhcpd` is enabled on the gateway, the socket binding `0.0.0.0:67` intercepts the packet directly.
5. **No Bridge Discard**: The packet does not traverse the station-to-station bridge filter; `Reason: IP Source Address DISCARD` is never evaluated.
6. **Offer & Acknowledgment**: Gateway unicasts `DHCPOFFER` followed by `DHCPACK` assigning IP `192.168.1.x`, Subnet `255.255.255.0`, Gateway `192.168.1.254`, and DNS `192.168.1.254`.
7. **Complete Binding**: Client reaches `BOUND` state in $<5\text{ ms}$.

### Path 2: Client Unicast Lease Renewal (`RENEWING` State)
1. **Timer Expiration**: Client reaches 50% of lease time ($T_1 = 12\text{ hours}$).
2. **Point-to-Point Request**: Client sends unicast UDP packet `192.168.1.x:68` $\to$ `192.168.1.254:67` (`DHCPREQUEST`).
3. **Bridge Forwarding**: Because the source IP is a valid assigned address (`192.168.1.x`), the gateway software bridge forwards the frame without inspection.
4. **Instant ACK**: Gateway renews lease timer for another 24 hours in $<1\text{ ms}$.

### Path 3: Personal Fleet Ad-Blocked DNS Resolution
1. **OS DNS Precedence**: Client OS (macOS/Android/Linux) receives gateway DHCP but possesses manually configured DNS servers (`192.168.1.92`, `192.168.1.80`).
2. **Direct UDP Query**: Application issues DNS lookup for `c.amazon-adsystem.com`. Query is dispatched directly to `192.168.1.92:53` via Ethernet switch fabric.
3. **Gravity Block**: Pi-hole v6 FTL matches domain against 288,000+ blocklist entries.
4. **Immediate Response**: Pi-hole returns `0.0.0.0` in $1.8\text{ ms}$. Ad request is blocked; zero WAN bandwidth consumed.
5. **Legitimate Query Recursive Lookup**: If domain is allowed, Pi 5 queries local Unbound (`127.0.0.1#5335`) or races Cloudflare (`1.1.1.1`) in $12–16\text{ ms}$.

---

## State Machine / Lifecycle

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   RFC 2131 DHCP CLIENT LIFECYCLE & FAILURE BOUNDARY                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│      ┌───────────────┐                                                                 │
│      │ [INIT STATE]  │ ◄── Power On, Cold Boot, MAC Randomization, or SSID Change      │
│      └───────┬───────┘                                                                 │
│              │ Broadcast DHCPDISCOVER (src=0.0.0.0, dst=255.255.255.255)               │
│              ▼                                                                         │
│      ┌────────────────────────────────────────────────────────┐                        │
│      │ BGW620 Wi-Fi Ingress Filter (wl0/1/2)                  │                        │
│      │ - IF Native DHCP == OFF: SILENT DISCARD (REASON: IP)   │ ◄── DEADLOCK BOUNDARY  │
│      │ - IF Native DHCP == ON : LOCAL DAEMON RESPONDS IN <5ms │ ◄── PRODUCTION FIX     │
│      └───────┬────────────────────────────────────────────────┘                        │
│              │ DHCPOFFER & DHCPREQUEST                                                 │
│              ▼                                                                         │
│      ┌───────────────┐                                                                 │
│      │ [BOUND STATE] │ ◄── Client assigned 192.168.1.x, Default Gateway 192.168.1.254  │
│      └───────┬───────┘                                                                 │
│              │ T1 Timer Expires (50% of lease = 12h)                                   │
│              ▼                                                                         │
│      ┌─────────────────┐                                                               │
│      │ [RENEWING STATE]│ ◄── Unicast DHCPREQUEST (src=192.168.1.x, dst=192.168.1.254)  │
│      └───────┬─────────┘     (Valid source IP -> Always passed bridge)                 │
│              │ Unicast DHCPACK                                                         │
│              ▼                                                                         │
│      Lease renewed without broadcast                                                   │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Why This Design (vs. Alternatives)

| Architecture Alternative | Fatal Flaw / Dealbreaker |
| :--- | :--- |
| **Pure Off-Gateway DHCP** (Pi-hole handles all DHCP) | **Fatal Bridge Discard**: BGW620 Wi-Fi driver silently drops `0.0.0.0` broadcasts when native DHCP is off. Clients suffer yellow `!` outages upon cold boot or sleep wake-up. |
| **IP Passthrough Mode** | **Security & Layer Mismatch**: Designed to pass public WAN IP to downstream routers; does not fix internal Wi-Fi bridge filtering; exposes Pi 5 to public internet as open resolver. |
| **Unified Single SSID Mesh** | **Sticky Roaming Drops**: Apple client devices hold onto weak 3rd-floor signal (`Uptop`) at -80 dBm while sitting next to 1st-floor router, dropping video calls. |
| **Gateway IPv6 LAN Enabled** | **Unstoppable Ad Leaks**: BGW620 hardcodes itself as RDNSS DNS resolver (`2600:...::1`), causing dual-stack OS clients to bypass Pi-hole and fetch ads via AT&T upstream. |
| **Chosen: Decoupled Zero Blast-Radius Hybrid Architecture** | **Zero Blast Radius**: Native Gateway handles 100% of DHCP/routing (rock-solid connectivity); personal fleet points to Pi-hole (100% ad-blocking); homelab restarts never affect household. |

---

## Failure Modes Observed Across Planes

| Failure Scenario | Control Plane (DHCP) | Data Plane (Throughput) | DNS Plane (Ad-blocking) | Blast Radius | Recovery Protocol |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Raspberry Pi 5 Crashes or Reboots** | 🟢 **100% Operational**<br>Gateway serves DHCP | 🟢 **100% Operational**<br>Zero impact on wire | 🟡 **Personal Fleet Fallback**<br>NAS Pi-hole (`.80`) answers | 🟢 **Zero Household Impact**<br>Roommates & IoT unaffected | Automatic: NAS handles DNS. Pi 5 auto-restarts via systemd. |
| **UGREEN NAS Reboots or Updates** | 🟢 **100% Operational**<br>Gateway serves DHCP | 🟢 **100% Operational**<br>Zero impact on wire | 🟢 **Primary Operational**<br>Pi 5 (`.92`) handles queries | 🟢 **Zero Household Impact**<br>Roommates & IoT unaffected | None needed: Pi 5 is primary resolver. |
| **Both Homelab Nodes Offline** | 🟢 **100% Operational**<br>Gateway serves DHCP | 🟢 **100% Operational**<br>Zero impact on wire | 🔴 **Personal DNS Pauses**<br>Fails until manual toggle | 🟢 **Zero Household Impact**<br>Roommates & IoT stay online | On Mac: Run `networksetup -setdnsservers Wi-Fi empty` to revert to gateway DNS. |
| **BGW620 Gateway Power Cycle** | 🔴 **Temporary Pause**<br>Recovers in ~90s | 🔴 **Temporary Pause**<br>Recovers in ~90s | 🔴 **No WAN Access**<br>WAN drop | 🔴 **Whole Home**<br>Gateway power cycle | Gateway boots in 90s; all devices re-associate automatically. |

---

## Concrete Incident Replay: October 23, 2026 Wake-Up Failure

### Before (Coupled Off-Gateway DHCP):
```text
State of Gateway: Native DHCP OFF
State of Pi 5: Authoritative DHCP ON (pihole-FTL UDP 67)
Client Action: Work Mac wakes from sleep on 'Rimjhim' Wi-Fi (State: INIT, IP: 0.0.0.0)
────────────────────────────────────────────────────────────────────────────────
Transmission: Work Mac broadcasts DHCPDISCOVER (src=0.0.0.0, dst=255.255.255.255)
Gateway Action: Bridge software br0 drops packet ("Reason: IP Source Address DISCARD")
Pi 5 Telemetry: 0 packets received on eth0 UDP 67
Client Consequence: IPv4 self-assigns to 169.254.142.88; yellow "!" captive portal stall;
                    zero internet connectivity; user forced to connect to Uptop.
```

### After (Decoupled Zero Blast-Radius Hybrid Architecture Live):
```text
State of Gateway: Native DHCP ON (Pool .64-.253, Lease 86400s)
State of Pi 5: Bare-metal Pi-hole DNS ON; DHCP OFF
Client Action: Work Mac wakes from sleep on 'Rimjhim' Wi-Fi (State: INIT, IP: 0.0.0.0)
────────────────────────────────────────────────────────────────────────────────
Transmission: Work Mac broadcasts DHCPDISCOVER (src=0.0.0.0, dst=255.255.255.255)
Gateway Action: Consumed by local dhcpd daemon on br0 socket in <1ms
Gateway Reply: DHCPOFFER (192.168.1.94, Router: 192.168.1.254, Mask: 255.255.255.0)
Client Consequence: Client bound in 3.8ms; Default Gateway route active;
                    Manual DNS settings route queries to 192.168.1.92 / .80;
                    Ad-blocking 100% operational; 0.0% packet loss; ZERO USER INTERVENTION.
```

---

## Exact Runbook Commands

### 1. Interrogating & Verifying BGW620 Gateway via CLI
```bash
# Verify Gateway DHCP Server is Active
curl -s "http://192.168.1.254/cgi-bin/dhcpserver.ha" | grep -i "selected"

# Verify 5 GHz Radio is on Non-DFS Channel 149
curl -s "http://192.168.1.254/cgi-bin/wconfig.ha" | grep -i "149"

# Verify IPv6 LAN is OFF
curl -s "http://192.168.1.254/cgi-bin/ip6lan.ha" | grep -i "checked"
```

### 2. Client-Side DNS Configuration (macOS Personal Fleet)
```bash
# Set Primary and Secondary Pi-hole DNS on Wi-Fi
networksetup -setdnsservers Wi-Fi 192.168.1.92 192.168.1.80

# Verify Configured DNS Servers
networksetup -getdnsservers Wi-Fi
# Expected Output:
# 192.168.1.92
# 192.168.1.80

# Set IPv6 to Link-Local Only (Eliminates 33s Router Solicitation Delay)
networksetup -setv6linklocal Wi-Fi

# Verify IPv6 Configuration
networksetup -getinfo Wi-Fi | grep -i "IPv6"
# Expected Output: IPv6: Link Local Only

# Break-Glass Revert to Gateway Default (If Pi 5 and NAS are both down)
networksetup -setdnsservers Wi-Fi empty
```

### 3. Client-Side DNS Configuration (Linux / Android / iOS)
- **Linux (`systemd-resolved`)**:
  ```ini
  # /etc/systemd/resolved.conf.d/pihole.conf
  [Resolve]
  DNS=192.168.1.92 192.168.1.80
  Domains=~.
  ```
- **Android 15 (Google Pixel 9 Pro XL)**:
  - Settings $\to$ Network & Internet $\to$ Internet $\to$ Gear next to `Rimjhim` $\to$ Pencil (Edit) $\to$ Advanced options:
  - IP Settings: `DHCP` (Leave as default to receive Gateway IP and Route).
  - Private DNS: Set to `Off` (Ensures local Wi-Fi DNS is utilized rather than public DoT hijack).
- **iOS / iPadOS**:
  - Settings $\to$ Wi-Fi $\to$ `Rimjhim` (i icon) $\to$ Configure DNS $\to$ `Manual`:
  - Add Server: `192.168.1.92`
  - Add Server: `192.168.1.80`
  - Configure IPv6 $\to$ `Link-Local Only`.

### 4. Homelab Node Health & Socket Audit
```bash
# Verify DHCP socket is CLOSED on Pi 5 (Port 67 must return nothing)
sudo ss -ulpn | grep :67

# Verify Pi-hole DNS is answering on Pi 5
dig @192.168.1.92 google.com +short

# Verify Pi-hole DNS is answering on NAS
dig @192.168.1.80 google.com +short

# Verify Ad-Blocking behavior
dig @192.168.1.92 pagead2.googlesyndication.com +short
# Expected Output: 0.0.0.0
```

---

## Key Learnings

1. **Hardware Switching Bypasses Software Bridge Filters**: Packets entering physical switch ports (LAN-1 via `Uptop`) bypass software anti-spoofing filters that kill packets on Wi-Fi interfaces (`Rimjhim`). Never assume wired and wireless ingress behave identically on ISP gateways.
2. **Coupling Application Concerns to Physical Control Planes Creates Fragility**: Forcing an entire household onto off-gateway DHCP merely to distribute DNS Option 6 creates an existential failure mode. Decoupling DHCP to the ISP gateway and configuring DNS at the client tier provides absolute stability.
3. **SSID Boundaries are Hard Security Isolation Gates in Client OS Stacks**: Operating systems never carry DHCP leases across SSID transitions. Switching from `Uptop` to `Rimjhim` forces a cold `0.0.0.0` broadcast under IEEE 802.11 standards.
4. **Link-Local IPv6 Retains Apple Ecosystem Discovery Without WAN Leaks**: Disabling IPv6 LAN on ISP gateways stops RDNSS DNS leaks, while setting Apple devices to "Link-local only" prevents the 33-second Router Solicitation timeout and preserves AirDrop/AirPlay functionality.

---

## Companion Docs

- Investigation Journey & Forensic Audit: [./2026_10_23_ATT_BGW620_BRIDGE_DHCP_KILLSWITCH_INVESTIGATION.md](./2026_10_23_ATT_BGW620_BRIDGE_DHCP_KILLSWITCH_INVESTIGATION.md)
- Network Operational Contract & SLA: [./DNS_NETWORK_HANDOFF.md](./DNS_NETWORK_HANDOFF.md)
- IoT Coexistence Baseline: [./WIFI7_GATEWAY_AND_IOT_COEXISTENCE_ARCHITECTURE.md](./WIFI7_GATEWAY_AND_IOT_COEXISTENCE_ARCHITECTURE.md)
- August 31 DHCP Incident RCA: [./INCIDENT_2026_08_31_DHCP_OUTAGE_RCA.md](./INCIDENT_2026_08_31_DHCP_OUTAGE_RCA.md)
