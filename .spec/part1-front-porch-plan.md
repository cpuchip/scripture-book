# Part 1 "Front Porch" — Restructure Plan (living doc)

*Started 2026-05-30. A working plan, not a finalized spec — we hone it in conversation. Captures Michael's decision to make ONE book with a practice-forward Part 1 ("front porch") opening into the current doctrine as Part 2.*

## The decision
- **NOT two books.** Finish this one. Add a practice-forward **Part 1** as the front porch; the current chapters become **Part 2: Do(ctrine)** — the *why* behind the practice.
- **Goal: not money.** Teach what we've learned/practiced/discovered — including the real battle scars.
- **Engineering sections of Part 2 fall away** (mostly) — the practical how-to moves to Part 1, so the book stops repeating itself. (Decision pending: a few load-bearing engineering parallels in Part 2 may leave a trace/link rather than vanish — e.g. Ch 8's refinement-arrow, which the skeptic reader rated the book's best insight.)
- **Becoming / Binding Question / Anchor scripture:** stay in Part 2 (the study format works there). Part 1 does NOT use them. Part 1 ends in **reader-action ("try this")**, not author-commitment. (This cleanly resolves the old decisions.md §5 question: Part 2's "I commit" is the author's inward witness; Part 1's "you try" is the reader's outward action.)
- **Linking = the graphDB:** bidirectional cross-references — each Part 1 practice links to its Part 2 doctrine ("why this works → Part 2, ch X"), and Part 2 chapters link back to the practice ("the practice of this → Part 1, §Y"). Print renders the graph as cross-refs; a digital edition could render it as an actual navigable graph. The content is a graph; the book is one linear walk through it.

## The spine (the deepest coupling of Michael's list + the chat-mining)
Michael's "recurring thought" and the mining's #1 finding are the SAME thing, and it's the doctrinally-deepest practice — so it opens Part 1:

> **You don't start with a question. You start with a vision — often just a direction, the *intent*. The conversation — the counciling, the back-and-forth — is how you and the AI converge on the vision and sharpen it until it's clear enough to build.** Promptcraft isn't crafting one clever prompt; it's communicating a vision and refining it in dialogue. The project-level intent sets the *why*; each build needs its own vision, found together.

This maps straight into Part 2's heart: vision/intent = Step 1 Intent; converging-through-counsel = Abraham 4:26 ("the Gods took counsel among themselves"); vision-clear-before-building = the spiritual creation (Moses 3:5). The spine of the practice IS the doctrine.

## Teaching principle for Part 1: teach through the scars
Each practice is introduced through a **real failure we hit** (vulnerability = credibility — the audit's #1 finding; and it dissolves the "aspirational" worry, because you teach what you learned the hard way, not what you mastered). Candidate scars: the runaway agent that burned 230M tokens (→ watchdogs/bounds); the fabricated D&C 104 quote (→ provenance gates); the 33% Ben-Test self-assessment (→ honest retros); the glm-5 shell-grep misdiagnosis (→ verify via the real path).

## Proposed Part 1 arc (groups Michael's 16 points + the mining into a throughline)
Throughline: **vision → converge → bound → context → delegate → keep honest → reflect → build your own.** Punchy (each ~2–4 pages, action-oriented), not exhaustive.

| Part 1 practice | Folds in (Michael's #) | Mining finding | → Part 2 doctrine |
|---|---|---|---|
| 1. Talk, don't command — promptcraft as conversation | 1, 16 | discover-by-iterating; conversational-for-meaning | Intent · Spiritual Creation |
| 2. Council & ratify before you build (plan first) | 2, 12 | councils + ratification batches | Covenant/Council (Abr 4:26) |
| 3. Set the bounds that do the heavy lifting — intent, covenant, stewardship (and why watching fades as they mature) | 3, 4, 6, 7 | delegate-with-bounds | Intent · Covenant · Stewardship · Watching |
| 4. Pack your context without waste — layering through files & memory | 5 | externalized memory; context engineering | Line upon Line |
| 5. Let it do the heavy lifting — research, tools, delegation | 9, 15 | delegate; multi-model brainstorm; tool discovery | Stewardship · Physical Creation |
| 6. Keep it honest — skills, MCPs, provenance against hallucination | 10 | provenance-as-gate; verify-via-real-path | Watching · Atonement |
| 7. The retro that changed everything — ask the AI what's working, what to build, what's in the way | 14 | Ben Test; the periodic retro (Michael's biggest early help) | Sabbath · Atonement |
| 8. Build it together — your workspace, your workflows, (advanced) your own harness | 8, 13, 11 | build-your-own-harness (pg-ai-stewards) | Consecration · Zion |

Multi-model division of labor (Claude=fidelity/logic, Gemini=voice, cheap panel=brainstorm) threads through 5 and 7.

## Proposed Part 1 entry format (repeatable, practice-forward)
1. **The practice** — name it in a sentence.
2. **The scar** — the real failure that taught it (short story).
3. **How to do it** — concrete, transferable steps from real work.
4. **Why it works** → cross-link into Part 2 doctrine (the graph edge).
5. **Try this** — one concrete thing to do in your next AI session (reader-action; replaces Becoming for Part 1).

## Open decisions to hone (next conversation)
- **A. Battle-scars-as-teaching** — adopt as the Part 1 principle? (Recommend yes.) If so, we surface the real scars deliberately.
- **B. How short is "TL;DR"?** — confirm punchy (~2–4 pp/practice), ~8 practices, resist bloat.
- **C. Engineering parallels** — full migration to Part 1, or leave the best 1–2 as doctrinal illumination in Part 2 (with a link to the Part 1 practice)?
- **D. Part 1 organization** — by practical workflow (reader-first, proposed) vs. forced onto the 11-step skeleton (cleaner mapping, but re-imports the doctrine-forward problem). Recommend workflow-first + cross-links carry the 11-step mapping.
- **E. Front matter** — how does the existing preface adapt to a Part 1 / Part 2 book? Does Part 1 get its own short intro (the porch's door)? The afterword/epilogue placement.
- **F. Title/subtitle** — the weak subtitle (T2.5) now needs to signal *how-to + why*. Defer, but it's downstream of this.
- **G. Print vs digital** — print = cross-refs; a later digital/cpuchip.net edition could render the actual graph.

## Honing round 2 — 2026-05-30

**Resolved:**
- **Length (B):** Part 1 at 30–50+ pp is right — it must teach real skills *and* the scars we overcame to find them.
- **Organization (D):** workflow-first, confirmed. Framing: **the 11-step cycle is the aspirational ideal we strive toward; the 16 practices are how we work toward it, imperfectly — but they are meant to be ETERNAL CREATION PRINCIPLES that survive the weekly churn of new models and releases.**
- **Scars (A):** adopted — teach each practice through the failure that taught it.

**New:**
- **Part 1's thesis / promise:** *"The tools change weekly. These principles don't."* That durability is Part 1's unique value — most AI how-to is obsolete on arrival; a book grounded in eternal creation principles is not.
- **Format refinement (this is what delivers the durability):** each Part 1 entry separates **(a) the principle (eternal) → (b) how we do it today (a 2026 time-capsule; *will* date) → (c) try this.** The eternal principle is the edge into Part 2 doctrine; the dated implementation (MCPs, harnesses, specific models) is openly marked "this is how, for now," and the reader is taught to re-apply the principle to tomorrow's tools. NOTE for honesty: some of the 16 are deep principle (council, intent, bounded stewardship — eternal); some are 2026 implementation (build-your-own-harness, MCPs/skills — dated). Part 1 must name which layer each is, or it dates with the tools.
- **The retro (#14) is a THREAD, not just one practice:** anchored by 1–2 main Part 1 chapters, bleeding into the bounds + build-together practices, and threading into Part 2's Atonement (re-aiming) + Sabbath (reflection) chapters. The retro is the connective tissue between Part 1 practice and Part 2 atonement doctrine — the practical face of "turning the eye back to intent."
- **Audience reframe:** ONE larger audience, two parts ("two doors, one house") — NOT two wary tribes. **Rework or drop the front-matter "note to the Saint wary of AI" / "note to the engineer wary of religion."** Replace with a single short orientation: two parts, start where you are, the parts cross-link.
- **Biographical numbers (corrected):** 18 yrs software engineering; ~3.5 yrs using AI; ~5 months of the with-AI retro discipline in this workspace. (Earlier "14 years of retro" was an agent overstatement — corrected.)

**RATIFIED (round 2 close):**
- **Retro anchors:** TWO Part 1 chapters — **"The Retro"** (diagnose: ask what's working / what to build / what's in the way; the cadence) + **"Build It Together"** (fix: turn the retro's answers into workflows, skills, MCPs, your own harness). Diagnose→fix pair. Bleed into Part 2 **Atonement (Ch 8)** + **Sabbath (Ch 11)**; cross-links point there.
- **Front-matter:** DROP the two wary-tribe notes; REPLACE with one short orientation — "two parts (practice / doctrine), start where you are, they cross-link. Two doors, one house."
- **Engineering parallels (C):** drop most from Part 2, keep the best (Ch 8's "what's refined is the developer, not the model"), trim hard to kill duplication. **Placement deferred on purpose** — build Part 1 first, then decide empirically whether the kept parallels live in Part 1 or stay as doctrinal illumination in Part 2 (with a link).

**LOCKED — Part 1 chapter format (Agans-informed; reviewed `books/debugging/9-indispensable-rules/08-keep-an-audit-trail.md`):**
1. **Open with the story that taught it** (reframed 2026-05-30) — a failure we learned from, a spectacular **success** where the principle paid off, or (best) a **scar→fix→payoff arc**. Lead with a real failure where one exists (vulnerability = the audit's #1 credibility signal); use success where there's no scar or it teaches better; keep the failures in — don't curate to a brag reel (Ben Test). Agans leads with the story; the rule is named after the reader feels it. Per-practice lead recommendations + verified stories: `.scratch/provenance_part1.md` (incl. the scar-vs-success addendum). Candidate scars: 230M-token runaway → bounds; fabricated D&C 104 → provenance gates; 33% Ben-Test → the retro. Candidate successes: the becoming/brain memory app → portability; pg-ai-stewards + simple-games (built beyond his own competence) → delegation; storygames with his child → conversational collaboration.
2. **The principle (eternal)** — named with a memorable slogan → cross-link "why this holds: Part 2, ch X."
3. **How we do it today** — the dated 2026 implementation, openly stamped "this is how, for now."
4. **(more scars as earned)** — Agans uses several per rule; do likewise where we have them. Consider a recurring connective analogy (Agans' food-allergy diary).
5. **Try this** — one concrete reader-action for their next session (Part 1's outward analog of Part 2's inward "Becoming").
6. **Remember** — a short recap box: the principle in a line + its scar (Agans' "Remember" box).
Agans confirms the LENGTH call: his rule-chapters are 13–38 KB, dense with stories — "TL;DR" = practice-forward, not thin.

**Still open:** E (does Part 1 get its own short intro/door; afterword/epilogue placement) · F (title/subtitle) · the empirical Ch-8-parallel placement (decide while building) · which scars pair to which of the 8 practices.

## Status
Recording + honing. NO building yet. Source list: Michael's 16 pressing practices (this session) + `.draft/20260530-how-we-actually-work.md` (the mining). Continue the conversation.
