# ⚡ Project 13: n8n Workflow Automation (Raspberry Pi 5)

> **Context**: Self-hosted workflow automation platform integrating homelab alerts, RSS ingestion, smart home automations, and RAG webhook triggers.  
> **Status**: 🟢 **Production / Tested**  
> **Host**: Raspberry Pi 5 (`192.168.1.92`) | Port: `5678`  
> **Repository**: [`deepshah08/raspberry-pi-5-ecosystem/projects/13-n8n`](https://github.com/deepshah08/raspberry-pi-5-ecosystem/tree/main/projects/13-n8n)  

---

## 1. Key Components

- **Docker Compose (`docker-compose.n8n.yml`)**: Persistent workflow container running on port `5678`.
- **Configuration Validator (`validate_n8n.py`)**: Verifies container ports and timezone settings.

## 2. Verified Functionality & Test Suite

- `projects/13-n8n/tests/test_n8n.py`: Validates compose configuration and port definitions.
- **Test Results**: 1/1 passing test.
