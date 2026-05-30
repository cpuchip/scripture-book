# Architectural & Compilation Decisions

This file tracks the key decisions made regarding the book's design, layout, compilation script, and target formats.

## 1. Trim Size and Margins (Paperback Print Specs)
*   **Decision:** We adopted a 6" x 9" trim size.
*   **Marginal Layout:** Inside gutter set to 0.8" and outside to 0.5" using CSS Paged Media `@page :left` and `@page :right` rules, ensuring correct margins when printed and bound.
*   **Rationale:** Standard KDP paperback margins require a minimum of 0.75" inside for a 100-page book to avoid text getting swallowed by the binding. Suppressing headers on first pages of chapters matches standard trade paperback typography.

## 2. Compilation and Link Resolution (build.py)
*   **Decision:** The build script (`scripts/build.py`) is self-contained with zero external dependencies.
*   **Link Resolution:** Script converts local `gospel-library/` links to absolute `churchofjesuschrist.org/study/...` URLs, parsing chapter and verse ranges (handling en-dashes `–` and standard hyphens `-`).
*   **Rationale:** Keeps the build environment fast, lightweight, and executable on any machine with python3 installed, while ensuring EPUB and manuscript links work on standard devices.

## 3. EPUB Validation Rules
*   **Decision:** Built a custom EPUB packer in python's `zipfile` library.
*   **Mimetype Rule:** The `mimetype` file must be written as the first entry in the ZIP archive, stored uncompressed (`ZIP_STORED`). All other assets are compressed (`ZIP_DEFLATED`).
*   **Rationale:** This is a strict requirement of the EPUB specification; without it, standard ebook readers (including Google Play Books) will reject the archive as corrupted.

## 4. Headless PDF Compilation via Edge
*   **Decision:** We use Microsoft Edge (available on Windows) in headless print-to-pdf mode to compile the final PDF document:
    `msedge --headless --disable-gpu --no-sandbox --print-to-pdf="dist/manuscript.pdf" "file:///path/to/manuscript.html"`
*   **Rationale:** Edge headless supports CSS Paged Media `@page` margin rules and running headers correctly, producing a print-ready manuscript matching KDP specifications without requiring heavy third-party layout engines like PrinceXML or Weasyprint.
*   **⚠️ Superseded (see §6):** The build no longer uses Edge headless; the PDF is now compiled via a multi-stage Docker + Typst pipeline, documented in §6 below. This entry is kept for history.

## 5. Becoming Commitments — First-Person Witness, Framed (Editorial)
*   **Decision (2026-05-29 council):** The Becoming Commitments stay in the author's **first-person voice** — honest worked examples (including where the practice is still aspirational), offered for the reader to adapt. They are **not** reader-directed prompts and **not** prescriptions.
*   **Frame:** A short reader-facing note in the preface ("A note on the chapter endings") names them as such and invites the reader to write their own. This restores the framing lost when the front-loading fix (`2b209c2`) deleted the introduction's "How to Read This Book."
*   **Rationale:** All three audit reader-passes named the vulnerable first-person witness as the book's credibility engine (the production notes, the 3.5-year journey, the Sabbath dogfooding note). Converting to reader-directed prompts would trade that engine for a safer-but-flatter register and risk the preachy/prescriptive voice the audit flagged. Keeping the witness *and framing it* resolves the original ambiguity — the deleted frame said "you study this" while the commitments say "I commit" — and keeps the Ben-Test calibration meaningful. The format spec (`CLAUDE.md`, `.github/copilot-instructions.md`, `template.md`) was updated so future drafting holds this register rather than re-drifting.
*   **Authorship note:** the book is authored by Michael but drafted by Claude + Gemini and shaped by other models through brainstorm passes. The first-person "I" is where the reader touches the author directly — itself part of the credibility engineering.

## 6. PDF Compilation via Docker + Typst (supersedes §4)
*   **Decision (active as of 2026-05):** The print-ready PDF is compiled by a multi-stage Docker build. Stage 1 (`python:3.11-slim`) runs `scripts/build_typst.py`, converting the Markdown chapters into a single Typst source (`dist/book.typ`) against the custom template `src/template.typ`. Stage 2 (`ghcr.io/typst/typst`) runs `typst compile dist/book.typ dist/manuscript.pdf`. Stage 3 (`alpine`) copies `dist/` back to the mounted host volume. The pipeline is driven by `build.ps1` (PowerShell) or `build.sh` (bash); `python scripts/build.py` still produces the HTML + EPUB.
*   **Rationale:** Containerized Typst gives a reproducible build with no dependency on a locally-installed browser, and `template.typ` provides typographic control the Edge / CSS-Paged-Media path could not — custom functions for the binding-question, anchor-passage, blockquote, production-note, cycle-step, and margin-QR elements, plus precise KDP trim/margin handling.
*   **Gotcha:** `build_typst.py` recognizes specific frontmatter `<div>` *signatures* (e.g. `page-break-before: always; margin-top: 1in`) and maps each to Typst. Adding a new styled front-matter block requires teaching the converter the new signature — see the 2026-05-29 dedication fix (commit `e2509a7`), where a centered-italic dedication div and a page-break-less consecration div both leaked raw `<div>` into `book.typ` until handlers were added.
