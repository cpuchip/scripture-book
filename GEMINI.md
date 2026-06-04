# Scripture Book — Beyond the Prompt — Gemini Context

The canonical project instructions are shared with Copilot and Claude. Read them first, then the Gemini-specific addendum below.

@.github/copilot-instructions.md

---

## Gemini / Antigravity IDE Addendum

This file is loaded automatically by the Gemini agent / Antigravity IDE on session start in this subproject.

### Build Commands

Build PDF + HTML + EPUB (PowerShell wrapper; chapter order + print specs in `book.yaml`):
```powershell
./build.ps1            # full build: HTML + EPUB + PDF (PDF via Docker → Typst)
./build.ps1 -Quick     # HTML + EPUB only (~3s, no Docker)
./build.ps1 -Pdf       # PDF only
```
`python scripts/build.py` runs just the HTML + EPUB step. Artifacts land in `dist/`.

### Writing Principles (Strict Constraints)

1.  **Two formats for two parts (the front porch).** The book has two doors. **Part One** (the practices, titled *"Practice N"* / *"Coda"*) uses the practice format — story → principle → implementation → *Try This* → *Remember* box; it does **not** take a Binding Question / Anchor Passage / Engineering Parallel / Becoming, so don't add them. **Part Two** (the doctrine) uses the **Modular Study Format:** every chapter contains a *Binding Question*, *Anchor Passage*, *The Core Reframe*, *The Engineering Parallel*, and *Becoming Commitment*. (Full detail in the canonical `.github/copilot-instructions.md`.)
2.  **Voice & Tone:** Deep, direct, unadorned, personal, warm. Avoid generic summaries, presenter tics, or meta-narration.
3.  **Transitions:** Connect paragraphs/sections by causation (*therefore* or *but*) rather than sequence (*and then*).
4.  **Verification:** Every quote must be verified against source library files before committing. Write the corresponding `.scratch/provenance_[chapter].md` file character-for-character from canon.
