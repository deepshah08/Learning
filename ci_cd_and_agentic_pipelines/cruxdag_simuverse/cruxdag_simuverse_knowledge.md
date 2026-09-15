# CruxDAG + SimuVerse — Pathfinder, Provenance, and Simulation Boundary

> Durable end-state knowledge for the independent CruxDAG Pathfinder and SimuVerse learning products.
> Origin: investigation journey at [./cruxdag_simuverse_investigation.md](./cruxdag_simuverse_investigation.md)

## Role / Position

CruxDAG answers “what should I read, what concepts connect, and where is the
source?” SimuVerse answers “what happens when I operate the concept?” CruxDAG is
the learner's reading and visualization entry point; SimuVerse is an optional
interactive destination.

```text
  [GFG curriculum] ─► [TutorialPath] ─► [Reader + source figures]
                              │                    │
                              ▼                    ▼
                       [Concept Canvas] ───► [CruxCard]
                              │ optional concept/simulation link
                              ▼
                       [SimuVerse Player]
```

**Key facts about the boundary:**

- CruxDAG owns source ingestion, provenance, graph layout, and reading UX.
- SimuVerse owns simulation state, player controls, scenarios, and algorithm UX.
- Neither repository requires the other to compile or run.
- Links can be URL/API contracts; shared model code is not required.

## Architecture

| Component | Role | Location | Touched |
|---|---|---|---|
| FastAPI service | Extracts, normalizes, stores, and serves DAGs. | `app/` | ✅ |
| SQLite WAL store | Persists documents, nodes, edges, provenance. | `data/` at runtime | ✅ schema |
| Tutorial path | Orders Computer Networks article nodes. | `frontend/src/components/TutorialPath.tsx` | ✅ |
| Provenance Reader | Shows distilled text, original link, and source figures. | `frontend/src/components/Reader.tsx` | ✅ |
| DAG Canvas | Renders tiers, edges, zoom, fit, and expansion. | `frontend/src/components/Canvas.tsx` | ✅ |
| CruxCard | Displays selected concept, provenance, and optional figure. | `frontend/src/components/CruxCard.tsx` | ✅ |
| Pathfinder shell | Coordinates article selection and map/reader state. | `frontend/src/App.tsx` | ✅ |
| SimuVerse | Independent simulation player and compiler. | `simuverse/` snapshot | 🟡 bundled |
| Agent instructions | Cross-harness model routing and operating context. | `instructions/` and `context/` | ✅ |

## Source-file map

| Path | Role |
|---|---|
| `app/api/endpoints.py` | Graph, GFG curriculum, and source preview API. |
| `app/db/schema.sql` | Documents, concept nodes, edges, and provenance schema. |
| `app/db/database.py` | WAL connection, initialization, migration, and persistence. |
| `app/core/config.py` | Environment-driven runtime configuration. |
| `app/core/canary_watcher.py` | Optional Gemini model discovery and probes. |
| `frontend/src/App.tsx` | Reading/map state, article selection, expansion, and resize. |
| `frontend/src/components/TutorialPath.tsx` | Ordered article curriculum. |
| `frontend/src/components/Canvas.tsx` | Tiered graph and guided progression rendering. |
| `frontend/src/components/Reader.tsx` | Reading pane and original-source figures. |
| `frontend/src/pathfinder.css` | Learner-first responsive layout. |
| `simuverse/src/` | Simulation application snapshot; independent runtime. |

## Mechanics — learner flow

1. The user opens CruxDAG Pathfinder.
2. `TutorialPath` groups the Computer Networks manifest by section and orders
   article nodes by `tutorial_order`.
3. Selecting an article loads its canonical source URL and requests graph data.
4. `Reader` displays the distilled explanation, original article link, and a
   source-preview gallery when the origin exposes figures.
5. `Canvas` lays concepts into Tier 0–4 columns/rows and preserves source edges.
6. Missing educational continuity is rendered as green guided links, never
   silently labelled as source evidence.
7. Selecting a node opens `CruxCard`; the user can zoom, fit, expand, or resize.
8. An optional concept-to-simulation link can launch a matching SimuVerse model.

## Why this design

| Alternative | Why it is not the default |
|---|---|
| One combined application | Couples release cadence and makes reading depend on simulation UI. |
| Raw article website only | Provides source text but not concept connectivity or visualization. |
| Only source-derived edges | Produces sparse/disconnected learning maps for incomplete articles. |
| Unlabelled inferred edges | Blurs evidence and pedagogy; learners cannot judge provenance. |
| Fixed-size canvas | Clips dense graphs and hides relationships. |
| **Independent Pathfinder + optional player link** | Preserves reading-first learning while allowing each system to scale independently. |

## Configuration

| Property | Default | Control |
|---|---|---|
| Backend port | `8000` container / `8085` host | CruxDAG API service. |
| Database path | `data/cruxdag.db` locally | SQLite WAL runtime state; ignored by Git. |
| `GEMINI_API_KEY` | unset | Optional cloud extraction; local tests do not require it. |
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Local provider endpoint. |
| Map width | `540px` | Persisted in browser local storage; user-resizable. |
| Map mode | compact | Expanded mode fits larger concept graphs. |

## State / lifecycle

```text
  [Browse path] ─► [Select article] ─► [Read + inspect DAG]
        ▲                                  │
        │                                  ▼
        └──────────── [Return / choose next article]
                                           │
                                           ▼
                                  [Launch simulation]
```

## Failure modes and safeguards

| Failure | Signal | Safeguard |
|---|---|---|
| Missing cloud key | Import or extraction failure | Lazy Gemini client; use local provider or configure `.env`. |
| Sparse source graph | Disconnected concepts | Explicit guided progression links. |
| Dense graph clipping | Nodes outside viewport | Fit, zoom, expand, and resize controls. |
| Schema drift | SQLite missing provenance columns | Additive migration during `init_db()`. |
| Secret leakage | Key appears in source/config | `.env.example`, ignored `.env`, redaction before commit. |
| Coupled release | One product blocks the other | Separate repositories and optional linking contract. |

## Related repositories and synchronization

- CruxDAG: [deepshah08/cruxdag](https://github.com/deepshah08/cruxdag)
- Agent workflows: [deepshah08/agentic-workflows](https://github.com/deepshah08/agentic-workflows)
- Learning SoT: [deepshah08/Learning](https://github.com/deepshah08/Learning)
- Bundled SimuVerse snapshot: `simuverse/` in the CruxDAG repository.

## Companion docs

- [Investigation](./cruxdag_simuverse_investigation.md)
- [Model routing guide](../../../agentic-workflows/instructions/MODEL_ROUTING.md)
