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

## 🔍 3. Hardware Specifications Ground-Truth Enforcement

- **Zero Hallucinated Specs:** NEVER guess, assume, or generalize physical hardware specifications (RAM, CPU, storage tiers, networking) from generic retail models or LLM weights.
- **Mandatory SSOT Inventory Reference:** All hardware facts MUST be cross-referenced directly with `Learning/HARDWARE_AND_SYSTEMS_INVENTORY.md` or verified via live host commands (`free -h`, `lscpu`, `lsblk`) before making comparisons or statements.
  - **UGREEN DXP2800 NAS (`192.168.1.80`):** Intel N100 | **8 GB DDR5 RAM** | 10TB Seagate IronWolf CMR HDD (`/volume1`) | 4TB WD_BLACK SN850X NVMe SSD (`/volume2`) | 2.5GbE Wired Ethernet.
  - **Raspberry Pi 5 (`192.168.1.92`):** Broadcom BCM2712 | **16 GB LPDDR4X RAM** | 128GB MicroSD | Wi-Fi 5 (`wlan0`).

---

## 🗂️ 4. Single Source of Truth (SoT) Documentation Maintenance

- **Continuous Knowledge Base Sync:** All architectural changes, incident post-mortems, and new service deployments must be logged immediately in the version-controlled `Learning/` repository.
- **Domain Runbooks:** Every deployed homelab service must have an authoritative `README.md` containing:
  - System architecture diagram (Mermaid)
  - Configuration parameter matrix
  - Live CLI health-check and verification commands
  - Disaster recovery and rollback steps
- **Zero Hallucinations:** Reference only verified local paths and active network endpoints (`192.168.1.92`, `192.168.1.80`, `192.168.1.254`).
