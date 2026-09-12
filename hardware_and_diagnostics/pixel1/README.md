# Google Pixel 1 (sailfish) — Hardware Diagnostics & Wi-Fi Configuration

> **Context**: Hardware telemetry, battery degradation metrics, and Wi-Fi WPA3-SAE association failure runbook for the Google Pixel 1 (sailfish, Snapdragon 821, Android 10).  
> **Last Verified**: 2026-09-12 16:01 PDT  
> **Status**: 🟢 **Wi-Fi Connected & Verified / ⚠️ Hardware Battery Degraded (Requires Tether or Cell Replacement)**

---

## 1. Device Hardware Profile & Telemetry

| Specification | Value / Metric | Source |
| :--- | :--- | :--- |
| **Model / Codename** | Google Pixel 1 (`sailfish`) | `ro.product.model`, `getprop ro.product.device` |
| **SoC / Chipset** | Qualcomm Snapdragon 821 (MSM8996 Pro) | Hardware specs / kernel |
| **Wi-Fi / BT Subsystem** | Qualcomm WCN3680B (802.11ac, 2.4/5 GHz) | Kernel driver (`wlan0`) |
| **OS Version / Build** | Android 10 (`QP1A.191005.007.A3`) | `ro.build.display.id` |
| **Assigned LAN IP** | `192.168.1.83/24` (wlan0) | `ip addr show wlan0` |
| **Hardware MAC** | `40:4e:36:7f:fb:d9` | Kernel `ip link` |
| **Connected BSSID** | `d8:d8:e5:b3:8d:b0` (SSID: `Rimjhim`, 5GHz) | `dumpsys wifi` |
| **Link Speed / RSSI** | `866 Mbps` (5180 MHz) / `-44 dBm` | `dumpsys wifi` |

---

## 2. Issue 1: Wi-Fi Disconnected / "Forgotten" on Every Reboot

### Symptom
On every phone restart, Wi-Fi would not auto-connect to the home network (`Rimjhim`). It appeared to the user as if the Wi-Fi credentials were "forgotten", requiring manual intervention.

### Root Cause Analysis
1. **Network Infrastructure**: The AT&T Gateway router (`192.168.1.254`, BSSID `d8:d8:e5:b3:8d:af` / `b0`) advertises **WPA2/WPA3-Personal Transition Mode** (mixed mode).
2. **Duplicate Stored Profiles**: Android 10 automatically provisioned **two separate network configurations** for the same SSID `Rimjhim`:
   - `ID: 1`: `KeyMgmt: SAE Protocols: WPA RSN PMF: true` (WPA3-Personal)
   - `ID: 2`: `KeyMgmt: WPA_PSK Protocols: WPA RSN PMF: false` (WPA2-PSK)
3. **Chipset Incompatibility**: Pixel 1's Qualcomm Snapdragon 821 Wi-Fi driver / vendor HAL does not support WPA3-SAE key negotiation.
4. **Scoring Bias**: On boot, Android's `SavedNetworkEvaluator` scored the WPA3-Personal profile higher than the WPA2 profile because Android prioritizes SAE security over PSK.
5. **Association Failure Loop**: Android continuously issued `CMD_START_CONNECT nid=1`, triggering the following kernel `wpa_supplicant` failure:
   ```text
   wpa_supplicant: wlan0: Trying to associate with SSID 'Rimjhim'
   wpa_supplicant: wlan0: WPA: Failed to select authenticated key management type
   wpa_supplicant: wlan0: WPA: Failed to set WPA key management and encryption suites
   ```
   This triggered `Association Rejection code: 0` every 5–10 seconds. Because it was locked in an infinite retry loop on profile 1, it never fell back to profile 2 (WPA2-PSK).
6. **Parasitic Radio Drain**: The constant scanning and association loop drew **164 mAh** from the battery, preventing the Wi-Fi chip from entering low-power DTIM sleep.

### Fix Applied
1. Accessed `Settings > Network & internet > Wi-Fi > Saved networks`.
2. Selected the duplicate `WPA3-Personal` entry (`ID: 1`) and tapped **Forget**.
3. Android immediately fell back to the remaining `WPA2-PSK` entry (`ID: 2`), successfully completed the 4-way EAPOL handshake, and connected at 866 Mbps:
   ```text
   wpa_supplicant: wlan0: Associated with d8:d8:e5:b3:8d:b0
   wpa_supplicant: wlan0: WPA: RX message 1 of 4-Way Handshake from d8:d8:e5:b3:8d:b0 (ver=2)
   wpa_supplicant: wlan0: WPA: Key negotiation completed with d8:d8:e5:b3:8d:b0 [PTK=CCMP GTK=CCMP]
   wpa_supplicant: wlan0: CTRL-EVENT-CONNECTED - Connection to d8:d8:e5:b3:8d:b0 completed
   ```

### Permanent Prevention Recommendation
To prevent Android from auto-generating a WPA3 profile if the network is ever forgotten and re-added:
- Log into the AT&T Gateway router at `http://192.168.1.254`.
- Under **Wi-Fi > Advanced Options**, set the security mode for SSID `Rimjhim` to **WPA2-PSK (AES) only**, or configure a dedicated 2.4GHz IoT SSID with pure WPA2 for legacy hardware.

---

## 3. Issue 2: Severe Battery Percentage Drops

### Symptom
The battery drops abruptly (e.g. from 70–80% down to 1–2%) or shuts down unexpectedly under light usage.

### Telemetry & Hardware Findings
From `/sys/class/power_supply/battery/` and `dumpsys batterystats`:

1. **Physical Cell Aging**:
   - **Factory Design Capacity**: 2,770 mAh
   - **Reported Charge Full**: 2,530 mAh
   - **Cycle Count**: 241 cycles (original OEM battery manufactured ~2016; ~10 years old)
2. **The Voltage Sag Evidence (`dumpsys batterystats`)**:
   ```text
   Discharge step durations:
     #0: +3m48s to 73 (screen-off)
     #1: +10m41s to 74 (screen-off)
     #2: +38s to 2 (screen-on)
   ```
   **The battery dropped from 74% to 2% in 38 seconds immediately upon turning the screen on.**
3. **Internal Resistance (ESR) Collapse**:
   - In standby / screen-off mode, current draw is negligible (~20–50 mA). The battery voltage remains at ~3.8V–4.0V, leading the PMIC fuel gauge to calculate a high State of Charge (SOC ~75%).
   - The moment the screen turns on and the Snapdragon 821 CPU boosts, current draw jumps to 500mA–1.5A.
   - Due to severe chemical aging, the cell's Equivalent Series Resistance (ESR) has spiked. By Ohm's law ($\Delta V = I \cdot R_{\text{internal}}$), the terminal voltage instantly collapses below the critical low-voltage cutoff (~3.3V–3.4V).
   - The Qualcomm SMB charger fuel gauge reads the voltage cliff, recalibrates the estimated SOC down to 1–2%, or triggers emergency brownout shutdown.
4. **Energy Accounting Mismatch**:
   ```text
   Estimated power use:
     Capacity: 2770 mAh, Computed drain: 404 mAh, Actual drain: 2078-2161 mAh
     Unaccounted drain: 1674 mAh
   ```
   The CPU, screen, apps, and radio only consumed **404 mAh**, but the battery lost over **2,000 mAh**. The **1,674 mAh unaccounted loss** confirms pure chemical/hardware cell exhaustion.

### Operational Guidance
- **Software Wakelocks**: Zero active partial wake locks (`Wake Locks: size=0`). The OS software state is clean.
- **Remediation**: Software calibration or cache wiping cannot fix high internal cell resistance. If keeping the Pixel 1 in active portable use, replace the internal Li-ion battery. If used as a stationary homelab display/dashboard/camera, keep it permanently connected to a 5V USB power supply.

---

## 4. Diagnostic CLI Commands

```bash
# Verify ADB connection
adb devices -l

# Check battery fuel gauge status & voltage
adb shell dumpsys battery
adb shell cat /sys/class/power_supply/battery/uevent

# Check battery historical sudden drop steps
adb shell dumpsys batterystats | grep -A 20 "Discharge step durations:"

# Inspect configured Wi-Fi networks
adb shell dumpsys wifi | grep -E -A 10 "Configured networks Begin"

# Check Wi-Fi association and supplicant logs
adb shell 'logcat -d -b all -s "Wifi*" wpa_supplicant | tail -n 30'

# Verify current Wi-Fi link speed and IP
adb shell ip addr show wlan0
adb shell dumpsys wifi | grep "mWifiInfo"
```
