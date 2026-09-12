# HeyPocket Bridge: Architecture, Remote MCP & Agentic Swarm Ingress

> Durable system knowledge for the HeyPocket Bridge homelab integration.  
> Origin: investigation journey at [./heypocket_bridge_integration_investigation.md](./heypocket_bridge_integration_investigation.md)

---

## 1. Role / Position

The HeyPocket Bridge sits at the perimeter of the homelab agent swarm, acting as the secure ingress adapter for physical and voice captures from HeyPocket wearable hardware and cloud services. It translates incoming streaming webhooks into structured, Git-backed Markdown notes for Project 02 (Second Brain) and task queues for Project 16 (Morning Briefing). Concurrently, it exposes Pocket's remote Model Context Protocol (MCP) server to local autonomous AI agents (Google Antigravity, Claude Code, OpenAI Codex).

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        HOMELAB SYSTEM BOUNDARY                         │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   [HeyPocket Hardware] ──► [Pocket Cloud API]                          │
│                                  │                                     │
│                                  ├──► [Remote MCP Server] (SSE/JSON)   │
│                                  │           │                         │
│                                  │           ▼                         │
│                                  │    [Autonomous Agents]              │
│                                  │                                     │
│                                  └──► [Cloudflare Edge] (Port 8095)    │
│                                              │                         │
│                                              ▼                         │
│                                       [heypocket-bridge]               │
│                                              │                         │
│                                              ▼                         │
│                                       [MarkdownEmitter]                │
│                                              ├──► Project 02 Vault     │
│                                              └──► Project 16 Queue     │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Plane Decomposition

### A. Ingress & Webhook Plane (Write Path)

```text
┌────────────────────────────────────────────────────────────────────────┐
│                      INGRESS PLANE: WRITE PATH                         │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   Cloud POST ──► Cloudflare Edge ──► ThreadingHTTPServer (:8095)       │
│                                                │                       │
│                                                ▼                       │
│                                      verify_hmac_signature()           │
│                                                │                       │
│                                                ▼                       │
│                                         MarkdownEmitter                │
│                                                ├──► Second Brain Vault │
│                                                └──► Briefing Queue     │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

**Key facts about Ingress Plane:**
- **Zero Public Port Forwarding**: Traffic enters via Cloudflare Tunnel (`cloudflared`) to `http://localhost:8095`, terminating TLS at edge without opening router firewall ports.
- **Constant-Time Verification**: `hmac.compare_digest` prevents timing attacks on `X-HeyPocket-Signature`.
- **Replay Protection**: Strict $\le 300\text{s}$ timestamp skew bounds with millisecond-to-second auto-disambiguation.
- **CWE-22 Confinement**: Target note filenames sanitized with alphanumeric masks; canonical containment asserted via `Path.is_relative_to()`.

### B. Query & MCP Plane (Read & Reasoning Path)

```text
┌────────────────────────────────────────────────────────────────────────┐
│                      QUERY PLANE: MCP AGENT PATH                       │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   Autonomous Agent ──► PocketMCPClient ──► public.heypocketai.com/mcp  │
│   (Antigravity/Claude)          │                                      │
│                                 ▼                                      │
│                      Streamable JSON-RPC 2.0                           │
│                      Header: Authorization: Bearer pk_...              │
│                      Header: mcp-session-id: <id>                      │
│                                 │                                      │
│                                 ▼                                      │
│                      Tool: search_pocket_conversations                 │
│                      Tool: search_pocket_actionitems                   │
│                      Tool: get_account_info                            │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

**Key facts about Query Plane:**
- **Transport**: JSON-RPC 2.0 over streamable HTTP with Server-Sent Events (SSE) data lines (`data: {...}`).
- **Session Continuity**: Retains `mcp-session-id` across queries for stateful context window caching.
- **Standard Library Compliance**: Uses Python stdlib `urllib.request` exclusively. Zero third-party packages.

---

## 3. Architecture

### Component Inventory

| Component | Role | Owner / Where it lives | Touched? |
|---|---|---|:---:|
| `webhook_receiver.py` | Multi-threaded HTTP listener, HMAC auth, replay guard | `plugins/heypocket-bridge/core/` | ✅ Created |
| `markdown_emitter.py` | Frontmatter serialization, diarization, task routing | `plugins/heypocket-bridge/core/` | ✅ Created |
| `pocket_client.py` | Remote MCP client, CLI, SSE parser, cloud syncer | `plugins/heypocket-bridge/core/` | ✅ Created |
| `simulator.py` | Offline synthetic payload generator & fault tester | `plugins/heypocket-bridge/core/` | ✅ Created |
| `test_heypocket_bridge.py`| Comprehensive 33-case test suite | `plugins/heypocket-bridge/core/tests/` | ✅ Created |
| `SKILL.md` | Autonomous agent operating protocol & tool descriptors | `plugins/heypocket-bridge/skills/` | ✅ Created |
| `pihole-FTL` | Whole-home DNS & DHCP (Port 53, Option 6) | Raspberry Pi 5 (`192.168.1.92`) | ❌ Unchanged |
| `Second Brain Vault` | Git-backed Markdown knowledge repository | Homelab Storage (`Project 02`) | ❌ Target |

### Source Files

| File Path | Responsibility |
|---|---|
| `core/pocket_client.py` | Pure stdlib MCP client connecting to `https://public.heypocketai.com/mcp`. |
| `core/webhook_receiver.py` | `ThreadingHTTPServer` listener on port 8095 validating HMAC-SHA256 signatures. |
| `core/markdown_emitter.py` | Formats recording transcripts and summaries into Obsidian-compatible notes. |
| `core/simulator.py` | Generates meetings, calls, and memos for offline testing and fault-injection. |
| `skills/pocket-assistant/SKILL.md`| Standard agentskills guide for Antigravity, Claude Code, and Codex. |

---

## 4. Resource Footprint & Sandboxing Invariants

To safeguard homelab operations and comply with host protection rules:

| Constraint | Allocation / Invariant | Rationale |
|---|---|---|
| **Port Choice** | `TCP 8095` | Zero collision with Jellyfin (`8096`), Pi-hole (`80/8080`), Vaultwarden (`8085`), or n8n (`5678`). |
| **CPU Limit** | `CPUQuota=50%`, `Nice=15` | Throttles background processing so core homelab daemons never starve. |
| **Memory Bound** | `MemoryMax=512M` | Caps container memory to eliminate Out-Of-Memory (OOM) risks. |
| **Host Isolation** | Containerized / Unprivileged | Never bind `network_mode: host` on bare metal; run inside Docker with bridged networking. |
| **DNS Shielding** | Zero Public Ingress on Pi 5 | Pi 5 (`192.168.1.92`) runs DNS resolver; public ingress strictly prohibited on that node. |

---

## 5. Architectural Comparison: Pixel 9 Pro XL vs. HeyPocket

| Evaluation Dimension | Google Pixel 9 Pro XL (Recorder) | HeyPocket (Hardware + Cloud) |
|---|---|---|
| **Acoustics & Microphones** | 3-mic beamforming array with Audio Magic Eraser DSP. Superior raw audio fidelity and wind rejection. | Dual MEMS microphones + chassis vibration conduction sensor. |
| **Transcription Privacy** | 100% on-device (Tensor G4 TPU via Gemini Nano / Conformer). Zero data leaves device. | Cloud-processed (Whisper + proprietary LLM pipeline on startup infrastructure). |
| **Financial Cost** | $0 (included natively with hardware purchase). | Hardware cost (~$150) + optional subscription tiers. |
| **Phone Call Recording** | Blocked by Android OS telephony sandbox. Google Phone requires loud mandatory announcements. | Physical conduction sensor on phone backplate records incoming and outgoing calls cleanly. |
| **Capture Ergonomics** | Pull out phone, unlock screen, launch app, tap record. Socially visible and distracting. | Tactile single-click physical button or clip-on wearable. Screen stays off. |
| **Swarm Automation** | Walled garden: no public API, no webhooks, no MCP server. Requires manual export. | Open agentic ecosystem: automated HMAC webhooks + first-party remote MCP server. |

---

## 6. Verification Commands

```bash
# 1. Run complete unit and integration test suite (33 tests)
python3 -m unittest agentic-workflows/plugins/heypocket-bridge/core/tests/test_heypocket_bridge.py

# 2. Verify ASCII diagram box alignment and <= 90 column width
python3 agentic-workflows/plugins/work-journal/core/tools/asciicheck.py --verbose --width 90 \
  agentic-workflows/plugins/heypocket-bridge/README.md \
  agentic-workflows/plugins/heypocket-bridge/skills/pocket-assistant/SKILL.md \
  Learning/ci_cd_and_agentic_pipelines/heypocket_bridge_integration_investigation.md \
  Learning/ci_cd_and_agentic_pipelines/heypocket_bridge_integration_knowledge.md

# 3. Verify zero credential leakage
python3 agentic-workflows/plugins/work-journal/core/tools/redact.py --check \
  Learning/ci_cd_and_agentic_pipelines/heypocket_bridge_integration_investigation.md \
  Learning/ci_cd_and_agentic_pipelines/heypocket_bridge_integration_knowledge.md
```
