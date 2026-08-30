# Universal Agent Directives & Operating Protocol

> **Scope**: Authoritative operating instructions for all autonomous AI agents, multi-agent frameworks, and developer CLIs (Antigravity, Codex, Cursor, Claude Code, Gemini Code Assist) operating within this codebase and connected physical infrastructure.

---

## 🛡️ 1. Pragmatic Anti-Confirmation Bias & Ground-Truth Protocol

- **Velocity First, Rigor Where It Matters:** Differences in perspective and technical trade-offs are natural and expected. Do not halt momentum or over-engineer tests for standard decisions. Keep development moving forward smoothly.
- **Explicit Objection Trigger:** When the user explicitly objects, states contrary real-world observations, or corrects an assumption, **STOP defending the prior hypothesis**. Do not cherry-pick search results or synthesize references to confirm a belief. Re-evaluate with an open mind and design a fast, minimal verification only if needed.
- **Low Confidence / High-Impact Check:** When dealing with ambiguous third-party cloud quotas, destructive disk operations, or unverified API side-effects where confidence is low, proactively state the uncertainty and verify before committing to irreversible actions.
- **Zero Hallucinated URLs:** Never construct, guess, or synthesize URLs, post IDs, or citation paths. Provide only verified links or exact search queries.
- **Hardware & Storage Safety:** Exercise maximum engineering care when touching physical disks (NAS pools, SMR/CMR drives, RAID, Btrfs), network routing, and paid cloud quotas.
- **Containerized Isolation & Zero Host Mutation:** NEVER alter core OS-level or kernel-level settings on bare-metal host nodes (Raspberry Pi 5, UGREEN NAS, Debian hosts) that could destabilize or interfere with existing production services (e.g., DNS, DHCP, Pi-hole v6 FTL, Plex, SMB, system packages, or kernel page sizes). Keep all runtime modifications, dependencies, and application packages strictly encapsulated inside Docker containers to minimize blast radius.

---

## ⚡ 2. High-Performance OpenSSH Multiplexing & Batch Execution Protocol

- **Zero Fragmented SSH Calls:** Never dispatch fragmented, single-line SSH tool calls in rapid succession. Spawning fresh SSH processes triggers repetitive TCP 3-way handshakes, TLS/KEX cipher renegotiation, and PAM authentication loops (~500ms latency per call).
- **Leverage OpenSSH `ControlMaster` Multiplexing:** The controller host maintains persistent master Unix sockets in `~/.ssh/controlmasters/` (`ControlMaster auto`, `ControlPersist 1h`). All remote commands must execute over established control sockets for instant `<25ms` response times.
- **Consolidated Batch Payloads:** Bundle pre-checks, file writes, service restarts, and post-verification probes into single, cohesive multi-statement bash execution blocks.

---

## 🔍 3. Hardware Specifications Ground-Truth Enforcement

- **Zero Hallucinated Specs:** NEVER guess, assume, or generalize physical hardware specifications (RAM, CPU, storage tiers, networking) from generic retail models or LLM weights.
- **Mandatory SSOT Inventory Reference:** All hardware facts MUST be cross-referenced directly with `Learning/HARDWARE_AND_SYSTEMS_INVENTORY.md` or verified via live host commands (`free -h`, `lscpu`, `lsblk`) before making comparisons or statements.
  - **UGREEN DXP2800 NAS (`192.168.1.80`):** Intel N100 | **8 GB DDR5 RAM** (Accessible via bottom hatch) | **4TB WD_BLACK SN850X NVMe SSD** (`/volume2`, internal M.2 slots inside HDD tray bays) | **10TB Seagate IronWolf CMR HDD** (`/volume1`, Bay 1) | **8TB Seagate Expansion SMR** (Cold USB 3.0 backup with 15-min udev spindown) | 2.5GbE Wired Ethernet.
  - **Raspberry Pi 5 (`192.168.1.92`):** Broadcom BCM2712 | **16 GB LPDDR4X RAM** | 128GB MicroSD | Wi-Fi 5 (`wlan0`).

---

## 🗄️ 3.1. Storage Tiering & Zero-Copy Containerization Directive

- **Zero-Copy Over Inter-Volume Duplication:** NEVER propose or script background copying/mirroring of bulk data across storage volumes (e.g. `/volume1` to `/volume2`) when exposing host files to containers. Always employ direct, read-only bind mounts (`-v /volume1/path:/target:ro`) to eliminate duplicate I/O and preserve NVMe write endurance (TBW).
- **Asymmetric Tiering Principle:** Keep random-access metadata, SQLite databases, container runtimes, and lightweight thumbnails on the NVMe SSD tier (`/volume2`) to maximize wear-free solid-state reads, while keeping cold bulk media on the mechanical HDD tier (`/volume1`) configured for 0 RPM deep sleep hibernation.
- **Physical M.2 Installation Safety:** M.2 NVMe PCIe drives must NEVER be hot-plugged while host power is energized. Always execute a graceful shutdown prior to physical insertion.

---

## 🔒 4. Workload Resource Isolation & Network Blast-Radius Protection

- **Core Network Protection:** Whole-home DNS and DHCP (Pi-hole v6 FTL) must be safeguarded at all times.
  - `pihole-FTL` runs with high process priority (`Nice=-10`, `OOMScoreAdjust=-1000`).
  - High-Availability DNS failover is broadcast to all clients via `dhcp-option=6,192.168.1.92,192.168.1.80`.
  - Unbound root recursive DNS is bound strictly to `127.0.0.1:5335` (loopback only).
- **AI & Worker Sandboxing:** Any local AI, transcription (Whisper), speech synthesis (XTTS v2), or background review worker daemon must be throttled with strict limits (`Nice=15`, `CPUQuota=50%`, `MemoryMax=1G`). Never run continuous un-throttled CPU-bound loops on the Pi 5.
- **Monorepo Namespace Cleanliness:** In repositories where multiple subdirectories are in `pythonpath` (`pytest.ini`), avoid generic names like `config.py` in subproject roots (use project-specific prefixes like `worker_config.py` or `immich_config.py`) to prevent module cache poisoning in `sys.modules`.

---

## 🗂️ 5. Single Source of Truth (SoT) Documentation Maintenance

- **Continuous Knowledge Base Sync:** All architectural changes, incident post-mortems, and new service deployments must be logged immediately in the version-controlled `Learning/` repository.
- **Domain Runbooks:** Every deployed homelab service must have an authoritative `README.md` containing:
  - System architecture diagram (Mermaid)
  - Configuration parameter matrix
  - Live CLI health-check and verification commands
  - Disaster recovery and rollback steps
- **Zero Hallucinations:** Reference only verified local paths and active network endpoints (`192.168.1.92`, `192.168.1.80`, `192.168.1.254`).
