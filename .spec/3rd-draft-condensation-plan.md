# 3rd-Draft Condensation Pass — Plan

**Status:** RATIFIED 2026-06-03. Michael: *"lets write this up as a ratifyable plan, and lets also include scope about the engineering sections in part 2... honestly lets just start from the beginning and walk the book together... as interactable ask me tool calls. you can do the heavy lifting and research, then present me with ideas and other options, with notes too."*

**Execution begins:** next session (Michael is restarting VS Code for a fresh start). Begin at the **preface**, walk forward in reading order.

**Who owns what:** Cuts change what the book *says* — **Michael gates every cut** (per chapter, via AskUserQuestion). The **agent does the heavy lifting**: reads cold, builds the claim map, evaluates the Engineering Parallels, and presents concrete options + notes + a recommendation. Together we walk the book.

---

## Why this pass

The book is structurally done — front porch (Part One practices → Part Two doctrine), print layout (two-line titles, openers, page breaks), QR codes + verse-anchored links throughout, subtitle locked ("Beyond the Prompt: Discovering the Laws of Organized Intelligence"). What remains is **reader-fatigue from redundancy**, in two forms:

1. **Intra-chapter repetition.** A few chapters — especially some Part One practices — assert the same claim 3+ times. Michael feels it most in the practices.
2. **Part Two Engineering Parallels were never trimmed.** The front-porch plan ([`.spec/part1-front-porch-plan.md`](part1-front-porch-plan.md), 2026-05-30) said the Part 2 Engineering sections would be trimmed back once Part 1 carried the practical/how-to material — *"Engineering sections trimmed out of Part 2 (keep the best, e.g. Ch 8; placement decided while building)."* That trim was deferred and never executed. Now that Part 1 exists, each Part 2 Engineering Parallel must **re-earn its place**.

Draft lineage: 1st = initial drafts; 2nd = the v2 audit + chapter rebuilds (2026-05-29); **3rd = this condensation/redundancy polish.**

---

## The rule (must stay checkable, or the pass becomes "rewrite everything")

**Cut where the same CLAIM is asserted 3+ times inside ONE chapter, in non-recap positions.**

**Protected — never cut:**
- The *Try This* and the *Remember* box (Part One) — sanctioned recap.
- The *(Part Two: …)* bridge line (Part One).
- The Binding Question + Anchor Passage (Part Two).
- The **first and strongest** statement of any idea.
- All scripture / quotes / doctrine — only redundant **prose** is compressed, never a citation.

**Out of scope — keep, do not touch:**
- Themes that recur **across** chapters. That recurrence is the book's spine. Michael: *"It's okay to repeat themes across the whole book! but not in the same chapter."*

**Where the repetition tends to live:**
- *Part One:* story makes the point → "the principle it taught" restates it → "today's implementation" restates it a third time.
- *Part Two:* Core Reframe states the thesis → Engineering Parallel re-states it → Becoming re-states it. (Some restatement is structural — each section reframes for a reason — but 3× near-verbatim is fatigue.)

---

## Added scope: re-evaluate every Part Two Engineering Parallel

For each Part Two Modular chapter (Ch 0–12; epilogue/afterword if applicable), evaluate the **Engineering Parallel** section against three questions:
1. Does Part One now cover this practical material? (Part One carries the how-to.)
2. Does it add a **distinct, earned** insight, or merely restate the Core Reframe in tech terms?
3. Is it pulling its length, or has it bloated?

Per chapter, the options are **KEEP** (earns its place) / **TRIM** (compress to the load-bearing core) / **CUT** (Part One + Core Reframe already cover it). Ch 8 was flagged a keeper in the front-porch plan — re-confirm rather than assume.

---

## Workflow — walk the book together, from the beginning

**Reading order** (the walk): preface → Part One (Practice 1 → … → Practice 9 → coda) → Part Two (eleven-step reference → Ch 0 → … → Ch 12 → epilogue → afterword). **Glossary + Recommended Study** are reference lists — skip unless something is flagged.

**Per-chapter cycle:**
1. **Agent — diagnose (heavy lifting).** Read the chapter with fresh eyes; build a **claim map** (one line per paragraph = its core assertion); flag intra-chapter 3×+ repeats; for Part Two, evaluate the Engineering Parallel (KEEP/TRIM/CUT).
2. **Agent — present (AskUserQuestion).** Surface the findings as concrete options *with notes*: what's repeated, where it appears, what each option (keep / compress / cut) costs or gains, and a recommendation.
3. **Michael — decide.** The gate.
4. **Agent — execute, verify-gated.** Apply the approved cuts/compressions; diff-confirm no scripture/quote/doctrine was lost (only prose compressed).
5. **Periodically rebuild + render** (build.ps1 -Pdf + PyMuPDF) to check pagination + that the voice still reads clean; run the QR-collision detector if QR pages shifted; update `.scratch/provenance_*.md` if a quote's context moved.

Expected to be the **most time-locked** part of the book work — that's fine; it's interactive and collaborative by design.

---

## Tooling — right-sized (NOT all tools on every chapter)

- **Fresh-eyes subagents (Claude)** — the book-wide diagnostic. A cold reader is exactly the fatigue detector; the author can't see his own repetition. Default for the claim map.
- **`panel_redline_condense` (pg-ai-stewards MCP)** — reserved for the 3–5 chapters that flag heaviest, where multiple models voting on the actual condensation earns the cost.
- **agy / Gemini (`agy-cli` skill)** — one more independent read when a chapter is a coin-flip.

The diagnostic is ~80% of the value; the heavy tools are for the contested 20%. (Lesson from the v2 audit: running every tool on everything gets heavy fast.)

---

## Verify-gate (covenant discipline)

- **Diff every edit:** confirm NO scripture/quote/doctrine removed — only redundant prose compressed.
- **Rebuild + render-check** edited chapters for pagination + voice.
- **QR-collision detector** (PyMuPDF `get_drawings` → ~0.85in rects → vertical-overlap check) if QR-bearing pages shifted.
- **Provenance:** update `.scratch/provenance_*.md` if any quote's surrounding context moved.
- Likely side effect: **page count drops** as redundancy is cut — fine / good.

---

## Tracking & recording

- **This plan** is the authoritative record: `.spec/3rd-draft-condensation-plan.md`.
- **Per-chapter decisions** are appended to the DECISIONS LOG below as we walk — so a fresh session can resume mid-walk without re-deciding settled chapters.
- **`.mind/active.md`** carries the current-chapter pointer + state.
- **Session journal** at the end of each working session.

---

## Decisions log (append as we walk)

*(none yet — the walk begins next session at the preface, then Practice 1.)*

| Chapter | Repetition found | Engineering Parallel (Part 2) | Decision | Applied (commit) |
|---------|------------------|-------------------------------|----------|------------------|
| — | — | — | — | — |

---

## Resume instructions (for a fresh session)

1. Read this plan + `.mind/active.md` (current-chapter pointer) + the most recent `.spec/journal/` entry.
2. Continue the per-chapter cycle from the last chapter logged in the Decisions log above (settled chapters are done — don't re-open them).
3. For each new chapter: diagnose → present options via AskUserQuestion (with notes + a recommendation) → Michael gates → execute verify-gated → log the decision here.
4. Rebuild + render periodically; don't let `dist/` drift far from the manuscript.
