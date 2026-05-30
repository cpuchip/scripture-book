# Multi-Pass Audit Workflow (v1 — 2026-05-28/29 pass)

The audit + brainstorm process that drove the *Beyond the Prompt* completion pass. Captured here as a reusable recipe for future passes on this book and the next book.

---

## Premise

A single editor reading the manuscript catches a fraction of what the manuscript has wrong. A converged read across multiple deliberately-different perspectives catches most of it. The convergence itself is the signal — when three independent passes flag the same thing, the priority is unambiguous.

## The six passes

Each pass writes its output to `.draft/NN-name.md` with sequential numbering. The synthesis document at `.draft/00-COUNCIL.md` is the entry point for ratification.

### 1. In-house editor pass — `.draft/01-editor-pass.md`

The agent reads every chapter file in order. Output is structural: factual issues, gaps in understanding, contradictory passages, repeated passages, voice mismatches per chapter, content gaps (questions the book promises but doesn't answer). Format the audit as a numbered tier list (Tier 1 structural / Tier 2 polish / Tier 3 factual / Tier 4 carry-forward).

### 2. Gospel reader pass — `.draft/03-gospel-reader-pass.md` (subagent, background)

A `research-gospel` subagent reads the manuscript as a *faithful Latter-day Saint with no AI background* — Relief Society sister, Sunday School teacher, EQ member. They care about gospel content, not technical content. When they hit AI jargon they skim. Output answers: where did they get pulled in (the lines that landed), where did they lose the thread (jargon walls), which doctrinal moves felt fresh, which felt strained, which chapter would they tell a friend to read first, which to skip if not into tech, three concrete edits to make it friendlier without losing the AI parallel, Ben Test flags on overclaimed practice.

### 3. AI engineer reader pass — `.draft/04-ai-reader-pass.md` (subagent, background)

A `research` subagent reads as a *senior software engineer (10+ years), agnostic about religion or new to Christianity*. They're skeptical of mysticism but open to wisdom. They will sniff out hand-waving, theology-pretending-to-be-physics, anything that reads as the author flattering the tech without engaging real failure modes. Output answers: where does the engineering parallel land cleanly, where does it strain, where is the author overstating what AI is/does, where is the author understating, what skeptical-but-curious engineer concerns are missing (hallucination problem, stochastic-parrots critique, agency question, training-data problem, pace-of-change), which chapter most credible, which weakest, three concrete edits.

### 4. Editing research pass — `.draft/05-editing-research.md` (subagent, background)

A `research` subagent does web research on crossover-genre editing techniques. Survey successful crossover non-fiction (theology + technology, science + spirituality, parallel-pattern books) — C.S. Lewis, Eugene Peterson, Marcus Aurelius, Stephen Wolfram, Jaron Lanier, Cal Newport, Yuval Harari, plus LDS-flavored non-fiction (Bushman, Givens). Specific questions: how do they open? how long is their front matter? where do successful editors place personal narrative? what's the editorial received wisdom on "How to Read This Book" sections? specific recommendations for our book based on what's found. Cite sources with URLs.

### 5. Fact-check pass — `.draft/06-fact-check-results.md` (in-house)

Verify every scripture quoted against canon using `mcp__gospel-engine-v2__gospel_get` (workspace MCP). For each citation: confirm verbatim, flag inconsistencies (capitalization, paraphrase-vs-quote), flag misframings (where the chapter's claim about the verse doesn't match the verse). Categorize: confirmed accurate, confirmed errors actionable, still unverified (carry-forward). Same discipline applies to apostolic talks — verify against local talk files in `gospel-library/eng/general-conference/`.

### 6. Multi-model brainstorm — `.draft/07-multi-model-brainstorm.md` (pg-ai-stewards, parallel)

Fire 4+ brainstorm-lens pipelines in parallel via `mcp__pg-ai-stewards__spawn_subagent`. The same binding question goes to each lens; different models surface different perspectives.

**v1 used four lenses** (2026-05-28/29):
- Six Hats (kimi-k2.6) — White/Red/Black/Yellow/Green/Blue
- Reverse (kimi-k2.6) — failure modes → inverted moves
- SCAMPER (qwen3.6-plus) — Substitute/Combine/Adapt/Modify/Put-to-other-use/Eliminate/Reverse
- Crazy 8s (qwen3.6-plus) — eight chapter-targeted concrete moves

**v2 expansion shipped 2026-05-29** (substrate j8+j9, commits `7753424` + `23ce243`): 12 lenses total now available (added Mind Mapping, Brainwriting, Starbursting, Disney Method, Storyboarding, TRIZ, Forced Analogy, Worst Possible Idea). Pluggable model overrides at three layers (work_items → stages → pipelines metadata → catalog defaults). Lens selection via `start_brainstorm(p_lenses text[])`, model override via `p_models jsonb`.

For v2 of this audit, consider firing all 12 lenses; the marginal cost is small (~$0.10-0.30 per lens at default models) and the additional perspectives are non-redundant by design (each lens prompt targets a different output shape, not just a different topic).

**Gotchas learned on the 2026-05-29 v2 run (read before firing 12 lenses):**
- **~~The MCP `start_brainstorm` `models` param has a broken JSON schema~~ FIXED 2026-05-29** (`cmd/stewards-mcp/brainstorm.go`). The param was typed `json.RawMessage` (= `[]byte`), which the MCP SDK reflected as an array-of-int — so the documented per-lens object failed client-side with `InputValidationError`. Now typed `map[string]any` → free-form object schema; a regression test (`brainstorm_test.go`) guards it via the SDK's own generator. **The per-lens object now works over MCP** — `models: {"disney": {"model": "gemini-2.5-flash", "provider": "google_gemini"}, "triz": "kimi-k2.6"}`. **Note:** the fix is live only after `bin/stewards-mcp.exe` is rebuilt — the running binary is locked by Claude Code's MCP connection, so rebuild requires a Claude Code restart/MCP-reload, then `cd cmd/stewards-mcp && go build -o ../../bin/stewards-mcp.exe .`. Until that rebuild lands, the psql fallback still works: `SELECT stewards.start_brainstorm(p_binding_question:=…, p_destination:=…, p_models:='{...}'::jsonb, p_lenses:=ARRAY[…]::text[], …)` (8-arg signature in `extension/j9c-start-brainstorm-lenses.sql`; on Windows run via the **PowerShell** tool — write SQL to a temp file and `docker cp` + `psql -f`, MSYS mangles `/tmp/...`).
- **When dispatched via the SQL function directly, the aggregate `destination` does NOT propagate to file materialization.** The synthesis lands in `work_items.stage_results->'aggregate'->>'output'` for the `…-aggregator` work_item but no file is written. Recover it from the DB and write the `.draft` file by hand. (The MCP wrapper presumably handles this; the SQL path skips it.)
- **One opencode model is verified-unusable; GLM was a false alarm — settled 2026-05-29 by the substrate's own auto-probe** (`extension/m4-model-autoprobe.sql`; the earlier `smoke/test-glm-*.sh` shell probes were misleading — see below).
  - **`qwen3.7-max` — unusable, do not assign it to any lens.** The substrate's dispatch gets `HTTP 401` whose body is `Model qwen3.7-max is not supported for format oa-compat` — the gateway rejects this model on the OpenAI-compat endpoint and expresses it as a 401. Confirmed across multiple probes.
  - **`glm-5` / `glm-5.1` — usable; they stream fine.** Both map to backend `frank/GLM-5.1` (a reasoning model). An initial shell-grep streaming probe reported 0 content chars and these were wrongly flagged unusable — but that was a parser artifact. The substrate's real SSE parser (`parse_chat_sse`) extracts GLM's content fine: an auto-probe with a substantive prompt returned 385 chars, `finish=stop`. The v2-run emptiness on the glm-5 disney lens was therefore a **per-lens budget/transient issue, not a streaming incompatibility** — give a reasoning model adequate per-call `max_tokens` so reasoning doesn't exhaust the budget before content. GLM is fine for lenses.
  - **The substrate now self-corrects this class of error.** Model dispatchability lives in `stewards.model_capability` (M.1), the dispatcher substitutes an unusable resolved model for a usable one and logs it (M.2), and `enqueue_model_probe` + the work_queue terminal-transition trigger keep the verdicts current by testing the real streaming path (M.4). Browse it with the `list_models` / `list_connectors` MCP tools. The free models `deepseek-v4-flash` and `mimo-v2.5` stream reliably at $0 — a good default for fan-out. Still check each child's `status`/`maturity` after a run.
- **Diversify models across lenses** (Michael's v2 call): don't run all 12 on the two default models. Survey the catalog (`extension/j10-provider-models-pricing.sql`) and spread across gemini + the opencode_go set so each technique pairs with a different model.

## The synthesis document — `.draft/00-COUNCIL.md`

The synthesizer reads all six pass outputs and assembles a ratifiable council document. Structure:

- **TL;DR** — one paragraph naming the single biggest move + the single most credible page + the single most strained parallel
- **Tier 1+ — Brainstorm additions** (items the brainstorm surfaced that weren't in the original audit)
- **Tier 1 — Convergence items** (multi-pass agreement; recommend ratifying most)
- **Tier 2 — High-value single-pass findings** (one pass flagged; high impact)
- **Tier 3 — Verified factual fixes** (all should ship — no controversy)
- **Tier 4 — Carry-forward** (worth a council decision, not blocking)

Each Tier 1 item gets:
- Finding (what was flagged)
- Move (proposed action)
- Cost (small / medium / large)
- Source (which passes flagged it)
- **Ratification question (RQ#)** formatted for `AskUserQuestion`

Convergence map at the end: a table showing which item was flagged by which pass(es). Multi-pass agreement is the strongest signal.

## Convergence as a quality metric

The strongest signal isn't any single pass — it's two or more passes independently flagging the same thing. In v1 the convergences that drove the day's work:

- Front-loading (in-house + editing-research + brainstorm) → Tier 1.1 fix
- Ch 6 production-note credibility (gospel + AI + in-house) → Tier 1.2 carry-forward
- Ch 10 connection-pool strain (gospel + AI + in-house) → Tier 1.3 fix
- AI→gospel validation arrow (AI + brainstorm + editing-research Hodgson model) → RQ1.0b fix

When you see the same flag in two or three passes, that item ratifies essentially automatically. The disagreements between passes are where you spend ratification effort.

## Execution order after ratification

1. **Tier 3 first** (small, uncontroversial, factual). Clears ground.
2. **Tier 2 polish** (small wins; build momentum and feedback).
3. **Tier 1 structural** (do these last; they integrate the small wins rather than colliding with them).

In v1 this order held: Tier 3.1-3.5 small fixes shipped through the day, Tier 2.x landed in passes, the structural Tier 1.1 front-loading fix landed at the end as a single sweep.

## Memory discipline during execution

Update `.mind/active.md` and write a journal entry at the END of every substantive session, not in batches. The covenant clause `update_memory` is load-bearing — when memory is current, the next session loads cold with full context.

The v1 weakness: memory wasn't updated until Michael explicitly asked at end-of-day. v2 fix: update memory after each ratified Tier 1 item lands, not at end-of-session.

## Cost reference

v1 actual costs:
- Three reader-pass subagents: ran in parallel, ~$1-2 each (research-agent overhead)
- Editing research subagent: ~$1.50
- Fact-check pass (gospel_get + local file reads): essentially free
- Multi-model brainstorm (4 lenses): $0.32 total
- Estimated total audit cost: ~$8-10

For v2 with 12 lenses + same three reader passes: probably ~$10-15. Cheap relative to the work it enables.

## What to change in v2

Based on v1 lessons:

1. **Fire more lenses.** v1 used 4; substrate j8+j9 makes 12 available with the same machinery. Each lens prompt targets a different output shape so they aren't redundant.
2. **Pre-write the binding questions for each reader-pass subagent more carefully.** v1 reader passes were good but the AI-reader pass was the strongest; it had the most precise persona spec ("agnostic / new to Christianity, 10+ years engineering"). Apply the same precision to the gospel-reader persona spec.
3. **Update memory after each Tier 1 closes**, not at end-of-session. The pattern of long sessions without memory updates is fragile.
4. **Tag the audit's output `.draft/` files** with the date of the audit, e.g. `.draft/2026-05-28-01-editor-pass.md`. v1 used unprefixed numbering, which means a v2 audit would collide with v1 files. The date prefix preserves history.
5. **Include a "what changed since last audit" pass.** v2 should start by diffing the current manuscript against the v1 audit's covered state, so the editor pass knows what's new.

## Where this fits in the larger workflow

The multi-pass audit is the *gathering* step of an audit → council → execute → memory loop. The council document is the ratification surface. The execution is the actual manuscript work. The memory update is what makes the loop survive context boundaries.

Run this loop whenever a major manuscript pass is needed. Don't run it on small edits — the cost is in the perspective-shifting setup, and small edits don't benefit from multi-perspective input.
