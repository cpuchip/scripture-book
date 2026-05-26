# Scripture Book — Beyond the Prompt

The canonical project instructions are documented in:
@.github/copilot-instructions.md

---

## Directory Structure

*   `src/chapters/` — Markdown files for individual chapters.
*   `src/style.css` — Custom print-styling CSS used for PDF rendering.
*   `scripts/` — Build and formatting tools.
*   `dist/` — Compiled artifacts (PDF/EPUB output).

## Build Commands

Compile book artifacts:
```bash
python scripts/build.py
```

## Writing Principles
1.  **Modular Study Format:** Each chapter must open with a *Binding Question* and *Anchor Passage*, proceed through *The Core Reframe* and *The Engineering Parallel*, and conclude with a *Becoming Commitment*.
2.  **Voice & Tone:** Deep, direct, unadorned, personal. Avoid generic AI summaries, presenter tics, or meta-narration of the document's structure.
3.  **Transitions:** Chapters are structured chronologically, and paragraphs/sections connect by causation (*therefore* or *but*) rather than sequence (*and then*).
