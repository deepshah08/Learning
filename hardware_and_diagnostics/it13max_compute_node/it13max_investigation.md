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

## 9. Companion Docs

- Durable system knowledge: [it13max_knowledge.md](./it13max_knowledge.md)
- Implementation and review evidence: [private IT13 source repository](https://github.com/deepshah08/it13max)
- Model selection record: [`it13-model-audit.md`](https://github.com/deepshah08/it13max/blob/main/it13-model-audit.md)
- Existing hardware and homelab records: [IT13 Max compute-node folder](./README.md)
