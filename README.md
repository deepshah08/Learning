# 🧠 Learning — Single Source of Truth (SoT) Knowledge Base

Welcome to the centralized, version-controlled Single Source of Truth (SoT) knowledge base for autonomous AI agents, developers, and project ecosystems.

This repository eliminates Single Points of Failure (SPOF) by providing a stateless, durable, and structured directory of proven architectures, runbooks, system bugs, and resolutions.

---

> [!IMPORTANT]
> **Universal Agent Operating Protocol**: All agents, CLIs (Codex, Claude Code, Google Cloud Code, Cursor, Antigravity), and automation scripts must adhere to the [**`AGENTS.md`**](AGENTS.md) Anti-Confirmation Bias, Ground-Truth, and OpenSSH Multiplexing Protocols.

---

## 🗺️ Domain Directory Map

| Domain | Sub-Domain | Description | Documentation Link |
| :--- | :--- | :--- | :--- |
| **System Overview** | Hardware & Status | Complete inventory of physical nodes, drives, and live services | [HARDWARE_AND_SYSTEMS_INVENTORY.md](HARDWARE_AND_SYSTEMS_INVENTORY.md) |
| **Agent Protocols** | Global Directives | Anti-confirmation bias, empirical ground truth, safety, SSH multiplexing | [AGENTS.md](AGENTS.md) |
| **Networking & Protocols** | Storage & Gateways | SMB, NFS, AFP, mDNS/Bonjour, LAN/Tailscale Routing | [networking/NETWORK_FILE_SHARING_EXPLAINER.md](networking/NETWORK_FILE_SHARING_EXPLAINER.md) |
| **Networking & Protocols** | SSH Session Pipeline | High-performance OpenSSH ControlMaster/ControlPersist multiplexing | [networking/SSH_MULTIPLEXING_AND_SESSION_MANAGEMENT.md](networking/SSH_MULTIPLEXING_AND_SESSION_MANAGEMENT.md) |
| **Raspberry Pi 5** | System & Hardware | Host access, OS tuning, VMs, hardware devices | [raspberrypi/README.md](raspberrypi/README.md) |
| **Raspberry Pi 5** | Pi-hole (Primary) | High-Availability DNS, Unbound+Cloudflare, 24h DHCP, Option 6 Dual-DNS | [raspberrypi/pihole/README.md](raspberrypi/pihole/README.md) |
| **Raspberry Pi 5** | Unbound (Recursive) | 192MB In-Memory Root DNSSEC Resolver, 2-Thread Execution, Zero Rate Limit | [raspberrypi/unbound/README.md](raspberrypi/unbound/README.md) |
| **UGREEN DXP2800** | Storage Tiering | NVMe Docker Engine (`/volume2`) + CMR Mass Media (`/volume1`) TBW Protection | [ugreen_nas/STORAGE_TIERING_AND_NVME_ARCHITECTURE.md](ugreen_nas/STORAGE_TIERING_AND_NVME_ARCHITECTURE.md) |
| **UGREEN DXP2800** | Pi-hole (Secondary) | High-Availability failover DNS on 2.5GbE, 1:1 Parity (309k domains) | [ugreen_nas/pihole/README.md](ugreen_nas/pihole/README.md) |
| **UGREEN DXP2800** | Plex & *Arr | 8-service media stack, QuickSync HW transcoding, atomic hardlinks | [ugreen_nas/arr_stack/README.md](ugreen_nas/arr_stack/README.md) |
| **UGREEN DXP2800** | AI Telegram Media Bot | Natural language Telegram bot for Plex, Sonarr, Radarr, Prowlarr | [ugreen_nas/telegram_bot/README.md](ugreen_nas/telegram_bot/README.md) |
| **UGREEN DXP2800** | OpenClaw AI Gateway | Multi-channel autonomous AI agent framework & Telegram/Discord gateway | [ugreen_nas/openclaw/README.md](ugreen_nas/openclaw/README.md) |
| **UGREEN DXP2800** | Vaultwarden | Encrypted password manager for Deep & Pranali + shared vault | [ugreen_nas/vaultwarden/README.md](ugreen_nas/vaultwarden/README.md) |
| **UGREEN DXP2800** | Homepage Dashboard | Unified single-pane-of-glass homelab monitoring & launcher | [ugreen_nas/homepage/README.md](ugreen_nas/homepage/README.md) |
| **UGREEN DXP2800** | UGOS Pro Native Suite | Native Apps (Photos, Office, Vault, Sync) vs. Docker Hybrid Model | [ugreen_nas/UGOS_PRO_NATIVE_APPS_AND_HYBRID_ARCHITECTURE.md](ugreen_nas/UGOS_PRO_NATIVE_APPS_AND_HYBRID_ARCHITECTURE.md) |
| **UGREEN DXP2800** | SMB Network Sharing | macOS Finder drag-and-drop, photo ingestion, Google Photos | [ugreen_nas/smb/README.md](ugreen_nas/smb/README.md) |
