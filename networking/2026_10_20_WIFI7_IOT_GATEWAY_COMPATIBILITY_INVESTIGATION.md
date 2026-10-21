# Investigation: Wi-Fi 7 Gateway Outage, IoT Association Failures & Packet Filter Collisions

> **Date**: 2026-10-20  
> **Status**: RESOLVED (Root Cause Identified & Persisted)  
> **Severity**: SEV-0 (Smart Plugs Offline, Roommate Streaming Disrupted, Wi-Fi "!" Captive Portal Stalls)  
> **Target Hardware**: AT&T BGW620-700 Gateway (`192.168.1.254`, Firmware `5.40.4`), Raspberry Pi 5 (`192.168.1.92`, Pi-hole v6 FTL)  
> **Companion Architecture**: [WIFI7_GATEWAY_AND_IOT_COEXISTENCE_ARCHITECTURE.md](./WIFI7_GATEWAY_AND_IOT_COEXISTENCE_ARCHITECTURE.md)

---

## 1. Incident Timeline & Reported Symptoms

```text
+----------------------------------------------------------------------------------------+
|                                    INCIDENT TIMELINE                                   |
+-------------------+--------------------------------------------------------------------+
| Timestamp         | Event / Observed Behavior                                          |
+-------------------+--------------------------------------------------------------------+
| 2026-10-19 04:04  | AT&T BGW620 Wi-Fi driver crash; kernel watchdog reboots gateway.   |
| 2026-10-19 04:07  | Gateway cold boot; in-memory ARP & conntrack state completely lost.|
| 2026-10-19 ~23:00 | Roommates report streaming stalls on Roku TV and Wi-Fi disconnects.|
| 2026-10-20 Morning| Smart Plugs (AiDot BK7231) offline; replugging fails to associate. |
| 2026-10-20 Midday | Work & Personal MacBooks experience 2-5 min "!" No Internet delay  |
|                   | before obtaining DHCP lease.                                       |
| 2026-10-20 20:33  | Gateway switched to Max Interoperability (G/N, pure WPA2);         |
|                   | Smart Plugs 2 & 3 associate immediately on 2.4 GHz Channel 10.     |
+-------------------+--------------------------------------------------------------------+
```

---

## 2. Forensic Hypotheses & Empirical Verification

### Hypothesis 1: Pi-hole v6 DHCP Engine Failure
- **Hypothesis**: Pi-hole v6 FTL daemon stopped responding to DHCPDISCOVER broadcasts, causing all home devices to stall on fallback APIPA addresses (`169.254.x.x`).
- **Audit & Evidence**:
  - Live probe on Pi 5 (`192.168.1.92`) verified `pihole-FTL` active with `Nice=-10`, `OOMScoreAdjust=-1000`.
  - Checking `pihole.toml` revealed `dhcp.hosts` had been populated with in-memory host structures during morning triage. Every time FTL restarted, it reloaded leases from scratch.
  - However, Pi-hole was actively processing DHCP requests for the MacBooks and phones once packets reached `eth0`.
- **Verdict**: **Partially Contributing / Secondary**. Volatile `dhcp.hosts` lacked static reservations, but Pi-hole was alive and functioning. The primary drop occurred upstream before packets ever reached Pi-hole.

---

### Hypothesis 2: Gateway L2/L3 Packet Filters Dropping Cold Broadcasts
- **Hypothesis**: The AT&T Gateway's internal switch dropped DHCP broadcast frames originating from unassigned IP addresses (`0.0.0.0`).
- **Audit & Evidence**:
  - Inspection of `/cgi-bin/packetfilter.ha` revealed `Packet Filter = On`.
  - Inspection of `/cgi-bin/dosprotect.ha` revealed:
    - `Reflexive ACL = On`
    - `Drop incoming ICMP Echo requests to Device LAN = On`
    - `Drop incoming ICMP Echo requests to Device WAN = On`
  - In `/cgi-bin/eventlog.ha`, dozens of dropped frames were logged per minute with:
    ```text
    Firewall Drop: Reason: IP Source Address (src=0.0.0.0, dst=255.255.255.255, proto=UDP/67)
    ```
  - **Mechanics**: Modern MacBooks and IoT devices performing cold boot transmit DHCPDISCOVER from `0.0.0.0:68` to `255.255.255.255:67`. The gateway's anti-spoofing filter flagged `0.0.0.0` as an invalid source IP on the LAN bridge and dropped it. Furthermore, Reflexive ACLs rejected incoming traffic with no matching outbound state.
- **Verdict**: **CONFIRMED (Primary Blocker for Initial Association)**. Disabling Packet Filters and Reflexive ACLs immediately restored sub-second DHCPACK responses for both MacBooks and iPhones.

---

### Hypothesis 3: Wi-Fi 7 Protocol Mismatch & Management Frame Rejections on 2.4 GHz
- **Hypothesis**: Cheap 2.4 GHz IoT smart plugs and the Roku TV cannot parse Wi-Fi 7 (`802.11be`) management frames or WPA3 Protected Management Frames (PMF).
- **Audit & Evidence**:
  - Inspecting `/cgi-bin/wconfig.ha` revealed:
    - `standard = gnaxbe` (802.11g/n/ax/be on 2.4 GHz)
    - `mode_switch = custom`
    - `wpaversion = 2-3` (`WPA3-Personal-Transition`)
  - The AT&T BGW620-700 transmits Wi-Fi 7 Multi-Link Operation (MLO) and Target Wake Time (TWT) information elements inside its 2.4 GHz beacon frames.
  - Low-cost IoT microcontrollers (Tuya / AiDot Shanghai Beken BK7231N chips) have fixed 802.11b/g/n state machines. When receiving 802.11be beacon elements and WPA3-Transition PMF negotiation frames, their firmware fails beacon parsing or encounters driver buffer overflows, triggering continuous disassociation.
  - The gateway event log recorded **over 2,350 deauth frames** targeting the smart plug MAC addresses (`04:b2:47:c6:xx:xx`).
  - Furthermore, in `lanstatistics.ha`, the router misclassified the 2.4 GHz Roku TV as `Wi-Fi 6 GHz` due to aggressive band-steering.
- **Verdict**: **CONFIRMED (Root Cause of IoT & TV Outage)**. Legacy IoT hardware cannot tolerate Wi-Fi 7 beacons or PMF on the 2.4 GHz band.

---

## 3. Why the Failure Emerged Today (The "Warm Unicast" Illusion)

The central operational question: **Why did this infrastructure work stably for 60 days before failing catastrophically today?**

```text
+----------------------------------------------------------------------------------------+
|                       WARM STEADY-STATE vs COLD BOOT COLLISION                         |
+----------------------------------------------------------------------------------------+
|                                                                                        |
| 1. WARM STEADY-STATE (Last 60 Days):                                                   |
|    [Device (192.168.1.x)] ──Unicast DHCPREQUEST──> [Pi-hole (192.168.1.92)]            |
|    • Valid IP in header (192.168.1.x)                                                  |
|    • Bypasses Gateway "IP Source Address" anti-spoofing filter.                        |
|    • Matches existing conntrack state in Reflexive ACL.                                |
|    • Established WPA session; no 802.11 association re-negotiation.                    |
|                                                                                        |
| 2. COLD BOOT DISASTER (Oct 19 04:04 AM Router Crash):                                  |
|    [Device (0.0.0.0)] ────Broadcast DISCOVER────> [AT&T Gateway Switch]                |
|                                                          │                             |
|                                               [Packet Filter / ACL]                    |
|                                                          │                             |
|                                                          ▼                             |
|                                                  DROPPED (Anti-Spoof)                  |
|                                               (Never reaches Pi-hole!)                 |
|                                                                                        |
| 3. SIMULTANEOUS IOT BEACON REJECTION:                                                  |
|    [AT&T Gateway] ──Wi-Fi 7 Beacons (MLO/TWT/PMF)──> [AiDot BK7231 Plug]               |
|                                                              │                         |
|                                                              ▼                         |
|                                                     FIRMWARE CRASH /                   |
|                                                     2,350+ DEAUTH LOOP                 |
+----------------------------------------------------------------------------------------+
```

1. **Unicast Lease Renewals**:
   - RFC 2131 dictates that once a client acquires an IP lease, subsequent renewals at $T_1$ (50% lease time) and $T_2$ (87.5% lease time) are transmitted via **direct unicast UDP** (`192.168.1.x ➔ 192.168.1.92`).
   - Unicast packets contain valid source IP addresses. The gateway's `0.0.0.0` anti-spoofing filter was never triggered, and Reflexive ACLs recognized established bidirectional state.
2. **The Router Reboot Trigger**:
   - The gateway had not undergone a cold reboot for 2 months.
   - When the Wi-Fi driver crashed at 04:04 AM on Oct 19, the hardware switch wiped all connection-tracking and ARP tables from RAM.
   - Every client in the home was forced to begin from scratch with a cold broadcast discovery (`0.0.0.0 ➔ 255.255.255.255`), exposing the latent firewall drop rules that had been hidden during steady-state operation.

---

## 4. Programmatic Reversing of Gateway Web Authentication

To eliminate manual click-paths and prevent human error, the AT&T BGW620 web interface was audited and automated via Python:

### Authentication Architecture:
1. **Challenge Extraction**: A GET request to `/cgi-bin/wconfig.ha` returns a 64-character hexadecimal `nonce` and sets a session cookie.
2. **Hashing Algorithm**:
   - In `/cgi-bin/login.ha`, an inline script executes `hashpwd()`:
     $$\text{hashpassword} = \text{MD5}(\text{password} + \text{nonce})$$
   - The cleartext password field is masked with asterisks (`*` repeated for `len(password)`).
3. **Multi-Stage Commit**:
   - Submitting Wi-Fi configuration changes triggers a 302 redirect to `/cgi-bin/wifiwarn.ha?11` (or `wifiwarn_advanced.ha`).
   - The warning page presents an intermediate form with a new `nonce` and a `Continue=Continue` submit button.
   - Form 0 must be POSTed back to `/cgi-bin/wconfig_unified.ha` to commit the hardware register update and restart the Wi-Fi radio subsystem.

---

## 5. Verification & Live Operational State

Following the programmatic commit of `Max Interoperability`:

```bash
# Gateway lanstatistics.ha output (2026-10-20 20:35):
['Wi-Fi Radio Status', 'Enabled', 'Enabled', 'Enabled']
['Mode', 'G/N', 'N/AC/AX/BE', 'AX/BE']
['Bandwidth', '20MHz', '80MHz', '320MHz']
['MLO Status', 'Disabled', 'Disabled', 'Disabled']
```

- **2.4 GHz Band**: Running pure `G/N` (802.11g/n). Wi-Fi 7 MLO is **Disabled**.
- **5 GHz Band**: Running `N/AC/AX/BE` on Channel 149/153. Macs and mobile devices maintain full Wi-Fi 6/7 gigabit throughput.
- **6 GHz Band**: Running `AX/BE` on Channel 165 for Pixel 9 Pro XL and modern laptops.
- **Smart Plugs**: Smart Plug 2 (`192.168.1.64`, $-50\text{ dBm}$) and Smart Plug 3 (`192.168.1.149`, $-49\text{ dBm}$) successfully associated on Channel 10.
