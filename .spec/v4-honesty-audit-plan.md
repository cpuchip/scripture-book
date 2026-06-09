# Draft v4 — Full-Book Honesty Audit (plan + findings log)

**Status:** WALK IN PROGRESS (started 2026-06-09 by Claude Fable 5). Findings accumulate
in [`.draft/20260609-v4-walk-findings.md`](../.draft/20260609-v4-walk-findings.md) — that
file is the live state; this file is the plan.

**Council updates ratified 2026-06-09 (Michael, first Fable 5 session):**
1. **Stewardship grant extends to Claude Fable 5** — commit + push as Fable 5; trailer
   `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>` so the audit trail names the
   actual agent.
2. **Cadence changed from the condensation-walk pattern:** the agent walks the WHOLE book
   solo first, logging findings to the scratch file — then Michael and the agent walk the
   findings together **in chat** (not AskUserQuestion), so he can pause, think, and ask
   for more detail. Michael still gates every edit; nothing is applied during the solo walk.
3. **VOICING JOINS THE WALK (category 8 below).** Michael: he reads Opus's prose and
   doesn't catch the tics himself ("it's not x it's y" etc.); Gemini's voicing read as
   more natural. He wants the book to "sound and flow natural, if not poetic." Fable, as
   a different model, can see Opus's fingerprint from outside — so the walk carries a
   voicing lens alongside the honesty lenses. Rephrase-proposals keep meaning exactly;
   doctrine and quoted text untouched. (The dedicated pass-3 voicing/consistency pass
   still follows; this lens just means we only walk the book once per pass.)
4. **v5 QUEUED (do NOT start):** a conversational-voice pass learned from Michael's real
   podcast with his siblings — transcripts at workspace `books/creators-playbook/`
   (speaker attribution is suspect; Michael hasn't cleaned it yet). Learn his real
   conversational pacing from it and pull that into the book. After v4.
5. Michael's own manual read continues in parallel (he's ~4 days into a deliberate rest
   break from it). The two reads stay independent on purpose.

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
8. **Voicing — the Opus fingerprint (added 2026-06-09, Michael's ask).** Flag where
   AI-generated cadence clusters, and propose rephrasings that keep the meaning exactly.
   The tic list to hunt:
   - **Negation-contrast:** "it's not X — it's Y" / "not X but Y" / "This isn't X. It's Y."
     (the big one; fine once, a fingerprint at density)
   - **Staccato aphorism:** the dramatic one-line paragraph or sentence-fragment landing
   - **Symmetric pairs & triads:** "the A and the B", "A, B, and C" flourishes where one
     word would do
   - **Anaphora chains:** consecutive sentences/paragraphs opening with the same phrase
   - **Self-restating closers:** a paragraph that ends by saying its own point again,
     one notch more poetic
   - **Em-dash density** beyond the one-per-paragraph budget
   - **Abstract-noun stacking:** "the discipline of the practice of the principle"
   Rules: flag CLUSTERS (a tic twice on one page), not every instance; propose the natural
   alternative inline in the finding; never alter quoted scripture/talk text or doctrinal
   content; where the tic IS the right rhetoric (a deliberate antithesis the meaning needs),
   say so and leave it. Goal per Michael: "sound and flow natural, if not poetic."

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

## The walk method (resumable — UPDATED 2026-06-09 per Michael)

1. Walk in reading order: frontmatter → preface → How-and-Why → eleven-step ref → **Part One**
   (P1–P10 + coda) → **Part Two** (Ch 0–12) → Epilogue → Afterword → Glossary → Further Reading.
2. Per unit: cold read against all eight categories; log findings (claim → problem →
   category → proposed fix or question) to
   [`.draft/20260609-v4-walk-findings.md`](../.draft/20260609-v4-walk-findings.md) as the
   walk goes — files are durable, context is not. For "how we work" contradictions, cite the
   ground-truth doc.
3. **No edits during the solo walk.** When the walk completes (or at a natural checkpoint),
   Michael and the agent walk the findings together **in chat** — conversational, pausable,
   with the agent able to expand any finding on request. **Michael gates every edit.**
4. Apply ratified edits verify-gated: diff-confirm no scripture/quote/doctrine lost; re-verify
   any touched quote against canon; rebuild + render-check + 0-collision check periodically.
5. Each finding carries a disposition column (open / ratified / rejected / deferred) so a
   fresh session resumes mid-walk without re-deciding settled items.

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
