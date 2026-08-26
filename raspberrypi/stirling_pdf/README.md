# 📄 Project 09: Stirling-PDF Utility (Raspberry Pi 5)

> **Context**: Offline, privacy-first PDF manipulation suite (OCR, splitting, merging, redaction) running locally via Docker.  
> **Status**: 🟢 **Production / Tested**  
> **Host**: Raspberry Pi 5 (`192.168.1.92`) | Port: `8083`  
> **Repository**: [`deepshah08/raspberry-pi-5-ecosystem/projects/09-stirling-pdf`](https://github.com/deepshah08/raspberry-pi-5-ecosystem/tree/main/projects/09-stirling-pdf)  

---

## 1. Key Components

- **Docker Compose (`docker-compose.stirling.yml`)**: Deploys `stirlingtools/stirling-pdf` on port `8083` with persistent volume mappings.
- **Validator (`validate_stirling.py`)**: Verifies container health and port bindings.

## 2. Verified Functionality & Test Suite

- `projects/09-stirling-pdf/tests/test_stirling.py`: Validates YAML compose configuration and port mappings.
- **Test Results**: 1/1 passing test.
