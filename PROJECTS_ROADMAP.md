# 🗺️ Master Project Roadmap & Execution Queue

A persistent, cross-session Single Source of Truth (SoT) tracking active, completed, and upcoming projects across the home lab, autonomous agent swarm, Raspberry Pi 5, Ugreen NAS, and local AI pipelines.

---

## 🌟 Master Status Overview

| # | Project Name | Domain / Target | Status | Primary Interface / Ports |
| :--- | :--- | :--- | :--- | :--- |
| **01** | **Offline Socratic Tutor** | RAG / Education | 🟡 Staged | Local RAG Pipeline |
| **02** | **Git-Backed Second Brain** | PKM / Documentation | 🟡 Staged | Gitea + Obsidian Webhook |
| **03** | **WhisperX Meeting Indexer** | Audio / Search | 🟡 Staged | Local Diarization SQLite |
| **04** | **Immich Photo Backup** | Photos / Cloud | 🟡 Staged | Port `8084` + Pixel 1 Sync |
| **05** | **Jellyfin Media Server** | Media Streaming | 🟢 Operational | Port `8096` |
| **06** | **Voice Clone TTS Sandbox** | Audio / ML | 🟡 Staged | Coqui XTTS v2 |
| **07** | **Backup Engine (B2 + Restic)**| Storage / Disaster Recovery | 🟡 Staged | Backblaze B2 Encrypted |
| **08** | **TripDrop Drag & Drop** | Storage / Transfers | 🟢 Staged | Port `8088` |
| **09** | **Stirling-PDF Utility** | Tools / Productivity | 🟡 Queue | Port `8083` |
| **10** | **Intrusion Monitor** | Security / Defense | 🟢 Staged | `ufw` Log Tailing Daemon |
| **11** | **Dead Man's Switch** | Security / Crypto | 🟡 Queue | Shamir's Secret Sharing |
| **12** | **Pi-hole v6 DNS Ad-Blocker** | Network / Privacy | 🟢 Production | Port `53`, `80`, `443` |
| **13** | **n8n Workflow Automation** | Automation / Pipelines | 🟡 Queue | Port `5678` |
| **14** | **Market Sentiment Tracker** | Finance / News RAG | 🟢 Staged | RSS + Local Ollama |
| **15** | **Financial Pipeline Dashboard** | Finance / Analytics | 🟢 Staged | PDF Parser + PostgreSQL |
| **16** | **Morning Briefing Generator** | Productivity / Podcasts | 🟡 Queue | Whisper Audio Summaries |
| **17** | **Plex + *Arr Automation Stack**| Media Automation (Intel QSV + Hardlinks) | 🟢 Operational (UGREEN NAS) | Ports `32400`, `9696`, `7878`, `8989`, `8080`, `6767`, `5055`, `8181` |
| **18** | **High-Availability (HA) Dual Pi-hole** | Network / Redundancy | 🆕 **Ready to Execute** | **Ugreen NAS DXP 2800 (Docker) + Pi 5 (Gravity-Sync)** |

---

## 🚀 Newly Added: Project 18 — High-Availability (HA) Dual Pi-hole

### Objective:
Eliminate the Single Point of Failure (SPOF) for whole-home DNS ad-blocking by deploying a synchronized secondary Pi-hole container on the **Ugreen NAS DXP 2800** paired with the primary Pi-hole on the **Raspberry Pi 5**.

### Key Architecture Components:
1. **Primary DNS**: Raspberry Pi 5 (`192.168.1.92` / `100.68.196.14`).
2. **Secondary DNS**: Ugreen NAS DXP 2800 (`192.168.1.80` via Docker).
3. **Gravity-Sync**: Automated background sync daemon mirroring blocklists, whitelists, regex, and local DNS records between Pi 5 and NAS.
4. **Zero-Outage Guarantee**: If either device reboots, updates, or loses power, 100% of DNS queries resolve instantly with 0ms interruption to household users.

---

## 🛠️ Global Execution Protocol for Agents
When initiating a session:
1. Reference this `PROJECTS_ROADMAP.md` to identify dependencies and target ports.
2. Update project status (`🟡 Staged` ➔ `🟢 Production`) upon completing verification.
3. Synchronize changes to `deepshah08/Learning` repository via the `md-writer` skill.
