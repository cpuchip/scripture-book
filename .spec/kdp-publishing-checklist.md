# KDP Publishing Checklist — *Beyond the Prompt*

**Researched 2026-06-04 from current KDP help + 2026 guides (sources at the bottom).**
A follow-it-in-order runbook. Every step is tagged **[AGENT]** (I can do it) or **[YOU]**
(only you can — account, money, art direction, the final click, the honesty calls).

> **Reality check on KDP:** specifics (print-cost numbers, exact margin minimums, the AI
> checkbox wording) drift. Where a number can change, this doc points you at the official
> KDP calculator/help rather than asserting a figure. Verify at the moment of upload.

> **One listing, two products.** A Kindle ebook and a paperback are published from the
> *same* KDP title and Amazon links them automatically. Each needs a *different* file:
> **EPUB for the ebook, print-ready PDF for the paperback.** (Uploading a PDF as an ebook
> is the #1 cause of the "TOC missing / PDF not recommended" error.) We already build both.

---

## Our book, at a glance (pre-filled)
- **Title:** Beyond the Prompt — **Subtitle:** Discovering the Laws of Organized Intelligence
- **Author:** Michael Stufflebeam
- **Trim:** 6 × 9 in (standard US; not a "large" trim). Set in `book.yaml`.
- **Interior:** ~123 pages, black text on white, no full-bleed images (so **no bleed needed** in the interior — see Phase 2).
- **Margins/gutter:** already set in `book.yaml` (top/bottom 0.75", outside 0.5", inside/gutter 0.75").
- **Build:** `./build.ps1` → `dist/manuscript.pdf` (paperback) + `dist/beyond_the_prompt.epub` (ebook).
- **Spine width** (white paper) = `0.002252 × pages`. At 123 pp ≈ **0.277"**. Recompute from the *final* page count before building the cover.

---

## Phase 0 — Decisions only you can make (do these first; they gate everything) **[YOU]**

1. **AI-content disclosure** — the most important honesty call, and it has teeth (undisclosed AI-generated content can get a title pulled and an account suspended). KDP's line:
   - **AI-*assisted*** (brainstorming, outlining, research, grammar, *refining human-written text*) → **no disclosure required.**
   - **AI-*generated*** (text or images substantially produced by AI) → **must disclose** (separate checkboxes for Text and Images).
   - **My honest read for this book:** much of the prose was AI-*drafted* from your studies and intent and then heavily edited/verified by you — that leans toward **disclosing the Text as AI-generated**, and it's the call most consistent with the book's own transparency about being a human–AI collaboration. **Your decision, but I'd disclose.** If the cover art is AI-made, disclose Images too. (We can discuss the exact boundary during the v4 audit.)
2. **ISBN** — paperback needs one; ebook does not (it uses an Amazon ASIN).
   - **Free KDP ISBN:** $0, fast, but imprint prints as "Independently published" and the number is locked to Amazon. Fine to ship quickly.
   - **Your own ISBN (Bowker):** $125 for one, $295 for ten (~$30 each) — lets you name your own imprint and use the same number on IngramSpark / in bookstores. Worth it if this is the first of a series (the canon-walk books) or you want your imprint.
   - **My rec:** if the goal is "out the door before interest fades," take the **free KDP ISBN** now; buy your own later only if you go wide. **Your call.**
3. **Cover approach** (this is the real gap — we have an interior, not a cover):
   - (a) **KDP Cover Creator** — free, in-portal, template-based. Fastest.
   - (b) **A designer / tool** (Canva, a freelancer) — best-looking, costs money/time.
   - (c) **[AGENT] a typographic cover in Typst** matching the interior's type — I can produce a clean, text-forward full-wrap PDF (front + spine + back) at the exact spec. Not "designed art," but honest and consistent. Good enough to ship; upgradeable later.
   - **My rec:** (c) to ship now, since it's the thing blocking you and I can do it.
4. **List prices** — paperback and ebook. See Phase 5 for the royalty math; pick after you see the numbers.
5. **Barcode** — *nothing to decide.* KDP auto-generates the back-cover barcode from whichever ISBN you use. Don't put your own barcode on the cover.

---

## Phase 1 — Account & tax setup **[YOU]**
- [ ] Sign in at **kdp.amazon.com** (your Amazon account works).
- [ ] Complete the **tax interview** (W-9 for US) and **banking** for royalty deposits. *KDP will not let you publish without this.* ~10 minutes.

---

## Phase 2 — Prepare the files **[AGENT, with your review]**
- [ ] **Interior PDF (paperback):** I confirm `dist/manuscript.pdf` meets KDP print specs — 6×9, fonts embedded (Typst embeds by default), images ≥300 DPI (we have ~none), and that inside/outside margins clear KDP's minimums for our page count. No bleed needed (no full-bleed art). **[AGENT]**
- [ ] **EPUB (ebook):** confirm `beyond_the_prompt.epub` has a working **NCX (navigation) TOC** and an **HTML TOC** page (KDP requires both). I verify/fix in the build. **[AGENT]**
- [ ] **Cover PDF (paperback):** once page count is final, I compute spine width and build a single full-wrap PDF = back + spine + front, sized `(bleed + back + spine + front + bleed) × (bleed + 9" + bleed)`, 0.125" bleed all sides, 300 DPI, < 650 MB. Spine text is allowed (we're well over the 79-page minimum). **[AGENT builds the spec/typographic version; YOU approve or replace with designed art]**
- [ ] **Copyright page / ISBN:** once the ISBN exists (free one is assigned during setup), I add it to the front-matter copyright page and rebuild. **[AGENT]**
- [ ] **Ebook cover image** (separate from the print wrap — just the front, ~1.6:1, ≥ 1600px tall). **[AGENT from the front-cover art]**

---

## Phase 3 — Create the title & metadata in KDP **[YOU drive; AGENT drafts the content]**
On your Bookshelf: **+ Create** → start with **Paperback** (or Kindle eBook; you'll add the other format to the same title after).
- [ ] **Language, Title, Subtitle** — must match the cover exactly. **[AGENT will hand you the exact strings]**
- [ ] **Author / contributors.** **[YOU]**
- [ ] **Description / blurb** — the back-cover/marketing copy. **[AGENT drafts 2–3 options]**
- [ ] **Keywords** — 7 backend slots, up to 50 chars each, 2–3-word reader-search phrases. **[AGENT researches + drafts]**
- [ ] **Categories** — pick 3 that fit (likely Religion & Spirituality / Christian Living, and Computers & Technology / AI). **[AGENT researches + recommends]**
- [ ] **AI-content disclosure** — answer per your Phase-0 decision. **[YOU]**
- [ ] **ISBN** — choose free KDP ISBN or enter your own. **[YOU]**

---

## Phase 4 — Upload & preview **[YOU click; AGENT fixes any file issue]**
- [ ] Upload the **interior PDF** (paperback) / **EPUB** (ebook).
- [ ] Upload the **cover**.
- [ ] **Open the previewer and check every page** — headings, the two block quotes on each Part-Two opener, the QR codes, the Glossary, page breaks. This is where problems show up. If anything is off, I fix the source and you re-upload. **[AGENT fixes]**

---

## Phase 5 — Pricing & royalties **[AGENT computes; YOU decide]**
- **Paperback royalty (US):** 60% of list **if priced ≥ $9.99** (50% below), **minus** the print cost. Print cost = fixed + (pages × per-page); compute it on the official calculator for our final page count.
- **Ebook royalty:** **70%** if priced **$2.99–$9.99** (minus a small per-MB delivery fee), else 35%.
- [ ] I'll run several list-price scenarios (e.g., paperback $12.99 / $14.99, ebook $6.99 / $9.99) through the official **KDP printing-cost & royalty calculator** and hand you a small table; you pick. **[AGENT → YOU]**

---

## Phase 6 — Proof copy **[YOU]**
- [ ] Order a **proof copy** (printed at cost + shipping, no royalty markup; up to 5). ~a few dollars + shipping.
- [ ] **Hold the physical book.** Check trim, margins/gutter (text not swallowed by the spine), cover wrap alignment, spine text centering, paper feel. Typos read differently on paper. **This is the last gate before the world sees it.**

---

## Phase 7 — Publish **[YOU]**
- [ ] Resolve anything the proof surfaced (I fix files, you re-upload/re-preview).
- [ ] Click **Publish**. Live globally in ~24–72 hours.

---

## What I (AGENT) can hand you, ready to go
- Verified print PDF + EPUB (TOC-correct).
- A typographic full-wrap cover PDF at exact spec (if you want option 3c).
- The exact title/subtitle strings, a drafted description (2–3 options), 7 keywords, 3 recommended categories.
- Spine-width and royalty/price tables computed from the final page count.
- The copyright page updated with the ISBN once it exists.

## What only you can do
- KDP account + tax/banking.
- The AI-disclosure answer (I recommend disclosing Text), the ISBN choice, the prices.
- Final cover art direction (approve mine or supply designed art).
- Upload, preview, order the proof, hold and approve it, and click Publish.

---

## Appendix — formulas & specs (verified 2026-06-04)
- **Bleed:** 0.125" trimmed from top/bottom/outside. Interior needs bleed *only* if art touches the page edge (ours doesn't). Cover *always* needs 0.125" bleed all around.
- **Spine width (white paper):** 0.002252" × page count (cream: 0.0025"). Spine text allowed at ≥ 79 pages.
- **Images:** ≥ 300 DPI (≤ 600 DPI recommended); total file < 650 MB.
- **Trim:** 6×9 is standard (≤ 6.12" w / 9" h = not "large trim").
- **EPUB:** needs NCX + HTML TOC.
- **Barcode:** auto-generated by KDP from the ISBN.

## Sources
- KDP — Create a Book; Paperback Submission Guidelines; Set Trim Size, Bleed, and Margins; Create a Paperback Cover; Cover Calculator (kdp.amazon.com/cover-calculator); Printing Cost & Royalty Calculator (kdp.amazon.com/royalty-calculator); Metadata/Keywords/Categories help; Content Guidelines (AI disclosure); Proof & Author Copies.
- 2026 guides: kidillus, kindlepreneur, kdpeasy, inkfluenceai, neucitepress (ISBN), univers.studio + aipolicydesk (AI disclosure), ebookpbook (ISBN/barcode).
- *Verify any cost/spec against the official KDP page at upload time — KDP changes these.*
