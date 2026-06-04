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

Build PDF + HTML + EPUB (PowerShell wrapper; chapter order + print specs in `book.yaml`):
```powershell
./build.ps1            # full build: HTML + EPUB + PDF (PDF via Docker → Typst)
./build.ps1 -Quick     # HTML + EPUB only (~3s, no Docker) — fast iteration
./build.ps1 -Pdf       # PDF only
```
`python scripts/build.py` runs just the HTML + EPUB step. Artifacts land in `dist/`
(`manuscript.pdf`, `manuscript.html`, `beyond_the_prompt.epub`).

## Writing Principles
1.  **Two formats for two parts (the front porch).** The book is one volume with two doors — keep their formats distinct.
    *   **Part One (the practices)** — titled *"Practice N"* / *"Coda,"* not chapters — uses the **practice format**: story (real scar or success) → the eternal principle (separated from the perishable 2026 mechanics) → today's implementation → a *Try This* → a *Remember* box, with a parenthetical *(Part Two: …)* cross-reference. It deliberately does **not** use the Modular Study Format; do not add Binding Question / Anchor Passage / Engineering Parallel / Becoming to a Part One piece.
    *   **Part Two (the doctrine)** uses the **Modular Study Format:** each chapter opens with a *Binding Question* and *Anchor Passage*, proceeds through *The Core Reframe* and *The Engineering Parallel*, and concludes with a *Becoming Commitment*. The *Becoming Commitment* is the author's first-person voice — an honest worked example (including where the practice is still aspirational), offered for the reader to adapt rather than prescribed to them. The preface frames it this way for the reader. Calibrate against the Ben Test: do not let an "I will" outrun real practice; mark aims as aims.
2.  **Voice & Tone:** Deep, direct, unadorned, personal. Avoid generic AI summaries, presenter tics, or meta-narration of the document's structure.
3.  **Transitions:** Chapters are structured chronologically, and paragraphs/sections connect by causation (*therefore* or *but*) rather than sequence (*and then*).
