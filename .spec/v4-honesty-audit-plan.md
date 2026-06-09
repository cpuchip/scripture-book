# Draft v4 — Full-Book Honesty Audit (plan + findings log)

**Status:** scaffold written 2026-06-08; **walk not yet started.** Michael chose this
(option 1) as the next book work. Pick up here.

## The standard (Michael's words)

> "Write this book as we know it, not project stuff we don't know but present it as fact."

He is a physicist; **empirical honesty is the bar.** The model for the right call is
already in the book's history: the **Ch 12 measured-gift deferral** (we left a true-sounding
claim OUT because the data was n=1) and the **n=1 / "on one task" caveats**. The audit's job
is to find every place the manuscript asserts more than we actually know — or contradicts how
we actually work — and surface it for Michael to gate.

## What this pass IS and IS NOT

- **IS:** a factual / honesty / contradiction / clarity audit. Hunt: claims-asserted-as-fact-
  we-can't-verify, contradictions against how we really work, internal contradictions, genuine
  ambiguities, and places to be plainer.
- **IS NOT:** the voice/consistency pass. That is **pass 3**, after this. Do not re-litigate
  prose rhythm here; flag only clarity problems that change *meaning* or *truth*.

This is the same collaborative cadence as the condensation walk: **the agent reads + flags;
Michael gates every edit.** No content change without his ratification.

## Categories to hunt (the audit lens)

1. **Asserted-as-fact, not actually known.** Stats, counts, dates, biographical and industry
   claims, "everyone is doing X," any law drawn from a single data point. The 99.98%→99% and
   the bake-off n=1 are the type specimens. Every number, date, and count must trace to
   something we verified — or carry an honest hedge — or come out.
2. **Contradiction against how we actually work** (the Ben Test failure mode — describing
   aspirational practice as current practice). Ground truth:
   `.draft/20260530-how-we-actually-work.md` (evidence-mined from the real chat logs) and the
   substrate blueprint-vs-implementation audit. **The single biggest known candidate:** the
   real method is *vision-discovery-through-iteration*, and **spec-first is real mostly for
   code, largely absent for prose** — does the book still overclaim "spiritual creation
   (spec) before physical creation" as a universal practice? (The front-porch restructure +
   Ben-Test calibration were the *response* to this; the audit verifies it actually landed
   and nothing residual still overclaims.)
3. **Internal contradictions.** Chapter A vs. chapter B; glossary definition vs. in-chapter
   usage; chapter tags vs. content; a claim softened in one place but left hard in another.
4. **Genuine ambiguities.** Vague antecedents, a sentence a reader could fairly read two ways,
   a term used load-bearingly before it's defined.
5. **Plainer.** Doctrine-dense or jargon-dense passages where a clearer line would teach more
   honestly — only where it serves truth/clarity, not style (style = pass 3).
6. **Engineering-side overclaims.** The 2026-06-04 EP-accuracy audit already softened Ch
   9/10/12 and verified "context engineering" / "spec-driven development" as real. Re-confirm
   those held, and look for any *new* tool/industry/term claim that needs a source or a hedge.
7. **Quote/scripture accuracy (spot-check).** The Tier-4 provenance pass + condensation
   re-verified most quotes. Read-before-quoting still binds: if the audit touches any quoted
   line, re-verify it via `gospel_get` against canon before editing. Watch the known drift
   pattern (LoF "great prototype", Ether "melting" not "molting", Helaman "walk
   circumspectly").

## Already settled — do NOT re-flag (or you'll re-open closed councils)

- **Ch 12 measured-gift council** — deliberately NOT in the book (deferred, n=1). Do not add it.
- **Ch 2 harness beat** — already revised to the honest WIP framing ("six of seven"; Sabbath
  named as the rung still not made structural). Settled; don't re-soften.
- **Ch 9/10/12 EP overreaches** — already softened 2026-06-04. *Verify they held*, don't re-cut.
- **Becoming Commitments** — already Ben-Test calibrated (firm "I will" only where genuinely
  practiced; "strive" elsewhere; Ch 11 Sabbath cluster marked aspirational). Don't re-flatten.
- **"99.98%" → "99%"** in Ch 2 — *changed* (commit `1badd85`). NOTE the stale residue risk:
  an older audit note still reads "only 99.98% remains untouched." **First concrete check
  below.**

## Lived figures needing Michael's ground truth (he confirms; the agent cannot verify these)

These are the purest "do we actually know this?" items — they read as fact and only Michael
can confirm. Collect them as the walk hits each, present together:

- **P1 (Talk, Don't Command):** pg-ai-stewards "3 weeks / 3 days" timeframe.
- **P4 (Pack the Context):** "300+ microservices"; the "four of six" sub-agents figure.
- **P6 (Let It Carry):** "Dart/Rust"; "18 years"; "my kids played them."
- **Ch 2:** bacteriopolis "230 million input tokens" (verified once; re-confirm it's the
  figure he wants stated, with the right framing).
- **Part One scars generally:** the dated project history (the 230M-token runaway, the
  fabricated-D&C-104 scar, Ben Test, glm-5 misdiagnosis) — confirm each scar is told as it
  happened, not sharpened past the truth.

## The walk method (resumable)

1. Walk in reading order: frontmatter → preface → How-and-Why → eleven-step ref → **Part One**
   (P1–P10 + coda) → **Part Two** (Ch 0–12) → Epilogue → Afterword → Glossary → Further Reading.
2. Per unit: cold read against the seven categories; build a short findings list (claim →
   problem → category → proposed fix or question). For "how we work" contradictions, cite the
   ground-truth doc.
3. Present findings per unit (or per small batch) via AskUserQuestion; **Michael gates.**
4. Apply ratified edits verify-gated: diff-confirm no scripture/quote/doctrine lost; re-verify
   any touched quote against canon; rebuild + render-check + 0-collision check periodically.
5. Log every finding + its disposition in the table below so a fresh session resumes mid-walk
   without re-reading settled units. (Same discipline that let the condensation walk resume.)

## First concrete checks queued (start here)

1. **Ch 2 stray "99.98%":** grep the whole `src/` for `99.98` — confirm it's gone everywhere
   (commit `1badd85` changed the Ch 2 instance to 99%; make sure no sibling instance survived).
   Then confirm the surrounding sentence reads honestly as illustration, not measurement.
2. **Spec-first vs. iterate (category 2, the big one):** read Ch 3 (*Spiritual Before
   Temporal*) and Ch 2's four-disciplines mapping against
   `.draft/20260530-how-we-actually-work.md`. Does the book now make the
   *code-vs-prose / tooling-enforced-vs-conversational* distinction, or does it still present
   spec-first as how everything is made? Flag, propose, gate.
3. **Tag/triptych consistency:** verify the Atonement triptych tags (Ch8 *Refinement* → Ch9
   *Hope* → Ch10 *Yielding*) and all chapter tags match current content (tags drifted once).

## Findings log (fill during the walk)

| # | Unit | Finding | Category | Disposition |
|---|------|---------|----------|-------------|
| — | — | *(walk not started)* | — | — |

---

*When the walk completes: write the journal entry, update `.mind/active.md`, then it's the
voicing/consistency pass (pass 3), then KDP. Cover baseline + KDP runbook already staged.*
