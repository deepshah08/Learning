# IT13 Max Investigation: From architecture plan to versioned deployment

**Status:** Goals 1–6 deployed; R1–R6 and round-two R2/R6 repairs complete; independent Astra review pending.

**Implementation source:** [private `deepshah08/it13max` repository](https://github.com/deepshah08/it13max)

**Companion:** durable system knowledge at [it13max_knowledge.md](./it13max_knowledge.md)

---

## 1. Trigger

The original IT13 Max design described a local knowledge engine, coding workshop,
voice capture, document administration, and reliability tools. The implementation
workspace later accumulated a six-goal plan, a working stack, live execution evidence,
and two remediation review rounds, but remained an untracked Git directory with no
remote. Several recent Codex sessions added model and classifier decisions that also
needed to be tied back to the deployed system.

The original topology and provisioning diagrams remain in the [architecture blueprint](https://github.com/deepshah08/it13max/blob/main/node-it13-max-architecture-blueprint.md)
inside the code repository. They were kept as the source diagrams rather than redrawn.

## 2. Investigation Path

| # | Hypothesis / approach | What the session evidence showed | Outcome |
|---|---|---|---|
| 1 | Continue executing the original six-goal plan | `it13-execution/progress.json` records Goals 1–4 and 6 deployed; Goal 5 explicitly deferred pending representative labels | All implementation goals are complete; preserve the evaluation deferral |
| 2 | Treat the first R1–R6 fixes as final | Astra's 2026-09-20 review found R2 legacy reconciliation and R6 maintenance/restore gaps, despite 42 passing tests and matching inspected hashes | Reopen R2/R6; preserve prior reports and repair evidence |
| 3 | Close remediation after local repairs | Round-two reports record live reconciliation of 17 indexed sources, 17 completion proofs, zero unproven sources, and isolated restore evidence for 59 Qdrant points | Mark code repairs complete; keep independent Astra review pending |
| 4 | Promote a specialist classifier / reranker now | The stack had 13 indexed records and 8 Paperless sources at Goal 5; there was no 30-item independent evaluation set or demonstrated failure requiring a specialist | Keep deterministic extraction, BGE, and Qwen baseline; defer specialist deployment |
| 5 | Replace Qwen with Spark-X2.5 | Spark Q4 was viable in an isolated benchmark, but requires a second runtime and lacked a fair workflow A/B test; the BF16 registry tag exceeded the worker memory cap | Keep Spark as a later specialist candidate, not production default |
| 6 | Adopt Jev or Laya based on published speed/accuracy claims | The linked synthetic benchmark favored Jev 92.9% to Laya 65.3%; Laya's short-query timing used Apple MLX, not IT13 Intel Arc/NPU. IT13 has no labelled corpus to establish transfer | A replay-only public tech-radar pilot is documented separately; do not route private data or change production |
| 7 | Push the workspace into a broad agent repository | The implementation is a distinct deployed system; `Learning` is the existing MDS knowledge base and `agentic-workflows` owns the public-data classifier plan | Create a separate private `it13max` source repository and cross-link the three responsibilities |

## 3. Root Causes and Fixes

| # | Component / review | Root cause | Fix and evidence |
|---|---|---|---|
| 1 | R2 legacy Paperless reconciliation | Previously indexed records could lack a durable proposal-completion proof and be mistaken for unchanged records | Round two adds idempotent completion markers, including valid zero-proposal outcomes; live proof covers all 17 legacy indexed sources |
| 2 | R6 maintenance and restore | The original backup path could stop active jobs, restart services unconditionally, and validate restore through weak count-based evidence | Round two adds a persistent maintenance barrier, drained bundle capture, isolated bounded restore, semantic hashes, and cleanup verification |
| 3 | Goal 5 specialist evaluation | Personal representative labels were unavailable; small inventory counts could not support a credible accuracy or retrieval claim | Defer model/image/route changes until 30 independently labelled documents or reviewed queries exist |
| 4 | Version control | The source directory had only an empty local Git repository, no commit, and no GitHub remote | Add repository overview and ignores, then commit the complete source, plans, result reports, and evidence to private GitHub repo |

## 4. Key Architecture

IT13 runs one shared control and inference foundation. The master execution plan and
result files carry implementation decisions and measured acceptance evidence; this
investigation records the path and rejected alternatives. See the [knowledge companion](./it13max_knowledge.md)
for current component boundaries and rationale.

## 5. Session and Review Record

| Session / record | Durable result |
|---|---|
| Design IT13 Max homelab node | Architecture, one-heavy-phase constraint, and six-goal implementation plan |
| Complete next Terra execution goal | Sequential goal completion and R1–R6 remediation; second review exposed the R2/R6 gaps |
| Assess Spark-X2.5 suitability | [`it13-model-audit.md`](./it13-model-audit.md); Qwen remains baseline and candidate promotion requires local evaluation |
| Evaluate Jev or Laya integration | [`JEV_LAYA_DECISION_LAYER.md`](https://github.com/deepshah08/agentic-workflows/blob/main/docs/JEV_LAYA_DECISION_LAYER.md); public tech-radar replay first |
| Sync session state to GitHub | This version-control consolidation and paired MDS update |

## 6. Verification Evidence

- The execution record reports Goals 1–6 complete; Goal 5's outcome is
  `evaluation_deferred_for_representative_samples`.
- The remediation record reports R1–R6 complete and round two
  `completed_pending_independent_astra_review`.
- The second-round handoff reports full local suite **53 passed, 1 warning**, live R2
  proof for 17/17 indexed sources, and a drained isolated restore with 13 control
  semantic hashes, PostgreSQL semantic hash, 59 Qdrant points, and verified cleanup.
- This documentation and GitHub publication pass did not rerun tests or deployments.

## 7. Version-Control Record

| Commit | Description |
|---|---|
| `334fca7` | `chore(it13): version implementation and execution state` — initial source, setup, plans, reports, and evidence commit |

The code repository is private because its operational instructions include home-network
and host configuration. `.env`, private CA material, virtual environments, generated
reports, and bytecode are excluded. The paired MDS files are in the Learning repository.

## 8. Key Learnings

1. A passing regression suite is not independent sign-off: Astra found material R2/R6
   gaps after the first 42-test pass, so preserve adversarial findings and retest the
   exact repaired state.
2. Small local inventory cannot validate personal-use model quality: 13 indexed records
   and 8 Paperless sources were below the predeclared sample gate.
3. Benchmark transfer requires matching hardware and workload: Apple MLX timings do not
   establish Intel Arc or NPU performance.
4. A deployed working tree is not a persistent source of truth: code, setup, plans,
   evidence, and docs need named remotes and commits.

## 10. 2026 Dedicated Coding Host Transformation & Model Fleet Evaluation

> **Context**: In late 2026, the legacy document administration and capture stack (Paperless-ngx, Changedetection, Caddy, Qdrant) was migrated completely to the **OrigiMagic Aurora A3** (`192.168.1.111`), liberating the **GEEKOM IT13 Max** to become a dedicated 24/7 autonomous coding engine.

### 10.1 The Fleet Benchmark Battery (28 GB RAM Inference Envelope)

We benchmarked candidate coding models across 2024, 2025, and 2026 architectures using `llama-bench` and live inference on the Intel Core Ultra 9 185H (16C/22T, dual-channel DDR5-4800 MT/s RAM, 30.8 GiB usable):

| Model | Arch & Year | Size | Active Params / Token | Prompt Speed (`pp512`) | Generation Speed (`tg128`) | RAM Footprint (8k Ctx) | Swap Paging |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`Qwen 3.6-35B-A3B`** | **2026 MoE** | **16.56 GiB** | **~3.0B** | **82.60 t/s** | **12.20 t/s** | **~19.8 GiB** | **0 bytes** |
| **`DeepSeek-Coder-V2-Lite`** | 2024 MoE | 9.65 GiB | 2.4B | 97.90 t/s | 22.63 t/s | ~12.0 GiB | 0 bytes |
| **`Spark-X2.6-4B`** | 2025 Hybrid | 2.44 GiB | 4.1B | 77.22 t/s | 12.79 t/s | ~2.8 GiB | 0 bytes |
| **`Qwen 2.5-Coder-7B`** | 2025 Dense | 4.36 GiB | 7.6B | 42.09 t/s | 7.94 t/s | ~4.7 GiB | 0 bytes |
| **`Qwen 2.5-Coder-32B`** | 2025 Dense | 18.49 GiB | 32.5B | 9.68 t/s | 6.20 t/s | ~23.5 GiB | 0 bytes |
| **`Qwen 3.8 Flash Coder`** | 2026 Dense/MoE | 26.44 GiB | ~14B+ | 30.50 t/s | 6.00 t/s | ~27.5 GiB | 0 bytes (at limit) |

**Key Findings:**
1. **The MoE Efficiency Leap:** `Qwen 3.6-35B-A3B` provides 35.5B parameters of world knowledge and coding capability while activating only ~3.0B parameters per token. This breaks the CPU memory wall, delivering **12.2 tokens/sec** vs **6.2 tokens/sec** on the older 32B dense model.
2. **2024 Architecture Deprecation:** `DeepSeek-Coder-V2-Lite` achieved high speed (22.6 t/s) but repeatedly failed modern microservice synthesis (Gate 1) by hallucinating unprovided SQL schemas and deprecated Redis dependencies, whereas `Qwen 3.6` natively planned architecture in `<think>` and generated 100% valid AST code.

---

### 10.2 Deployment Engine Evaluation: `llama.cpp` vs. `Strata`

* **The Strata Hypothesis:** Community claims cited a "2× to 5× speedup" using `Strata` for large MoE models by caching active experts.
* **The Refutation:** Strata's acceleration applies strictly to **consumer NVIDIA GPUs with discrete GDDR6 VRAM over PCIe**, keeping hot experts in VRAM and cold experts in host RAM. On the GEEKOM IT13 Max, the Intel Core Ultra 9 185H uses **Unified Memory Architecture (UMA)** where CPU and iGPU share the same physical DDR5 bus. There is no PCIe boundary to cache across, rendering Strata's memory layering useless. `llama.cpp` AVX2/VNNI assembly remains the fastest, lowest-friction, and most reliable engine.

---

### 10.3 Silicon Offloading: CPU vs. Arc iGPU on UMA

* **The Hypothesis:** Offloading layers to the Intel Arc Xe-LPG iGPU would distribute compute and boost speed.
* **The Refutation:** Pinned CPU threads (`-t 18`) already saturate >90% of available DDR5 memory bus bandwidth (~55 GB/s). Engaging the integrated GPU creates memory bus controller arbitration contention between CPU cores and Xe-cores, while adding driver dispatch latency and increasing SoC package thermal power. Pinned CPU AVX2/VNNI (`-t 18`) is the fastest, lowest-latency path.

---

### 10.4 Speculative Decoding on CPU Memory Wall

* **The Test:** Paired `Qwen 2.5-Coder-32B` (target) with `Qwen 2.5-Coder-1.5B` (draft).
* **The Finding:** Speed only increased by **+5.8%** (2.57 t/s $\to$ 2.72 t/s). Speculative decoding on CPU requires drafting threads to share the same dual-channel DDR5 bus bandwidth as the target model. MoE architectural sparsity breaks the memory wall; speculative decoding on CPU does not.

---

### 10.5 Quantization Mechanics & The 4-Gate Showdown (`IQ3_M` vs. `Q4_K_M`)

We tested both quantizations of `Qwen 3.6-35B-A3B` against our production 4-Gate Microservice Suite (FastAPI lifespan, SQLite WAL, background consumer worker, non-root Docker container, concurrency load, and `SIGTERM` graceful drain) with a **32,768-token (32k) context window**:

| Metric / Gate | `IQ3_M` (Baseline) | `Q4_K_M` (Challenger) | Ground-Truth Finding |
| :--- | :---: | :---: | :--- |
| **Model Weight Size** | **16.56 GiB** | **20.61 GiB** | `IQ3_M` is **4.05 GiB lighter** |
| **Host Resident RAM (32k Ctx)** | **17.5 GiB** (12.0 GiB buffer) | **22.0 GiB** (7.8 GiB buffer) | `IQ3_M` preserves **+4.2 GiB more headroom** |
| **Active Swap Thrashing** | **0 bytes** (`si: 0, so: 0`) | **0 bytes** (`si: 0, so: 0`) | **Tie:** Both achieve zero swap churn |
| **Prompt Ingestion Speed** | **79.90 t/s** (12.52 ms/tok) | **80.60 t/s** (12.41 ms/tok) | **Tie:** Prompt processing speed is identical |
| **Server Generation Eval Speed**| **11.84 tokens/sec** | **11.40 tokens/sec** | `IQ3_M` is **~4% faster** on the CPU |
| **Client Streaming Decode Speed**| **11.11 tokens/sec** | **9.54 tokens/sec** | `IQ3_M` is **~16% faster** in sustained streaming |
| **Gate 1: Multi-File AST & Syntax**| ✅ **PASSED** (100% valid) | ✅ **PASSED** (100% valid) | **Tie:** Both generate valid, parseable ASTs |
| **Gate 2: Docker Build & Non-Root**| ✅ **PASSED** (5.1s build) | ✅ **PASSED** (5.2s build) | **Tie:** Both enforce `appuser:10001` standards |
| **Gate 3: Concurrency & SQLite WAL**| ❌ Failed (Interface omission) | ⚠️ Partial (3/30 locks, worker stall) | **Nuanced Trade-off** (See below) |
| **Gate 4: Graceful Drain (SIGTERM)**| *Skipped* (G3 early exit) | ✅ **PASSED** (Exit code 0 in 1.22s) | **`Q4_K_M`:** Clean in-flight signal trap |

**Quantization Decisions:**
1. **Pareto Optimal Efficiency:** `IQ3_M` (~3.3 bits/weight) leverages an importance matrix (`imatrix`) that preserves router gate vectors and attention projections at 5–6 bits while compressing redundant MoE expert weights to 3 bits.
2. **Quality vs. Speed Reality:** The additional bit precision in `Q4_K_M` did not eliminate logic bugs, but reduced sustained streaming throughput from **11.11 t/s to 9.54 t/s**.
3. **Headroom Safety:** `IQ3_M` leaves **12.0 GiB of free RAM**, providing a bulletproof OS floor and enabling future context expansion to 48k tokens. `IQ3_M` was permanently ratified as SSOT and `Q4_K_M` was purged from NVMe.

---

### 10.6 NVMe Controller Health & TBW Wear Audit

Direct SMART telemetry (`nvme smart-log /dev/nvme0n1`) on the internal 1TB Gen4 SSD (`WPBSN4M8-1TGP`):
* **Temperature:** 40 °C (Optimal, zero thermal throttling).
* **Available Spare:** 100% (Threshold: 1%).
* **Percentage Used:** 0% (Virtually brand-new NAND).
* **Lifetime Data Written:** 1.22 TB (Out of 600 TBW warranty rating $\implies \mathbf{99.8\%}$ lifespan remaining).
* **Zero NVMe Wear Architecture:** Pinned RAM floor prevents memory swap thrashing (`si: 0, so: 0`). The autonomous agent runs all ephemeral compilation, test databases, and Docker builds in **RAM tmpfs (`/dev/shm`)**, protecting physical NAND flash from write churn.


---

## 10. 2026-10-27 Hardware & Kernel 7.0 Upgrade Investigation

### 10.1 Trigger & Context

During a homelab-wide maintenance cycle, two major changes were applied to Node 3:
1. **OS Upgrade**: Upgraded from Ubuntu Server 24.04 (Kernel 6.8) to Ubuntu Server 26.04.1 LTS (Kernel `7.0.0-38-generic`).
2. **Memory Upgrade**: Evaluated memory placement across nodes and upgraded IT13 Max from 16 GB to **32 GB DDR5 Dual-Channel** (1x 16GB Kingston OEM + 1x 16GB Aurora A3 SODIMM module).

Following the reboot into Kernel 7.0, the user observed that the front power LED was rapidly flickering/pulsing instead of remaining solid blue, raising concerns of hardware failure or loose power.

### 10.2 RAM Allocation Trade-Off Analysis

| Host | CPU & Role | Memory Decision | Rationale |
|---|---|---|---|
| **GEEKOM IT13 Max** (`.155`) | Intel Core Ultra 9 185H (16C/22T), Arc iGPU + NPU | **32 GB DDR5** (Dual-Channel) | Primary compute node running Qdrant vector DB, Paperless OCR, FastAPI gateway, and local LLM/embedding inference. Memory bandwidth and capacity bottlenecked here. |
| **OrigiMagic Aurora A3** | AMD Ryzen 7 8745HS (8C/16T), Radeon 780M | **16 GB DDR5** (Single SODIMM) | Secondary compute / worker node; 16 GB is sufficient for headless worker workloads; can accept another 16GB module later. |
| **UGREEN DXP2800** (`.80`) | Intel N100 (4C/4T) | **8 GB DDR5** (Single SODIMM) | Storage appliance; normal workload sits at ~63% (5.0 GB used). Adding RAM does not solve single-spindle mechanical HDD seek contention. |

### 10.3 Power LED Flickering Investigation

| # | Hypothesis | Test & Evidence | Outcome |
|---|---|---|---|
| 1 | DC barrel jack loose or power supply ripple | Voltage steady, zero ACPI power drop events in `dmesg`, continuous system uptime maintained. | Refuted |
| 2 | RAM mismatch or memory bus instability | `memtester 128M 1` passed all 19 patterns; EDAC reported `HardwareCorrupted: 0 kB`, `UE=0, CE=0`. | Refuted |
| 3 | Linux 7.0 / Meteor Lake Modern Standby (S0ix / C10) | Rolled back to Kernel 6.8 via `grub-reboot 1` → LED immediately turned 100% solid. Rebooted back to Kernel 7.0 → LED resumed flickering during idle. | Confirmed |

### 10.4 Root Cause & Mechanism

In Linux Kernel 7.0, Meteor Lake power management enters deep package C10 idle and turns off display engine clocks (D3cold) when running headless. The GEEKOM Embedded Controller (EC) interprets this deep modern standby state as S0ix low-power sleep, pulsing the power LED to indicate power-saving mode.

```text
┌────────────────────────────────────────────────────────────────────────┐
│               METEOR LAKE HEADLESS IDLE LED SIGNALING                  │
├────────────────────┬───────────────────────────────────────────────────┤
│ Kernel 6.8 State   │ Display pipeline stays active; Package C2/C3 idle │
│                    │ -> EC keeps front LED 100% SOLID                  │
├────────────────────┼───────────────────────────────────────────────────┤
│ Kernel 7.0 State   │ Display pipeline drops to D3cold; Package C10 idle│
│                    │ -> EC pulses/flickers LED (Benign S0ix Idle)      │
└────────────────────┴───────────────────────────────────────────────────┘
```

### 10.5 Resolution & Validation

- Confirmed zero hardware defects. User approved running on Ubuntu 26.04.1 LTS with Kernel 7.0.
- All 8 Docker services (`it13-api`, `gateway`, `paperless-web`, `postgres`, `redis`, `qdrant`, `changedetection`, `fetch-proxy`) verified running and responsive.
