# 🔌 Flipper Zero Hardware Add-ons & Expansion Roadmap

> **Context**: Dedicated catalog of physical hardware expansion modules, GPIO pinout requirements, and capabilities to unlock in the future when external hardware is acquired.  
> **Parent Runbook**: [flipper_zero/README.md](README.md)  
> **Status**: 📋 **Future Backlog / Hardware Acquisition Queue**  

---

## 1. GPIO Header Architecture & Pinout Overview

The Flipper Zero features a standard 18-pin 2.54mm pitch GPIO expansion header:

```text
┌──────────────────────────────────────────────────────────────────────────────────────┐
│                            FLIPPER ZERO 18-PIN GPIO HEADER                           │
├────────────────────┬─────────────────────────────┬───────────────────────────────────┤
│ Pin #              │ Pin Name                    │ Hardware Functionality            │
├────────────────────┼─────────────────────────────┼───────────────────────────────────┤
│ Pin 1              │ VCC 5V                      │ 5V Power Output (USB or Boost)    │
│ Pin 2 / 11 / 18    │ GND                         │ Common Ground Reference           │
│ Pin 9              │ 3V3                         │ 3.3V Low-Noise Logic Supply       │
│ Pin 13 / 14        │ TX (USART1) / RX (USART1)   │ Hardware UART Serial Bus          │
│ Pin 15 / 16        │ SCL (I2C1) / SDA (I2C1)     │ Hardware I2C Sensor/EEPROM Bus    │
│ Pin 2 / 3 / 4 / 5  │ SCK / MISO / MOSI / CS      │ Hardware SPI Bus (External Radios)│
└────────────────────┴─────────────────────────────┴───────────────────────────────────┘
```

---

## 2. Expansion Module Wishlist & Acquisition Queue

### Tier 1: Core RF & Wireless Expansion (High Priority)

#### 1. ESP32-S2 / Flipper WiFi Devboard
* **Hardware Specs**: Espressif ESP32-S2-WROVER (802.11 b/g/n, 2.4 GHz, USB-C, PCB antenna + external IPEX connector).
* **Target Applications**:
  * **ESP32 WiFi Marauder**: Packet monitoring, probe request sniffing, deauthentication auditing, and PMKID capture for home Wi-Fi security.
  * **LAN & Homelab Webhook Bridge**: Allows Flipper to trigger HTTP/REST webhooks over local Wi-Fi directly to the Raspberry Pi 5 `n8n` workflow engine (`http://192.168.1.92:5678`).
* **Estimated Cost**: ~$30 (Official) or ~$15 (Community clones).

#### 2. NRF24L01+ 2.4 GHz Transceiver Module
* **Hardware Specs**: Nordic Semiconductor NRF24L01+ 2.4 GHz ISM transceiver with SMA antenna.
* **Target Applications**:
  * **MouseJack Auditing**: Assesses vulnerabilities in non-Bluetooth wireless mice and keyboards that communicate over unencrypted 2.4 GHz protocols.
  * **2.4 GHz Spectrum Sniffing**: Detects frequency-hopping bursts and RF traffic density across 2.400–2.525 GHz.
* **Estimated Cost**: ~$3–$5.

---

### Tier 2: Advanced RF & Specialty Sensors (Medium Priority)

#### 3. All-in-One Multi-Board (e.g. Mayhem / Minnow)
* **Hardware Specs**: Single integrated PCB that combines:
  1. ESP32-S2 (Wi-Fi Marauder)
  2. NRF24L01+ (2.4 GHz MouseJack)
  3. CC1101 + High-Gain SMA Antenna (Extends Sub-GHz range to 100m+)
* **Target Applications**: Complete multi-spectrum transceiver eliminating the need to physically swap individual breadboard modules.
* **Estimated Cost**: ~$40–$55.

#### 4. The "Flippenheimer" Geiger Counter Module
* **Hardware Specs**: High-voltage boost inverter board driving a glass Geiger-Müller radiation tube (J305 or M4011) with pulse output connected to a Flipper GPIO interrupt pin.
* **Target Applications**: Portable beta and gamma radiation detection, background $\mu\text{Sv/h}$ logging, and antique Uranium glass/radium dial inspection.
* **Estimated Cost**: ~$25–$35.

#### 5. MCP2515 SPI-to-CAN Transceiver (Automotive OBD-II)
* **Hardware Specs**: Microchip MCP2515 standalone CAN controller paired with TJA1050 high-speed CAN transceiver and OBD-II connector cable.
* **Target Applications**: Real-time vehicle CAN bus monitoring, decoding dashboard instrument clusters, and sniffing automotive interior sensors.
* **Estimated Cost**: ~$5–$8.

---

## 3. Preparation & Firmware Readiness

1. **Firmware Support**: Core apps like `marauder_gui.fap` and `can_tools.fap` can be flashed in seconds via the local catalog pipeline when hardware arrives.
2. **Current Directive**: Hardware remains in the backlog queue. All current operational workflows prioritize the stock Flipper Zero, onboard Sub-GHz (CC1101), 125 kHz RFID, 13.56 MHz NFC, Infrared, and BadUSB.

---

## 4. References

* **Primary Flipper Runbook**: [README.md](README.md)
* **Hardware Inventory**: [HARDWARE_AND_SYSTEMS_INVENTORY.md](../../HARDWARE_AND_SYSTEMS_INVENTORY.md)
