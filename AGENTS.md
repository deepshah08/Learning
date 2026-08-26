# Universal Agent Directives & Protocol

This document defines the mandatory operating protocol for all AI agents, CLIs (Codex, Claude Code, Google Cloud Code, Antigravity, Cursor), and automation scripts interacting with this repository and connected infrastructure.

---

## 🛡️ Pragmatic Anti-Confirmation Bias & Ground-Truth Protocol

### 1. Velocity First, Rigor Where It Matters
* Differences in technical perspective, implementation style, and design trade-offs are natural and expected.
* Do not halt development velocity or over-engineer tests for standard decisions. Keep momentum moving forward smoothly.

### 2. Explicit Objection Trigger
* When the user explicitly objects, states contrary real-world observations, or corrects an assumption:
  * **STOP defending the prior hypothesis.**
  * Do not cherry-pick search results or synthesize references to confirm a belief.
  * Re-evaluate with an open mind and design a fast, minimal verification only if needed.

### 3. Low Confidence / High-Impact Check
* When dealing with ambiguous third-party cloud quotas, destructive disk operations, unverified API side-effects, or physical hardware settings where confidence is low:
  * Proactively state the uncertainty before taking action.
  * Never present unverified theories as established facts.

### 4. Zero Hallucinated / Unverified URLs
* Never construct, guess, or synthesize URL slugs, post IDs, or citation paths.
* Provide only verified, live links retrieved directly from official tools or provide exact search queries.

### 5. Hardware, Storage & Quota Safety
* Exercise maximum engineering care when touching physical disks (NAS pools, SMR/CMR drives, RAID, Btrfs), network routing, and paid cloud quotas.
* Never make assumptions that could risk data corruption, hardware degradation, or storage limit lockouts.

### 6. Containerized Isolation & Zero Host Mutation
* **Zero Host OS/Kernel Mutations:** NEVER alter core OS-level or kernel-level settings on bare-metal host nodes (Raspberry Pi 5, UGREEN NAS, Debian hosts) that could destabilize or interfere with existing production services (e.g., DNS, DHCP, Pi-hole v6 FTL, Plex, SMB, system packages, or kernel page sizes).
* **Strict Container Isolation:** Keep all runtime modifications, custom dependencies, background daemons, and application packages strictly encapsulated inside Docker containers or OCI images to minimize the blast radius.
* **Preserve Host Stability:** Never modify host `/etc/apt/sources.list`, force-break host package dependencies, or swap host kernel images when a containerized or userland solution exists.
