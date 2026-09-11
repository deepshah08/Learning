# 🛡️ LAN Client Diagnostics & RF Interference Troubleshooting Runbook

> **Scope**: Standard Operating Procedure (SOP) and automated diagnostic toolkit for troubleshooting Wi-Fi/Ethernet client disconnects, latency jitter, dual-server DHCP conflicts, and hardware RF attenuation across the homelab network.  
> **Tool Location**: `networking/tools/diagnose_client.sh`  
> **Primary DNS/DHCP Node**: Raspberry Pi 5 (`192.168.1.92` Gigabit Wired)  
> **Secondary Standby Node**: UGREEN DXP2800 NAS (`192.168.1.80` 2.5GbE Wired)  
> **Gateway Router**: AT&T Fiber BGW320 (`192.168.1.254`)

---

## ⚡ 1. Quickstart: 10-Second Automated Client Audit

When any client device (Pixel, Mac, iPhone, Smart TV) experiences connectivity stalls, buffering, or drops, execute the diagnostic suite from your workstation terminal:

```bash
# Diagnose any client by IP (defaults to 192.168.1.98 if omitted)
./networking/tools/diagnose_client.sh 192.168.1.98
```

### The 5-Layer Diagnostic Sequence:
```text
[1/5] Probing Layer 2 ARP Neighbor State on Pi 5...
      ➔ Checks MAC reachability, resolves factory vs randomized MACs.
[2/5] Inspecting DHCP Leases & Static Reservations...
      ➔ Audits /etc/pihole/dhcp.leases and verifies zero duplicate static host entries on NAS.
[3/5] Auditing Recent DHCP Transactions for Conflicts...
      ➔ Scans for DHCPNAK rejections and "wrong server-ID" offer races.
[4/5] Running 15-Packet Latency, Jitter & DTIM Power-Save Profiler...
      ➔ Calculates min/avg/max/mdev, distinguishing true RF degradation from 802.11 sleep.
[5/5] Auditing DNS Query Stream for Captive Portal Probes...
      ➔ Inspects live Pi-hole resolution and flags connectivitycheck.gstatic.com captive portal triggers.
```

---

## 🔬 2. Hardware RF Interference & Case Physics

Recent empirical investigations uncovered that client-side physical accessories can completely destabilize 5 GHz Wi-Fi performance without any network-layer fault.

```text
+-------------------------------------------------------------------------+
|                  PIXEL 9 PRO XL RF INTERFERENCE DIAGRAM                 |
+-------------------------------------------------------------------------+
|                                                                         |
|   +-----------------------------------------------------------------+   |
|   |                       CAMERA VISOR (Top Edge)                   |   |
|   |   [ High-band 5 GHz / 6 GHz Wi-Fi & mmWave Perimeter Feedlines ]|   |
|   +-----------------------------------------------------------------+   |
|                                    |                                    |
|                                    v [Near-Field Reactive Coupling]     |
|   +-----------------------------------------------------------------+   |
|   |  ⚠️ METAL MAGSAFE RING / STICKER PLATE ATTACHED TO PHONE COVER   |   |
|   |  - Conductive metal inside the reactive near-field (<5mm)       |   |
|   |  - Detunes resonant frequency away from 5.18 GHz (Ch 36)        |   |
|   |  - VSWR spikes -> Transmit power reflected back into amplifier  |   |
|   |  - Faraday RF shielding blocks 5.8cm wavelength Wi-Fi waves     |   |
|   +-----------------------------------------------------------------+   |
|                                    |                                    |
|                                    v [In-Band RF Desense]               |
|   +-----------------------------------------------------------------+   |
|   |  🎙️ HEYPOCKET / MAGSAFE HARDWARE PUCK (52g Battery + Radios)     |   |
|   |  - Dual Bluetooth & 2.4/5GHz radios pressed to rear glass       |   |
|   |  - Broadcom/Qualcomm modem downshifts MCS: 1024-QAM -> QPSK     |   |
|   |  - Result: 800 Mbps link collapses to 6 Mbps + 500ms jitter     |   |
|   +-----------------------------------------------------------------+   |
|                                                                         |
+-------------------------------------------------------------------------+
```

### Key Physical Lessons:
1. **Antenna Detuning**: A conductive metal ring/kickstand placed on the rear cover sits directly inside the **reactive near-field** of the phone's internal PIFA/patch antennas. It detunes the antenna's impedance match, reducing Effective Radiated Power (ERP).
2. **The "Death Grip" Synergy**: Holding the phone by a metal grip combines metal RF reflection with human hand tissue absorption (saltwater absorbs 5 GHz energy), attenuating the signal by 15–25 dBm.
3. **MCS Index Collapse**: Under high packet-loss conditions, 802.11 rate adaptation algorithms drop modulation down to basic BPSK/QPSK modes. This collapses bandwidth from 800+ Mbps down to single-digit Mbps.
4. **Remediation**: Use non-metallic phone cases. If mounting an accessory (like HeyPocket), detach it when browsing or streaming at home, or use plastic/silicone attachments.

---

## 📻 3. Local Ad-Hoc Wi-Fi Hotspot Conflict (HeyPocket Case Study)

AI voice recorders and peripheral devices (like HeyPocket) that sync audio over Wi-Fi introduce a specific architectural failure on Android:

1. **The Mechanism**: Because Bluetooth LE throughput is capped at ~1–2 Mbps, the peripheral spins up an **ad-hoc local Wi-Fi hotspot** (`PKT-XXXXXX`) to transfer bulk audio files.
2. **The Failure**: The companion mobile app commands Android to switch Wi-Fi networks from the home router (`Rimjhim`) to `PKT-XXXXXX`.
3. **The Blackout**: The ad-hoc hotspot has **zero WAN routing**. Android's network validator immediately flags the connection as "No Internet" (`connectivitycheck.gstatic.com`), causing the OS to flap between cellular and Wi-Fi, severing local LAN connectivity.
4. **Mitigation**:
   - On Android: Disable **"Switch to mobile data automatically"** under Wi-Fi preferences.
   - In Companion App: Disable continuous background auto-sync; configure sync to manual or use **USB-C direct wire sync**.

---

## ⚙️ 4. Split-Scope Dual DHCP Invariant Rules

In an **Active-Active Dual DHCP network** (Pi 5 Primary + NAS Secondary Standby):

```text
+-------------------------------------------------------------------------+
|                  SPLIT-SCOPE DUAL DHCP ARCHITECTURE                     |
+-------------------------------------------------------------------------+
|                                                                         |
|   [ PRIMARY: Raspberry Pi 5 ]            [ SECONDARY: UGREEN NAS ]      |
|   • Pool: 192.168.1.64 - 189             • Pool: 192.168.1.190 - 250    |
|   • All Client Static Reservations       • Standby Dynamic Pool ONLY    |
|   • no-dhcp-interface=wlan0              • port=0 (DHCP-only mode)      |
|   • Non-Authoritative Coexistence        • Non-Authoritative Coexistence|
|                                                                         |
+-------------------------------------------------------------------------+
```

### The Golden Rule: Zero Duplicate Static Reservations
- **Rule**: Client static reservations (e.g. `dhcp-host=...,192.168.1.98,Pixel9ProXL`) MUST reside **exclusively on Primary Pi 5**.
- **The Violation Trap**: If NAS also defines `dhcp-host=...,192.168.1.98`, NAS's 2.5GbE interface races Pi 5 and answers first. When the client acknowledges NAS (`server-id: 192.168.1.80`), Pi 5 sees a request for its reserved IP with another server's ID and broadcasts:
  ```text
  DHCPNAK(eth0) 192.168.1.98 wrong server-ID
  ```
  This immediately invalidates the client's network lease on Android and tears down Wi-Fi.

---

## 📈 5. Baseline Metric Matrix

| Metric | Healthy Active Wi-Fi | 802.11 DTIM Sleep | Hardware/RF Degraded |
| :--- | :--- | :--- | :--- |
| **Ping Latency (min/avg)** | `2.5 ms / 3.5 ms` | `2.5 ms / 15 ms` | `100 ms / 500+ ms` |
| **Jitter (`mdev`)** | `< 1.0 ms` | Variable (bursts) | `> 100 ms` |
| **Packet Loss** | `0.0%` | `0.0%` | `> 10.0%` |
| **DHCP NAKs** | `0` | `0` | `Repeated wrong server-ID` |
| **DNS Resolution** | `< 1.0 ms` (cached) | `< 1.0 ms` | `Stalls / Timeouts` |

---

## 🚀 6. Verification and Recovery Protocol

If a client device behaves erratically:
1. Run `./networking/tools/diagnose_client.sh <IP>`.
2. If `DHCPNAK` is detected, verify `cat /volume2/docker/dhcp_server/dnsmasq.conf` on NAS has no conflicting `dhcp-host` line.
3. If high latency (>500ms) is continuous, remove any metal phone covers, MagSafe rings, or external wireless accessories.
4. Toggle Wi-Fi OFF and ON on the client to force a clean, conflict-free DHCP handshake with Pi 5.
