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
| **Master Roadmap** | Execution Queue | All 23 projects, statuses, interfaces, and test verifications | [PROJECTS_ROADMAP.md](PROJECTS_ROADMAP.md) |
| **Agent Protocols** | Global Directives | Anti-confirmation bias, empirical ground truth, safety | [AGENTS.md](AGENTS.md) |
| **Networking & Protocols** | Storage & Gateways | SMB, NFS, AFP, mDNS/Bonjour, LAN/Tailscale Routing | [networking/NETWORK_FILE_SHARING_EXPLAINER.md](networking/NETWORK_FILE_SHARING_EXPLAINER.md) |
| **Raspberry Pi 5** | System & Hardware | Host profile, OS hardening, Wi-Fi stability, IP forwarding | [raspberrypi/README.md](raspberrypi/README.md) |
| **Raspberry Pi 5** | Unbound Recursive DNS | Private root DNSSEC resolver, zero 3rd-party logging | [raspberrypi/unbound/README.md](raspberrypi/unbound/README.md) |
| **Raspberry Pi 5** | Jules Agent Worker | Autonomous 24/7 background PR review & test runner | [raspberrypi/agent_worker/README.md](raspberrypi/agent_worker/README.md) |
| **Raspberry Pi 5** | Projects Suite | 18 implemented & tested local RAG, automation, security services | [raspberrypi/README.md#4-pi-5-projects-portfolio](raspberrypi/README.md#4-pi-5-projects-portfolio) |
| **Raspberry Pi 5** | Pi-hole (Primary) | Primary DNS ad-blocking, ISP/SLAAC bypass, v6 web admin | [raspberrypi/pihole/README.md](raspberrypi/pihole/README.md) |
| **UGREEN DXP2800** | Plex & *Arr | 8-service media stack, QuickSync HW transcoding, atomic hardlinks | [ugreen_nas/arr_stack/README.md](ugreen_nas/arr_stack/README.md) |
| **UGREEN DXP2800** | Pi-hole (Secondary) | High-Availability failover DNS, automated 30-min Gravity-Sync | [ugreen_nas/pihole/README.md](ugreen_nas/pihole/README.md) |
| **UGREEN DXP2800** | Vaultwarden | Encrypted password manager for Deep & Pranali + shared vault | [ugreen_nas/vaultwarden/README.md](ugreen_nas/vaultwarden/README.md) |
| **UGREEN DXP2800** | Homepage Dashboard | Unified single-pane-of-glass homelab monitoring & launcher | [ugreen_nas/homepage/README.md](ugreen_nas/homepage/README.md) |
| **UGREEN DXP2800** | SMB Network Sharing | macOS Finder drag-and-drop, photo ingestion, Google Photos | [ugreen_nas/smb/README.md](ugreen_nas/smb/README.md) |
