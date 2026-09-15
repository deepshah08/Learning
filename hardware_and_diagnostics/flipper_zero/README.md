# 🐬 Flipper Zero (`Epriesol`) — Hardware, Diagnostics & Multi-Tool Runbook

> **Context**: Multi-protocol portable penetration testing, hardware diagnostic, and RF/NFC/IR transceiver tool integrated into the developer and homelab management workflow.  
> **Last Verified**: 2026-09-14  
> **Status**: 🟢 **Production / Healthy (Firmware 1.4.3)**  

---

## 1. Hardware Specifications & Interfaces

```text
┌──────────────────────────────────────────────────────────────────────────────────────┐
│                             FLIPPER ZERO SPECIFICATIONS                              │
├────────────────────────────┬─────────────────────────────────────────────────────────┤
│ Specification              │ Configuration / Ground Truth                            │
├────────────────────────────┼─────────────────────────────────────────────────────────┤
│ Device Name                │ Epriesol                                                │
│ Hardware Model             │ Flipper Zero (Target 7, Hardware Ver 15, Body 9)        │
│ Hardware UID               │ 58688D0127E18000                                        │
│ Core SoC                   │ STM32WB55RG (ARM Cortex-M4 + Cortex-M0+)                │
│ Radio Subsystem            │ CC1101 Sub-GHz (300-928 MHz) + BLE 5.0 (M0+)            │
│ Radio Firmware             │ 1.20.0 (Light Stack)                                    │
│ Installed Firmware         │ Release 1.4.3 (8622f1a2, built 05-12-2025)              │
│ Primary Storage            │ 32GB MicroSD Card (FAT32, ~29.7 GiB, 1-bit SPI)         │
│ Serial Device (macOS)      │ /dev/cu.usbmodemflip_Epriesol1 (CDC ACM 115200)         │
│ Web Management Interface   │ https://lab.flipper.net                                 │
└────────────────────────────┴─────────────────────────────────────────────────────────┘
```

---

## 2. Filesystem & Database Directory Architecture

All persistent user assets reside on the MicroSD card at `/ext`:

```text
/ext/
├── Manifest                      # Firmware and asset checksum manifest
├── apps/                         # Standalone application packages (.fap)
│   ├── Bluetooth/                # hid_ble.fap (BLE presentation/media remote)
│   ├── GPIO/                     # gpio.fap (Pin reader, logic generator)
│   ├── Infrared/                 # infrared.fap (IR transmitter/receiver)
│   ├── NFC/                      # nfc.fap (13.56 MHz NFC reader/emulator)
│   ├── RFID/                     # lfrfid.fap (125 kHz RFID badge cloner)
│   ├── Scripts/                  # Built-in JavaScript execution runtime
│   ├── Sub-GHz/                  # subghz.fap (Radio protocol sniffer/analyzer)
│   ├── USB/                      # bad_usb.fap, hid_usb.fap, u2f.fap (FIDO2)
│   └── iButton/                  # ibutton.fap (1-Wire Dallas key cloner)
├── infrared/                     # Universal & Brand-specific IR payloads
│   ├── Universal_TV.ir           # Universal TV power/mute/volume dictionary
│   ├── Universal_AC.ir           # Universal Air Conditioner control dictionary
│   ├── Universal_Audio.ir        # Soundbar and AV receiver dictionary
│   ├── Universal_Fans.ir         # Ceiling and oscillating fan dictionary
│   ├── Universal_Projectors.ir   # Office & theater projector dictionary
│   └── [Brand_Remotes]/          # Apple_TV, Samsung_TV, LG_TV, Sony_TV, Roku
├── subghz/                       # Sub-GHz frequency files & configuration
│   ├── assets/setting_user       # Frequency unlock (300-348, 387-464, 779-928 MHz)
│   ├── Tesla_Charge_AM650.sub    # Tesla charge port opener (433.92 MHz AM650)
│   └── Tesla_Charge_AM270.sub    # Tesla charge port opener (433.92 MHz AM270)
├── nfc/                          # NFC keys and card dumps
│   └── assets/                   # mf_classic_dict_user.nfc (Mifare Classic dict)
└── badusb/                       # DuckyScript keyboard automation scripts
    ├── Party_Parrot_OSX.txt      # macOS ASCII parrot terminal demo
    ├── OSX_Rickroll.txt          # macOS YouTube audio-visual automation
    ├── Matrix_Wake_Up.txt        # Terminal typewriter effect demo
    ├── GoodUSB.txt               # Harmless USB security audit popup
    └── Hacker_Typer.txt          # Automated typing simulation
```

---

## 3. Known Bugs, Quirks & Resolved Solutions

### A. "MicroSD card not detected" Mount Failure
* **Issue**: Device displays `"MicroSD card not detected. It seems that the MicroSD card is not mounted or damaged. Insert the microSD card into the slot and try again."`
* **Root Cause**: The Flipper Zero communicates with the MicroSD card exclusively via a **1-bit SPI bus** (unlike high-speed 4-bit SDIO on PCs). Generic cards with incompatible cluster sizes (>32KB), multi-partition tables, or loose spring latch seating fail to negotiate SPI communication.
* **Fix Applied**:
  1. Orient the card with **gold pins facing UP** (toward the screen, not the rear shell).
  2. Push firmly until a distinct mechanical click locks the card into the spring slot.
  3. Navigate on the device to **Left / Menu $\rightarrow$ Settings $\rightarrow$ Storage $\rightarrow$ Format SD Card** to initialize FAT32 partition geometry optimized for on-device SPI access.
* **Revert Command**: N/A (Standard hardware seating procedure).

### B. Serial Port Resource Lock (`[Errno 16] Resource busy`)
* **Issue**: Local diagnostic scripts or python CLI automation fail with `[Errno 16] Resource busy: '/dev/cu.usbmodemflip_Epriesol1'`.
* **Root Cause**: Google Chrome (`lab.flipper.net`) holds an exclusive WebSerial lock via macOS `IOUSBHostFamily`.
* **Fix Applied**: Disconnect or close the `lab.flipper.net` browser tab in Chrome before running local serial automation commands.
* **Verification**: Run `lsof /dev/cu.usbmodemflip_Epriesol1` to ensure no browser or terminal process holds the file descriptor.

### C. Web App Store Accidental Installation Clutter
* **Issue**: Bulk installation on Flipper Lab flooded the 128×64 monochrome LCD with 45+ unneeded games, niche tools, and unsupported GPIO plugins.
* **Root Cause**: Clicking "Install" on multiple catalog pages deploys unneeded `.fap` binaries directly into `/ext/apps`.
* **Fix Applied**: Executed an automated serial CLI pruning script to delete 45 third-party applications and empty directories (`Games/`, `Media/`, `Tools/`), preserving only the 10 core official system tools.

### D. Serial CLI Write Throughput Optimization
* **Issue**: Naive serial CLI `storage write_chunk` transfers were artificially limited to ~0.9 KB/s when throttled by fixed `sleep()` delays.
* **Root Cause**: Waiting on arbitrary delays rather than reacting to asynchronous prompt events (`Ready\r\n` and `>: `).
* **Fix Applied**: Implemented an event-driven Python uploader using 4096-byte chunks, achieving **120–131 KB/s** throughput over USB CDC ACM. For bulk multi-gigabyte collections (e.g. full 35,000-file UberGuidoZ archive), an external MicroSD card reader directly on the host Mac remains recommended.

---

## 4. Operational Runbook

### 1. Connecting via Serial CLI
```bash
# Direct interactive serial terminal
screen /dev/cu.usbmodemflip_Epriesol1 115200

# Exit screen session: Press Ctrl+A followed by Ctrl+\
```

### 2. Quick Filesystem & Health Inspection
```python
import serial, time

ser = serial.Serial('/dev/cu.usbmodemflip_Epriesol1', 115200, timeout=2)
ser.write(b'\r\nstorage info /ext\r\n')
time.sleep(0.5)
print(ser.read(ser.in_waiting).decode('utf-8', errors='replace'))
ser.close()
```

### 3. Hard Rebooting the Device
* Press and hold **Back (↩) + Left (◀)** simultaneously for **3 seconds**.
* The device will trigger a hardware watchdog reset and reload the OS from internal flash.

---

## 5. Future Expansion Roadmap & To-Do Queue

### A. Momentum Custom Firmware Integration (Evaluation & To-Do)
* **Status**: 📋 **Planned / Backlog**
* **Primary Motivations**:
  1. **Unlocked Sub-GHz TX Spectrum**: Removes regional geo-blocking in the CC1101 radio driver to allow transmission/replay on custom gate and vehicle bands (e.g. 300–348 MHz, 387–464 MHz, 779–928 MHz).
  2. **Device-Level Security (PIN Lock)**: Adds a startup and idle button-sequence PIN lock to protect sensitive NFC keys, Sub-GHz captures, and 2FA credentials if physically lost or stolen.
  3. **On-Device File Manager**: Full filesystem navigation directly on the LCD screen (copy, paste, rename, and hex-preview files on `/ext`).
  4. **Custom BLE Personas**: Disguise Bluetooth advertising identity (name, MAC address, appearance) for advanced security auditing.
* **Trade-Offs & Known Constraints**:
  - **App Store Sync**: Potential API drift from official `lab.flipper.net` builds; will rely on Momentum's integrated app catalog.
  - **RF Responsibility**: Hardware filters are unlocked; operator is responsible for avoiding restricted/emergency radio frequencies.
  - **Battery Impact**: Standby run-time slightly reduced from ~7–10 days to ~5–7 days due to richer background hooks.
  - **Mobile BLE Re-pairing**: May require "Forgetting Device" in phone Bluetooth settings when switching firmwares.
* **Execution Runbook (When Ready)**:
  1. Create a full SD card snapshot via CLI or card reader.
  2. Connect to [https://momentum-fw.dev](https://momentum-fw.dev) in Chrome via WebUSB.
  3. Flash the latest release build (preserves existing SD card assets).
  4. Set PIN lock under `Settings -> Security`.

### B. Hardware Expansion Modules (GPIO Header)
* **ESP32-S2 / WiFi Devboard**: Adds 802.11 Wi-Fi packet monitoring, Marauder deauthentication auditing, and direct webhook dispatching to Raspberry Pi 5 `n8n` (`http://192.168.1.92:5678`).
* **NRF24L01+ Module**: Adds 2.4 GHz transceiver for wireless mouse/keyboard auditing (MouseJack) and 2.4 GHz spectrum sniffing.
* **All-in-One Multi-Board (Mayhem)**: Combines ESP32 + NRF24 + amplified external CC1101 SMA antenna (100m+ RF range).

---

## 6. References & Cross-Links

* **Single Source of Truth Inventory**: [HARDWARE_AND_SYSTEMS_INVENTORY.md](../../HARDWARE_AND_SYSTEMS_INVENTORY.md)
* **Master Documentation Index**: [README.md](../../README.md)
* **Official Flipper Documentation**: [https://docs.flipper.net](https://docs.flipper.net)
* **Flipper Lab (Apps & Web Serial)**: [https://lab.flipper.net](https://lab.flipper.net)
* **Momentum Firmware Portal**: [https://momentum-fw.dev](https://momentum-fw.dev)

