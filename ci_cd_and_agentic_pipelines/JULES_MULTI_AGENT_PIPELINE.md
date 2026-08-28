# 🤖 Jules Multi-Agent Reviewer & Autonomous Pipeline Blueprint

> **Context**: Architectural specification for the autonomous multi-agent code review, iterative test-fix loop, and Jules session orchestrator.  
> **Blueprint Version**: `v2.2.0` ([`deepshah08/antigravity-pipeline-blueprint`](https://github.com/deepshah08/antigravity-pipeline-blueprint))  
> **Status**: 🟢 **Production Standard across Antigravity Swarm**

---

## 1. Multi-Agent Orchestration Architecture

```text
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                               JULES MULTI-AGENT REVIEW & MERGE LOOP                             │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                 │
│   ┌─────────────────────┐        PR Created         ┌─────────────────────────┐                 │
│   │   Jules Subagent    │ ────────────────────────> │      GitHub Pull        │                 │
│   │   Coding Session    │                           │        Request          │                 │
│   └─────────────────────┘                           └───────────┬─────────────┘                 │
│              ▲                                                  │                               │
│              │ Fix Feedback                                     │ Trigger Review                │
│              │                                                  ▼                               │
│   ┌─────────────────────┐      pytest / Flake8      ┌─────────────────────────┐                 │
│   │  Session Reply via  │ <──────────────────────── │   jules-auto-reviewer   │                 │
│   │      Jules MCP      │      (If Tests Fail)      │       Orchestrator      │                 │
│   └─────────────────────┘                           └───────────┬─────────────┘                 │
│                                                                 │                               │
│                                                                 │ All Checks Pass (LGTM)        │
│                                                                 ▼                               │
│                                                     ┌─────────────────────────┐                 │
│                                                     │  Auto-Merge into `main` │                 │
│                                                     │    & Close Session      │                 │
│                                                     └─────────────────────────┘                 │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Reusable Skill Specifications

### A. `jules-auto-reviewer` Skill
Located in `deepshah08/antigravity-pipeline-blueprint/skills/jules-auto-reviewer/SKILL.md`.
- **Purpose**: Autonomous monitoring of GitHub pull requests opened by Jules sessions.
- **Workflow**:
  1. Polls `list_pull_requests` or `list_sessions`.
  2. Inspects changed code diffs (`show_code_diff` / `get_pull_request_files`).
  3. Executes local validation (`flake8`, `pytest`, `npm test`).
  4. If defects are found: sends structured feedback back to the active Jules session (`send_reply_to_session`).
  5. If clean: approves and merges the pull request (`merge_pull_request`).

### B. `keenable-cli` Skill
Located in `deepshah08/antigravity-pipeline-blueprint/skills/keenable-cli/SKILL.md`.
- **Purpose**: High-speed terminal web search and clean markdown extraction for RAG pipelines without browser bloat.
- **Usage**: Real-time factual ground truth verification for autonomous agents.

---

## 3. Verified Multi-Agent Milestones

| Task / Milestone | Session ID | Scope | Merged Status |
| :--- | :--- | :--- | :--- |
| **Task 2.1: Scraper** | `4600636120631080933` | Article scraping & asset pipeline | Merged into `antigravity_projects` |
| **Task 2.2: Markdown Exporter** | `18423709579804580568`| Structured JSON/MD transformer | Merged into `antigravity_projects` |
| **Task 3.1: App Data Fix** | `1254256874060117829` | Dynamic route & JSON loader | Merged into `antigravity_projects` |
| **Task 3.2: PWA Implementation** | `10209587440075337467`| Offline service worker & caching | Merged into `antigravity_projects` |
| **Task 4.1: API Contracts** | `11932163683604836360`| FastAPI contracts & schema validation | Merged into `antigravity_projects` |
| **Task 4.2: Keenable RAG** | `9886028625017370185` | Semantic vector RAG engine | Merged into `antigravity_projects` |
| **Task 5.1: E2E Pipeline** | `2962213264803450290` | Automated execution wrapper | Merged into `antigravity_projects` |
| **Task 5.2: Documentation** | `7763833166648587711` | Master README & architecture | Merged into `antigravity_projects` |
| **Plex/Arr Stack Pi 5 Fix** | `14783501220091300745`| Hardware QuickSync & port isolation | Resolved on `main` (`raspberry-pi-5-ecosystem`) |

---

## 4. Runbook: How to Invoke Jules PR Reviewer in New Sessions

1. Load the skill via slash command: `/jules-auto-reviewer` or reference the skill markdown.
2. The orchestrator will scan open PRs across active repos.
3. Once validated, PRs are cleanly merged, tagged, and closed.
