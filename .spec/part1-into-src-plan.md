# Part 1 → `src/` Integration Plan (the `into-src` ratification gate)

**Status:** AWAITING MICHAEL'S RATIFICATION. Drafts are done, voiced, verify-gated, and committed in `.draft/`. This is the structural step that wires them into the live manuscript + build — and it forks on decisions that are yours, not mine. I stopped here on purpose (Mosiah 4:27 — wisdom and order; and the yes-agent correction — surface the fork, don't guess it).

**Date:** 2026-05-31
**Author:** Claude Opus 4.8 (Claude Code), under the scripture-book stewardship grant.

---

## What's already done (committed + pushed)

- All 10 Part 1 pieces drafted: P1–P9 + coda (`.draft/20260530-p1-draft.md`, `.draft/20260531-{p2..p9,coda}-draft.md`).
- Voiced via `agy -p` (Gemini 3.5 Flash) — report at `.draft/20260531-agy-voicing-part1.md`.
- 60 voicing edits integrated **verify-gated**: git-diff confirms no blockquote, scripture quote, scripture link, or provenance comment changed; all 9 Remember blocks intact. 3 unsafe Gemini suggestions correctly refused.

So the **content** is ready. What remains is purely structural wiring — and that's where the decisions live.

---

## Why this isn't a safe file-add (the measured risk)

I read `book.yaml` + `build_typst.py` before writing this. Three hard facts:

1. **Chapter order lives in `book.yaml`'s explicit `chapters:` list.** The build iterates it. Wiring Part 1 in = editing that list (reversible) — but *where* Part 1 sits, and whether the doctrine chapters renumber, is a structural choice.
2. **No Part-divider exists in the build.** `build_typst.py` supports `#`/`##`/`###`, binding-question, anchor-passage, blockquote, production-note, cycle-step, hr. There is **no half-title "Part One / Part Two" page**. Front-porch needs a new `#part-divider[]` in `template.typ` + a build branch. The *design* of that page (half-title, epigraph, vertical rhythm) is a book-design call.
3. **The build would mangle the drafts as-is.** `preprocess_html_blocks` strips only `production-note` and `cycle-list`. The `<!-- DRAFT -->` / `<!-- PROVENANCE -->` comments would leak into the rendered PDF. Conversion to clean src files (provenance → `.scratch/provenance_part1.md`, the gate) is required.

---

## The 6 decisions (with my recommendation for each)

### D1 — Where does Part 1 sit? **(RECOMMEND: front porch)**
```
00_frontmatter            (title / dedication / consecration / colophon)
00_preface                (REWORKED — see D5)
  ── PART ONE: HOW ──     [new divider, D3]
p1_01 .. p1_09 + p1_coda  (the practices)
  ── PART TWO: WHY ──     [new divider, D3]
00_eleven_step_reference  (the framework — opens Part 2; see D4)
00_chapter_0 .. 16        (existing doctrine, unchanged internally)
```
This *is* the front-porch architecture you ratified: practice-forward door first, opening into doctrine. The coda already hinges into Part 2 on Mosiah 4:27.

### D2 — Numbering of the existing doctrine chapters? **(RECOMMEND: leave as-is)**
Keep the doctrine chapters numbered exactly as they are (Chapter 0–16). Part 1 pieces are **"Practice 1–9 + Coda,"** not "Chapter N" — which naturally distinguishes the two doors and reinforces "two doors, one house."
- **Why not renumber 1–26:** it ripples through every internal cross-reference *and* all 17 `provenance_*.md` files, for zero reader benefit. The Ben-Test read: renumbering is work that looks like progress and isn't.

### D3 — Part-divider design? **(RECOMMEND: minimal half-title, but it's your eye)**
Add a `#part-divider(title, subtitle)` to `template.typ`: page-break, vertical centering, large title ("Part One"), italic subtitle ("How — the practices"). One template function + one build branch. **The look is yours** — half-title pages are a real design decision (do you want an epigraph on each? a rule? just the words?).

### D4 — Where does the eleven-step reference go? **(RECOMMEND: opens Part 2)**
You called the 11-step cycle "aspirational." Part 1 is workflow-first and doesn't need the framework to start; Part 2 is the framework + doctrine. So the reference opening Part 2 fits. (Alternative: keep it in front-matter as a shared reference. Your call.)

### D5 — Preface rework? **(RECOMMEND: I draft a proposal, you own the voice)**
The current preface frames a single book, the "Becoming Commitment is aspirational" note, and (per the front-porch plan) two-audience statements to drop. "Two doors, one house" belongs here. This is **authorial voice** — I'll draft a reworked preface to `.draft/` for your edit; I won't write it into `src/` directly.

### D6 — Spec-gap: the Modular Study Format constraint **(RECOMMEND: carve-out, mine to apply on ratification)**
`copilot-instructions.md` #1 + `CLAUDE.md` mandate *every* chapter carry Binding Question / Anchor Passage / Core Reframe / Engineering Parallel / Becoming Commitment. Part 1 deliberately uses the practice format. Without an explicit carve-out, a future agent will "fix" Part 1 by jamming the doctrine format in. Fix: amend both instruction files to "Part 2 chapters use the Modular Study Format; Part 1 practices use the practice format (story → principle → today's implementation → Try This → Remember)." I'll apply this *with* the into-src execution, not before (the structure isn't live yet).

---

## What I execute the moment you ratify (the mechanical part — mine)

1. Convert the 10 voiced drafts → clean `src/chapters/p1_*.md` (strip HTML comments; titles per D-decisions).
2. Move all provenance + verify-flags → `.scratch/provenance_part1.md` (the gate), with a verification-log footer.
3. Add `#part-divider` to `template.typ` + the build branch in `build_typst.py` (per D3).
4. Insert Part 1 + the two dividers into `book.yaml` (per D1/D4).
5. Apply the D6 carve-out to `copilot-instructions.md` + `CLAUDE.md`.
6. Run the build (Docker → Typst) and confirm a clean PDF — inverse-hypothesis the divider (it renders) and a Part 1 chapter (no leaked comments).
7. Commit + push per logical unit.

## Still open (carry-forward, not blocking)
- 5 authorial judgment calls from the voicing pass (see `.mind/active.md`): council/counsel title-vs-text, Ch3-P4 em-dashes (kept to protect a link), coda title "Go Touch Some Grass" vs report's "Step Outside" (recommend keep yours).
- Scar-detail verifications flagged in each draft's provenance comments.
- Consent flags: naming Ben, naming Leah (age 14), the storygames "nine-year-old."
