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
