# 🕳️ Project 12: Pi-hole v6 FTL Primary DNS & High-Availability (Raspberry Pi 5)

> **Context**: Production deployment of whole-home network ad-blocking with AT&T Fiber Gateway takeover, IPv6 SLAAC leak mitigation, static IP binding, High-Availability Dual-DNS DHCP broadcasting to UGREEN NAS, and Tailscale MagicDNS integration.  
> **Primary Host**: Raspberry Pi 5 (`192.168.1.92` Static / Tailscale `100.68.196.14`)  
> **Secondary Host**: UGREEN DXP2800 NAS (`192.168.1.80` Static 2.5GbE)  
> **Gateway**: AT&T Fiber BGW210/320 (`192.168.1.254`)  
> **Wi-Fi SSID**: `Rimjhim` (Password: `Restlessinsect`)  
> **Status**: 🟢 **Production (100% High-Availability Ad-Blocking Active & Tested)**  
> **Repository**: [`deepshah08/raspberry-pi-5-ecosystem/projects/12-pihole`](https://github.com/deepshah08/raspberry-pi-5-ecosystem/tree/main/projects/12-pihole)  
> **Last Verified**: 2026-08-25 23:30 PDT

---

## 1. Executive Summary & Live Verification

Whole-home network ad-blocking is fully active and verified live on client devices. All LAN traffic across laptops, mobile phones (Pixel/iOS), tablets, and smart TVs routes DNS queries through our High-Availability Dual-Pi-hole cluster (Primary: Pi 5, Secondary: UGREEN NAS).

### Live Client Verification (macOS Terminal):
```text
$ scutil --dns | grep -A 4 "resolver #1"
resolver #1
  search domain[0] : lan
  nameserver[0] : 192.168.1.92  <-- 🎯 Primary: Pi 5
  nameserver[1] : 192.168.1.80  <-- 🎯 Secondary: UGREEN NAS (2.5GbE)

$ dig googleads.g.doubleclick.net +short
0.0.0.0  <-- ✅ 100% Blocked

$ dig speedtest.net +short
151.101.194.219  <-- ✅ Valid Domain Resolved
```

---

## 2. Master Toggle & Configuration Checklist

Below is the complete record of every setting toggled across all layers:

### Layer 1: AT&T Fiber Gateway (`http://192.168.1.254`)
1. **Home Network ➔ Subnets & DHCP**:
   - `DHCP Server Enable`: ➔ **`Off`** *(Stops AT&T router from handing out its own DHCP/DNS)*.
   - `Device IPv4 Address`: `192.168.1.254`.
   - `Subnet Mask`: `255.255.255.0`.
   - Click **Save**.
2. **Home Network ➔ IPv6**:
   - `IPv6`: ➔ **`Off`** *(CRITICAL: Shuts down ICMPv6 SLAAC Router Advertisements that broadcast AT&T unfiltered DNS 2600:1702:...::1)*.
   - `DHCPv6`: `Off`.
   - Click **Save**.

---

### Layer 2: Pi-hole DHCP & High-Availability Dual-DNS

1. **Pi-hole Web Admin (`http://192.168.1.92/admin`)**:
   - `DHCP server enabled`: ➔ **`Checked`**.
   - `Range`: `192.168.1.64` to `192.168.1.250`.
   - `Router (gateway) IP`: `192.168.1.254`.
   - `Enable additional IPv6 support (SLAAC + RA)`: ➔ **`Unchecked`**.
2. **DHCP Option 6 Dual-DNS Broadcast (`/etc/dnsmasq.d/02-pihole-dhcp-options.conf`)**:
   ```ini
   # Broadcast both Pi 5 and UGREEN NAS as DNS servers to all LAN clients
   dhcp-option=6,192.168.1.92,192.168.1.80
   ```
   *Guarantees zero downtime if one node ever drops Wi-Fi or reboots.*

---

### Layer 3: Raspberry Pi 5 Operating System (Terminal)
1. **Static IP Binding (Solved the DHCP Chicken-and-Egg Trap)**:
   ```bash
   sudo nmcli connection modify "Rimjhim" ipv4.method manual ipv4.addresses 192.168.1.92/24 ipv4.gateway 192.168.1.254 ipv4.dns "127.0.0.1"
   sudo nmcli connection up "Rimjhim"
   ```
2. **Wi-Fi Sleep / Power-Saving Disabled**:
   - Stored in `/etc/NetworkManager/conf.d/disable-wifi-powersave.conf`:
   ```ini
   [connection]
   wifi.powersave = 2
   ```
3. **Kernel IP Packet Forwarding**:
   - Stored in `/etc/sysctl.d/99-tailscale.conf`:
   ```ini
   net.ipv4.ip_forward = 1
   net.ipv6.conf.all.forwarding = 1
   ```

---

## 3. Key Architectural Decisions & Problem Resolutions

### Problem 1: The IPv6 SLAAC / RDNSS Leak
*   **Symptom**: After disabling AT&T DHCP, ads still popped up on `speedtest.net`. Running `scutil --dns` revealed `nameserver[0] : 2600:1702:6951:6030::1`.
*   **Root Cause**: In IPv6, routers broadcast DNS via **ICMPv6 Router Advertisements (RFC 8106 RDNSS)** even when `DHCPv6` is `Off`. Apple and Android devices prioritize IPv6 over IPv4, bypassing Pi-hole.
*   **Resolution**: Toggled `IPv6: Off` on the AT&T gateway. This stopped RDNSS broadcasts, leaving `192.168.1.92` (Pi-hole) as the sole active nameserver.

### Problem 2: The "DHCP Chicken-and-Egg" Trap
*   **Symptom**: When Wi-Fi reset after saving AT&T router settings, the Pi 5 dropped off the network and could not re-associate.
*   **Root Cause**: The Pi was configured as a DHCP client. Because AT&T's DHCP server was turned off, the Pi had no server to give it an IP address.
*   **Resolution**: Configured a persistent **static IP (`192.168.1.92/24`)** on `wlan0` in NetworkManager.

### Problem 3: Wi-Fi AP Deauth (`reason=7`) & Single Point of Failure (SPOF)
*   **Symptom**: Mac and Smart TV suddenly reported *"Wi-Fi: No Internet Connection..."* while iPhones on cellular still worked.
*   **Root Cause**: The AT&T router sent an 802.11 deauthentication frame (`reason=7`) during periodic channel calibration. `wpa_supplicant` on the Pi 5 put the AP on a 60-second backoff cooldown before reconnecting. Because DHCP only advertised the Pi 5's IP (`192.168.1.92`), whole-home DNS dropped during the 3-minute re-association window.
*   **Resolution**: Added `dhcp-option=6,192.168.1.92,192.168.1.80` to Pi-hole's DHCP config. All devices now automatically receive **both DNS servers**. If the Pi 5 ever drops or reboots, devices seamlessly query the hardwired UGREEN NAS with zero downtime.

---

## 4. Active Curated Blocklists (309,418 Domains)

| Category | Source URL | Purpose |
| :--- | :--- | :--- |
| **General Baseline** | `https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts` | Unified ad & tracker baseline (~93k domains) |
| **Smart TV Ads** | `https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV.txt` | Samsung / LG / Roku telemetry & home screen ads |
| **FireTV Tracking** | `https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/AmazonFireTV.txt` | Amazon FireTV telemetry & ad logging |
| **Malware Defense** | `https://urlhaus.abuse.ch/downloads/hostfile/` | Live malware distribution sites (abuse.ch) |
| **Phishing Defense**| `https://phishing.army/download/phishing_army_blocklist_extended.txt` | Scam & fraudulent banking phishing domains |
| **Curated Mobile** | `https://small.oisd.nl` | OISD curated mobile app ad & tracker list |

- **Gravity Auto-Update**: Pi-hole automatically updates these 6 lists every Sunday at 3:00 AM.
- **Automated HA Sync**: Pi 5 syncs `gravity.db` and custom DNS records to UGREEN NAS every 30 minutes via `/usr/local/bin/sync-pihole-to-nas.sh`.
- **Total Unique Blocked Domains**: **309,418**

---

## 5. Verified Functionality & Test Suite

- `projects/12-pihole/tests/test_pihole.py`: Tests DNS socket listener validation on port 53 and gravity database file integrity.
- **Test Results**: 2/2 passing tests.
