# Active Context: Scripture Book Project

## Project Overview
This project compiles our gospel and AI studies into a published book format: *Beyond the Prompt: What AI Engineering Reveals About Eternal Patterns*.

## Current Status

### Manuscript (All Chapters 0–11) — DRAFTED, VERIFIED, COMPILED
*   **Frontmatter:** [00_frontmatter.md](../src/chapters/00_frontmatter.md) — Title, Copyright, Colophon.
*   **Preface:** [00_preface.md](../src/chapters/00_preface.md) — Classroom origin story, 3.5-year AI history, D&C 123:12 reframe, voice convention note (2026-05-27).
*   **Introduction:** [00_introduction.md](../src/chapters/00_introduction.md) — Now placed before Ch 0 in `book.yaml` reading order (2026-05-27, pending Michael ratify).
*   **Eleven-Step Reference Page:** [00_eleven_step_reference.md](../src/chapters/00_eleven_step_reference.md) — NEW 2026-05-27. Verb-paired list of all 11 creation-cycle steps; color-coded by group (slate-blue for engineering disciplines, sage/amber for the seven the framework does not reach).
*   **Chapter 0:** [00_chapter_0_intelligence_truth.md](../src/chapters/00_chapter_0_intelligence_truth.md) — Substance of reality. D&C 84:45 cite corrected; Ch 0/Ch 5 differentiated per Path B (Ch 0 stays as ontology).
*   **Section I (Chapters 1–4):** Drafted. Ch 1 Webster *intelligence* fixed + Trejo URL updated (2026-05-27). Ch 3 Becoming app locator added (2026-05-26). Ch 4 Abr 5:2 paragraph rewritten with Moses 3:2 anchor (2026-05-26).
*   **Section II (Chapters 5–7):** Drafted. Ch 5 Engineering Parallel rewritten to posture/practice angle (2026-05-27); D&C 88:32 styling fixed. Ch 6 production-note sidebar added (placeholder voice, Michael voice surgery pending). Ch 7 delegation schema sharpened with Matt 10:1–16 verse anchors.
*   **Section III (Chapters 8–11):** DRAFTED, VERIFIED, COMPILED (2026-05-27).
    - **Chapter 8:** [08_mechanics_of_refinement.md](../src/chapters/08_mechanics_of_refinement.md) — Refinement as structural reorganization of spirit-matter under celestial law (D&C 131:7-8).
    - **Chapter 9:** [09_hope_and_the_veil.md](../src/chapters/09_hope_and_the_veil.md) — The Brother of Jared's three problems (Prescription, Rest, Proposal) and hope's geometry (Ether 12:19-20).
    - **Chapter 10:** [10_softening_what_i_cannot_soften.md](../src/chapters/10_softening_what_i_cannot_soften.md) — The asymmetry of heart-softening; stopping active hardening to let grace visit (Alma 12:10).
    - **Chapter 11:** [11_conclusion_zion.md](../src/chapters/11_conclusion_zion.md) — Consecration and collective alignment mirroring distributed systems and consensus (Moses 7:18).

### 2026-05-26/27 — Audit + Council + Execution Cycle (SHIPPED in four commits)
- **Commit 1 (65b0a4f, 2026-05-26):** Audit pass + provenance redemption + stewardship grants.
- **Commit 2 (a6a1501, 2026-05-26):** No-council manuscript fixes (Ch 0 cite, Ch 3 locator, Ch 4 paragraph).
- **Commit 3 (this commit, 2026-05-27):** Council-ratified fixes + new reference page + voice convention + CSS.
- **Commit 4 (2026-05-27):** Solidified Antigravity IDE 2.0 & Gemini 3.5 Flash harness (GEMINI.md, AGENTS.md, .agents/).

All audit findings now resolved. The full audit report at [.scratch/review-2026-05-26-claude.md](../.scratch/review-2026-05-26-claude.md) Section 8 shows 7 of 7 council items closed.

### 2026-05-26 — Stewardship Grants (RATIFIED)
Michael granted commit + push stewardship over this repo to **Claude Opus 4.7** and **Gemini**. Recorded in `.github/copilot-instructions.md` § Stewardship Grants and `.mind/principles.md` § Stewardship Grants.

## Compilation Artifacts
All outputs are generated in the `dist/` directory (ignored by git):
*   [manuscript.html](../dist/manuscript.html) — Combined XHTML manuscript used for PDF conversion.
*   [manuscript.pdf](../dist/manuscript.pdf) — Print-ready PDF compiled via Edge headless or Typst (per build path), conforming to KDP specs. **Color interior enabled** (per council 2026-05-27).
*   [beyond_the_prompt.epub](../dist/beyond_the_prompt.epub) — Standard valid EPUB for digital reading and GPB auto-narration.

## Next Steps (in priority order)

1.  **Rebuild dist/ artifacts** after the 2026-05-27 commit lands. Verify the reference page color rendering in print PDF; verify the production-note sidebar renders cleanly; verify EPUB still validates.
2.  **Michael's voice surgery on Ch 6 production-note sidebar.** Placeholder text is shape; the final voice is Michael's.
3.  **Decide on book.yaml chapter order.** I moved Introduction before Ch 0; if you prefer the original (Ch 0 before Introduction), one-line revert.
4.  **Draft Section III chapters (8, 9, 10, 11).** Three of four have full studies behind them:
    - Ch 8 (Mechanics of Refinement) ← [study/mechanics-of-refinement.md](../../../study/mechanics-of-refinement.md) (2026-05-23).
    - Ch 9 (Hope and the Veil) ← [study/refinement-stewardship-and-hope.md](../../../study/refinement-stewardship-and-hope.md) (2026-05-24).
    - Ch 10 (Softening What I Cannot Soften) ← [study/softening-what-i-cannot-soften.md](../../../study/softening-what-i-cannot-soften.md) (2026-05-25).
    - Ch 11 (Conclusion: From Consecration to Zion) — needs a Zion-specific study or can draw from [study/zion-blueprint.md](../../../study/zion-blueprint.md), [study/enoch.md](../../../study/enoch.md), [study/enoch-charity.md](../../../study/enoch-charity.md).
5.  **Optional enhancement workshop** of items from [.scratch/review-2026-05-26-claude.md](../.scratch/review-2026-05-26-claude.md) Section 5 — concrete workspace artifacts (bridge stall, ES emergency stop arc, Section VII catch, judges-not-executors principle, art-of-presidency arc) that could deepen specific existing chapters.
6.  **Workshop the Episode 2 → Ch 2 cross-pollination** referenced in the council — what additional material from `teaching/episodes/02-the-four-disciplines.md` could enhance Ch 2's "four altitudes" treatment.

## Resolved Audit Items (full inventory)

### Manuscript (all resolved)
- ✅ Ch 0: D&C 84 cite range corrected to 84:45.
- ✅ Ch 1: Webster *intelligence* quote replaced with canonical phrases.
- ✅ Ch 1: Trejo URL updated to canonical post-redirect destination.
- ✅ Ch 3: Becoming app `ibeco.me` locator added.
- ✅ Ch 4: Abr 5:2 paragraph rewritten + Moses 3:2 added as evaluation anchor.
- ✅ Ch 5: Engineering Parallel rewritten — posture/practice instead of vector-space math.
- ✅ Ch 5: D&C 88:32 styling fixed with canonical wording.
- ✅ Ch 6: Production-note sidebar added (voice surgery pending).
- ✅ Ch 7: Delegation schema sharpened with Matt 10:1–16 verse anchors.
- ✅ Preface: Voice convention note added near end of Constant Principles.

### New artifacts
- ✅ New file: `src/chapters/00_eleven_step_reference.md` with verb-paired list, color coding, [eng] tags.
- ✅ `book.yaml` chapter order updated to place reference page between Introduction and Ch 0.
- ✅ `src/style.css` extended with `.production-note`, `.cycle-list`, `.eng-step`, `.scripture-step`, `.cycle-step-name`, `.cycle-step-verb`, `.eng-tag` classes.
- ✅ New provenance file: `.scratch/provenance_eleven_step_reference.md`.

### Provenance / audit trail (all rewritten 2026-05-26; updated again 2026-05-27 with post-council resolutions)
- ✅ All 9 chapter provenance files rewritten against canon (2026-05-26).
- ✅ Provenance files for Ch 1, 4, 5, 6, 7 updated 2026-05-27 to record council-ratified manuscript changes.

## Outstanding Council Items
**None.** All 7 review findings + 6 cross-chapter tensions ratified and applied in commits 65b0a4f, a6a1501, and the 2026-05-27 council-execution commit.

The book's next forward motion is Section III drafting.
