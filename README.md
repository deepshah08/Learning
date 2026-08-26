# 🧠 Learning — Single Source of Truth (SoT) Knowledge Base

Welcome to the centralized, version-controlled Single Source of Truth (SoT) knowledge base for autonomous AI agents, developers, and project ecosystems.

This repository eliminates Single Points of Failure (SPOF) by providing a stateless, durable, and structured directory of proven architectures, runbooks, system bugs, and resolutions.

---

> [!IMPORTANT]
> **Universal Agent Operating Protocol**: All agents, CLIs (Codex, Claude Code, Google Cloud Code, Cursor, Antigravity), and automation scripts must adhere to the [**`AGENTS.md`**](AGENTS.md) Anti-Confirmation Bias & Ground-Truth Protocol.

---

## 🗺️ Domain Directory Map

| Domain | Sub-Domain | Description | Documentation Link |
| :--- | :--- | :--- | :--- |
| **System Overview** | Hardware & Status | Complete inventory of physical nodes, drives, and live services | [HARDWARE_AND_SYSTEMS_INVENTORY.md](HARDWARE_AND_SYSTEMS_INVENTORY.md) |
| **Master Roadmap** | Execution Queue | All 21 projects, statuses, interfaces, and test verifications | [PROJECTS_ROADMAP.md](PROJECTS_ROADMAP.md) |
| **Agent Protocols** | Global Directives | Anti-confirmation bias, empirical ground truth, safety | [AGENTS.md](AGENTS.md) |
| **Networking & Protocols** | Storage & Gateways | SMB, NFS, AFP, mDNS/Bonjour, LAN/Tailscale Routing | [networking/NETWORK_FILE_SHARING_EXPLAINER.md](networking/NETWORK_FILE_SHARING_EXPLAINER.md) |
| **Raspberry Pi 5** | System & Hardware | Host profile, OS hardening, Wi-Fi stability, IP forwarding | [raspberrypi/README.md](raspberrypi/README.md) |
| **Raspberry Pi 5** | Projects Suite | 16 implemented & tested local RAG, automation, security services | [raspberrypi/README.md#4-pi-5-projects-portfolio](raspberrypi/README.md#4-pi-5-projects-portfolio) |
| **Raspberry Pi 5** | Pi-hole (Primary) | Primary DNS ad-blocking, ISP/SLAAC bypass, v6 web admin | [raspberrypi/pihole/README.md](raspberrypi/pihole/README.md) |
| **UGREEN DXP2800** | Plex & *Arr | 8-service media stack, QuickSync HW transcoding, atomic hardlinks | [ugreen_nas/arr_stack/README.md](ugreen_nas/arr_stack/README.md) |
| **UGREEN DXP2800** | Pi-hole (Secondary) | High-Availability failover DNS, automated 30-min Gravity-Sync | [ugreen_nas/pihole/README.md](ugreen_nas/pihole/README.md) |
| **UGREEN DXP2800** | Vaultwarden | Encrypted password manager for Deep & Pranali + shared vault | [ugreen_nas/vaultwarden/README.md](ugreen_nas/vaultwarden/README.md) |
| **UGREEN DXP2800** | Homepage Dashboard | Unified single-pane-of-glass homelab monitoring & launcher | [ugreen_nas/homepage/README.md](ugreen_nas/homepage/README.md) |
| **UGREEN DXP2800** | SMB Network Sharing | macOS Finder drag-and-drop, photo ingestion, Google Photos | [ugreen_nas/smb/README.md](ugreen_nas/smb/README.md) |

---

## 🗂️ Standard Folder Hierarchy

```text
Learning/
├── README.md                          # This Global Index
├── HARDWARE_AND_SYSTEMS_INVENTORY.md  # Physical Nodes, Drives & Live System Status
├── PROJECTS_ROADMAP.md                # Master Project Roadmap & Execution Queue
├── AGENTS.md                          # Universal Agent Operating Protocol
├── CLAUDE.md                          # Claude Code CLI Directives
├── GEMINI.md                          # Google Cloud Code / Gemini CLI Directives
├── networking/                        # Networking & Protocols Domain
│   └── NETWORK_FILE_SHARING_EXPLAINER.md # SMB/NFS/Gateways/Avahi guide
├── raspberrypi/                       # Pi 5 Domain
│   ├── README.md                      # Host & Hardware SoT + Project Index
│   ├── SETUP_AND_TUNING_GUIDE.md      # OS hardening, sleep prevention
│   ├── offline_tutor/README.md        # Project 01: Offline Socratic Tutor
│   ├── second_brain/README.md        # Project 02: Git-Backed Second Brain
│   ├── whisper_indexer/README.md     # Project 03: WhisperX Meeting Indexer
│   ├── immich/README.md              # Project 04: Immich Photo Staging
│   ├── jellyfin/README.md            # Project 05: Jellyfin Media Server Profile
│   ├── voice_clone/README.md         # Project 06: Voice Clone TTS Sandbox
│   ├── backup_engine/README.md       # Project 07: Backup Engine & Pixel 1 Sync Guard
│   ├── trip_drop/README.md           # Project 08: TripDrop Staging Portal
│   ├── stirling_pdf/README.md        # Project 09: Stirling-PDF Utility
│   ├── intrusion_monitor/README.md   # Project 10: Network Intrusion Monitor
│   ├── deadmans_switch/README.md     # Project 11: Dead Man's Switch
│   ├── pihole/README.md              # Project 12: Primary Pi-hole v6 FTL
│   ├── n8n/README.md                 # Project 13: n8n Workflow Automation
│   ├── market_sentiment/README.md    # Project 14: Market Sentiment Tracker
│   ├── financial_pipeline/README.md  # Project 15: Financial Pipeline Dashboard
│   └── morning_briefing/README.md    # Project 16: Morning Briefing Generator
└── ugreen_nas/                        # UGREEN DXP2800 Domain
    ├── arr_stack/                     # Media Automation Sub-Domain (8 Services)
    ├── pihole/                        # Secondary HA Pi-hole Sub-Domain
    ├── vaultwarden/                   # Password Manager Sub-Domain
    ├── homepage/                      # Central Dashboard Sub-Domain
    └── smb/                           # macOS Finder & File Sharing Sub-Domain
```
