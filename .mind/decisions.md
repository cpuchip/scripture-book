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
