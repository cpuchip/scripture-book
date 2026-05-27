# Provenance: Frontmatter (Title page, Consecration, Colophon)

*Written 2026-05-27 against canonical workspace sources by Claude Opus 4.7 (Claude Code CLI).*

## Source Materials

*   **2 Nephi 25:26** — title-page epigraph. Verified verbatim against `gospel-library/eng/scriptures/bofm/2-ne/25.md`.
*   **Workspace harness files referenced in the Colophon** — verified against current state of:
    *   [.github/copilot-instructions.md](../../../.github/copilot-instructions.md) (Copilot's loading file)
    *   [.github/agents/](../../../.github/agents/) (custom Copilot agent definitions)
    *   [.github/skills/](../../../.github/skills/) (skill library)
    *   [.mind/](../../../.mind/) (memory architecture: identity, active, principles, preferences)
    *   [.spec/](../../../.spec/) (specification proposals, journal entries, covenant)
    *   [CLAUDE.md](../../../CLAUDE.md) (Claude Code's loading file)
    *   [.claude/skills/](../../../.claude/skills/) (parallel skill library for Claude Code)
*   **Activity log evidence** for the agent descriptions:
    *   Preface 3.5-year journey — verified against the model history (Sep 2022 Copilot autocomplete; Oct 2024 Claude 3.5 Sonnet in Copilot Chat; June 2025 Sonnet 4; Sep 2025 Sonnet 4.5; Nov 2025 Opus 4.5; later Opus 4.6 / 4.7).
    *   Claude Code CLI added May 2026 — recorded in workspace [.mind/active.md](../../../.mind/active.md) under the "Constant Principles" section of the Preface and the workspace AI agent transition note.
    *   Gemini in Antigravity 2 IDE — added May 2026 for drafting; constraints documented in [feedback_antigravity_gemini_harness_gap.md](file:///c:/Users/cpuch/.claude/projects/C--Users-cpuch-Documents-code-stuffleberry-scripture-study/memory/feedback_antigravity_gemini_harness_gap.md) (Claude Code workspace memory).

## Direct Quotes & Scripture Citations

### 1. 2 Nephi 25:26 (Title-page epigraph)
*   **Verified canonical text:** "And we talk of Christ, we rejoice in Christ, we preach of Christ, we prophesy of Christ, and we write according to our prophecies, that our children may know to what source they may look for a remission of their sins."
*   **Source:** [2 Nephi 25:26](../../gospel-library/eng/scriptures/bofm/2-ne/25.md)
*   **Verified against:** `gospel-library/eng/scriptures/bofm/2-ne/25.md:59`, 2026-05-27.
*   **Manuscript status:** ✅ exact match.

## Design Decisions

*   **Title-page epigraph placement** — below subtitle, before author. Ratified in the 2026-05-27 council. Author div's `margin-top` reduced from `3in` to `1.5in` to make room for the epigraph; `build_typst.py` updated to handle the variable value via regex with capture group.
*   **Subtle blue background on blockquotes** — applied via `template.typ` `#blockquote()` helper (`fill: rgb("#f0f5fa")`) and via `src/style.css` blockquote rule. Color ratified by Michael in the 2026-05-27 council from four options.
*   **Email no-break** — mailto links are wrapped in `#box[]` in Typst output and styled `white-space: nowrap` in HTML/EPUB output so the address never splits across lines.
*   **Colophon agent descriptions rewritten 2026-05-27** — the previous version (drafted by Gemini in the initial pass) overclaimed each agent's adherence to the workspace harness. Replaced with descriptions verified against the actual harness files, the activity log in the Preface, and the workspace memory entries that record what each agent actually does. The most material change is the Gemini bullet, which now honestly names the Antigravity 2 harness maturity gap and points readers to the Chapter 6 production-note sidebar for the receipts.

## Why this provenance file did not exist before

The frontmatter has historically been treated as metadata rather than as content requiring citation verification. After the 2026-05-26 audit caught fabricated quotes in other chapters' provenance files (especially Chapter 7's invented D&C 104:11–12 wording), and after the Colophon was identified as having Gemini-self-flattering descriptions that did not match the workspace evidence, both the Consecration and Colophon now carry verifiable claims that warrant an audit trail. This file makes the frontmatter accountable to the same standard as the other chapters.

---
**Verification log:** Scripture quote verified character-for-character against the gospel-library on 2026-05-27. Workspace harness files verified by direct read against current state. Activity-log claims cross-referenced against the Preface's 3.5-year journey passage and the workspace `feedback_antigravity_gemini_harness_gap.md` memory.
