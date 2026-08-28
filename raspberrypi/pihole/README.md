# 🕳️ Pi-hole v6 & Whole-Home Network DNS: Single Source of Truth

> **Context**: Production deployment of whole-home network ad-blocking with AT&T Fiber Gateway takeover, IPv6 SLAAC leak mitigation, static IP binding, High-Availability Dual-DNS DHCP broadcasting to UGREEN NAS, and Tailscale MagicDNS integration.  
> **Primary Host**: Raspberry Pi 5 (`192.168.1.92` Static / Tailscale `100.68.196.14`)  
> **Secondary Host**: UGREEN DXP2800 NAS (`192.168.1.80` Static 2.5GbE)  
> **Gateway**: AT&T Fiber BGW210/320 (`192.168.1.254`)  
> **Wi-Fi SSID**: `Rimjhim` (5GHz BSSID: `D8:D8:E5:B3:8D:B0`)  
> **Status**: 🟢 Production (100% High-Availability Ad-Blocking Active)  
> **Last Verified**: 2026-08-27 22:52 PDT

---

## 1. Executive Summary & Verification

Whole-home network ad-blocking is fully active and verified live on client devices. All LAN traffic across laptops, mobile phones (Pixel/iOS), tablets, and smart TVs routes DNS queries through our High-Availability Dual-Pi-hole cluster (Primary: Pi 5, Secondary: UGREEN NAS).

### Live Client Verification:
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

### Layer 2: Pi-hole v6 DHCP Core (`/etc/pihole/pihole.toml`)

In **Pi-hole v6**, configuration is managed via `pihole.toml`. Both `etc_dnsmasq_d` and `dnsmasq_lines` must be explicitly configured:

```toml
[dhcp]
  active = true
  start = "192.168.1.64"
  end = "192.168.1.250"
  router = "192.168.1.254"
  ipv6 = false  # CRITICAL: Must be false to eliminate [::] blackhole & Android Private DNS drops

[misc]
  etc_dnsmasq_d = true
  dnsmasq_lines = [
    "dhcp-option=6,192.168.1.92,192.168.1.80"
  ]
```

* **DHCP Option 6**: Injects `192.168.1.92` (Pi 5) and `192.168.1.80` (UGREEN NAS) as dual DNS nameservers into all DHCP leases.
* **`ipv6 = false`**: Eliminates bogus `[::]` IPv6 DNS broadcasts, resolving Pixel / Android captive portal timeouts and Apple Private Relay hangs.

---

### Layer 3: Raspberry Pi 5 Wi-Fi Stabilization & NetworkManager
1. **Static IP & 5GHz BSSID Lock (Prevents 2.4GHz Hopping Outages)**:
   ```bash
   sudo nmcli connection modify "Rimjhim" ipv4.method manual ipv4.addresses 192.168.1.92/24 ipv4.gateway 192.168.1.254 ipv4.dns "127.0.0.1"
   sudo nmcli connection modify "Rimjhim" 802-11-wireless.bssid "D8:D8:E5:B3:8D:B0"
   sudo nmcli connection modify "Rimjhim" 802-11-wireless.band "a"
   sudo nmcli connection modify "Rimjhim" ipv6.method "disabled"
   sudo nmcli connection up "Rimjhim"
   ```
2. **Wi-Fi Power-Saving Disabled**:
   - Stored in `/etc/NetworkManager/conf.d/disable-wifi-powersave.conf`:
   ```ini
   [connection]
   wifi.powersave = 2
   ```

---

## 3. Incident Post-Mortems & Architectural Resolutions

### Problem 1: The IPv6 SLAAC / RDNSS Leak
*   **Symptom**: Ads popped up on `speedtest.net`. `scutil --dns` revealed `nameserver[0] : 2600:1702:...::1`.
*   **Root Cause**: In IPv6, routers broadcast DNS via **ICMPv6 Router Advertisements (RFC 8106 RDNSS)** even when `DHCPv6` is `Off`.
*   **Resolution**: Toggled `IPv6: Off` on the AT&T gateway to eliminate SLAAC unfiltered DNS.

### Problem 2: The "DHCP Chicken-and-Egg" Trap
*   **Symptom**: Pi 5 dropped off network upon reboot.
*   **Root Cause**: Pi was a DHCP client with no external DHCP server to assign an IP.
*   **Resolution**: Configured a persistent **static IP (`192.168.1.92/24`)** on `wlan0`.

### Problem 3: The IPv6 `[::]` Blackhole (Pixel 9 Pro XL & Apple Private Relay)
*   **Symptom**: Pixel 9 Pro XL showed *"Failed to connect / No internet"* while Apple laptops hung on *"Limit IP Address Tracking"* probes.
*   **Root Cause**: `dhcp.ipv6 = true` was active in `pihole.toml` without a configured IPv6 subnet, causing Pi-hole to advertise `[::]` as the primary IPv6 DNS. Android and Apple devices tried to reach `[::]`, timed out on captive portal checks (`connectivitycheck.gstatic.com`), and dropped off Wi-Fi.
*   **Resolution**: Set `dhcp.ipv6 = false` in `pihole.toml` and disabled IPv6 on Pi 5 NetworkManager. Clean IPv4 DHCP with Dual-DNS (`192.168.1.92, 192.168.1.80`) is now broadcasted exclusively.
