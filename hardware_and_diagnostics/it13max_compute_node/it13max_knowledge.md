# IT13 Max — Deployed Stack and Decision Rationale

> Durable end-state knowledge for the local knowledge, capture, and execution stack.
> Origin: investigation journey at [it13max_investigation.md](./it13max_investigation.md)

---

## Role / Position

IT13 is the homelab compute and intelligence node. It provides explicit document/audio
ingestion, retrieval, bounded OCR and website fetching, review workflows, and isolated
coding execution. The node does not replace the Pi's network authority or the NAS's
storage role. The deployable source and runbooks live in the [private IT13 repository](https://github.com/deepshah08/it13max).

## Architecture

```
                 [Explicit client inputs]
                           |
                           v
                 [Authenticated API]
                           |
                           v
             [SQLite queue, ledger, outbox]
                 |                 |
                 v                 v
            [FTS5 search]      [Single worker]
                                     |
                                     v
                              [Heavy phase gate]
                           /          |          \
                          v           v           v
                    [Paperless] [Browser fetch] [Audio / runner]
                          \           |           /
                           v          v          v
                      [Review and durable events]
```

The execution constraint is one heavy phase at a time. SQLite owns durable queue and
source state; Qdrant stores vectors alongside SQLite FTS5 lexical retrieval. The worker
owns OCR, model inference, browser automation, and coding jobs so resource admission,
container cleanup, and maintenance remain coordinated.

### Component map

| Component | Role | Owner / location | State |
|---|---|---|---|
| Caddy + FastAPI | Authenticated front door, API, and capture UI | IT13 Compose stack | Deployed |
| SQLite WAL + FTS5 | Durable queue, source ledger, review history, and lexical retrieval | IT13 local NVMe | Deployed |
| Qdrant | Vector retrieval | Private local service | Deployed |
| systemd worker | Queue recovery, dispatch, heavy-phase admission, isolated jobs | IT13 host | Deployed |
| Paperless-ngx | Selected-document storage and bounded OCR | Private Compose services; OCR worker window controlled by IT13 | Deployed |
| changedetection + fetch proxy | Watch history and allowlisted HTTP/browser fetch | Private Compose services | Deployed; no real recurring watches configured |
| OpenVINO models | BGE embeddings, Qwen grounded answers, Whisper transcription | Short-lived worker containers | Deployed baseline |
| Coding runner | Bounded Python/Node/browser execution in detached worktrees | Network-disabled containers | Deployed |
| n8n event receiver | Optional downstream event destination | External Pi integration | Unconfigured |

## Mechanics — Normal Operation

1. A client submits explicit input through the authenticated API or documented CLI.
2. The API stores the request and source ledger in SQLite; durable event creation is
   transactional with accepted review state.
3. The single worker claims one heavy phase under the shared admission and resource
   policy. Paperless OCR, browser fetches, inference, and builds do not overlap.
4. Source text is indexed into FTS5 and Qdrant with stable source identity and version.
   Removals require a complete authorized manifest; an interrupted sync cannot erase
   sources.
5. Document/action proposals remain reviewable. Accepted decisions create typed,
   versioned local outbox events; external delivery requires an explicit destination.
6. Maintenance blocks new writers, drains active work, captures a consistent bundle,
   and uses an isolated restore check before recovery actions.

## Why This Design (vs. alternatives)

| Alternative | Why it was rejected or deferred |
|---|---|
| Run independent heavy daemons | 16 GiB shared CPU/Arc memory and measured workload gates require one owner to prevent OCR, inference, browser, and builds from colliding |
| Replace Qwen/BGE or add a specialist immediately | No representative labelled evaluation corpus established a concrete weakness; keep baseline until a predeclared quality gate can be measured |
| Use Spark-X2.5 as default | Q4 ran within the cap but adds an Ollama/llama.cpp runtime and lacks a fair held-out workflow comparison; BF16 official tag exceeded the cap |
| Adopt Jev/Laya from published results | The synthetic benchmark is only a screening signal; Laya's MLX latency does not transfer to Intel and neither is validated on private IT13 data |
| Enable crawlers, real watches, or automatic external actions | Explicit user selections and destinations preserve data scope, review, and side-effect control |
| Treat a local backup as disaster recovery | Goal 6's bundle is local; no approved off-node destination is configured |
| Reuse the general agent repo for deployed source | A dedicated private repo keeps IT13 setup, code, and operational evidence together; Learning remains the MDS knowledge base |

## Configuration and Guardrails

| Property | Current contract |
|---|---|
| Heavy execution | One controller-owned phase at a time; serialize OCR, ML, browser automation, and builds |
| Normal inference cap | 6 GiB; heavy slice has an 8 GiB aggregate limit |
| Retrieval | BGE-small embeddings + Qdrant cosine collection + SQLite FTS5/RRF |
| Generation | Qwen2.5-3B-Instruct exported to INT4; citation IDs checked against retrieved evidence |
| Document input | Explicit UTF-8 files or authorized Paperless API; no recursive crawler or default NAS mount |
| Website fetch | Allowlisted destinations, bounded response sizes and deadlines, private-address protections |
| User review | Required for obligation candidates; stale source decisions return conflict and require reload |
| External task delivery | Typed durable outbox; n8n URL/token and intended destination remain unconfigured |
| Backup | Local quiescent recovery bundle exists; off-node protection is not configured |
| Model promotion | Requires representative held-out quality, output-contract, latency, memory, and rollback gates |

## Failure Modes and Operational Limits

| Failure | Behavior and operator response |
|---|---|
| Controller or API restart | Durable queue and startup recovery preserve state; inspect status before retrying external side effects |
| Paperless worker interruption | Quarantine Paperless work, preserve staging, explicitly reconcile before another OCR window |
| Partial source sync | Keep existing indexed records until a complete authorized manifest is available |
| Source revision after review | Reject stale decisions; reload current review queue |
| Fetch error, empty/oversized page, or private destination | Fail the fetch without replacing the last successful snapshot |
| Event receiver unavailable | Retain durable events and retry; consumers must deduplicate `event_id` |
| Maintenance cannot drain or restore validation fails | Keep explicit maintenance/recovery state; do not overwrite live state from a test bundle |
| Small or biased evaluation corpus | Do not claim personal-use model accuracy or promote a specialist |

## Current Completion State

- Goals 1–4 and 6 are deployed with acceptance evidence in the execution records.
- Goal 5 is `evaluation_deferred_for_representative_samples`; the system stays on the
  current deterministic/BGE/Qwen baseline.
- R1–R6 and the round-two R2/R6 changes are complete. Independent Astra review is still
  pending; completion reports are not a substitute for that review.
- Real recurring watches, n8n delivery, and off-node backup destination remain
  unconfigured.
- Code, setup, source plans, reports, and live evidence are versioned in private
  [`deepshah08/it13max`](https://github.com/deepshah08/it13max). MDS docs are versioned
  in the public Learning repository.

## Companion Docs

- Investigation and decision history: [it13max_investigation.md](./it13max_investigation.md)
- Implementation and execution evidence: [private IT13 repository](https://github.com/deepshah08/it13max)
- Original architecture diagrams and provisioning record: [architecture blueprint](https://github.com/deepshah08/it13max/blob/main/node-it13-max-architecture-blueprint.md)
- Candidate model decisions: [IT13 model audit](https://github.com/deepshah08/it13max/blob/main/it13-model-audit.md)
- Jev/Laya public-data classifier pilot: [decision-layer plan](https://github.com/deepshah08/agentic-workflows/blob/main/docs/JEV_LAYA_DECISION_LAYER.md)
