# HeyPocket Bridge Integration Investigation: Homelab Agentic Bridge & Pixel 9 Pro XL Trade-offs

> Companion: durable knowledge at [./heypocket_bridge_integration_knowledge.md](./heypocket_bridge_integration_knowledge.md)  
> Origin: investigation journey for HeyPocket AI companion integration into homelab swarm.

**Plugin**: `heypocket-bridge`  
**Repository**: `agentic-workflows` & `Learning`  
**Branch**: `main`  
**Status**: 🟢 Verified & Certified by Challenge Agent  
**Reviewer**: Challenge Agent (Adversarial Invariant Auditor)  
**Date**: September 2026  

---

## 1. Trigger

User acquired HeyPocket hardware (`heypocket.com`, docs at `public.heypocketai.com/docs`) and requested seamless integration into local autonomous agent swarms (Google Antigravity, Claude Code, OpenAI Codex) and homelab repositories (Project 02 Second Brain, Project 16 Morning Briefing). Follow-up inquiry introduced girlfriend's sharp technical counter-objection: why carry a secondary \$150 gadget when the Pixel 9 Pro XL already provides on-device Tensor G4 Gemini Nano transcription, 3 studio-grade beamforming microphones, and zero hardware overhead?

```text
┌────────────────────────────────────────────────────────────────────────┐
│                      INITIAL INTEGRATION TRIGGER                       │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   [HeyPocket Hardware] ──► [Pocket Cloud API]                          │
│                                   │                                    │
│                                   ├──► [Remote MCP Server]             │
│                                   │    (public.heypocketai.com/mcp)    │
│                                   │           │                        │
│                                   │           ▼                        │
│                                   │    [Agent Swarm Discovery]         │
│                                   │    (Antigravity / Claude)          │
│                                   │                                    │
│                                   └──► [Incoming Cloud Webhook]        │
│                                        (Requires Public Website URL)   │
│                                               │                        │
│                                               ▼                        │
│                                        [Homelab Ingress Setup]         │
│                                        (Protect Pi 5 / NAS)            │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Investigation Path

| # | Hypothesis / Approach | What we found | Outcome |
|---|----------------------|---------------|---------|
| 1 | Expose webhook receiver directly via Tailscale Funnel on Raspberry Pi 5 (`192.168.1.92`). | Pi 5 runs primary LAN DNS resolver (`pihole-FTL` on port 53, DHCP Option 6, Unbound on 5335). Public ingress on host risks resource exhaustion and network outages. Violates Gate 2 (Zero Host Mutation). | **Rejected** |
| 2 | Route Pocket webhooks through containerized Cloudflare Tunnel (`cloudflared`) to port 8095. | Cloudflare Edge terminates SSL, shields local IP, maps HTTPS to `http://localhost:8095` inside an unprivileged container with strict cgroups (`--cpus=0.5 --memory=512m`). Port 8095 has 0 collisions with homelab ports (Jellyfin :8096, TripDrop :8088, Pi-hole :80/8080). | **Selected** |
| 3 | Use hypothetical tool names (`pocket_list_recordings`, `pocket_get_recording`) in operational skills. | Live inspection of `https://public.heypocketai.com/mcp` revealed actual tools: `get_account_info`, `list_pocket_folders`, `search_pocket_conversations`, `search_pocket_actionitems`, `update_pocket_actionitem`. Challenge Agent rejected hypothetical names. | **Pivoted & Aligned** |
| 4 | Fallback to hardcoded default API key in `pocket_client.py` for developer convenience. | Challenge Agent flagged hardcoded `DEFAULT_KEY` as critical secret leakage vulnerability. Violates Gate 6 (Zero Live Secrets). | **Purged & Rejected** |
| 5 | Single-threaded `HTTPServer` in standard library `webhook_receiver.py`. | Concurrent deliveries blocked listener loop; slow clients degraded webhook ingestion. Challenge Agent required multi-threaded non-blocking server. | **Upgraded to ThreadingHTTPServer** |
| 6 | Replace HeyPocket with Pixel 9 Pro XL Recorder app natively. | Pixel Recorder has superior microphones, Tensor G4 on-device privacy, and zero cost, but is an un-automatable walled garden (no API, no webhooks, no MCP) and Android sandboxes prevent 2-way cellular/VoIP call recording without loud announcements. | **Hybrid Architecture Selected** |

---

## 3. Root Causes and Fixes

### Invariant & Security Audits

| # | Component / Layer | Root Cause | Fix |
|---|-------------------|------------|-----|
| 1 | `core/pocket_client.py` | Hardcoded default key fallback in source code. | Removed constant. Enforced dynamic reading from `HEYPOCKET_API_KEY` environment variable with explicit `ValueError`. |
| 2 | `.gitignore` | Missing plugin `.gitignore` permitted potential staging of audio notes and bytecode. | Created `.gitignore` ignoring `output/notes/`, `output/actions/`, `.env`, `*.key`, `__pycache__/`. Cleaned sample notes from disk. |
| 3 | `core/webhook_receiver.py` | Single-threaded `HTTPServer` created potential connection stalling. | Replaced with `ThreadingHTTPServer` and set `daemon_threads = True` for instant `SIGTERM`/`SIGINT` cleanup. |
| 4 | `core/webhook_receiver.py` | Brittle direct import `from markdown_emitter import ...` failed when executed as package. | Replaced with defensive try-except importing `.markdown_emitter` before falling back to direct import. |
| 5 | `skills/pocket-assistant/SKILL.md` | Hypothetical tool names conflicted with live MCP schema. | Rewrote instructions to reference real MCP tools discovered on `https://public.heypocketai.com/mcp`. |
| 6 | `core/tests/test_heypocket_bridge.py` | `PocketMCPClient` lacked mock tests for SSE streams, headers, and error codes. | Added 8 mock test cases covering JSON-RPC serialization, SSE parsing, HTTP errors, and unwrapping. |

---

## 4. Key Architecture

```text
┌────────────────────────────────────────────────────────────────────────┐
│                     HEYPOCKET DUAL-PLANE TOPOLOGY                      │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   [INGRESS PLANE]                                                      │
│   Pocket Hardware ──► Cloud API ──► Cloudflare Edge                    │
│                                             │                          │
│                                             ▼ (:8095)                  │
│                                     ThreadingHTTPServer                │
│                                             │                          │
│                                     MarkdownEmitter                    │
│                                      │             │                   │
│                                      ▼             ▼                   │
│                                Project 02     Project 16               │
│                               (Second Brain)  (Briefing Queue)         │
│                                                                        │
│   [QUERY / MCP PLANE]                                                  │
│   Autonomous Agents ──► PocketMCPClient ──► public.heypocketai.com/mcp │
│   (Antigravity/Claude)  (JSON-RPC 2.0 SSE)                             │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### Configuration Matrix

| Environment Variable | Default Value | Description |
|---|---|---|
| `HEYPOCKET_API_KEY` | *None (Required)* | Bearer API token for Pocket Cloud and remote MCP endpoint. |
| `HEYPOCKET_WEBHOOK_SECRET` | `""` | Shared secret for HMAC-SHA256 signature verification. |
| `HEYPOCKET_PORT` | `8095` | Local TCP listening port for `ThreadingHTTPServer`. |
| `HEYPOCKET_OUTPUT_DIR` | `./output/notes` | Target directory for Obsidian Second Brain markdown notes. |
| `HEYPOCKET_ACTION_ITEMS_DIR` | `./output/actions` | Target directory for Project 16 Morning Briefing JSONL tasks. |

---

## 5. CI, Testing & Resource Footprint

### Local Test Execution Results

Executed complete test suite in `core/tests/test_heypocket_bridge.py`:
```text
Ran 33 tests in 1.094s

OK
```

- **HMAC Verification Suite**: 10 tests (timing attack immunity, prefix normalization, clock skew rejection).
- **Security Edge Cases**: 5 tests (CWE-22 path traversal prevention, type confusion safety, 10MB bounds).
- **HTTP Server Integration**: 3 tests (GET /health, POST /webhook, signature verification).
- **Markdown Emitter**: 6 tests (frontmatter quote escaping, diarization, duration formatting, action queueing).
- **Simulator & Fault-Injection**: 3 tests (offline local emission, live dispatch, corrupted signature detection).
- **Pocket MCP Client**: 9 tests (key validation, RPC headers, SSE extraction, JSON-RPC error propagation, HTTP error handling, tool unwrapping, and Second Brain sync).

### Resource Footprint & Sandboxing
- **RAM Allocation**: Max 512 MB (`MemoryMax=512M`).
- **CPU Quota**: Max 50% single core (`CPUQuota=50%`, `Nice=15`).
- **Network Ingress**: Unprivileged port `8095`, bound locally (`127.0.0.1:8095` or Docker bridge).
- **Dependencies**: 0 pip packages (Pure Python 3 standard library: `http.server`, `urllib`, `hmac`, `hashlib`, `json`).

---

## 6. Challenge Agent Review Iterations

| Gate | Focus | Initial Verdict | Remediation & Final Verdict |
|---|---|:---:|---|
| **Gate 1** | Manifests & Docs | ✅ Approved | Unified manifests for Antigravity, Claude, and Codex. Clean 84-col diagrams. |
| **Gate 2** | Cryptographic Webhook | ❌ Rejected | Initial rejection for path traversal and missing payload bounds. Fixed and re-audited: ✅ Approved. |
| **Gate 3** | Markdown Emitter | ❌ Rejected | Initial rejection for YAML quote injection and duration type error. Fixed with `json.dumps()` escaping: ✅ Approved. |
| **Gate 4** | Offline Simulator | ✅ Approved | Verified offline generation (`--emit-local`) and fault-injection testing. |
| **Gate 5** | Skill Specification | ✅ Approved | Validated frontmatter, linted ASCII box diagrams (`asciicheck.py`), zero credentials. |
| **Live Gate** | Live Integration & Key | ❌ Rejected | Caught hardcoded secret, missing `.gitignore`, single-threaded server, and missing MCP tests. Fully remediated: **✅ EXPLICIT FINAL APPROVAL**. |

---

## 7. Key Learnings

1. **Physical conduction bypasses software sandboxes**: While modern smartphone operating systems strictly sandbox call audio to protect user privacy, hardware accessories with chassis acoustic sensors can record two-way conversations without violating OS boundaries or triggering automated announcements.
2. **Automated pipelines trump raw microphone specs**: A recording trapped in a mobile app without an API is dead data. An open webhook and MCP pipeline transforms ambient audio into queryable, durable intelligence for autonomous agent swarms.
3. **Continuous adversarial auditing catches blind spots**: The Challenge Agent caught critical vulnerabilities (secret leakage in CLI defaults, single-threaded socket stalls, YAML quote injection) that functional unit tests initially missed.
