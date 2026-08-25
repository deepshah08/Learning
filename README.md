# 🧠 Learning — Single Source of Truth (SoT) Knowledge Base

Welcome to the centralized, version-controlled Single Source of Truth (SoT) knowledge base for autonomous AI agents, developers, and project ecosystems.

This repository eliminates Single Points of Failure (SPOF) by providing a stateless, durable, and structured directory of proven architectures, runbooks, system bugs, and resolutions.

---

> [!NOTE]  
> Agents invoking the `md-writer` skill must follow the directory structure and authoring guidelines defined herein.

---

## 🗺️ Domain Directory Map

| Domain | Sub-Domain | Description | Documentation Link |
| :--- | :--- | :--- | :--- |
| **Raspberry Pi 5** | System & Hardware | Host access, OS tuning, VMs, hardware devices | [raspberrypi/README.md](raspberrypi/README.md) |
| **Raspberry Pi 5** | Pi-hole | DNS ad-blocking, ISP/SLAAC bypass, v6 web admin | [raspberrypi/pihole/README.md](raspberrypi/pihole/README.md) |
| **UGREEN DXP2800** | Plex & *Arr | 8-service media stack, QuickSync HW transcoding, atomic hardlinks | [ugreen_nas/arr_stack/README.md](ugreen_nas/arr_stack/README.md) |

---

## 🗂️ Standard Folder Hierarchy

```text
Learning/
├── README.md                      # This Global Index
├── PROJECTS_ROADMAP.md            # Master Project Roadmap & Execution Queue
├── raspberrypi/                   # Pi 5 Domain
│   ├── README.md                  # General Pi 5 Host & Hardware
│   ├── SETUP_AND_TUNING_GUIDE.md  # Detailed setup guide
│   └── pihole/                    # Pi-hole Sub-Domain
│       └── README.md              # DNS Configs, ISP Bypass, Tailscale
└── ugreen_nas/                    # UGREEN DXP2800 Domain
    └── arr_stack/                 # Media Automation Sub-Domain
        ├── README.md              # 8-Service Docker Stack, QuickSync, Hardlinks
        └── docker-compose.yml     # Complete Docker Compose configuration
```

---

## ✍️ Contribution & Sync Rules for Agents

1. **Read Before Write**: Always check existing domain folders for registered ports, IP addresses, and known quirks.
2. **Structured Documentation**: Every new topic must include a System Context, Architecture Table, Known Bugs & Fixes, operational runbooks, and copy-paste revert commands.
3. **Non-Redundancy**: Update existing documents when modifying a subsystem rather than creating folder sprawl.