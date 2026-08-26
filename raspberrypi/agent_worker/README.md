# 🤖 Project 18: Headless Jules Agent Review Worker (Raspberry Pi 5)

> **Context**: Autonomous 24/7 background agent worker running on Raspberry Pi 5 ARM64 with strict CPU/memory throttling, polling GitHub pull requests, executing automated pytest test suites, AST static syntax validation, and generating automated code review summaries.  
> **Status**: 🟢 **Production / Tested**  
> **Host**: Raspberry Pi 5 (`192.168.1.92`)  
> **Repository**: [`deepshah08/raspberry-pi-5-ecosystem/projects/18-agent-worker`](https://github.com/deepshah08/raspberry-pi-5-ecosystem/tree/main/projects/18-agent-worker)  

---

## 1. Architecture Overview

```mermaid
flowchart TD
    JulesSession["Google Jules / Cloud Agent PR"] --> GitHubPR["GitHub PR Created (deepshah08/...)"]
    GitHubPR --> Worker["agent-worker Daemon on Pi 5 (worker.py)"]
    Worker --> DiffCheck["AST Syntax & Import Inspector"]
    Worker --> Subprocess["Isolated Test Runner (pytest -v --tb=short)"]
    
    Subprocess --> Verdict{"All Tests & Syntax Pass?"}
    Verdict -->|Yes (LGTM)| Approve["Post APPROVE Review Summary"]
    Verdict -->|No (Errors)| ReqChanges["Post REQUEST_CHANGES + Diagnostic Logs"]
```

---

## 2. Resource Sandboxing & Throttling (Zero Network Interference)

- **Systemd Unit**: `/etc/systemd/system/agent-worker.service`
- **Priority**: `Nice=15` (low scheduling priority so network DNS/DHCP packets preempt the worker instantly).
- **CPU Quota**: `CPUQuota=50%` (capped to prevent CPU starvation).
- **Memory Ceiling**: `MemoryMax=1G` (prevents OOM events).
- **Filesystem Isolation**: `ProtectSystem=strict`, `ReadWritePaths=/tmp/agent_swarm_workspace`.

---

## 3. Verified Functionality & Test Suite

- `projects/18-agent-worker/tests/test_agent_worker.py`:
  - `test_inspect_diff_syntax_valid`: Verifies zero AST errors on valid Python modules.
  - `test_inspect_diff_syntax_invalid`: Detects syntax errors and line references.
  - `test_generate_review_summary_approval`: Generates structured LGTM approval review.
  - `test_generate_review_summary_rejection`: Generates actionable failure diagnosis.
  - `test_run_tests_success`: Validates isolated subprocess test runner.
- **Test Results**: 5/5 passing tests (73/73 across repository).
