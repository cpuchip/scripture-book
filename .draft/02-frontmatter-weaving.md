# Frontmatter Weaving Council — The Five-Chapter-Zero Problem

**Date:** 2026-05-28
**Question:** Five files before Chapter 1 makes the book front-heavy. How do we get the reader to the hook faster without losing what's valuable in the frontmatter?

---

## Current State

The book's reading order before Ch 1:

```
1. 00_frontmatter.md       42 lines   Title + Consecration + Colophon
2. 00_preface.md           70 lines   Classroom + 3.5-year journey + Constant Principles + Voice note
3. 00_introduction.md      31 lines   Confluence + How to Read This Book
4. 00_eleven_step_reference.md  19 lines   11-step card
5. 00_chapter_0_intelligence_truth.md  80 lines   Substance of Reality (Ch 0)
                          ────────
                          242 lines before Ch 1 line 1
```

For a ~870-line manuscript, that's 28% of the book before the engineer's hook ("I have been a software engineer for eighteen years"). For a print book at roughly 8 lines per page, that's pages 1-30 before Ch 1.

## What each piece is actually carrying

| File | Purpose | Strongest element | Weakest element |
|------|---------|-------------------|-----------------|
| **frontmatter** | Title, copyright, attribution | Consecration's "freely shared" stance | Colophon is on the long side |
| **preface** | Origin story | The January 2026 classroom moment ("AI" in the margin) | "Constant Principles" — repeats Ch 1 material |
| **introduction** | Book tour | (none very strong) | "How to Read" — readers skip this |
| **eleven-step reference** | Visual tool / promise | The verb-pair list itself | Standalone — doesn't introduce a chapter |
| **chapter 0** | Ontology | "Spirit, light, and truth are not abstract concepts. They are substances." | Densest chapter in the book opening at front |

---

## What I think a reader experiences right now

Open the book.

**Page 1:** Title page. Beautiful epigraph (2 Nephi 25:26). Good.

**Page 2:** Consecration. *"freely shared, no restrictions."* The reader trusts you.

**Page 3:** Colophon. The reader doesn't read colophons. They flip past.

**Page 4-12:** Preface. *"Sitting in a classroom in January 2026..."* The reader is hooked by paragraph 3 — the **AI** in the margin. Then the chapter pulls the reader into a 3.5-year chronology of GitHub Copilot, Stable Diffusion, the dream, Emad Mostaque, Sonnet 4.5, Opus 4.5. This is interesting but **it's a memoir, not a thesis**. The reader keeps thinking: *wait, why am I reading this? Is this the book?*

**Page 13-16:** Introduction. The reader gets "This book is organized into three sections..." Now they know it's not the book — that was the preface. They flip ahead looking for the start.

**Page 17:** Eleven-Step Reference. *Wait, what is this? I haven't read any chapters yet but here's a reference page.*

**Page 18-25:** Chapter 0. Now the actual ontology hits. *Webster 1828... spirit is matter... vector spaces...* Heavy lifting on the first chapter for a reader still trying to land.

**Page 26+:** Chapter 1 finally opens. *"I have been a software engineer for eighteen years."* **THIS** is the line that meets a target reader where they are. By the time they reach it, they've crossed 25+ pages of mostly-warmup.

---

## Options — ratify any one or any combo

### Option A — Compress the Preface; cut the Introduction

**What changes:**
- Preface keeps the classroom moment + voice convention. Cut from 70 lines → ~20 lines.
- The 3.5-year journey moves to **backmatter** as "Afterword: How I Got Here." This honors it (it's gold material) without front-loading.
- Introduction is **dissolved**. Its "How to Read" becomes a single 2-line note at the start of Section I. Its "Confluence of Code and Covenant" overlaps with Ch 1; it goes.
- Eleven-step reference stays where it is (or moves — see Option D).
- Chapter 0 stays where it is.

**Net:** 242 lines before Ch 1 → ~110 lines before Ch 1. The reader meets "I have been a software engineer for eighteen years" by page 12 instead of page 26.

**Cost:** the 3.5-year journey is no longer the first impression. Some readers (the ones who love memoir) lose that hook.

### Option B — Weave the 3.5-year journey through the body

**What changes:**
- Preface keeps the classroom moment only (~20 lines).
- The chronology gets distributed:
  - **2022 Copilot autocomplete + Stable Diffusion** → Ch 1 (Value Shift — fits the "execution becoming free" arc)
  - **2023 dream + Mostaque interview** → Ch 3 (Spiritual Before Temporal — the dream as spiritual creation)
  - **2024-2025 chat + planning mode** → Ch 6 (Bilateral Covenant — fits "structured intent")
  - **2025 multiplayer games + Opus 4.5** → Ch 7 (Delegation — multi-agent dream working)
  - **January 2026 classroom** → stays in Preface as the lead-in
- Introduction dissolved as in Option A.

**Net:** the book gains warmth throughout. Personal experience is no longer ghettoized in the preface; it's threaded through doctrine.

**Cost:** harder to execute. Each chapter needs careful surgery to integrate a personal beat without breaking its modular study structure. Risk: the chapters get cluttered.

### Option C — Demote Chapter 0 to "Appendix A: The Substance of Reality"

**What changes:**
- Ch 0's ontology is the densest material in the book. It is the philosophical scaffolding the rest of the book USES — but it can be read **after** the body.
- Move Ch 0 to backmatter as Appendix A. Add a single sentence in Ch 5 (which currently calls back to Ch 0): *"For the full physics, see Appendix A."*
- Book starts at Ch 1 — "I have been a software engineer for eighteen years."

**Net:** the strongest opening sentence in the book becomes the opening sentence. Theological depth is preserved but waits for readers who want it.

**Cost:** Ch 5's reference to "Chapter 0 mapped the physics" needs rewording. Some readers will never read the Appendix. The book becomes slightly less of a "doctrine first, application second" piece — but maybe that's a strength.

### Option D — Hybrid (my recommended)

Combine the surgical bits of A + C without going as far as B:

**What changes:**
1. **Preface trimmed to ~25 lines.** Keep the classroom moment. Keep the voice convention. Cut "The 3.5-Year Journey" and "The Constant Principles" sections.
2. **Introduction dissolved.** Its content goes two places:
   - "How to Read" → moved to the back of the Preface as a single short paragraph: *"You can read this book front to back to follow the discovery arc, or open to any chapter as a standalone study. Each chapter opens with a Binding Question and closes with a practical Becoming Commitment."*
   - "Confluence of Code and Covenant" → its content is already in Ch 1 (Value Shift). Cut as duplicative.
3. **3.5-Year Journey moves to backmatter** as "Afterword: How I Got Here." Adds value for readers who finish the book and want the chronology. Doesn't gate readers who don't.
4. **Eleven-Step Reference becomes a foldout / endpapers** in print — or just moves to backmatter as a reference card. It's a TOOL, not an introduction. The first chapter that needs it (Ch 2 — Four Disciplines) can preview it.
5. **Chapter 0 stays where it is.** It anchors the metaphysics. Readers who reach it are ready.

**Net:** ~242 frontmatter lines → ~70 frontmatter lines. The reader hits Ch 0 by page 8 instead of page 18. Ch 1 by page 15-18 instead of page 26.

**Cost:** moderate execution work. The Afterword needs a brief opener ("If you've reached this page, you've heard the principles. Here's the chronology that taught them to me."). The 11-step reference needs a single-sentence introduction wherever it lands.

### Option E — Do nothing

Keep the current order. The book is short enough (~80 pages total) that 25 pages of frontmatter is not actually a death sentence. Many theology books open this way (Lewis, Chesterton). Trust the reader.

**Net:** zero work. Risk: readers who don't make it past the front matter never meet Ch 1's hook.

---

## My recommendation

**Option D (Hybrid).** It honors what's working (classroom moment, Ch 0's ontology) while moving what's clerical (Introduction, 3.5-year journey, reference card) out of the way of the hook.

## Specific ratifiable items (for AskUserQuestion when Michael returns)

1. **The Preface** — keep it or trim it (and how much)?
2. **The Introduction** — dissolve it, keep it, or shrink it?
3. **The 3.5-Year Journey** — keep in preface, move to backmatter, or weave through body?
4. **The 11-Step Reference** — keep where it is, move to start of Section I, move to backmatter, or treat as foldout/endpapers?
5. **Chapter 0** — keep where it is, demote to appendix, or do voice surgery in-place?
6. **The Section II problem** (Ch 5 doesn't fit "Bilateral Stewardship") — rename the section, or move Ch 5 to Section I, or leave?
7. **The Section III "11-step walk-through" promise** — fulfill it by adding Atonement/Sabbath chapters, soften the promise on the reference page, or annotate each chapter with its step?

Items 1-5 are about the front-end weighting.
Items 6-7 are about the body integrity.

---

## What I am NOT recommending

- I am **not** recommending we cut the Preface entirely. The classroom moment is the warmest opening in the book and should NOT be hidden in backmatter.
- I am **not** recommending we add chapters. The book is lean. Lean is a feature.
- I am **not** recommending we change the modular study format. It works.
- I am **not** recommending we drop the 11-step framework. It's the spine of the book's architecture. We may need to honor it differently.
