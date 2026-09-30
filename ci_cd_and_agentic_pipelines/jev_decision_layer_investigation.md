# Jev Decision Layer — Investigation Journey

> Companion: durable architecture at [./jev_decision_layer_knowledge.md](./jev_decision_layer_knowledge.md)

Date: 2026-09-30
Session scope: Research Jev, build adapter, integrate into 3 workflows, verify live API, harden with HA circuit breaker.

---

## Context & Trigger

User observed growing popularity of "JEV based models" for classification tasks with binary/probability outputs. Hypothesis: Jev could replace expensive LLM output token costs for classification, segmentation, and binary attribution tasks where full generative text is overkill.

Three candidate workflows identified by user:
1. Email labels (currently Qwen 2.5 3B via Ollama)
2. Model picker (currently manual escalation ladder)
3. Tech radar tier classification (currently deterministic 4-point rubric)

### Prior Art: Deferred Decision (2026-09-24)

A prior evaluation in `JEV_LAYA_DECISION_LAYER.md` (commit `0203cdf`) had **deferred** Jev/Laya pilots because:
- No costly classification failure had been demonstrated
- No 100 independently reviewed gold labels existed
- Radar tiers are baseline rule outputs, not ground truth

This session revisited the decision with user-initiated momentum and budget approval.

---

## Phase 1: API Schema Discovery (The Hard Part)

### Initial assumptions (wrong)

Based on web research and the prior decision doc, we built the adapter with:
- Choice questions using `"options": ["label1", "label2"]` (list)
- Score questions using inline text descriptions
- Response parsing expecting `{"probability": 0.5}` for noul

### API reality (learned from 422 errors)

| Element | Expected | Actual |
|---|---|---|
| Choice options | `"options": [list]` | `"criteria": {label: description}` (dict) |
| Score scale | Inline text | `"criteria": [ordered list]` (0-indexed) |
| Noul response | `{"probability": 0.5}` | `{"noul": 0.13}` |
| Choice response | `{"selected": "X"}` | `{"choice": "X", "probabilities": {...}}` |
| Score response | `{"value": 3}` | `{"score": 2.81, "legend": {...}}` |

The initial smoke test returned 200 OK for a single noul question, but multi-question payloads with choice types returned 422. The error messages were clear:
```json
{"detail": [{"loc": ["body", "questions", "category", "choice", "criteria"], "msg": "Field required"}]}
```

For score, `criteria` as a dict returned:
```json
{"msg": "Input should be a valid list"}
```

**Lesson:** The Jev API's `criteria` field is polymorphic — dict for choice, list for score. This isn't documented prominently.

---

## Phase 2: Live API Validation Results

### Email Classification (5 test cases)

| Email | Category | Priority | Action | Archive | Confident? |
|---|---|---|---|---|---|
| Substack digest | Newsletter ✓ | LOW ✓ | False ✓ | True ✓ | **Yes** |
| Chase fraud alert | Finance ✓ | URGENT ✓ | True ✓ | False ✓ | **Yes** |
| Cold outreach (B2B) | ColdOutreach ✓ | LOW ✓ | — | — | Low conf (noul ambiguous) |
| GitHub PR review | Work ✓ | IMPORTANT ✓ | — | — | Low conf (priority 0.57) |
| Amazon shipping | Shopping ✓ | NORMAL ✓ | — | — | Low conf (noul ambiguous) |

**Key finding:** Category classification is excellent (1.00 confidence across all 5). The noul questions (`action_needed`, `auto_archive`) are less decisive, which drags down the "all confident" flag. The fallthrough to Qwen for ambiguous cases is exactly the right behavior — Jev handles the easy 40-60% instantly, and Qwen handles the rest.

### Model Router (5 test cases — all correct)

| Task | Jev Tier | Scope | Deep Reasoning | Correct? |
|---|---|---|---|---|
| "thanks lgtm" | luna_light | 0.0 | False | ✓ |
| "Fix typo in README line 42" | luna_light | 0.0 | False | ✓ |
| "Refactor email classifier for multi-user" | terra_medium | 2.9 | True | ✓ |
| "Debug SSH multiplexing drops on NAS" | sol_high | 0.6 | True | ✓ |
| "Design new agent memory architecture" | astra | 3.9 | True | ✓ |

**100% correct.** The model router is the most immediately useful integration.

### Radar Shadow Evaluation (55 cards)

- Agreement rate with deterministic rubric: **27.8%**
- Jev classified 41/55 cards as `benchmark_candidate`
- The deterministic rubric had 31 cards in "Adopt Now"
- All cards got `repro=False` — card summaries lack concrete reproducibility evidence

**Interpretation:** Jev is not wrong — it's more conservative. The deterministic rubric awards tiers based on stars/forks/score, while Jev evaluates whether the card's text description provides enough evidence for the tier. Both perspectives are useful; they should run in parallel.

---

## Phase 3: High-Availability Hardening

### Problem

User requirement: "If we run out of credits, services should run normally."

### Solution: Circuit Breaker Pattern

Implemented a process-local circuit breaker (no external state) with:
- 3 consecutive failures → breaker opens for 60s
- 402 (credits exhausted) → immediate 5-min cooldown
- 401 (bad API key) → immediate 5-min cooldown
- 422 (schema error) → logged but does NOT trip breaker (our bug)
- Catch-all exception guard — `evaluate()` never raises

**Verified behavior:**
1. Normal path: API call succeeds, breaker stays closed
2. Breaker open: all calls return `None` in 0ms, services run on existing baselines
3. Cooldown expiry: breaker auto-resets, next call goes through
4. Full email pipeline: breaker open → Tier 3.5 returns None → Tier 2 (seed knowledge) catches Chase fraud → Tier 4 (Qwen fallback) handles unknown senders

---

## Phase 4: English-Only Global Directive

Triggered by user observing Laya-MLX's multilingual config. Established Section 6 in `AGENTS.md`:
- Default to English-only checkpoints for all AI models
- 5-level trimming hierarchy: checkpoint selection → config flags → dependency pruning → quantized checkpoints → manual pruning (last resort)
- Never destructively modify shared transformer weights
- Exception: TTS/ASR retain Hindi (`hi`) and Gujarati (`gu`) for family use

---

## Decisions & Rationale

| Decision | Rationale |
|---|---|
| Jev as Tier 3.5 (not replacement) | Preserves all existing tiers; Jev is additive with fallthrough |
| Confidence threshold 0.7 | Matches prior eval doc's promotion gate; avoids false accepts |
| Circuit breaker (not retry) | Credits are finite; retrying a 402 wastes time. Fast-fail is better. |
| 422 doesn't trip breaker | Schema errors are deterministic bugs, not transient failures |
| Shadow eval before promotion | Matches the eval contract in `JEV_LAYA_DECISION_LAYER.md` |
| API key in `~/.env.local` | Never committed to any repo; loaded via `export $(grep ...)` |
