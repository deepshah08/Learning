# 🧳 Project 08: TripDrop Staging Portal (Raspberry Pi 5)

> **Context**: High-speed, local zero-configuration drag-and-drop web portal for instant photo/video ingestion from SD cards and mobile devices on LAN.  
> **Status**: 🟢 **Production / Tested**  
> **Host**: Raspberry Pi 5 (`192.168.1.92`) | Port: `8088`  
> **Repository**: [`deepshah08/raspberry-pi-5-ecosystem/projects/08-trip-drop`](https://github.com/deepshah08/raspberry-pi-5-ecosystem/tree/main/projects/08-trip-drop)  

---

## 1. Key Components

- **FastAPI Server (`server.py`)**: Asynchronous chunked file upload endpoint supporting multi-gigabyte RAW and 4K video drops without RAM bloat.
- **mDNS / Zeroconf (`_tripdrop._tcp.local.`)**: Broadcasts service capability on LAN for zero-config client discovery.

## 2. Verified Functionality & Test Suite

- `projects/08-trip-drop/tests/test_trip_drop.py`: Tests health probe, mDNS peer endpoint, and chunked upload handling.
- **Test Results**: 2/2 passing tests.
