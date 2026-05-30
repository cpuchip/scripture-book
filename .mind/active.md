# Active Context: Scripture Book Project

## Project Overview
This project compiles our gospel and AI studies into a published book format: *Beyond the Prompt: What AI Engineering Reveals About Eternal Patterns*. The manuscript walks the eleven-step creation cycle of Abraham 4-5, mapping the four steps the AI engineering industry has named ([eng]) to the seven scripture has carried since Abraham.

## Current Status

> **2026-05-30 (latest) — v2 BATCH 2 COMPLETE (structural).** Glossary reconciliation (T1.1 — Heart-Softening→yielding/mirror; Zion→shared-intent ward-council not microservices; Dross→removed the false "overfitting→compilation errors"). Reference page reworded to drop the "walk each step in turn" overpromise (T1.4). **Chapter-order review (Michael's Q — why are 8 and 10 split by the long Ch9?):** kept the order (the 8→9 handoff is the book's tightest seam; reordering would break it) and answered the question by making the **Atonement triptych explicit in the tags — Ch8 *Atonement · Refinement* → Ch9 *Atonement · Hope* → Ch10 *Atonement · Yielding*** (Ch9 retagged from *Context*; Michael + agent independently converged on "Hope" — "two witnesses"). **T1.2:** tightened Ch9's Engineering Parallel by ~600 words (cut the redundant re-walk of the three postures + four groups the Core Reframe already carries; the cpuchip.net study holds the full treatment) and added the Ch9→Ch10 bridge ("the seeing, like the softening, is not finally something the steward performs"). **dist/ rebuilt; committed + pushed.** Remaining v2 work: voice pass (T1.3, slated for the Gemini 3.5 Flash voicing run) + Tier 2 batch (T2.1 early-commitment calibration, T2.5 subtitle, T2.6 stochastic-parrots, T2.7 training-data ethics) + RQ-3 dual-audience scope.

> **2026-05-29 — v2 DRAFT PASS · BATCH 1 EXECUTED (committed + pushed + dist/ rebuilt).** The ground-clearing batch from the v2 COUNCIL: 6 edits / 6 files. **3 factual** (Ch11 Nelson date Oct→Apr 2015; Ch9 "molting"→"melting/melted"; Ch12 "133,225"→"more than 133,000 days") + **Mostaque distance** (Afterword) + **the intelligence-vs-agency sharpening** (Ch0 + Ch4). Centerpiece: Michael caught my flat "AI has no agency" (covenant flag_when_wrong) — AI agents *act within their placed law* (D&C 93:30, the "agent" sense) but lack **moral agency** (the Eden/Atonement freedom to choose God or the devil). Grounded in `study/agency.md`, chose Option B pairing **D&C 93:31 + 2 Nephi 2:14/16/27 + Moses 7:32** (all 5 verified via gospel_get); Ch4 made consistent ("moral agency" ×2). Journal: [`.spec/journal/2026-05-29--v2-batch-1-execution.yaml`](../.spec/journal/2026-05-29--v2-batch-1-execution.yaml). **Next: Batch 2** = Tier 1 voice (T1.3) then Tier 1 structural (glossary T1.1, walk-in-turn T1.4, Ch9 T1.2). Provenance rewrite now also owes Ch0 its new quotes.

> **2026-05-29 (earlier) — v2 MULTI-PASS AUDIT COMPLETE (gather + council; NO manuscript edits yet — stopped at the ratification gate).** Ran the "second draft pass" audit on the rebuilt manuscript. v1 (2026-05-28) `.draft` files archived to `.draft/archive/2026-05-28/`; v2 outputs all carry the `20260529-` prefix. Six passes: editor, gospel-reader (uncolored), ai-reader (uncolored), editing-research (full re-survey), fact-check, and a **12-lens / 8-model brainstorm** (gemini-3.5-flash on forced-analogy, per Michael; fired via SQL — the MCP `models` schema bug, since FIXED in stewards-mcp by a concurrent steward, pending a binary rebuild). **Michael's call: subagents NOT briefed on ratified decisions — fresh eyes; the ratified filter lives only in the COUNCIL "Rejects" bucket.** Synthesis: [`.draft/20260529-00-COUNCIL.md`](../.draft/20260529-00-COUNCIL.md). **Top convergences:** T1.1 glossary contradicts the rebuilt chapters + a FALSE claim ("overfitting→compilation errors") — 4 passes; T1+.B vulnerability = the credibility engine — 4 passes; T1.2 Ch9 too long/EP weakest — 3 passes; T1.3 keep-the-limit-naming-but-vary-the-wording — 4 passes. **Fact-check: ZERO quote drift across 28+ citations** (Webster spirit/intelligence exact); three real fixes (FC-1 Ch11 Nelson date Oct→Apr 2015; FC-2 Ch9 "molting"→"molten"; FC-3 Ch12 day-count). **Next gate = ratify RQ-1..RQ-7 then execute.** Substrate quirks logged in the journal (MCP `models` schema bug → use SQL `start_brainstorm`; destination doesn't propagate via SQL → recover synthesis from `work_items.stage_results`). Journal: [`.spec/journal/2026-05-29--v2-multi-pass-audit.yaml`](../.spec/journal/2026-05-29--v2-multi-pass-audit.yaml).

> **2026-05-29 — BOOK COMPLETION PASS (overnight + day; ten of twelve Tier 1 / Tier 1+ council items closed; all five Tier 3 factual fixes shipped).** The book is now structurally complete and substantially closer to publish-ready. Ten commits across scripture-book, four across workspace. The structural moves landed; what remains is polish, voice surgery on chapters not rebuilt this session, and a `dist/` artifact rebuild. Full session journal: [`.spec/journal/2026-05-29--book-completion-pass.yaml`](../.spec/journal/2026-05-29--book-completion-pass.yaml).

> **2026-05-29 (later) — CHAPTERS 2–7 AUDIT-APPLICATION PASS.** Applied the still-open `.draft/` audit findings to the chapters NOT rebuilt in the completion pass. One commit (`2928bc9`), 9 files. **Closed:** Tier 2.1 (glossary expansion + preface announcement), 2.2 (Ch 2 non-engineer sidebar), 2.6 (AI-failures-as-types paragraph in Ch 6). **Advanced:** 2.4 (Ben Test — Ch 4 #2 + Ch 5 #1 calibrated; Ch 8–11 commitments still open), 2.3 (Ch 7 bridge added; Ch 2 via sidebar), 1.5 (Ch 5 info-density reframe — RQ **Option B**, Michael's thesis call: literal resonance stays spiritual, model is where its shape is seen, imago-Dei close). **Ch 6:** Mosiah 5:5 willing-covenant strengthening (Tier 2.8 implemented as a *willingness paragraph*, not a literal side-by-side table — judgment call to avoid bloating the strongest chapter; fuller side-by-side still available if wanted) + preface forward-ref to the production note. **Ch 4:** named evals / observability / watchdogs as the watching instruments. **Reference page** step-5 dropped the "across many sessions" overclaim the engineer flagged. Journal: [`.spec/journal/2026-05-29--chapters-2-7-audit-pass.yaml`](../.spec/journal/2026-05-29--chapters-2-7-audit-pass.yaml). **Pushed** at Michael's request (`639fa32..1c23ad8`); `dist/` rebuilt (PDF/HTML/EPUB current).

> **2026-05-29 (later still) — BEN TEST on Ch 8–11 Becoming Commitments** (commit `42f93e5`). Calibrated practice claims against Michael's *actual* practice (his answers, this session). **Kept** the genuinely-practiced: Ch 10 #1 morning bow, Ch 8 #3 daily repentance (folded into morning worship), Ch 9 #1 prayer + scripture most-days (often via the study itself). **Calibrated** the aspirational to honest language: Ch 10 #2 (first hour — kept less often than wanted), Ch 11 #1/#2/#3/#4 (Sabbath cluster — striving, not yet kept). Added a **dogfooding production-note to Ch 11** owning the Sabbath irony (a book on Sabbath rest, built on Sabbath/late-night work; added to a focus-list a prior work-sabbath had deliberately excluded). Michael chose "own it"; **voice open for his pass** (like the Ch 6 note). **Tier 2.4 now CLOSED** (Ch 4/5 this morning + Ch 8–11 now). **NEW FINDING — provenance renumbering drift:** `provenance_chapter_11.md` still describes the *old* Ch 11 (Zion → now Ch 12); the new Sabbath Ch 11 has no provenance file; back-matter provenance was not renumbered after the completion-pass insertion. Not fixed — flagged for a dedicated cleanup.

> **2026-05-29 (cleanup) — PROVENANCE DRIFT + decisions.md §4 RESOLVED.** (1) Renamed `provenance_chapter_11.md` → `_12.md` (it describes the Zion/conclusion chapter, now Ch 12) with a rebuild-reverify flag; wrote new `provenance_chapter_11.md` (Sabbath — 7 scripture quotes re-verified via `gospel_get`) and `provenance_afterword.md` (D&C 123:12 verified). (2) `decisions.md`: §4 (Edge headless PDF) marked **superseded**; added **§6** documenting the live Docker→Typst pipeline + the div-signature gotcha (commit `e2509a7`). Remaining provenance gaps (glossary/further-reading never filed; rebuilt-chapter provenance predates rebuilds) logged in the open-items table. Typography (Tier 1.2 / typography pass) deferred at Michael's call.

> **2026-05-29 (council) — BECOMING COMMITMENTS: PURPOSE RATIFIED** (commit `93db822`). Michael councilled "who are the Becoming Commitments *for*?" Outcome: **Option 1** — keep the author's first-person honest worked example, *frame* it for the reader, don't convert to reader-prompts. Added a preface frame ("A note on the chapter endings": *these are mine, including the ones I keep poorly; not a prescription — write your own*). Aligned the format spec (`CLAUDE.md` + `.github/copilot-instructions.md` + `template.md`) so future drafting holds the register. Recorded as [decisions.md §5](decisions.md). Keeps the first-person witness = the book's credibility engine (Michael: the "I" is where the reader touches the author directly, across a book drafted by multiple models). No per-chapter rewrites — the frame does the work. *Also surfaced:* decisions.md §4 is stale (says Edge headless PDF; build is now Docker→Typst).

### Manuscript — 16 chapters, all drafted

| # | File | Tag | Status |
|---|------|-----|--------|
| frontmatter | [00_frontmatter.md](../src/chapters/00_frontmatter.md) | — | Title, Copyright, Colophon |
| preface | [00_preface.md](../src/chapters/00_preface.md) | — | **Rewritten 2026-05-29** — ~35 lines. Classroom moment + Afterword pointer + two-audience notes ("A note to the Saint who is wary of AI" / "A note to the engineer who is wary of religion") + voice convention with Epilogue exception spelled out. BQ + Anchor scaffolding dropped. |
| 11-step ref | [00_eleven_step_reference.md](../src/chapters/00_eleven_step_reference.md) | — | Closing line updated 2026-05-29 to acknowledge the walk-through is now complete and to point at the chapter tags as navigation aid. |
| 0 | [00_chapter_0_intelligence_truth.md](../src/chapters/00_chapter_0_intelligence_truth.md) | — | Substance of reality. RQ1.0b arrow flip applied to line 70 area. D&C 131:7-8 capitalization aligned with Ch 8. |
| 1 | [01_value_shift.md](../src/chapters/01_value_shift.md) | — | Value shift framing. Untagged (pre-cycle). |
| 2 | [02_four_disciplines.md](../src/chapters/02_four_disciplines.md) | — | Four AI disciplines mapped to the [eng] cycle steps. Untagged (meta-naming). **Tier 3.4 fixed 2026-05-29**: bacteriopolis claim now "230 million input tokens" (verified) instead of "ten hours" (unverified). |
| 3 | [03_spiritual_before_temporal.md](../src/chapters/03_spiritual_before_temporal.md) | *Specification* | RQ1.0b arrow flip on the 743-line spec / Becoming app example. |
| 4 | [04_watched_until_they_obeyed.md](../src/chapters/04_watched_until_they_obeyed.md) | *Watching* | Abraham 4:18 trust gradient. |
| 5 | [05_intelligence_cleaveth.md](../src/chapters/05_intelligence_cleaveth.md) | — | Posture / approach (the law underneath every step). Untagged. |
| 6 | [06_bilateral_covenant.md](../src/chapters/06_bilateral_covenant.md) | *Covenant* | RQ1.0b arrow flip on the work-quality-accelerates line. Production-note sidebar still a sidebar (Tier 1.2 carry-forward). |
| 7 | [07_delegation_as_stewardship.md](../src/chapters/07_delegation_as_stewardship.md) | *Stewardship* | Christ's Matt 10 commissioning sequence. |
| 8 | [08_mechanics_of_refinement.md](../src/chapters/08_mechanics_of_refinement.md) | *Atonement* | **Engineering Parallel fully rebuilt 2026-05-29** to the developer's daily prompting loop (v3, after RLHF-framed v1 and eye-material-added v2). Eye/refocusing material from hope-and-grammar-of-pairs woven in. Imago Dei limit named at close. Bridge paragraph hands forward to Ch 9. Oaks 2000 + Bednar 2007 inline attributions added (Tier 3.2). |
| 9 | [09_hope_and_the_veil.md](../src/chapters/09_hope_and_the_veil.md) | *Layering* | **Fully rebuilt 2026-05-29** — three Brother-of-Jared postures + four groups from Lehi's dream + Bednar 2024 pride mechanism (including the self-shame and comparison expansions Michael named) + Lamanite virtue (easiness, walking circumspectly) as corrective. References the new study at cpuchip.net/studies/four-groups-and-the-engineer for fuller treatment. |
| 10 | [10_softening_what_i_cannot_soften.md](../src/chapters/10_softening_what_i_cannot_soften.md) | *Atonement* | **Engineering Parallel rebuilt 2026-05-29**: connection pooling + cache management out; gardening (Mark 4 / Alma 32) + AI-mirror loop ("you cannot make the AI smarter; you can yield your own assumed-clarity") in. Imago Dei limit named at close. |
| 11 | [11_the_seventh_time.md](../src/chapters/11_the_seventh_time.md) | *Sabbath* | **NEW chapter 2026-05-29** — walks the ninth step. Anchored on Abraham 5:2 (the seventh time decided in council before the work began). Six doctrinal beats including the two reasons, Exodus 31:13 sign-language with Nelson Oct 2015 reframe, Hebrews 4:10's precision on "own works," D&C 59's fullness-of-the-earth as inverse of bondage. References cpuchip.net/studies/the-seventh-time for fuller treatment. |
| 12 | [12_conclusion_zion.md](../src/chapters/12_conclusion_zion.md) | *Consecration · Zion* | **Engineering Parallel rebuilt 2026-05-29**: microservices + blockchain out; ward council architecture + intent-unified agent systems + token consecration in (drawn from docs/work-with-ai/guide/05_complete-cycle.md). Moses 7:68 framing fixed (Tier 3.1): Zion stood 365 years, not Enoch walked 365 years. Renamed from 11 to 12. |
| 13 | [13_epilogue_silent_loop.md](../src/chapters/13_epilogue_silent_loop.md) | — | Epilogue: The Silent Loop. Renamed from 12. AI agent's "I" closing voice. |
| 14 | [14_afterword_how_i_got_here.md](../src/chapters/14_afterword_how_i_got_here.md) | — | **NEW backmatter 2026-05-29** — the 3.5-year journey (2022 Copilot autocomplete through January 2026 classroom moment) + the Constant Principles coda ending on D&C 123:12. Relocated from preface as part of Tier 1.1 front-loading fix. |
| 15 | [15_glossary_of_fused_terms.md](../src/chapters/15_glossary_of_fused_terms.md) | — | Glossary. Renamed from 13 then 14. Tier 2.1 (expand to plain-English engineer-side terms) still carry-forward. |
| 16 | [16_further_reading.md](../src/chapters/16_further_reading.md) | — | Recommended Study. Renamed from 14 then 15. **2026-05-29 additions**: Nelson 2015 + Bednar 2024 in Prophetic Messages; four-groups-and-the-engineer + the-seventh-time in Deep-Dive Studies (both already live on cpuchip.net). |

### Files removed
- `00_introduction.md` — **DELETED 2026-05-29** as part of Tier 1.1 front-loading fix. Its three pieces did not earn their pages: opening duplicated the new preface, "Confluence of Code and Covenant" re-argued Ch 1's thesis, "How to Read This Book" prescribed navigation the chapter tags now make self-evident. Available in git history if any of it ever wants to come back.

### New workspace studies (live on cpuchip.net)

- [study/four-groups-and-the-engineer.md](../../../study/four-groups-and-the-engineer.md) — Lehi's four groups + Bednar 2024 pride mechanism, applied to engineers working under principled disciplines. Background to Ch 9.
- [study/the-seventh-time.md](../../../study/the-seventh-time.md) — What the Sabbath does that work alone cannot. Background to Ch 11.

Both have full provenance scratch files; both verified scripture quotes verbatim via gospel_get; both have pre-publish carry-forward lists in their scratch files.

## Council Status

### Closed in this session (2026-05-29)

| Item | What it was | Where it landed |
|------|-------------|-----------------|
| RQ1.0b | Directional editing pass: eliminate AI→gospel validation sentences | Commit a46a77f (Ch 0/3/6) + embedded in all Ch 8-12 rebuilds |
| RQ1.0c | Hybrid directional flow ratified | Embodied in every rebuild this session |
| Tier 1.1 | Front-loading (28% → ~5%) | Commit 2b209c2 |
| Tier 1.3 | Ch 10 connection-pooling parallel | Replaced with gardening + AI-mirror |
| Tier 1.4 | Imago Dei boundary | Per-chapter EP close (Ch 8, 9, 10, 11, 12) |
| Tier 1.5 | Engineering parallel surgery for Ch 0/8/9/10/12 | All five rebuilt or arrow-flipped |
| Tier 2.5 | Two-audiences paragraph | Embedded in 1.1 (notes-to framing, not how-to-read) |
| Tier 3.1 | Moses 7:68 framing | Ch 12 line 19 |
| Tier 3.2 | Oaks + Bednar attributions | Ch 8 lines 17 + 21 |
| Tier 3.3 | D&C 131:7-8 capitalization | Ch 0 aligned to Ch 8 |
| Tier 3.4 | Bacteriopolis "10 hours" | Replaced with verified 230M tokens |
| Tier 3.5 | 11-step walk-through promise | New Sabbath chapter + reference page close updated |
| Tier 4.6 | Chapter-to-step annotations | 8 chapters tagged in italics |

### Still open (in rough priority order)

| Item | Effort | Impact | Notes |
|------|-------:|--------|-------|
| Tier 1.2 | small | medium | Ch 6 production-note **visual** prominence — preface forward-ref shipped 2026-05-29; boxed-callout / page-break elevation is now a **typography-pass** item, not a content one |
| Tier 1.6 | small | low-medium | Section II label mismatch ("Bilateral Stewardship" but Ch 5 opens with posture) |
| Tier 2.7 | medium | medium | Training-data ethics paragraph (not in the 2026-05-29 batch; theological weight — Michael's call on how to engage) |
| Provenance gaps | small-med | low-med | **Renumbering drift fixed 2026-05-29** (`provenance_chapter_11`→`_12` renamed; Sabbath Ch 11 + Afterword provenance written, all quotes verified via gospel_get). *Remaining:* glossary (15) + further-reading (16) never had a provenance file (glossary now cites scriptures after the 2026-05-29 additions); and the conclusion (12) + chapters 8/9/10 provenance predate their completion-pass rebuilds — re-verify against current text in a future pass. |
| Tier 2.10 | small | medium | Epilogue close with unresolved questions for both audiences |
| Tier 4.x | varies | sequel material | Foreword, audiobook front matter, Webster 1828 re-verify, URL archival, title reconsideration, etc. (dedication ✅ added 2026-05-29 — to Krista, the kids, and Jesus Christ; on the consecration page) |
| RQ1.0a | (skipped) | — | Confidence rating on 11-step reference — Michael decided the restructured chapters carry it |
| RQ1.0d | (closed) | — | Stewardship Boundary callout — done via the per-chapter EP close pattern |

**Closed in the 2026-05-29 chapters-2–7 pass:** Tier 2.1 (glossary + announcement), 2.2 (Ch 2 sidebar), 2.6 (AI-failures-as-types), 2.3 (bridges: Ch 2 via sidebar + Ch 7; Ch 3/4 already had them), 2.8 (light "willingness" form), 1.5 (Ch 5 reframe completes the engineer-voice surgery across Ch 0/5/8/9/10/12), Tier 4.5 (Ch 6→7 transition). **Plus (Ben Test sub-pass):** Tier 2.4 fully closed (Ch 4/5 + Ch 8–11).

## Compilation Artifacts

All outputs are generated in the `dist/` directory (ignored by git). **The artifacts are stale** — they reflect the pre-2026-05-29 state. Rebuild needed before any publication:

- [manuscript.html](../dist/manuscript.html) — Combined XHTML for PDF conversion
- [manuscript.pdf](../dist/manuscript.pdf) — Print-ready PDF (KDP specs, color interior)
- [beyond_the_prompt.epub](../dist/beyond_the_prompt.epub) — Standard valid EPUB

Carry-forward verifications during the rebuild:
- Reference page color rendering in print PDF
- New Sabbath chapter (Ch 11) layout
- New Afterword (Ch 14) layout
- EPUB validity with the new chapter structure
- Chapter tag italics rendering across formats

## Stewardship Grants (RATIFIED 2026-05-26, ACTIVE)

Michael granted commit + push stewardship over this repo to **Claude Opus 4.7** and **Gemini**. Recorded in `.github/copilot-instructions.md` § Stewardship Grants and `.mind/principles.md` § Stewardship Grants.

This session exercised the grant heavily: ten scripture-book commits without per-action approval. The bilateral covenant binding still held — Michael read every chapter draft before commit, surfaced corrections (week-not-quarter, "this book" not "the book", the cpuchip.net agent edits to studies during publish), and steered structural decisions (Option A+D combination, the dual-audience hospitality framing, dropping the BQ/anchor from the preface).

## Next Steps (in priority order)

1. **Rebuild `dist/` artifacts** to reflect the 2026-05-29 manuscript. Verify chapter-tag rendering, the Sabbath chapter, the Afterword, and the front-matter compression.
2. **Voice pass on the Ch 8/9/10/11/12 rebuilds.** Michael flagged Gemini might do this. The content is in place; voice sharpening is cheap iteration if wanted.
3. **Tier 1.2 — Ch 6 production-note prominence.** Smallest remaining Tier 1 item with real impact.
4. **Tier 2.x batch** — pick a couple of small surgical improvements (2.1 glossary expansion, 2.10 epilogue close, 2.6 AI-failures-as-doctrinal-types) for the next session.
5. **`.draft/00-COUNCIL.md` status update.** The council document tracked which items closed; should be marked up to reflect this session's work.
6. **cpuchip.net publish verifications** for both new studies (per their scratch files' pre-publish carry-forward lists).

## What changed in the audit narrative

Before this session, the book had two known structural problems (front-loading + Sabbath gap) and a long council of nine Tier 1 / Tier 1+ items plus five Tier 3 fact fixes. This session closed all five Tier 3 items, closed ten of twelve Tier 1 / Tier 1+ items (RQ1.0a Michael decided to skip; Tier 1.2 and 1.6 are the small remaining ones), added two complete new workspace studies with full provenance, added one new chapter, deleted one chapter that wasn't earning its pages, and renumbered the back matter twice (in two separate commits with git mv preserving history).

The book is now substantively closer to publish-ready than it was before. The structural moves landed. What's left is polish.
