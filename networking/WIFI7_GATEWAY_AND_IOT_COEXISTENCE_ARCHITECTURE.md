# Architecture: Wi-Fi 7 Gateway & Low-Power IoT Coexistence

> **Domain**: Whole-Home Networking, RF Spectrum Management & LAN Infrastructure  
> **Target Hardware**: AT&T BGW620-700 Gateway (`192.168.1.254`), Raspberry Pi 5 (`192.168.1.92`), UGREEN NAS (`192.168.1.80`)  
> **Companion Investigation**: [2026_10_20_WIFI7_IOT_GATEWAY_COMPATIBILITY_INVESTIGATION.md](./2026_10_20_WIFI7_IOT_GATEWAY_COMPATIBILITY_INVESTIGATION.md)

---

## 1. Tri-Band Spectrum Tiering Architecture

A modern tri-band Wi-Fi 7 gateway operates across three distinct radio frequency bands. Each band presents fundamentally different physical propagation characteristics and protocol requirements:

```text
+--------------------------------------------------------------------------------------+
|                           TRI-BAND SPECTRUM TIERING MATRIX                           |
+---------+-----------+--------------+-----------------------------+-------------------+
| Band    | Frequency | Channel Width| Target Workloads            | RF Characteristics|
+---------+-----------+--------------+-----------------------------+-------------------+
| 2.4 GHz | 2.4 GHz   | 20 MHz       | Smart Plugs, IoT Sensors,   | Maximum wall      |
|         |           |              | Legacy TV Sticks, Smart Home| penetration;      |
|         |           |              | (AiDot BK7231, ESP32)       | narrow bandwidth  |
+---------+-----------+--------------+-----------------------------+-------------------+
| 5 GHz   | 5.1-5.8GHz| 80 MHz       | Laptops, Work Mac, iPhone,  | Balanced speed    |
|         |           |              | Apple TV, 4K Streaming      | (up to 1.2 Gbps)  |
|         |           |              | (UNII-3 Channels 149-161)   | & moderate range  |
+---------+-----------+--------------+-----------------------------+-------------------+
| 6 GHz   | 5.9-7.1GHz| 320 MHz      | Pixel 9 Pro XL, Wi-Fi 7 PCs,| Ultra-wide pipe   |
|         |           |              | High-Throughput Media Sync  | (>2.4 Gbps); zero |
|         |           |              |                             | legacy noise      |
+---------+-----------+--------------+-----------------------------+-------------------+
```

### The "Higher is Better" Myth vs. RF Physics
1. **Free Space Path Loss (FSPL)**:
   $$\text{FSPL} = 20 \log_{10}(d) + 20 \log_{10}(f) + 20 \log_{10}\left(\frac{4\pi}{c}\right)$$
   As frequency $f$ increases from $2.4\text{ GHz}$ to $6\text{ GHz}$, path attenuation increases significantly. A $6\text{ GHz}$ signal experiences substantially greater signal degradation when penetrating drywall, wood framing, and concrete compared to $2.4\text{ GHz}$.
2. **Device Capability Matching**:
   - High-throughput devices (Pixel 9 Pro XL, MacBook Pro) dynamically select $5\text{ GHz}$ or $6\text{ GHz}$ for latency-critical bulk data transfers.
   - Low-power IoT devices (microcontrollers with single-antenna $1\times 1$ SISO radios) operate strictly on $2.4\text{ GHz}$ to maintain reliable signal strength through walls with minimal power draw ($<0.5\text{ W}$).

---

## 2. Protocol Incompatibilities: Wi-Fi 7 vs. Legacy IoT

```text
+--------------------------------------------------------------------------------------+
|                          BEACON PROTOCOL PARSING COLLISION                           |
+--------------------------------------------------------------------------------------+
|                                                                                      |
| AT&T BGW620 (Wi-Fi 7 "Max Performance" Profile):                                     |
| +----------------------------------------------------------------------------------+ |
| | 802.11 Beacon: [SSID] [Rates] [HT] [VHT] [HE (Wi-Fi 6)] [EHT/MLO (Wi-Fi 7)] [PMF]| |
| +-----------------------------------------+----------------------------------------+ |
|                                           |                                          |
|                      +--------------------+--------------------+                     |
|                      |                                         |                     |
|                      v                                         v                     |
|       Modern Client (Pixel 9 / Mac)             Legacy IoT (AiDot BK7231 / Roku)     |
|       +-----------------------------+           +----------------------------------+ |
|       | Parses EHT Elements         |           | Fixed 802.11n Parser Overflow    | |
|       | Negotiates Multi-Link (MLO) |           | PMF Association Rejection        | |
|       | Establishes WPA3 Transition |           | Outcome: Disassociation (Deauth) | |
|       | Outcome: Connected (1 Gbps+)|           +----------------------------------+ |
|       +-----------------------------+                                                |
+--------------------------------------------------------------------------------------+
```

### 1. Multi-Link Operation (MLO) & Wi-Fi 7 Information Elements
- In **Max Performance** mode, the BGW620-700 Gateway injects Extremely High Throughput (EHT) elements into beacon management frames across all radios.
- Inexpensive IoT firmware (Shanghai Beken BK7231, Espressif ESP8266) allocates small, fixed-size memory buffers for beacon parsing. When confronted with large Wi-Fi 7 management frames containing MLO descriptors, these chips drop frames or abort the 802.11 association handshake.

### 2. Protected Management Frames (PMF / 802.11w)
- WPA3 mandates PMF to protect deauth/disassociation frames from spoofing attacks.
- In **WPA3-Personal-Transition** mode, PMF is advertised as *optional*. However, the gateway's Wi-Fi driver frequently enforces PMF negotiation during association. Legacy microcontrollers lacking cryptographic hardware for PMF fail key negotiation, resulting in repeated deauth cycles ($2,350+$ frames logged).
- **Rule**: The $2.4\text{ GHz}$ IoT radio must be pinned to **pure WPA2** (`wpaversion = 2`) with standard `G/N` framing.

---

## 3. DHCP Lifecycle: Unicast Renewal vs. Cold Broadcast Collisions

```text
+--------------------------------------------------------------------------------------+
|                    DHCP LEASE RENEWAL vs INITIAL ACQUISITION FLOW                    |
+--------------------------------------------------------------------------------------+
|                                                                                      |
| 1. COLD INITIAL ACQUISITION (Unassigned Device - 0.0.0.0):                           |
|    Client (0.0.0.0:68) ───Broadcast DISCOVER (255.255.255.255:67)───> Gateway Bridge |
|                                                                             |        |
|                       IF Packet Filter = ON / Anti-Spoof = ON:              |        |
|                       [Gateway Switch] ──DROPPED: Source IP 0.0.0.0──X      |        |
|                                                                             |        |
|                       IF Packet Filter = OFF:                               |        |
|                       [Gateway Switch] ─────────────────────────────────────+──────┐ |
|                                                                                    | |
|                                                                                    v |
|    Pi-hole (192.168.1.92:67) <────────────────────────────────────────────────────┘ |
|    Pi-hole ────Broadcast OFFER / ACK────> Gateway Bridge ────> Client Assigned IP    |
|                                                                                      |
| 2. STEADY-STATE RENEWAL (Warm Device - 192.168.1.x):                                 |
|    Client (192.168.1.x:68) ───Unicast REQUEST (UDP:67)───> Pi-hole (192.168.1.92:67)|
|    • Valid IP in L3 header: Bypasses anti-spoofing filters.                          |
|    • Bidirectional state established: Bypasses Reflexive ACLs.                       |
+--------------------------------------------------------------------------------------+
```

### Architectural Vulnerability:
When an entire network reboots simultaneously, no client has an assigned IP address. Every device concurrently transmits from `0.0.0.0`. If gateway packet filters or reflexive firewalls are active, the broadcast discovery frames are terminated at the hardware switch, preventing the off-gateway DHCP server (Pi-hole on Pi 5) from ever receiving them.

---

## 4. Single Source of Truth Configuration Baseline

### AT&T BGW620-700 Gateway (`192.168.1.254`):
| Category | Setting | Production Value | Architectural Rationale |
|---|---|---|---|
| **Firewall** | Packet Filter | **Off** | Permits `0.0.0.0` DHCP broadcast traversal to Pi-hole |
| **Firewall** | Reflexive ACL | **Off** | Prevents dropping incoming unsolicited DHCP response packets |
| **Firewall** | Drop ICMP Echo LAN | **Off** | Allows internal ICMP health probes across home nodes |
| **Firewall** | SIP ALG | **On** | Rewrites SIP headers for carrier Wi-Fi Calling |
| **LAN / IPv6**| IPv6 LAN & DHCPv6 | **On** | Answers client Router Solicitations in <5ms, eliminating 33s macOS `AUTOMATIC-V6` hang across all household Macs |
| **Wi-Fi** | Operation Mode | **Max Interoperability** | Disables MLO on 2.4 GHz; enforces clean 802.11g/n framing |
| **2.4 GHz Radio** | Mode (`standard`) | **G/N** (`bgn`) | Eliminates Wi-Fi 7 AX/BE beacons crashing IoT chips |
| **2.4 GHz Radio** | Security | **WPA2** (`wpaversion=2`)| Eliminates PMF rejection loops on smart plugs |
| **5 GHz Radio** | Mode | **N/AC/AX/BE** | Full Wi-Fi 7 performance for workstations & TVs |
| **5 GHz Radio** | Channel | **149 / 153 (UNII-3)** | Avoids lower DFS radar dropouts and co-channel congestion|
| **6 GHz Radio** | Mode | **AX/BE (320MHz)** | Gigabit+ low-latency tier for flagship mobile devices |

### Raspberry Pi 5 (`192.168.1.92`):
| Category | File Path | Parameter | Production Value |
|---|---|---|---|
| **Pi-hole v6 FTL** | `/etc/pihole/pihole.toml` | `dhcp.hosts` | `[]` (Prevents volatile RAM lease caching) |
| **Pi-hole v6 FTL** | `/etc/pihole/pihole.toml` | `dns.interface` | `"eth0"` (Listening mode: `"ALL"`) |
| **Static Leases** | `/etc/dnsmasq.d/99-static-reservations.conf` | `dhcp-host` | Immutable hardware MAC-to-IP bindings |
| **Secondary Sync**| `/usr/local/bin/sync-pihole-to-nas.sh` | Cron sync | Keeps standby UGREEN NAS container aligned |

---

## 5. Verification Runbook

```bash
# 1. Verify Gateway 2.4 GHz Mode from CLI (Local Mac):
python3 -c "
import urllib.request, http.cookiejar
from bs4 import BeautifulSoup
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
res = opener.open('http://192.168.1.254/cgi-bin/lanstatistics.ha')
soup = BeautifulSoup(res.read().decode('utf-8', errors='ignore'), 'html.parser')
for tr in soup.find_all('tr'):
    txt = tr.get_text(' ', strip=True)
    if 'Mode' in txt and '2.4 GHz' in txt or 'G/N' in txt:
        print(txt)
"

# 2. Check Pi-hole Static DHCP Binding (via SSH to Pi 5):
ssh 192.168.1.92 "grep -E 'SmartPlug|Roku' /etc/dnsmasq.d/99-static-reservations.conf"

# 3. Check Live IoT Associations on Gateway (via SSH to Pi 5 or Local Mac):
python3 -c "
import urllib.request, http.cookiejar
from bs4 import BeautifulSoup
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
res = opener.open('http://192.168.1.254/cgi-bin/lanstatistics.ha')
soup = BeautifulSoup(res.read().decode('utf-8', errors='ignore'), 'html.parser')
for tr in soup.find_all('tr'):
    txt = tr.get_text(' ', strip=True)
    if any(k in txt for k in ['192.168.1.64', '192.168.1.149', '192.168.1.174', '192.168.1.233']):
        print(txt)
"
```
