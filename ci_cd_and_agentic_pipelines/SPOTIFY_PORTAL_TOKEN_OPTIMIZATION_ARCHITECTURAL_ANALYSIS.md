# Architectural Deep Dive: Spotify's 90% Token Reduction Architecture

> **Source**: [Spotify Engineering (Sep 3, 2026)](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90)  
> **Author**: Dimitri Mazmanov, Principal Product Manager at Spotify  
> **Topic**: Shunting bulk I/O and boilerplate code generation to ephemeral worker models

---

## 1. Executive Summary & Core Engineering Thesis

Modern AI coding agents (Claude Code, Antigravity, Cursor) incur the overwhelming
majority of their token burn not on complex reasoning, but on brute-force **I/O**:
- Reading 5–10 large source files just to inspect a single method signature or return type.
- Generating unit tests or config files that mirror dozens of existing boilerplate patterns.
- Ingesting entire reference implementations into the primary agent context window.

Feeding multi-thousand-token files into top-tier frontier models (Claude 3.5/3.7 Sonnet,
GPT-4o) burns high-cost tokens on tasks that require zero deep reasoning. Spotify’s
engineering team designed an automated delegation system (**"Shunt" via AiKA Modes**)
that slashes Claude Code token consumption by **~90%** while preserving frontier-grade
code output quality.

```
┌────────────────────────────────────────────────────────┐
│             Frontier Agent (Claude Code)               │
│         High-Reasoning, High-Cost Context Window       │
└───────────────────────────┬────────────────────────────┘
                            │
               PreToolUse Hook Intercept
             (e.g., Read File > 350 lines)
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│            Shunt Router / Delegation Script            │
│         Wraps files in XML + Injects strict prompt     │
└──────────────┬────────────────────────────┬────────────┘
               │                            │
               ▼                            ▼
┌──────────────────────────────┐ ┌───────────────────────┐
│     Mode 1: `bulk-reader`    │ │ Mode 2: `code-writer` │
│    Worker: Gemini 2.5 Flash  │ │ Worker: Gemini Flash  │
│  Outputs structured bullets  │ │ Direct-to-disk write  │
│ (Raw code never enters host) │ │ (Claude never sees it)│
└──────────────┬───────────────┘ └──────────┬────────────┘
               │                            │
               ▼                            ▼
      Concise Findings Bullets       File on Disk Target
```

---

## 2. The Three-Layer "Shunt" Architecture

Spotify discovered that advisory instructions in documentation (`CLAUDE.md`, `AGENTS.md`)
inevitably fail because models frequently ignore advisory text and revert to native tool
calls. To guarantee compliance, Spotify decoupled the system into three rigid layers:

### Layer 1: Deterministic PreToolUse Hooks (Enforcement)
The Shunt plugin registers two pre-execution hooks in Claude Code:
1. `check-file-size`: Fires before every `Read` tool call. If the target file exceeds a
   configurable threshold (`SHUNT_MIN_LINES`, default: 350 lines), the hook actively
   blocks the tool execution and commands the model to use the `/bulk-reader` skill.
   Targeted slice reads (specifying offset/limit) pass through cleanly.
2. `check-bash-read`: Intercepts shell commands (`cat`, `head`, `tail`, `less`, `more`)
   targeting large files. Piped commands (`cat file | grep`) pass through since they
   are already targeted.

### Layer 2: Ephemeral Worker Modes (AiKA / Gemini 2.5 Flash)
Delegated work runs on ephemeral agent runtimes (analogous to AWS Lambda for LLMs)
powered by cheap, high-throughput models (Gemini 2.5 Flash, temperature 0.2):

#### A. Mode: `bulk-reader`
- **Purpose**: Digest multiple large files to answer specific questions.
- **System Prompt**:
  ```yaml
  name: bulk-reader
  instructions: >
    You are a precise code analyst. Read the provided files and answer the
    question concisely. Output structured bullets only. No greetings, no prose,
    no preambles. Lead every bullet with the exact name, type, or line number.
    Use nested bullets for details. Skip anything the caller did not ask for.
  model: gemini-2.5-flash
  resourceLimits:
    temperature: 0.2
  ```
- **Token Mechanism**: The files are wrapped in XML tags and sent directly to the worker.
  The multi-thousand token raw text **never enters the frontier model context**. Only
  the concise 5-line structured bullet summary is returned.

#### B. Mode: `code-writer`
- **Purpose**: Generate test suites, boilerplate scaffolding, and type stubs.
- **System Prompt**:
  ```yaml
  name: code-writer
  instructions: >
    You generate code files based on a spec and reference files. Match the
    existing patterns, conventions, naming, and style exactly. Output only the
    code — no explanations, no markdown fences unless asked. If the spec is
    ambiguous, make reasonable choices that match the reference code patterns.
  model: gemini-2.5-flash
  resourceLimits:
    temperature: 0.2
  ```
- **Token Mechanism**: Takes a spec and a reference pattern file. It writes the generated
  code directly to disk (`--target tests/UserTest.java`). The frontier model never
  ingests the reference file nor does it spend expensive output tokens generating
  repetitive test scaffolding.

### Layer 3: Skills & CLI Wrappers
Two CLI scripts wrap the API calls (`bulk-read --question ... --paths ...` and `code-write
--spec ... --reference ... --target ...`). Markdown skill definitions instruct the agent
on exact syntax, ensuring smooth recovery when a hook triggers a block.

---

## 3. Critical Boundaries & Failure Modes ("What Doesn't Work")

Spotify's empirical testing surfaced three non-negotiable architectural boundaries:

1. **You Cannot Delegate Line-Precise Editing**:
   Worker summaries cannot reliably provide exact line numbers or offset ranges needed for
   safe replacements. The frontier model must perform targeted reads (`view_file` with
   slice bounds) when making direct code edits.
2. **You Cannot Delegate Reasoning or Security**:
   In testing, worker models identified surface patterns but missed subtle concurrency bugs
   and thread-safety flaws. The frontier model spotted them in seconds once supplied the
   condensed context. Architecture, security audits, and root-cause analysis must remain
   with the frontier model.
3. **Latency Overhead Dictates the Threshold**:
   Each delegated call incurs a network round-trip of 10–30 seconds. For files under
   350 lines, the latency penalty outweighs token cost savings.

---

## 4. Homelab & Multi-Agent Adoption Roadmap

We can adapt Spotify's engineering patterns directly into our agentic workflows and homelab
infrastructure:

### Phase 1: Subagent Model Tiering in Antigravity (Immediate)
- **Subagent Shunting**: In Antigravity, we have `invoke_subagent` with model tiering:
  - `Model='flash'` or `Model='flash_lite'` for broad codebase exploration, repository
    inventories, and test scaffolding.
  - `Model='inherit'` / `pro` exclusively for deep architectural planning, debugging,
    and multi-model councils.
- **Reference-Pattern Testing**: When asking agents to generate unit tests, supply a
  single reference test file and direct a worker subagent to write to disk rather than
  generating large diffs in the primary conversation context.

### Phase 2: Claude Code & Terminal Hook Enforcement (Near-Term)
- For local Claude Code workflows on macOS:
  - Install or adapt the Shunt PreToolUse hooks (`check-file-size`) in `~/.claude/settings.json`.
  - Route bulk file reads to Google AI Studio Gemini API (`gemini-2.5-flash` at $0.075/M tokens
    or free tier quota) or local Ollama on the Raspberry Pi 5.

### Phase 3: Headless Homelab Code-Generation Daemon (Future Horizon)
- Deploy a lightweight worker container on the UGREEN NAS / Pi 5:
  - Listens for boilerplate requests (e.g. generating protobuf stubs, pytest scaffolding).
  - Uses local quantized models or OpenRouter free tier models to write scaffolding
    directly to filesystem volumes without cloud token overhead.

---

## 5. Summary Matrix: Frontier vs. Shunted Worker

| Dimension | Frontier Model (Sonnet / GPT-4o) | Shunted Worker (Gemini Flash / Edge) |
| :--- | :--- | :--- |
| **Primary Role** | Reasoning, Architecture, Safety | Raw File I/O, Scaffolding, Summaries |
| **Token Cost** | \$3.00 – \$15.00 / M tokens | \$0.075 / M tokens (or Free Tier) |
| **Context Hygiene**| Kept clean (<20k active tokens) | Absorbs 100k+ tokens of raw file text |
| **Output Target** | Decisions, tool calls, diff plans| Pure code directly written to disk |
