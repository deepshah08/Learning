# 🗺️ Master Project Roadmap & Execution Queue

A persistent, cross-session Single Source of Truth (SoT) tracking active, completed, and upcoming projects across the home lab, autonomous agent swarm, Raspberry Pi 5, Ugreen NAS, and local AI pipelines.

---

## 🌟 Master Status Overview

| # | Project Name | Domain / Target | Status | Primary Interface / Ports |
| :--- | :--- | :--- | :--- | :--- |
| **01** | **Offline Socratic Tutor** | RAG / Education | 🟡 Staged | Local RAG Pipeline |
| **02** | **Git-Backed Second Brain** | PKM / Documentation | 🟡 Staged | Gitea + Obsidian Webhook |
| **03** | **WhisperX Meeting Indexer** | Audio / Search | 🟡 Staged | Local Diarization SQLite |
| **04** | **UGREEN Photos AI Backup** | Photos / Cloud | 🟢 Production | Native UGOS AI (Deep & Pranali) |
| **05** | **Jellyfin Media Server** | Media Streaming | 🟢 Operational | Port `8096` |
| **06** | **Voice Clone TTS Sandbox** | Audio / ML | 🟡 Staged | Coqui XTTS v2 |
| **07** | **Backup Engine (B2 + Restic)**| Storage / Disaster Recovery | 🟡 Staged | Backblaze B2 Encrypted |
| **08** | **TripDrop Drag & Drop** | Storage / Transfers | 🟢 Staged | Port `8088` |
| **09** | **Stirling-PDF Utility** | Tools / Productivity | 🟡 Queue | Port `8083` |
| **10** | **Intrusion Monitor** | Security / Defense | 🟢 Staged | `ufw` Log Tailing Daemon |
| **11** | **Dead Man's Switch** | Security / Crypto | 🟡 Queue | Shamir's Secret Sharing |
| **12** | **Pi-hole v6 DNS (Primary)** | Network / Privacy | 🟢 Production | Port `53`, `80`, `443` (Pi 5) |
| **13** | **n8n Workflow Automation** | Automation / Pipelines | 🟡 Queue | Port `5678` |
| **14** | **Market Sentiment Tracker** | Finance / News RAG | 🟢 Staged | RSS + Local Ollama |
| **15** | **Financial Pipeline Dashboard** | Finance / Analytics | 🟢 Staged | PDF Parser + PostgreSQL |
| **16** | **Morning Briefing Generator** | Productivity / Podcasts | 🟡 Queue | Whisper Audio Summaries |
| **17** | **Plex + *Arr Automation Stack**| Media Automation (Intel QSV + Hardlinks) | 🟢 Production | Ports `32400`, `9696`, `7878`, `8989`, `8080`, `6767`, `5055`, `8181` |
| **18** | **High-Availability (HA) Dual Pi-hole** | Network / Redundancy | 🟢 Production | Port `53`, `8089` (UGREEN NAS + Gravity-Sync) |
| **19** | **Vaultwarden Password Manager** | Security / Identity | 🟢 Production | Port `8085`, `3012` (UGREEN NAS) |
| **20** | **Homepage Unified Dashboard** | Homelab Management | 🟢 Production | Port `3000` (UGREEN NAS) |
| **21** | **macOS SMB File Sharing** | Storage / Drag-and-Drop | 🟢 Production | Port `445` (`smb://192.168.1.80`) |

---

## 🛠️ Global Execution Protocol for Agents
When initiating a session:
1. Reference this `PROJECTS_ROADMAP.md` to identify dependencies and target ports.
2. Update project status (`🟡 Staged` ➔ `🟢 Production`) upon completing verification.
3. Synchronize changes to `deepshah08/Learning` repository via the `md-writer` skill.
