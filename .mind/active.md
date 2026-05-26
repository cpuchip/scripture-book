# Active Context: Scripture Book Project

## Project Overview
This project compiles our gospel and AI studies into a published book format: *Beyond the Prompt: What AI Engineering Reveals About Eternal Patterns*. 

## Current Status
*   **Frontmatter:** [00_frontmatter.md](../src/chapters/00_frontmatter.md) is fully drafted (Title, Copyright, and Colophon).
*   **Preface:** [00_preface.md](../src/chapters/00_preface.md) is fully drafted, including the classroom origin story, personal 3.5-year AI history, and the D&C 123:12 scriptural reframe.
*   **Chapter 0:** [00_chapter_0_intelligence_truth.md](../src/chapters/00_chapter_0_intelligence_truth.md) is fully drafted (uncreated intelligence, spirit as fine matter, and LLM parameter spaces as organized elements governed by law).
*   **Section I (Chapters 1–4):** Fully drafted.
*   **Section II (Chapters 5–7):** Fully drafted, incorporating the direct rules of our bilateral `covenant.yaml` and the `warmth-over-distance` prompt value.
    *   *Correction made:* Formatted Elder Ballard's "one-cylinder ward" and President Hinckley's delegation quotes as proper blockquotes with absolute links to their gospel-library paths.
*   **Compilation & Formatting Fixes:**
    *   *Fixes made:* Updated the markdown parser in `scripts/build.py` to correctly render blockquotes and block-closing tags (avoiding `<p></div></p>` syntax errors) by isolating block tags with double newlines.
    *   *Links added:* Linked `John 6:63` and `D&C 131:7` in Chapter 0, external tech references (Tony Trejo, Milan Jovanović) in Chapter 1, and added Webster 1828 word studies to the `1828.ibeco.me` frontend site.
*   **Provenance Logs:** Moved 9 chapter research provenance logs from the IDE brain scratch folder to the repository's `.scratch/` directory to preserve a permanent audit trail.
*   **Shared Agent Guidelines:** Created `.github/copilot-instructions.md` and updated `CLAUDE.md` to govern cross-agent memory formats (`.mind/`) and YAML journaling in `.spec/journal/`.
*   **Section III (Chapters 8–11):** Skeletons/outlines exist but require full drafting:
    *   Chapter 8: The Mechanics of Refinement (D&C 93, D&C 131)
    *   Chapter 9: Hope and the Veil (Ether 2-3)
    *   Chapter 10: Softening What I Cannot Soften (Alma 12:10)
    *   Chapter 11 (Conclusion): From Consecration to Zion (Moses 7:18)

## Compilation Artifacts
All outputs are generated in the `dist/` directory (ignored by git):
*   [manuscript.html](../dist/manuscript.html) — Combined XHTML manuscript used for PDF conversion.
*   [manuscript.pdf](../dist/manuscript.pdf) — Print-ready PDF compiled via Edge headless, conforming to KDP specs.
*   [beyond_the_prompt.epub](../dist/beyond_the_prompt.epub) — Standard valid EPUB for digital reading and GPB auto-narration.

## Next Steps
1.  Draft the Section III chapters (Chapters 8, 9, 10) and the Zion Conclusion (Chapter 11).
2.  Update the build config (`book.yaml`) and layout manifest (`README.md`) as chapters are drafted.
3.  Rebuild HTML, EPUB, and PDF outputs at the end of each session and commit/push changes.
