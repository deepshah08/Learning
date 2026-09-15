# CruxDAG + SimuVerse Investigation: Independent Pathfinder and Simulation Workspaces

> Companion: durable knowledge at [./cruxdag_simuverse_knowledge.md](./cruxdag_simuverse_knowledge.md)
> Origin: learner-first CruxDAG/SimuVerse integration and repository sync.

**Repositories**: `deepshah08/cruxdag`, local SimuVerse checkout, `deepshah08/agentic-workflows`
**Branch**: SimuVerse snapshot from `codex/compiler-prototype`
**Status**: CruxDAG private repository created and pushed; SimuVerse snapshot bundled
**Date**: 2026-09-14

## 1. Trigger

The initial integration placed the concept mesh and simulations in one learner
workspace. Reading-first evaluation showed that a new learner needs to understand
the source article and provenance before using a simulation. The durable boundary is
therefore two independently scalable products with optional links:

```text
  [CruxDAG Pathfinder] ──article path──► [Provenance Reader]
          │                                      │
          └──────── concept DAG ◄────────────────┘
                           │ optional launch link
                           ▼
                    [SimuVerse Player]
```

## 2. Investigation Path

| # | Hypothesis / approach | Evidence | Outcome |
|---|---|---|---|
| 1 | Keep CruxDAG embedded as a SimuVerse top-level view. | Clean navigation did not match the learner's reading sequence; the simulation became the entry point before comprehension. | Rejected as the default product boundary. |
| 2 | Treat each Computer Networks article as a graph node. | The GFG master index and hyperlink order provide a useful tutorial path; source URLs remain explicit. | Selected. |
| 3 | Show only extracted prerequisite edges. | Several articles, including OSI layers, had sparse or disconnected source edges. | Supplemented with visibly labelled guided progression links. |
| 4 | Let a fixed canvas carry every graph size. | Dense maps clipped concepts and made relationships hard to inspect. | Added fit-to-graph, zoom, expand, and user-resizable map width. |
| 5 | Keep the article reader separate from source provenance. | Learners need the original text and figures beside the distilled explanation. | Reader now exposes original links and source figures. |
| 6 | Commit the raw working directory as-is. | It contained SQLite state, build/dependency directories, and an embedded API-key default. | Rejected; created a curated private repository. |
| 7 | Assume fresh installs have the same runtime secrets as the workstation. | Backend test collection constructed a Gemini client without a key. | Made Gemini initialization lazy and added schema compatibility migration. |

## 3. Root Causes and Fixes

| # | Component | Root cause | Fix |
|---|---|---|---|
| 1 | Pathfinder map | CSS grid allocated the canvas row as zero height. | Use an explicit `auto minmax(250px, 1fr) auto` map layout. |
| 2 | Article curriculum | The graph API did not encode tutorial ordering as prerequisite edges. | Add a Computer Networks tutorial path ordered by manifest `tutorial_order`. |
| 3 | Sparse DAGs | Source-derived edges can be incomplete for educational visualization. | Add deterministic guided links and label them separately from source links. |
| 4 | Dense maps | Fixed viewport and overlay inspector reduced usable graph area. | Add Fit all, zoom controls, fullscreen expansion, and a keyboard-accessible resize handle. |
| 5 | Provenance | A concept card did not expose enough original-source context. | Show canonical article links, source text access, and extracted source figures. |
| 6 | Fresh repository | Runtime data and generated artifacts were mixed with source. | Add `.gitignore`; omit DB/WAL, virtualenv, dependencies, and build output. |
| 7 | Fresh tests | Gemini client was mandatory during import even for local/unit tests. | Initialize Gemini clients only when `GEMINI_API_KEY` exists; fail clearly at use time. |
| 8 | Database evolution | Code wrote RFC provenance columns missing from the base schema. | Add columns to schema and an additive startup migration for existing WAL databases. |

## 4. Key Architecture

CruxDAG is the reading and concept-visualization service. SimuVerse remains an
independent simulation product. Cross-linking may use article/concept URLs or an
explicit API contract; neither project requires the other to build.

| Plane | Responsibility | Durable boundary |
|---|---|---|
| Tutorial | Orders Computer Networks articles and sections. | GFG manifest and canonical source URLs. |
| Reading | Displays distilled explanation, provenance, original text, and figures. | CruxDAG Reader and source preview endpoint. |
| Concept map | Shows tiered DAG, source edges, and guided progression. | CruxDAG Canvas and SQLite graph model. |
| Simulation | Runs interactive algorithms and scenarios. | SimuVerse React/Vite player. |
| Documentation | Preserves journey, end state, routing policy, and handoffs. | Learning MDS plus bundled `docs/`. |

## 5. Branch / Environment Differences

- `services/cruxdag` had no Git repository or remote; its current working tree was
  copied into `/Users/deep/Desktop/Pi_Projects/CruxDAG` as a curated root project.
- The new private remote is `https://github.com/deepshah08/cruxdag`, branch `main`,
  commit `de18216`.
- The local SimuVerse checkout is on `codex/compiler-prototype` and has local
  changes without a configured remote. Those files are bundled under `simuverse/`
  in the CruxDAG repository as a snapshot; the original checkout is unchanged.
- The agent workflow audit is pushed to `deepshah08/agentic-workflows` as commit
  `e304020`, with model routing guidance in `instructions/MODEL_ROUTING.md`.

## 6. CI and Testing

The curated CruxDAG repository was verified with:

```text
Backend targeted tests: 10 passed, 5 warnings
Frontend: tsc && vite build passed
Credential scan: no literal token in compose, README, or .env.example
Git whitespace check: passed
```

The previous SimuVerse verification recorded 55 unit tests and 34 browser tests.
Because the source checkout still has local changes, a fresh `npm run verify` is
required before treating the bundled snapshot as a new release baseline.

## 7. Commit History

| Commit | Repository | Description |
|---|---|---|
| `de18216` | `deepshah08/cruxdag` | Add curated CruxDAG Pathfinder service and safe local configuration. |
| `e304020` | `deepshah08/agentic-workflows` | Add cross-harness model routing guide with Astra/Sol/Terra/Luna tiers. |

## 8. Key Learnings

1. **Reading precedes simulation**: source article, provenance, and concept shape
   should be visible before asking the learner to operate a model.
2. **Educational links need semantic labels**: inferred guided links must remain
   visually and textually distinct from evidence-backed source edges.
3. **Independent products scale better**: CruxDAG and SimuVerse can release and
   test independently while retaining learner-facing deep links.
4. **Fresh clones must be secret-free**: runtime keys belong in `.env`, never in
   defaults, fixtures, or committed compose files.
5. **Import-time cloud clients are brittle**: optional providers should initialize
   lazily so local tests and offline readers remain usable.
