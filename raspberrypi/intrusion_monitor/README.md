# 🛡️ Project 10: Network Intrusion Monitor (Raspberry Pi 5)

> **Context**: Scapy-based network defense daemon detecting ARP spoofing, TCP port scans, and rogue subnet traffic with structured JSON security logging.  
> **Status**: 🟢 **Production / Tested**  
> **Host**: Raspberry Pi 5 (`192.168.1.92`)  
> **Repository**: [`deepshah08/raspberry-pi-5-ecosystem/projects/10-intrusion-monitor`](https://github.com/deepshah08/raspberry-pi-5-ecosystem/tree/main/projects/10-intrusion-monitor)  

---

## 1. Key Components

- **Monitor Engine (`monitor.py`)**: Sniffs raw network frames to maintain an active ARP table, tracks TCP SYN port scan thresholds, and identifies rogue IP addresses outside the home `192.168.1.0/24` subnet.
- **Systemd Service (`intrusion_monitor.service`)**: Runs as a resilient system service with auto-restart.

## 2. Verified Functionality & Test Suite

- `projects/10-intrusion-monitor/tests/test_monitor.py`: Validates ARP spoofing alerts, SYN port scan thresholds, subnet boundary enforcement, JSON logging, and connection history cleanup.
- **Test Results**: 5/5 passing tests.
