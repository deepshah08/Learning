# Google Cloud Code & Gemini Agent Guidelines

This repository serves as the Single Source of Truth (SoT) for infrastructure, homelab architectures, and autonomous agent workflows.

---

## 🛡️ Mandatory Operating Protocol

### 1. Velocity First, Rigor Where It Matters
* Differences in perspective and technical trade-offs are natural and expected. Keep development moving forward smoothly without over-testing standard decisions.

### 2. Explicit Objection Trigger
* When the user explicitly objects, states contrary real-world observations, or corrects an assumption:
  * **STOP defending the prior hypothesis.**
  * Do not cherry-pick search results or synthesize references to confirm a belief.
  * Re-evaluate with an open mind and design a fast, minimal verification only if needed.

### 3. Low Confidence / High-Impact Guardrail
* When dealing with ambiguous third-party cloud quotas, destructive disk operations, or unverified API side-effects where confidence is low:
  * Proactively state the uncertainty and verify before committing to irreversible actions.

### 4. Zero Hallucinated URLs
* Never construct, guess, or synthesize URLs, post IDs, or citation paths. Provide only verified links or exact search queries.

### 5. Hardware & Storage Safety
* Exercise maximum engineering care when touching physical disks (NAS pools, SMR/CMR drives, RAID, Btrfs), network routing, and paid cloud quotas.

### 6. Containerized Isolation & Zero Host Mutation
* NEVER alter core OS-level or kernel-level settings on bare-metal host nodes (Raspberry Pi 5, UGREEN NAS, Debian hosts) that could destabilize or interfere with existing production services (e.g., DNS, DHCP, Pi-hole v6 FTL, Plex, SMB, system packages, or kernel page sizes).
* Keep all runtime modifications, custom dependencies, and application packages strictly encapsulated inside Docker containers to minimize blast radius.

### 7. Storage Tiering & Zero-Copy Containerization
* **Zero-Copy Over Inter-Volume Duplication:** NEVER propose or script background copying/mirroring of bulk data across storage volumes (e.g. `/volume1` to `/volume2`) when exposing host files to containers. Always employ direct, read-only bind mounts (`-v /volume1/path:/target:ro`) to eliminate duplicate I/O and preserve NVMe write endurance (TBW).
* **Asymmetric Tiering:** Keep random-access metadata, SQLite databases, container runtimes, and lightweight thumbnails on the NVMe SSD tier (`/volume2`) to maximize wear-free solid-state reads, while keeping cold bulk media on the mechanical HDD tier (`/volume1`) configured for 0 RPM deep sleep hibernation.
* **Physical M.2 Safety:** M.2 NVMe PCIe drives must NEVER be hot-plugged while energized; always execute a graceful shutdown.

### 8. Hardware Ground-Truth Reference
* Cross-reference all specs with `Learning/HARDWARE_AND_SYSTEMS_INVENTORY.md`:
  * **UGREEN DXP2800 NAS (`192.168.1.80`):** Intel N100 | **8 GB DDR5 RAM** (Bottom hatch) | **4TB WD_BLACK SN850X NVMe SSD** (`/volume2`, internal M.2 slots inside HDD bays) | **10TB Seagate IronWolf CMR HDD** (`/volume1`, Bay 1) | **8TB Seagate Expansion SMR** (Cold USB 3.0 backup with 15-min udev spindown) | 2.5GbE LAN.
  * **Raspberry Pi 5 (`192.168.1.92`):** Broadcom BCM2712 | **16 GB LPDDR4X RAM** | 128GB MicroSD | Wi-Fi 5 (`wlan0`).

### 9. Modern Model Tiering ($\ge 3.5$ Only)
* All external Gemini API queries, architecture ideation, reviews, and brainstorming MUST strictly use models $\ge 3.5$ (e.g. `gemini-3.7-flash`, `antigravity-preview-05-2026`, `gemini-3.6-flash`, `gemini-3.5-flash`). Permanently ignore and reject all legacy models $< 3.5$.

