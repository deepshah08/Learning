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
| **Agent Protocols** | Global Directives | Anti-confirmation bias, empirical ground truth, safety | [AGENTS.md](AGENTS.md) |
| **Networking & Protocols** | Storage & Gateways | SMB, NFS, AFP, mDNS/Bonjour, LAN/Tailscale Routing | [networking/NETWORK_FILE_SHARING_EXPLAINER.md](networking/NETWORK_FILE_SHARING_EXPLAINER.md) |
| **Raspberry Pi 5** | System & Hardware | Host access, OS tuning, VMs, hardware devices | [raspberrypi/README.md](raspberrypi/README.md) |
| **Raspberry Pi 5** | Pi-hole (Primary) | Primary DNS ad-blocking, ISP/SLAAC bypass, v6 web admin | [raspberrypi/pihole/README.md](raspberrypi/pihole/README.md) |
| **UGREEN DXP2800** | Plex & *Arr | 8-service media stack, QuickSync HW transcoding, atomic hardlinks | [ugreen_nas/arr_stack/README.md](ugreen_nas/arr_stack/README.md) |
| **UGREEN DXP2800** | AI Telegram Media Bot | Natural language Telegram bot for Plex, Sonarr, Radarr, Prowlarr | [ugreen_nas/telegram_bot/README.md](ugreen_nas/telegram_bot/README.md) |
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
├── AGENTS.md                          # Universal Agent Operating Protocol (Codex / Cursor / General)
├── CLAUDE.md                          # Claude Code CLI Directives
├── GEMINI.md                          # Google Cloud Code / Gemini CLI Directives
├── PROJECTS_ROADMAP.md                # Master Project Roadmap & Execution Queue
├── networking/                        # Networking & Protocols Domain
│   └── NETWORK_FILE_SHARING_EXPLAINER.md # Complete SMB/NFS/Gateways guide
├── raspberrypi/                       # Pi 5 Domain
│   ├── README.md                      # General Pi 5 Host & Hardware
│   ├── SETUP_AND_TUNING_GUIDE.md      # Detailed setup guide
│   └── pihole/                        # Primary Pi-hole Sub-Domain
│       └── README.md                  # DNS Configs, ISP Bypass, Gravity-Sync sender
└── ugreen_nas/                        # UGREEN DXP2800 Domain
    ├── arr_stack/                     # Media Automation Sub-Domain (8 Services)
    │   ├── README.md                  # QuickSync, Inodes, Custom Language Scoring
    │   └── docker-compose.yml         # Complete Docker Compose configuration
    ├── telegram_bot/                  # AI Telegram Media Bot Sub-Domain
    │   ├── README.md                  # SSOT Runbook & Bot Architecture
    │   ├── bot.py                     # Telegram Bot Engine & Handlers
    │   ├── llm_parser.py              # Natural Language Intent Parser
    │   ├── media_clients.py           # Radarr / Sonarr / Prowlarr API Client
    │   ├── Dockerfile                 # Container image specification
    │   └── docker-compose.yml         # Compose stack definition
    ├── pihole/                        # Secondary HA Pi-hole Sub-Domain
    │   └── README.md                  # Failover DNS, Port 53, Gravity-Sync target
    ├── vaultwarden/                   # Password Manager Sub-Domain
    │   └── README.md                  # Bitwarden backend, WebSockets, Multi-user
    ├── homepage/                      # Central Dashboard Sub-Domain
    │   └── README.md                  # Widgets for Plex, Arr, qBit, Pi-hole, NAS stats
    └── smb/                           # macOS Finder & File Sharing Sub-Domain
        └── README.md                  # SMB3, macOS vfs_fruit, Finder drag-and-drop
```
