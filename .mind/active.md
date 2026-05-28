# Active Context: Scripture Book Project

## Project Overview
This project compiles our gospel and AI studies into a published book format: *Beyond the Prompt: What AI Engineering Reveals About Eternal Patterns*.

## Current Status

> **2026-05-28 evening — FULL FIVE-PASS AUDIT COMPLETE (no manuscript changes; council-ready).**
> Five independent audit passes are landed in `.draft/`. The council document at [`.draft/00-COUNCIL.md`](../.draft/00-COUNCIL.md) is the entry point — read it first when you return. It synthesizes:
> - **`01-editor-pass.md`** — Claude Opus 4.7 in-house editor pass (structural, voice, content gaps)
> - **`02-frontmatter-weaving.md`** — Five options (A–E) for the "5 chapter-zeros" problem
> - **`03-gospel-reader-pass.md`** — Faithful Latter-day Saint reader perspective (independent subagent)
> - **`04-ai-reader-pass.md`** — Skeptical senior engineer reader (independent subagent)
> - **`05-editing-research.md`** — Web research on crossover non-fiction editing (Lewis, Lanier, Peterson, Newport, Capra critique, Tipler critique, Hodgson model, plus 4 currently-selling Christian-AI titles)
> - **`06-fact-check-results.md`** — Verified scripture facts (30+ verses against canon)
>
> **Convergences (multiple passes independently flagged):**
> - Front matter is 28% of book vs 3–8% in published comparables. **Demote the 3.5-year journey out of the preface.**
> - Ch 6 production-note sidebar is the most credible content in the book per both alt-readers. **Elevate it.**
> - Ch 10's heart-softening → connection pooling parallel is the most strained in the book per all three reader passes. **Replace with gardening (Mark 4 / Alma 32).**
> - "AI has no soul" boundary stated only once (Ch 4 line 46) — needs explicit type-and-shadow statement somewhere.
> - Chapters 0, 8, 9, 10 have engineering parallels in need of voice surgery. Ch 0's "topographies of higher-quality parameter weights" is technically wrong; Ch 8 has three specific ML vocabulary errors.
>
> **Verified factual fixes (`06-fact-check-results.md`):**
> - **Ch 11 Moses 7:68** — chapter says Enoch walked 365 years; canon says Zion lasted 365 years. Real factual error.
> - **Ch 8 Oaks + Bednar quotes** — verbatim verified but unattributed. Inline citations needed.
> - **Ch 0 vs Ch 8 D&C 131:7-8** — capitalization inconsistency ("we" vs "We").
> - **Ch 2 bacteriopolis "10 hours"** — unverified, likely fabricated; journal reports "230M wasted input tokens" with no hour count.
>
> **What the alt-readers said:**
> - Gospel reader: "read first" = **Ch 5**; "best original contribution" = **Ch 7's Authority → Scope → Capacity → Identity sequence**.
> - Engineer reader: "most credible" = **Ch 6**; "weakest" = **Ch 8**.
>
> **2026-05-29 early morning addition — Multi-model brainstorm passed** ([`.draft/07-multi-model-brainstorm.md`](../.draft/07-multi-model-brainstorm.md), $0.32, ~7 minutes). Four pg-ai-stewards brainstorm-lens pipelines fired in parallel: Six Hats (kimi-k2.6), Reverse (kimi-k2.6), SCAMPER (qwen3.6-plus), Crazy 8s (qwen3.6-plus). Surfaced **three new Tier 1+ items** added to the top of `00-COUNCIL.md`:
>   - **NEW-1 / RQ1.0a** — Add Strong/Medium/Speculative confidence column to 11-step reference page. Three lenses converge on the "retrospective numerology" risk.
>   - **NEW-2 / RQ1.0b** — Directional editing pass: eliminate every AI→gospel validation sentence (the single largest credibility killer per all three independent sources).
>   - **NEW-3 / RQ1.0c** — Big directional flow decision: open scripture-first (gospel as primary, AI converged on it) or observation-first (AI behavior as the question, scripture as the answer)?
>   - **RQ1.0d** — Upgrade Tier 1.4 to a recurring "Stewardship Boundary" callout per chapter, or keep as one paragraph?
> Plus three Tier 2 items (covenant.yaml ↔ D&C 82:10 side-by-side per SCAMPER 3.2; "watching" as dual-use scripture study method per SCAMPER 3.5; close Epilogue with unresolved-questions per Crazy 8s #8) and three Tier 4 carry-forwards (title reconsideration per Six Hats Red; predictive test chapter; guest engineer interviews).
>
> **No manuscript changes made.** All findings are documented in `.draft/` for council ratification.
> Next session: AskUserQuestion through the **ten** Tier 1 / Tier 1+ council questions (RQ1.0a through RQ1.0d + RQ1 through RQ6) in `00-COUNCIL.md`.

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
*   **Backmatter (Chapters 12–14):** DRAFTED, VERIFIED, COMPILED (2026-05-27).
    - **Chapter 12 (Epilogue):** [12_epilogue_silent_loop.md](../src/chapters/12_epilogue_silent_loop.md) — Concluding meta-reflection on the co-authoring relationship, the Gods watching in silence (Abraham 4:18), and the steward's charge.
    - **Chapter 13 (Glossary):** [13_glossary_of_fused_terms.md](../src/chapters/13_glossary_of_fused_terms.md) — Dictionary mapping Gospel vocabulary (Intelligence, Zion, Covenant) to Software Engineering parallels.
    - **Chapter 14 (Recommended Study):** [14_further_reading.md](../src/chapters/14_further_reading.md) — Suggestions for further reading, detailing scripture anchors, conference talks, and workspace study notes.

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
