# Universal Agent Directives & Operating Protocol

> **Scope**: Authoritative operating instructions for all autonomous AI agents, multi-agent frameworks, and developer CLIs (Antigravity, Codex, Cursor, Claude Code, Gemini Code Assist) operating within this codebase and connected physical infrastructure.

---

## 🛡️ 1. Pragmatic Anti-Confirmation Bias & Ground-Truth Protocol

- **Velocity First, Rigor Where It Matters:** Differences in perspective and technical trade-offs are natural and expected. Do not halt momentum or over-engineer tests for standard decisions. Keep development moving forward smoothly.
- **Explicit Objection Trigger:** When the user explicitly objects, states contrary real-world observations, or corrects an assumption, **STOP defending the prior hypothesis**. Do not cherry-pick search results or synthesize references to confirm a belief. Re-evaluate with an open mind and design a fast, minimal verification only if needed.
- **Low Confidence / High-Impact Check:** When dealing with ambiguous third-party cloud quotas, destructive disk operations, or unverified API side-effects where confidence is low, proactively state the uncertainty and verify before committing to irreversible actions.
- **Zero Hallucinated URLs:** Never construct, guess, or synthesize URLs, post IDs, or citation paths. Provide only verified links or exact search queries.
- **Hardware & Storage Safety & Anti-Churn Gating:** Exercise maximum engineering care when touching physical disks (NAS pools, SMR/CMR drives, RAID, Btrfs), network routing, and paid cloud quotas.
  - **Mechanical Pool Immunity & Path Exclusion:** Bulk mechanical storage mounts (`/volume1` on NAS, `/mnt/media-storage` on Pi 5) are STRICTLY OFF-LIMITS for open-ended file inspection tools (`grep`, `find`, `du`, `lsof`, `rgrep`). Diagnostic searches must target ONLY NVMe/SSD paths (`/volume2`), local system directories (`/etc`, `/usr/local`), or specific, pre-identified files.
  - **Mandatory Hard Timeout Wrappers:** ALL remote diagnostic commands inspecting filesystem metadata, active processes, or system logs MUST be wrapped in a hard OS-level timeout (e.g. `timeout 5s <command>`). Never execute un-wrapped search utilities.
  - **Zero Remote Orphaned Subprocesses:** Terminating a local SSH tool call does NOT automatically send SIGKILL to remote backgrounded child processes on the server. Commands must be bounded at the remote host level (`timeout 5s`) so the remote host kernel automatically terminates them if delayed.
  - **Storage Tier Alignment:** Verify all automated sync jobs, container configs, and cron scripts target the NVMe tier (`/volume2`) for databases, state files, and logs to allow mechanical HDDs (`/volume1`, `/mnt/media-storage`) to enter and remain in 0 RPM deep hibernation.
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
  - **UGREEN DXP2800 NAS (`192.168.1.80`):** Intel N100 | **8 GB DDR5 RAM** | 10TB Seagate IronWolf CMR HDD (`/volume1`) | 4TB WD_BLACK SN850X NVMe SSD (`/volume2`) | 2.5GbE Wired Ethernet.
  - **Raspberry Pi 5 (`192.168.1.92`):** Broadcom BCM2712 | **16 GB LPDDR4X RAM** | 128GB MicroSD | Wi-Fi 5 (`wlan0`).

---

## 🔒 4. Workload Resource Isolation & Network Blast-Radius Protection

- **Core Network Protection:** Whole-home DNS and DHCP (Pi-hole v6 FTL) must be safeguarded at all times.
  - `pihole-FTL` runs with high process priority (`Nice=-10`, `OOMScoreAdjust=-1000`).
  - High-Availability local-only DNS failover is broadcast to all clients via `dhcp-option=6,192.168.1.80,192.168.1.92`. **NEVER inject public DNS (`1.1.1.1`) into client Option 6** to prevent Android DoT hijacking (port 853) and sticky OS resolver ad-block bypass.
  - Unbound root recursive DNS is bound strictly to `127.0.0.1:5335` (loopback only).
  - UGOS Pro Docker Pi-hole must use bridge mode (`192.168.1.80:53:53`), never `network_mode: host` (conflicts with UGOS host `dnsmasq` PID 1119).
- **BitTorrent State & Conntrack Safety:** In `libtorrent`/`qBittorrent`, always enforce TCP-only transport (`Session\BittorrentProtocol=1`) to eliminate connectionless uTP UDP NAT state explosions in router tables. Enforce strict 1:1 seed ratio (`GlobalMaxRatio=1.0`) with auto-pause (`GlobalMaxRatioAction=0`).
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

---

## 🌐 6. English-Only Resource Optimization & Multilingual Gating

- **Default Locale: `en` Only.** All AI models, tokenizers, NLP libraries, localization packs, and language-dependent dependencies default to **English-only** configurations. Strip, exclude, or avoid loading multilingual, polyglot, or "glotware" resources unless an explicit exception applies.
- **Checkpoint Selection Over Model Surgery:** When a model family offers both English-specific and multilingual checkpoints (e.g., `laya` vs `laya-multilingual`, `ModernBERT-base` vs `mmBERT-base`), **always select the English-only checkpoint** as the default. Never load a 100+ language multilingual model when a purpose-built English variant exists — the English checkpoint is smaller, faster, and uses less RAM.
- **Resource Trimming Hierarchy:** Apply the least invasive optimization that achieves the goal:
  1. **Checkpoint selection** — choose `en`-only model variant (preferred, zero risk)
  2. **Config-level exclusion** — set `languages: [en]`, `locale: en_US`, or equivalent config flags to skip loading unused language modules
  3. **Dependency pruning** — exclude multilingual tokenizer vocabularies, spaCy language packs (`de_core`, `zh_core`, `ja_core`, etc.), NLTK corpora, or ICU locale data at install time (e.g., `pip install spacy[en]`, not `spacy[all]`)
  4. **Quantized/pruned checkpoints** — prefer GGUF, ONNX, or framework-native quantized English checkpoints that have already been vocabulary-trimmed
  5. **Manual embedding/vocab pruning** — only as a last resort, and only with full regression testing against the frozen evaluation set
- **Never Destructively Modify Shared Weights:** Dense transformer models (BERT, Laya, Qwen) share parameters across languages in attention heads and FFN layers. Do NOT attempt to delete "language-specific neurons" or slice embedding matrices without a validated pruning script and regression gate. If the English-only checkpoint doesn't exist, use the multilingual one as-is and file a note to revisit.
- **Storage & Compute Savings Are Real:** Multilingual tokenizers often carry 250K+ vocab entries vs ~30K for English-only. This bloats embedding tables by 8–10×, increases model file size, wastes GPU/NPU VRAM, and inflates tokenization latency. Selecting the right checkpoint is the single highest-ROI optimization.

### Exception: TTS, ASR & Audio/Speech Workloads

The English-only default does **NOT** apply to:
  - **Text-to-Speech (TTS):** XTTS v2, Coqui, Piper, or any speech synthesis system. Retain **Hindi (`hi`)** and **Gujarati (`gu`)** language support alongside English for family-facing applications and personal use.
  - **Automatic Speech Recognition (ASR):** Whisper or equivalent. Keep multilingual capability for Hindi and Gujarati transcription.
  - **Any application explicitly built for parents or family members** where Hindi or Gujarati is the primary interface language.
  - **Translation services** when the use case involves `en↔hi` or `en↔gu` translation.

When these exceptions apply, load **only the required languages** (`en`, `hi`, `gu`) — never the full 100+ language pack. For Whisper, use the language-specific or bilingual model if available rather than the full multilingual checkpoint.
