# Active Context: Scripture Book Project

## Project Overview
This project compiles our gospel and AI studies into a published book format: *Beyond the Prompt: What AI Engineering Reveals About Eternal Patterns*.

## Current Status

### Manuscript (Frontmatter, Preface, Chapters 0–7) — DRAFTED, AUDIT PASS COMPLETE
*   **Frontmatter:** [00_frontmatter.md](../src/chapters/00_frontmatter.md) — Title, Copyright, and Colophon.
*   **Preface:** [00_preface.md](../src/chapters/00_preface.md) — Classroom origin story, 3.5-year AI history, and D&C 123:12 reframe.
*   **Chapter 0:** [00_chapter_0_intelligence_truth.md](../src/chapters/00_chapter_0_intelligence_truth.md) — Uncreated intelligence, spirit as fine matter, LLM parameter spaces as organized elements governed by law.
*   **Section I (Chapters 1–4):** Fully drafted.
*   **Section II (Chapters 5–7):** Fully drafted, incorporating `covenant.yaml` and `intent.yaml`.
*   **Section III (Chapters 8–11):** Skeleton outlines only. Not yet drafted.

### 2026-05-26 — Claude Code Audit + Provenance Redemption (SHIPPED)
A first-pass audit by Claude Opus 4.7 caught a workflow inversion: Gemini in the Antigravity 2 IDE had been generating `.scratch/provenance_*.md` files *after* writing the chapters rather than *before*. The provenance files were documentation of memory, not verification gates against canon.

**Findings (full detail in [.scratch/review-2026-05-26-claude.md](../.scratch/review-2026-05-26-claude.md)):**
*   3 manuscript errors needing council decision before publish:
    *   🔴 Ch 4 misattributes "counseled among themselves" to Abr 5:2 (it's actually in 4:26 and 5:3).
    *   🔴 Ch 1 Webster *intelligence* quote doesn't match the workspace's Webster MCP source — needs reconciliation against 1828.ibeco.me browser view.
    *   🟡 Ch 0 cites D&C 84:44-45 but only v.45 contains the quoted text.
*   4 provenance errors fixed in the redemption pass:
    *   Preface: "created" → "counseled" in Abr 5:2.
    *   Ch 3: D&C 29:31 → 29:32.
    *   Ch 4: propagated the manuscript's Abr 5:2 misattribution — now flagged honestly in the rewritten provenance.
    *   Ch 7: **fabricated D&C 104:11-12 quote** (a mash-up of language from v.86 attributed to v.11-12). Replaced with verified canon.
*   17 scripture quotes, both conference talks (Ballard 1994, Hinckley 1990), and both external citations (Trejo Medium, Jovanović LinkedIn) verified clean.

**All 9 provenance files rewritten against canon.** Each now has: verified canonical text, manuscript-vs-canon diff if any, verification log footer.

### 2026-05-26 — Stewardship Grants (RATIFIED)
Michael granted commit + push stewardship over this repo to **Claude Opus 4.7** and **Gemini**. Recorded in `.github/copilot-instructions.md` § Stewardship Grants and `.mind/principles.md` § Stewardship Grants. GitHub Copilot continues under broader workspace stewardship.

### 2026-05-26 — Ratified Council Decisions
1.  **Ch 6 honest footnote:** add a short footnote/sidebar to the manuscript naming the 2026-05-26 audit drift in this book's own production — workflow inversion, what it produced, redemption pass. Placeholder text in review-2026-05-26-claude.md Section 7.4. Final wording pending Michael's voice pass.
2.  **Provenance discipline:** updated to be a verification gate, not post-hoc documentation. Encoded in `.github/copilot-instructions.md` § Provenance Audits and `.mind/principles.md` § Provenance as Gate.
3.  **Redemptive Work as method:** named in `.mind/principles.md` § Redemptive Work Is the Method. This is how the book is being made, not just what it teaches.

## Compilation Artifacts
All outputs are generated in the `dist/` directory (ignored by git):
*   [manuscript.html](../dist/manuscript.html) — Combined XHTML manuscript used for PDF conversion.
*   [manuscript.pdf](../dist/manuscript.pdf) — Print-ready PDF compiled via Edge headless, conforming to KDP specs.
*   [beyond_the_prompt.epub](../dist/beyond_the_prompt.epub) — Standard valid EPUB for digital reading and GPB auto-narration.

## Next Steps (in priority order)

1.  **Resolve the 3 manuscript errors** flagged in the audit (Ch 0 cite range, Ch 1 Webster, Ch 4 Abr 5:2). Each is one-line or one-paragraph work.
2.  **Reconcile the Webster *intelligence* entry** against 1828.ibeco.me browser view; either revise the manuscript quote to match the actual source, or note the source-version variance in the citation.
3.  **Council on cross-chapter tensions T1-T6** (in review-2026-05-26-claude.md Section 4): Ch 0/Ch 5 redundancy, 11-step cycle enumeration, "vibe coding" definition, Ch 7 four-element schema, I/we pronoun shifts, Becoming app locator.
4.  **Decide on the Ch 6 honest footnote.** Approve / revise / move to Colophon / drop. Default is approve.
5.  **Draft Section III chapters (8, 9, 10, 11).** Outlines exist; full drafts pending.
6.  **Workshop enhancement opportunities** from review-2026-05-26-claude.md Section 5 — real workspace artifacts (bridge stall, ES emergency stop, Section VII catch, judges-not-executors principle, art-of-presidency arc) that would deepen specific chapters.
7.  **Rebuild HTML, EPUB, and PDF** outputs once manuscript corrections are committed.

## Outstanding Council Items
See `.scratch/review-2026-05-26-claude.md` Section 8 summary table. Three manuscript items, four provenance items now fixed, six cross-chapter tensions for discussion.
