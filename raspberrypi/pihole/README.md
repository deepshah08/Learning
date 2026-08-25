# 🕳️ Pi-hole v6 & Whole-Home Network DNS: Single Source of Truth

> **Context**: Production deployment of whole-home network ad-blocking with AT&T Fiber Gateway takeover, IPv6 SLAAC leak mitigation, static IP binding, and Tailscale MagicDNS integration.  
> **Host**: Raspberry Pi 5 (`192.168.1.92` Static / Tailscale `100.68.196.14`)  
> **Gateway**: AT&T Fiber BGW210/320 (`192.168.1.254`)  
> **Wi-Fi SSID**: `Rimjhim` (Password: `Restlessinsect`)  
> **Status**: 🟢 Production (100% Whole-Home Ad-Blocking Active)  
> **Last Verified**: 2026-08-21 20:35 PDT

---

## 1. Executive Summary & Verification

Whole-home network ad-blocking is fully active and verified live on client devices. All LAN traffic across laptops, mobile phones (Pixel/iOS), tablets, and smart TVs routes DNS queries exclusively through Pi-hole.

### Live Client Verification (macOS Terminal):
```text
$ scutil --dns | grep -A 2 "nameserver[0]"
  nameserver[0] : 192.168.1.92  <-- 🎯 Pi-hole is the Sole Nameserver

$ dig googleads.g.doubleclick.net +short
0.0.0.0  <-- ✅ 100% Blocked

$ dig speedtest.net +short
151.101.194.219  <-- ✅ Valid Domain Resolved
```

---

## 2. Master Toggle & Configuration Checklist

Below is the complete record of every setting toggled across all 3 layers:

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

### Layer 2: Pi-hole Web Admin (`http://192.168.1.92/admin`)
1. **Settings ➔ DHCP**:
   - `DHCP server enabled`: ➔ **`Checked`**.
   - `Range of IP addresses to hand out`:
     - `From`: **`192.168.1.64`**
     - `To`: **`192.168.1.250`**
   - `Router (gateway) IP address`: **`192.168.1.254`** *(Directs internet traffic at full fiber speed)*.
   - `Netmask`: `255.255.255.0` (or automatic).
   - `Enable additional IPv6 support (SLAAC + RA)`: ➔ **`Unchecked`** *(Prevents no address range available for DHCPv6 warnings)*.
   - Click **Save & Apply**.

---

### Layer 3: Raspberry Pi 5 Operating System (Terminal)
1. **Static IP Binding (Solved the DHCP Chicken-and-Egg Trap)**:
   - When AT&T DHCP was disabled, the Pi needed a static IP so it never relied on an external DHCP server upon boot/reconnect:
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

### Problem 3: Client DHCP Cache Lag
*   **Symptom**: Connected devices held onto the old AT&T router DNS for up to 24 hours.
*   **Resolution**: Toggled Wi-Fi `OFF` ➔ `ON` on client devices (or clicked "Renew DHCP Lease") to instantly fetch Pi-hole configuration.

---

## 4. Active Curated Blocklists (309,414 Domains)

| Category | Source URL | Purpose |
| :--- | :--- | :--- |
| **General Baseline** | `https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts` | Unified ad & tracker baseline (~93k domains) |
| **Smart TV Ads** | `https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV.txt` | Samsung / LG / Roku telemetry & home screen ads |
| **FireTV Tracking** | `https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/AmazonFireTV.txt` | Amazon FireTV telemetry & ad logging |
| **Malware Defense** | `https://urlhaus.abuse.ch/downloads/hostfile/` | Live malware distribution sites (abuse.ch) |
| **Phishing Defense**| `https://phishing.army/download/phishing_army_blocklist_extended.txt` | Scam & fraudulent banking phishing domains |
| **Curated Mobile** | `https://small.oisd.nl` | OISD curated mobile app ad & tracker list |

- **Gravity Auto-Update**: Pi-hole automatically updates these 6 lists every Sunday at 3:00 AM.
- **Total Unique Blocked Domains**: **309,414**
