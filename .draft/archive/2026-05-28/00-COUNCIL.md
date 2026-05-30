# Council Document — *Beyond the Prompt* Audit (Five-Pass Synthesis)

**Date:** 2026-05-28
**For:** Michael Stufflebeam (asleep at writing)
**Purpose:** Synthesize four independent reads + scripture verification + editing research into one ratifiable council document. **No changes made to the manuscript.** All five passes are fact-gathering only.

---

## TL;DR — read this first

The book is closer to "ship it" than the audit makes it look. Four independent readers (in-house editor + faithful Latter-day Saint + skeptical engineer + editorial-research synthesis) converge on a small number of high-impact moves. Most of the manuscript holds. The bulk of the work is **restructuring front matter** (1 big move), **fixing 3 concrete factual issues** (small), and **strengthening 4 chapters where the engineering parallel needs work** (medium). The doctrine is overwhelmingly clean — 30+ scripture quotes verified verbatim against canon, including the Section III chapters Gemini drafted post-harness-solidification.

**The single most impactful move** (all four passes agree): **demote the 3.5-year journey out of the preface.** Weave milestones into the body chapters or move to an afterword. This unlocks the warmest sentence in the book ("I have been a software engineer for eighteen years") to land by page ~12 instead of page ~26. Five independent editorial sources (Gross, Williams, Hoffman, FriesenPress, Bold & Italic) converge on "weave personal narrative into the body, not the front matter." Published comparables (Lewis, Lanier, Peterson, Newport, Sapiens, Bushman) all keep front matter at 3-8% of the book; *Beyond the Prompt* is currently at 28%.

**The single most credible page** (all three reader passes agree): **the Ch 6 production-note sidebar** that records the book's own draft fabricating a quote and the audit catching it. Both the gospel reader and the engineer reader called it the most credible content in the book and recommended elevating it. **Elevate it.**

**The single most strained parallel** (all three reader passes agree): **Ch 10's heart-softening → connection pooling**. The doctrine is the highest-stakes pastoral content in the book; the parallel is the coldest engineering metaphor in the book. Replace with **gardening** (Mark 4 / Alma 32 — already in scripture).

---

## How to use this document

Items are grouped into four sections:

1. **Tier 1 — Convergence Items** (multiple passes independently flagged the same issue). High signal. Recommend ratifying most.
2. **Tier 2 — High-Value Single-Pass Findings** (one pass surfaced; high impact). Recommend ratifying selectively.
3. **Tier 3 — Verified Factual Fixes** (concrete + small). Recommend ratifying all.
4. **Tier 4 — Carry-Forward Items** (worth deciding but not blocking ship).

Each Tier 1 and Tier 2 item is structured as a ratifiable proposal: **{Finding} → {Move} → {Cost} → {Source pass}**.

Each ratification question is keyed to the AskUserQuestion format. When Michael returns, we can step through these one by one (or batch them).

---

## TIER 1+ — Three NEW Items from Multi-Model Brainstorm (2026-05-29)

Added after Michael's check-in from his phone. Four pg-ai-stewards brainstorm-lens pipelines fired in parallel (Six Hats + Reverse on kimi-k2.6, SCAMPER + Crazy 8s on qwen3.6-plus). Total cost $0.32, wall time ~7 minutes. Full details in [`07-multi-model-brainstorm.md`](./07-multi-model-brainstorm.md).

The brainstorm surfaced three findings large enough to upgrade into Tier 1.

### 1.0a — NEW: Epistemic Confidence Rating on the 11-Step Reference Page

**Finding:** Three of the four brainstorm lenses (Six Hats Black + SCAMPER Modify + Reverse 2.1) flagged "retrospective numerology" as a real engineer dismissal risk — *"if the 11-step cycle only matches AI workflows after the fact, skeptical readers will dismiss the entire book as apophenia; the parallel must show predictive or generative power, not just descriptive similarity."*

**Move:** Add a confidence column to the 11-step reference page. Each parallel rated:
- **Strong** — structural isomorphism (both systems require this step)
- **Medium** — functional analogy (both systems benefit from this step)
- **Speculative** — thematic resonance (interesting but not proven)

The Watching, Stewardship, and Specification parallels are likely Strong. Sabbath and Consecration are likely Medium. Atonement-as-re-aiming may be Speculative. This is sharper than my existing Tier 3.5 ("soften the promise") — it doesn't just soften, it *rates*.

**Cost:** Small. Adds one column to the existing reference page.

**Source:** [07-multi-model-brainstorm.md § 0 NEW-1](./07-multi-model-brainstorm.md) + [§ 1 Six Hats Black](./07-multi-model-brainstorm.md) + [§ 3.4 SCAMPER Modify](./07-multi-model-brainstorm.md)

**Ratification question (RQ1.0a):** Add Strong / Medium / Speculative column to the 11-step reference?
- (A) Yes — add the column; rate each parallel
- (B) Yes but use different labels
- (C) No — keep the framework presented as 11-for-11

---

### 1.0b — NEW: Directional Editing Pass — Eliminate AI→Gospel Validation

**Finding:** Three independent sources converge on this as **the single largest credibility killer for engineer readers**. SCAMPER (qwen3.6-plus) named it directly: *"Cut every sentence, paragraph, or implication that suggests AI engineering 'proves,' 'confirms,' or 'fulfills' gospel patterns... The book's thesis should be that gospel patterns are the lens through which we understand AI engineering, not that AI engineering validates the gospel."* Reverse lens echoed it (2.5 "let the engineering pattern be the question, not the answer"). The AI-reader pass independently flagged Tipler's "collapsing theology INTO the technical domain" as a failure mode the book is in real danger of.

**Move:** A single directional editing pass that searches the manuscript for verbs of validation (*proves, confirms, fulfills, demonstrates, validates, evidences*) applied to AI→gospel sentences. Flip each one. **Gospel is the lens; AI is the lit thing.**

Concrete examples to audit:
- Ch 0 line 70: *"We are literally aligning the model's physical states with the truth represented in its training data"* — uses AI to legitimize the "intelligence as truth" claim.
- Ch 3 line 44 (the 743-line spec example) — uses AI success to validate spiritual-creation doctrine.
- Ch 6 line 45 (*"the quality of the work accelerates"* when both honor covenant) — uses AI workflow improvement to validate D&C 82:10.

The fix is to invert: lead with the gospel principle, then show the AI workflow we already use is a small recent instance of that older pattern.

**Cost:** Medium. A focused grep + rewrite pass. ~20-30 sentences likely affected across the manuscript.

**Source:** [07-multi-model-brainstorm.md § 0 NEW-2](./07-multi-model-brainstorm.md) + [04-ai-reader-pass.md § 3](./04-ai-reader-pass.md) + [05-editing-research.md § 6.5 Hodgson direction-of-influence](./05-editing-research.md)

**Ratification question (RQ1.0b):** Run the directional editing pass?
- (A) Yes — flip every AI→gospel validation sentence
- (B) Partial — flip the most egregious ones; leave subtle cases for later
- (C) Defer — needs a fuller pass with more eyes
- (D) No

---

### 1.0c — NEW: Directional Flow Decision (Open With What?)

**Finding:** SCAMPER 3.7 and Reverse 2.5 offer two *opposite* resolutions to the same problem (the book's direction-of-influence). Both fixes resolve the AI→gospel arrow concern; they go in opposite directions.

**Option A (SCAMPER 3.7 — scripture-first):** *"Open with the gospel patterns as the primary, ancient framework... and then show how AI engineers — working in complete ignorance of these texts — independently converged on structurally similar patterns. AI is a recent, partial, secular instantiation of eternal patterns that faithful readers already recognize."*

**Option B (Reverse 2.5 — observation-first):** *"Start from observable AI behavior — emergent capability, attention mechanisms, latent space structure — and pose the honest question: 'If this is how engineered intelligence behaves, what would we expect from uncreated intelligence?' Then bring D&C 88 in as a rigorous hypothesis that fits the data."*

Both resolve the directionality. Option A honors the LDS reader's prior knowledge; Option B honors the engineer's empirical posture. The current book is in neither register — it interleaves them with the implicit "AI workflows reveal eternal patterns" arrow (subtitle).

**This is a thesis-direction question, not a chapter-level move.** It interacts with everything else in this council.

**Cost:** Big if changed. Larger than any other Tier 1 item. Probably should be Michael's call alone — directional framing is author territory.

**Source:** [07-multi-model-brainstorm.md § 0 NEW-3](./07-multi-model-brainstorm.md) + [§ 2.5 Reverse](./07-multi-model-brainstorm.md) + [§ 3.7 SCAMPER](./07-multi-model-brainstorm.md)

**Ratification question (RQ1.0c):** Directional flow:
- (A) Scripture-first throughout (Option A — gospel as primary, AI as recent instance)
- (B) Observation-first throughout (Option B — AI behavior as the question, gospel as the answer)
- (C) Keep current interleaving but enforce the directionality fix (RQ1.0b) without restructuring
- (D) Defer — make this decision after the structural moves in 1.1-1.6 land

---

### 1.0d — UPGRADE: Tier 1.4 may want to be a Recurring Frame, not a Single Paragraph

**Finding (Reverse 2.7):** The "AI has no soul" boundary that all three reader passes flagged could be addressed in a heavier way than the current Tier 1.4 proposes. Reverse lens (kimi-k2.6) suggests *"install a recurring epistemic frame — call it the 'Stewardship Boundary' — in every chapter that explicitly distinguishes three territories: (1) what we observe in AI engineering, (2) what the scripture says about eternal things, and (3) the narrow, provisional bridge between them that we are permitted to walk. Make the boundary itself a liturgical act of reverence and rigor."*

This is a structurally bigger move than the existing Tier 1.4 (one paragraph in Ch 0 or Glossary). It would add a recurring visual element to each chapter — like the production-note sidebar but smaller and chapter-uniform.

**Ratification question (RQ1.0d / replaces RQ4):** Is the "type-and-shadow" treatment —
- (A) One paragraph somewhere (current Tier 1.4)
- (B) A short recurring "Stewardship Boundary" callout in every chapter
- (C) Both — paragraph + recurring callout

---

## TIER 1 — Convergence Items (multi-pass agreement, high signal)

### 1.1 — The Front-Loading Problem

**Finding:** 28% of the book is front matter before Ch 1 line 13 ("I have been a software engineer..."). Published comparables sit at 3–8%.

**Move:** Adopt **Option D (Hybrid)** from `02-frontmatter-weaving.md`:
- Trim preface to ~20-25 lines (keep classroom moment + voice convention; add a 1-2 paragraph "two audiences" note)
- Dissolve the Introduction. "How to Read" → 2-line note at start of Section I. "Confluence of Code and Covenant" → cut (overlaps with Ch 1).
- Move the 3.5-year journey to an Afterword ("How I Got Here") OR weave into body chapters at the points where each milestone does work (2022 → Ch 1, 2023 dream/Mostaque → Ch 3, 2024-25 chat-to-code → Ch 6, 2025 multi-repo → Ch 7).
- Move the 11-step reference page to the front of Section I (or use as endpapers in print).
- Chapter 0 stays where it is.

**Cost:** Moderate execution work. 3.5-year material is gold and needs careful redistribution. Risk of cluttering body chapters if "weave" path is chosen. Lower risk on the "Afterword" path.

**Source:** [01-editor-pass.md § 2](./01-editor-pass.md), [02-frontmatter-weaving.md Option D](./02-frontmatter-weaving.md), [05-editing-research.md § 7 Recommendation 1](./05-editing-research.md) — five editorial sources converge on "weave, don't dump."

**Ratification question (RQ1):** Where does the 3.5-year journey go?
- (A) Weave into Ch 1, 3, 6, 7 at relevant milestone points
- (B) Move to Afterword titled "How I Got Here"
- (C) Keep where it is (do nothing)

---

### 1.2 — The Ch 6 Production-Note Is the Credibility Anchor

**Finding:** All three reader passes (gospel reader, engineer reader, in-house editor) independently named the Ch 6 production-note sidebar as the most credible content in the book. The note that records the book's own draft fabricating a D&C quote — and the audit catching it — is what the engineer reader called *"the thing that kept me reading."*

**Move:** Elevate the production note from sidebar to a more prominent placement. Options:
- Move to its own short chapter ("When the System Lies") between Ch 6 and Ch 7
- Keep as sidebar but increase visual weight (boxed callout in print, page break before)
- Reference it explicitly in the preface (in the "two audiences" addition) so readers know the witness is coming

**Cost:** Small. The text exists. The move is positioning.

**Source:** [01-editor-pass.md § 4.3](./01-editor-pass.md), [03-gospel-reader-pass.md § 1 (lines 70-75) + § 10](./03-gospel-reader-pass.md), [04-ai-reader-pass.md § 1.3 + § 6](./04-ai-reader-pass.md)

**Ratification question (RQ2):** How prominent should the production note be?
- (A) Promote to its own short chapter
- (B) Keep as sidebar but visually elevate (boxed callout, page break)
- (C) Mention in the preface so readers anticipate it
- (D) Leave where it is

---

### 1.3 — Ch 10's Connection-Pooling Parallel is the Most Strained in the Book

**Finding:** All three reader passes flagged Ch 10's heart-softening → connection pooling parallel as the most strained in the book. The doctrinal half of Ch 10 (Nephi, Alma, Lamoni's father, Helaman, Job, Ezekiel) is the highest-stakes pastoral content in the manuscript. The engineering parallel — releasing database locks, clearing stale cache — is in a different emotional register.

**Move:** Replace the connection-pooling parallel with a **gardening parallel** (Mark 4, Alma 32 — already in scripture). The gardener cannot force the seed to sprout; they can only clear stones, water, wait. *That* matches the asymmetry-of-agency the doctrine is teaching.

Alternative if a tech parallel is required: shift to **context-window saturation** (the engineer's part is not to "rewrite the reasoning engine" but to *release* the bad context — clearer match) and drop the connection-pool / cache content entirely.

**Cost:** Medium. Requires rewriting lines 23-27 of Ch 10. The doctrinal first half stays intact.

**Source:** [01-editor-pass.md § 5 (Ch 10 voice note)](./01-editor-pass.md), [03-gospel-reader-pass.md § 4 + § Summary card](./03-gospel-reader-pass.md), [04-ai-reader-pass.md § 2.5](./04-ai-reader-pass.md)

**Ratification question (RQ3):** Replace Ch 10 engineering parallel with —
- (A) Gardening (Mark 4 / Alma 32)
- (B) Context-window release (corrected version of current parallel)
- (C) Both — gardening as primary, context-window as the lighter tech echo
- (D) Leave as-is

---

### 1.4 — The "AI Has No Soul" Boundary Is Too Implicit

**Finding:** Three passes (in-house, gospel reader, AI reader) flagged that the book's *one* explicit statement of the asymmetry between human agency and AI mechanism appears in Ch 4 line 46 — and then the rest of the book uses language ("the model resonates with what we brought," "the agent commits to") that anthropomorphizes the very thing Ch 4 disowned. The editing research confirmed this as the **Tipler failure mode**: collapsing theology INTO the technical domain, rather than maintaining the type-and-shadow distinction.

**Move:** Add one explicit paragraph naming the categorical line — *these are tools, not souls; the parallel is type-and-shadow, not identity; the model imitates resonance, the model is not a soul* — in one of:
- Ch 0 (the ontology chapter, where the substance theology is most expensive)
- The Glossary's "Intelligence" entry
- A new short section in Ch 14 "Where the parallel ends"

The AI reader provided concrete draft language in [04-ai-reader-pass.md § 8 Edit 3](./04-ai-reader-pass.md).

**Cost:** Small. One paragraph. Strengthens credibility on both sides.

**Source:** [01-editor-pass.md § 4.2 + § 4.4](./01-editor-pass.md), [03-gospel-reader-pass.md § 4 last paragraph](./03-gospel-reader-pass.md), [04-ai-reader-pass.md § 8 Edit 3](./04-ai-reader-pass.md), [05-editing-research.md § 6.5](./05-editing-research.md) — direction-of-influence framing per Hodgson.

**Ratification question (RQ4):** Where does the "type-and-shadow, not identity" paragraph land?
- (A) Inside Ch 0
- (B) In the Glossary
- (C) New "Where the parallel ends" section in Ch 14
- (D) All three (echo across the book)

---

### 1.5 — Chapters 0, 8, 9, 10 Need Voice Surgery on the Engineering Parallels

**Finding:** Three passes converge on the visible drafting-author divide. Michael-drafted chapters (1, 3, 4, 6, 7) read as lived practice; Gemini-drafted chapters (0, 8, 9, 10) read as theology with imported engineering vocabulary. The engineer reader was specific:

- **Ch 0 lines 61-70** — "topographies of higher-quality parameter weights" is not a real thing; the mechanism is information-density, not moral-quality topology
- **Ch 8 lines 27-32** — "overfitting = dross," "pruning makes models more accurate," "high-voltage inference" are three specific ML vocabulary errors
- **Ch 9 lines 30-35** — Kubernetes-as-grace is the most theologically loaded analogy carried by the weakest engineering ground
- **Ch 10 lines 23-27** — connection-pool / cache parallel (covered in 1.3 above)
- **Ch 11 lines 25-28** — microservices-as-Zion is structurally backwards (microservices emphasize partition tolerance, not unity); blockchain-as-Zion will read as outdated/wrong in 2026

The gospel reader independently confirmed these chapters are where the jargon blocks doctrine for a non-engineer.

**Move:** Voice surgery on each. The AI reader provided concrete replacement language for Ch 0 (information-density framing) and Ch 8 (RLHF / instruction-tuning as the refinement parallel). See [04-ai-reader-pass.md § 8 Edit 1 + Edit 2](./04-ai-reader-pass.md).

Three options for scope:
- **(a) Full rewrite of all four engineering parallels** (Ch 0, 8, 9, 11) using the AI reader's suggested framings and Michael's voice.
- **(b) Targeted surgery on Ch 0 and Ch 8 only** (the load-bearing ones; Ch 9 and Ch 11 take lighter touches).
- **(c) Add a meta-note acknowledging where the parallels are weaker** (the Hodgson modesty move from editing research) and otherwise leave.

**Cost:** Medium to large depending on scope. Option (a) is the most work but produces the strongest book. Option (c) is the smallest but accepts a known weakness.

**Source:** [01-editor-pass.md § 5](./01-editor-pass.md), [03-gospel-reader-pass.md § 2 + § 4](./03-gospel-reader-pass.md), [04-ai-reader-pass.md § 2 + § 7 + § 8 Edits 1-2](./04-ai-reader-pass.md)

**Ratification question (RQ5):** Engineering parallel voice surgery scope:
- (A) Full rewrite — Ch 0, 8, 9, 11 (AI reader's framings as starting drafts, Michael's voice on top)
- (B) Targeted — Ch 0 + Ch 8 only
- (C) Meta-note — add a "where the parallel reaches its limit" acknowledgment, otherwise leave
- (D) Defer to a second editing pass after the structural moves land

---

### 1.6 — Section II Title Mismatch

**Finding:** The Introduction declares Section II as "Bilateral Stewardship — how God delegates authority and responsibility to human beings." But Section II's opener (Ch 5 — *Intelligence Cleaveth*) is about resonance/posture, not delegation. Delegation is Ch 7. The label misrepresents one of three chapters.

**Move:** Either rename Section II (something like "Alignment Under Law" or "The Bilateral Covenant") OR move Ch 5 into Section I.

**Cost:** Small. Rename is one line in the introduction; chapter move requires renumbering.

**Source:** [01-editor-pass.md § 3.4](./01-editor-pass.md). The gospel reader independently called Ch 5 the "chapter to read first" — which argues against moving it out of Section II's opening slot.

**Ratification question (RQ6):** Section II — keep Ch 5 in opening slot and —
- (A) Rename Section II to better cover all three chapters
- (B) Move Ch 5 into Section I and renumber
- (C) Leave as-is

---

## TIER 2 — High-Value Single-Pass Findings

### 2.1 — Glossary expansion + earlier announcement

**Finding (gospel reader):** The Glossary covers only 10 terms and isn't announced until the end. A gospel reader who hits "vector space" in Ch 0 has no recourse.

**Move:** Add 5-10 plain-English glossary entries (*vector space, parameter weights, context window, tool schema, microservice, neural network, Kubernetes, Dockerfile, prompt template, training data*), each with a one-sentence definition and a one-sentence scriptural parallel. Mention the glossary in the preface or introduction.

**Cost:** Small. Adds maybe 15-20 lines to the glossary.

**Source:** [03-gospel-reader-pass.md § 7 Edit 2](./03-gospel-reader-pass.md)

**Ratification:** Ratify (low cost, high gospel-reader payoff)?

---

### 2.2 — "For the non-engineer" sidebar in Ch 2

**Finding (gospel reader):** Ch 2 is the most jargon-dense chapter ("prompt craft," "context engineering," "intent engineering," "specification engineering" + "context window" + "tool schemas" + "active session state" inside three paragraphs). A non-engineer hits this and skims.

**Move:** Two-paragraph sidebar at the start of Ch 2: *"If you don't work in software, here's all you need to carry forward..."*

**Cost:** Small. ~6 lines.

**Source:** [03-gospel-reader-pass.md § 7 Edit 1](./03-gospel-reader-pass.md)

**Ratification:** Ratify?

---

### 2.3 — Lead each Engineering Parallel with a non-engineering bridge sentence

**Finding (gospel reader):** Ch 3 already does this (the chapter applies spiritual-creation to scripture study before software). Ch 4 does it. Ch 5 does it implicitly. **Ch 7, 8, 9, 10 do not.** Adding one human-life sentence before each tech parallel in those chapters carries the gospel reader across.

**Move:** Insert one bridging sentence at the head of each "Engineering Parallel" section in Ch 7, 8, 9, 10. Optionally also rename the section header from *"The Engineering Parallel"* to something less clinical like *"Where I see this in my work"* or *"How this works in software"*.

**Cost:** Small. 4-5 sentences total + optional header rename.

**Source:** [03-gospel-reader-pass.md § 7 Edit 3](./03-gospel-reader-pass.md)

**Ratification:** Ratify?

---

### 2.4 — Ben Test calibration on Becoming Commitments

**Finding (gospel reader):** Several "I will [daily X]" commitments imply *practiced* when they're closer to *aspirational*. Specifically:
- Ch 4 #2 ("Every week, I will pause my creative execution for meta-review")
- Ch 5 #1 ("Before I write a prompt, I will pause to evaluate my spirit")
- Ch 8 #3 ("Repent as a daily structural reset")
- Ch 9 #3 ("I will bring molten stones to the mount")
- Ch 10 #2 ("I will protect the first hour of my morning from digital inputs")
- Ch 11 #3 ("a generous fast offering")

**Move:** Walk through each Becoming Commitment with the Ben Test skill. Mark aspirational items explicitly ("I am working toward..." instead of "I will..."). The Preface earns enormous credibility from its honesty about the 3.5-year journey ("life got busy, I lost interest"); applying that honesty to commitments compounds it.

**Cost:** Small. A line-level pass on ~15 commitments.

**Source:** [03-gospel-reader-pass.md § 8](./03-gospel-reader-pass.md)

**Ratification:** Ratify?

---

### 2.5 — Two-audiences paragraph in the preface

**Finding (editing research):** All four currently-selling Christian-AI crossover books (Reinke, Driscoll, Webb, Russell) explicitly name two audiences in the front matter and acknowledge each side's reasonable wariness. The current preface assumes the believing-engineer reader and never names the AI-skeptic believer or the agnostic-engineer.

**Move:** Add 1-2 paragraphs in the preface (between classroom moment and voice convention) naming the two audiences and acknowledging the wariness from each side.

**Cost:** Small. ~10 lines.

**Source:** [05-editing-research.md § 7 Recommendation 3](./05-editing-research.md), echoes [01-editor-pass.md § 4.1](./01-editor-pass.md). Models: Bushman (Rough Stone Rolling preface), Russell (The Singularity).

**Ratification:** Ratify?

---

### 2.6 — AI-failures-as-doctrinal-types paragraph

**Finding (gospel reader):** A careful gospel reader will arrive at the inverse parallel on their own — if AI is a type-and-shadow of intelligence-organization, do AI's *failures* map onto something doctrinal? Hallucination → false revelation? Drift → apostasy? Training contamination → false tradition? The book is silent. Better to name the parallel and explain why the book doesn't pursue it further than leave the reader to do the work alone (and possibly go further than Michael would).

**Move:** Single paragraph in Ch 6 (Bilateral Covenant) or in the Glossary's "Dross" entry.

**Cost:** Small. 5-8 lines.

**Source:** [03-gospel-reader-pass.md § 9](./03-gospel-reader-pass.md)

**Ratification:** Ratify?

---

### 2.7 — Address the training-data ethics question

**Finding (engineer reader):** The book is silent on training-data ethics — copyright, consent, the NYT v. OpenAI / Stack Overflow discourse. An engineer who follows this conversation will reasonably ask: *what does "covenant" mean when one party was trained on contested labor?* The book has no answer because it doesn't pose the question.

**Move:** One paragraph somewhere acknowledging that the substrate of AI rests on contested training data, and what that means for using AI to write a book about covenants.

**Cost:** Small. ~8 lines. Difficulty is theological, not editorial — Michael's call on how to engage.

**Source:** [04-ai-reader-pass.md § 5.4](./04-ai-reader-pass.md)

**Ratification:** Ratify? (or defer — this is a substantive theological question)

---

## TIER 3 — Verified Factual Fixes (small, concrete, all should ship)

These are all verified against canon via gospel-engine-v2. See [06-fact-check-results.md](./06-fact-check-results.md) for full verification log.

### 3.1 — Moses 7:68 framing in Ch 11

**The book says** (Ch 11 line 19): *"Enoch did not build the city of holiness overnight; he walked with God three hundred and sixty-five years (Moses 7:68)."*

**Canon (verified):** Moses 7:68 — *"And all the days of Zion, in the days of Enoch, were three hundred and sixty-five years."* The 365 refers to Zion's duration, not Enoch's walking-with-God span.

**Fix:** Rewrite to: *"Enoch did not build the city of holiness overnight; Zion stood for three hundred and sixty-five years among his people..."* — preserves the 133,225-days math.

**Severity:** Real factual error. **Recommend fixing.**

---

### 3.2 — Unattributed Oaks + Bednar quotes in Ch 8

**Verified verbatim against canon:**
- Ch 8 line 17 quotes *"an acknowledgment of the final effect of our acts and thoughts—what we have become"* — this is Oaks, *The Challenge to Become*, Oct 2000 GC. **Verbatim accurate. Attribution missing.**
- Ch 8 line 21 quotes *"cleansing and redeeming power"* and *"sanctifying and strengthening power"* — this is Bednar, *Clean Hands and a Pure Heart*, Oct 2007 GC. **Verbatim accurate. Attribution missing.**

**Fix:** Add inline citations + links to both talks.

**Severity:** Real attribution violation. **Recommend fixing.**

---

### 3.3 — D&C 131:7-8 capitalization inconsistency between Ch 0 and Ch 8

- Ch 0 line 17: *"...by purer eyes; **we** cannot see it..."* (lowercase)
- Ch 8 line 6: *"...by purer eyes; **We** cannot see it..."* (capital)

Canon presents v.8 starting with "We" (capital — it's the start of a new verse). When run together, both lowercase (smoothing) and capital (preserving) are defensible. The issue is **inconsistency**.

**Fix:** Pick one and apply to both chapters. Recommend keeping the capital "We" (more canon-faithful when verses are concatenated).

**Severity:** Cosmetic. **Recommend fixing for consistency.**

---

### 3.4 — Bacteriopolis "10 hours" (Ch 2) likely fabricated

**The book says** (Ch 2 line 38): *"an autonomous research agent in our Postgres database ran for ten hours, looping on a single topic, until we hit the emergency stop."*

**Workspace journal check:** I grep'd `.spec/journal/` for "10 hour" / "ten hour" — no match. The actual journal at `.spec/journal/2026-05-15-ES-emergency-stop.md` reports the failure as *"DeepSeek churn, a bgworker crash loop, ~230M wasted input tokens."* No hour count.

**Fix:** Soften to *"...looped on a single topic until we hit the emergency stop"* OR replace with the concrete verified figure *"burned 230 million input tokens before we hit the emergency stop."* The 230M-token figure is more striking and verifiable than "ten hours."

**Severity:** Unverified claim presented as concrete fact. **Recommend fixing.**

---

### 3.5 — Section III "11-step walk-through" promise vs delivery

**Finding (in-house editor):** The 11-step reference page ends with *"the rest of this book is the walk through them."* But several scripture-only steps don't get explicit chapter treatment:
- Step 5 (Line upon Line) — absent
- Step 8 (Atonement) — Ch 10 is Atonement-adjacent but not named as Step 8
- Step 9 (Sabbath) — touched but no chapter
- Step 10 (Consecration) — blended with Ch 11 (Zion)

**Move (recommend):** Soften the promise on the reference page from *"the rest of this book is the walk through them"* to *"this book threads through them"* or *"this book lights up these eleven step-by-step."* Cheap honesty.

**Severity:** Low. The book delivers more than it admits. **Recommend tightening the language.**

---

## TIER 4 — Carry-Forward Items (worth a council decision, not blocking)

### 4.1 — Does the book need a foreword?

A short foreword by someone respected in the LDS-tech intersection (Brad Wilcox, Adam Miller, a tech-aware LDS scholar) would add credibility for skeptical-engineer readers. Bold & Italic Editing notes that forewords add credibility for debut authors. **Future move, not structural.** [Source: 05-editing-research.md § 11 Q2]

### 4.2 — Audiobook front matter

If the book ships as audiobook (per `book.yaml` `audio_generation: optimize_for_tts: true`), the print front matter may need to be even leaner for audio. Method Writing's standard advice: *"Acknowledgements, copyright, anything that stands in the way of diving in... cut!"* Print + audio may need slightly different openings. [Source: 05-editing-research.md § 11 Q3]

### 4.3 — Webster 1828 quote re-verification

Ch 0 and Ch 1 cite Webster's 1828 *spirit* and *intelligence* entries. These were verified in the May 26 audit but worth one more cross-check via `mcp__webster__webster_define` before publish.

### 4.4 — External URL archival

Ch 1's Trejo (Medium) and Jovanović (LinkedIn) URLs should be web.archive.org-snapshotted before publish, since both are volatile sources.

### 4.5 — Chapter 6 + 7 transition bridging

Ch 6 ends on covenant-document commitments; Ch 7 jumps into Ballard's "one-cylinder ward" cold. A single bridging sentence — *"Covenant gives us the binding; stewardship gives us the scaling"* — would smooth the transition. Low priority.

### 4.6 — Chapter-to-step annotations

If the 11-step framework is load-bearing for the book, each chapter could declare which step(s) it walks. Either in a one-line frontmatter ("This chapter walks Step 4: Specification") or via inline reference. Cheap. Helpful.

### 4.7 — Glossary scope expansion

Beyond Tier 2.1's plain-English additions, the glossary could also add: *Hardening, Sabbath, Atonement, Stewardship Grant, Council Moment* — all of which appear in body text.

### 4.8 — Dedication

The book has no dedication. Common in this genre. Worth asking whether Michael wants one (to family / to AI agents / to the council / to readers).

---

## What the alt-readers said about which chapter to read first

| Pass | "Read first" chapter | Why |
|------|---------------------|-----|
| Gospel reader | **Ch 5 — Intelligence Cleaveth** | Universal application (marriage, prayer, parenting, AI). Shortest doctrinal chapter. *"Coldness is not accuracy"* is the most quotable line outside Ch 1. |
| Engineer reader | **Ch 6 — Bilateral Covenant** | Describes a real practice (covenant.yaml). Production-note dogfoods the methodology. Earns the doctrinal frame by demonstrating it. |
| In-house | (no single pick) | The book is intentionally in cover-to-cover order. |

**Carry-forward decision:** if Michael ever produces marketing material (excerpts, sample chapters, podcast notes), **Ch 5** and **Ch 6** are the strongest two pieces to lead with.

---

## What the alt-readers said is the book's biggest contribution

- Gospel reader: **Ch 7's Matthew 10 sequence — Authority → Scope → Capacity → Identity.** "The best original doctrinal contribution of the book." "I have never heard anyone sequence Christ's commissioning of the Twelve like this." Belongs in a conference talk or Ensign article.
- Engineer reader: **Ch 6's bilateral covenant pattern + the production-note witness.** "Workflow theology grounded in the author's own production practice." Honestly disclosed dogfooding.
- Editing research: **The modular study form itself.** The book sits inside the Marcus Aurelius / Eugene Peterson / Walter Brueggemann lineage where the form *is* part of the argument.

All three views agree the book has a real and original contribution. They differ on which chapter carries it most.

---

## What the alt-readers said is the book's weakest chapter

- Gospel reader: **Ch 9** (Hope and the Veil) — *"the doctrine is gorgeous; the engineering parallel drops Docker, Terraform, and Kubernetes in three paragraphs."* Skip the engineering section; read the doctrine.
- Engineer reader: **Ch 8** (Mechanics of Refinement) — *"the engineering parallel is only nine lines long and three of those lines contain misused ML vocabulary."*
- In-house: **Ch 8 and Ch 10** — the heaviest doctrinal load with the most strained parallels.

Convergence: Section III (Ch 8-11) has the most cleanup ahead. Section I (Ch 1-4) is in good shape.

---

## Convergence map — what every pass agreed on

| Item | In-house | Gospel reader | Engineer reader | Editing research | Verified |
|------|:---:|:---:|:---:|:---:|:---:|
| Front-loading problem | ✅ | ✅ | (n/a) | ✅ | (n/a) |
| 3.5-year journey misplaced | ✅ | ✅ | (n/a) | ✅ | (n/a) |
| Ch 6 production-note = credibility anchor | ✅ | ✅ | ✅ | (n/a) | (n/a) |
| Ch 10 parallel is strained | ✅ | ✅ | ✅ | (n/a) | (n/a) |
| "AI has no soul" boundary too implicit | ✅ | ✅ | ✅ | ✅ | (n/a) |
| Ch 8/9/10 weaker than Ch 1/3/4/6/7 | ✅ | ✅ | ✅ | (n/a) | (n/a) |
| Moses 7:68 framing wrong | ✅ | ✅ | (n/a) | (n/a) | ✅ |
| Oaks/Bednar attribution missing | ✅ | (n/a) | (n/a) | (n/a) | ✅ |
| D&C 131:7-8 capitalization | ✅ | (n/a) | (n/a) | (n/a) | ✅ |
| Bacteriopolis "10 hours" unverified | ✅ | (n/a) | (n/a) | (n/a) | ✅ |
| Ch 5 = most quotable | ✅ | ✅ | (n/a) | (n/a) | (n/a) |
| Ch 7 Matt 10 sequence = best contribution | (n/a) | ✅ | ✅ | (n/a) | (n/a) |

---

## Files in this audit

| File | Purpose | Lines |
|------|---------|------:|
| `00-COUNCIL.md` | **This document** — synthesis of all six passes | ~700 |
| `01-editor-pass.md` | In-house Claude Opus 4.7 editor audit | ~270 |
| `02-frontmatter-weaving.md` | Five options for the 5-chapter-zero problem | ~150 |
| `03-gospel-reader-pass.md` | Faithful Latter-day Saint reader perspective | ~390 |
| `04-ai-reader-pass.md` | Skeptical senior engineer perspective | ~370 |
| `05-editing-research.md` | Web research on crossover non-fiction editing | ~550 |
| `06-fact-check-results.md` | Verified scripture facts (30+ verses) | ~165 |
| `07-multi-model-brainstorm.md` | Four pg-ai-stewards brainstorm-lens pipelines (kimi + qwen) | ~310 |

**Total audit work:** ~2,900 lines across eight files. Council-ready.

---

## Recommended ratification order

When Michael returns, the AskUserQuestion flow:

1. **RQ1** — 3.5-year journey placement (Tier 1.1)
2. **RQ2** — production note prominence (Tier 1.2)
3. **RQ3** — Ch 10 parallel replacement (Tier 1.3)
4. **RQ4** — "type-and-shadow" paragraph location (Tier 1.4)
5. **RQ5** — engineering parallel surgery scope (Tier 1.5)
6. **RQ6** — Section II label/structure (Tier 1.6)
7. **Tier 2 batch** — ratify Tier 2.1-2.6 (low-cost, high-value items). Tier 2.7 (training-data ethics) separately given theological weight.
8. **Tier 3 batch** — ratify all five factual fixes (none controversial, all small).
9. **Tier 4 batch** — defer most; pull forward 4.5 (Ch 6→7 transition) and 4.3 (Webster re-verify) into the same pass.

After ratification, execute in order: Tier 3 (small wins) → Tier 2 (small wins) → Tier 1 (structural moves). The structural moves benefit from happening last so they integrate the small wins rather than colliding with them.

---

## One closing observation

The book is more honest than the audit makes it look. Three independent passes, on three different question-types (doctrine, engineering, editorial craft), with three different posture-of-reading personas, converge on the same small set of fixes. That convergence is a signal of structural soundness — *the book has a real shape that holds up under different lights.* The fixes are restructuring, not rebuilding.

The strongest evidence for this is what the alt-readers wrote unsolicited at the end of their passes:

> *"It just needs three small bridges to land for more people."* — gospel reader [03-gospel-reader-pass.md final line]

> *"The workflow theology (covenant, stewardship, watching) is already there; the substance theology is one rewrite away."* — engineer reader [04-ai-reader-pass.md closing note]

The book lands. The audit shows where the landing can be cleaner.

---

*— Claude Opus 4.7, council document complete 2026-05-28 evening / 2026-05-29 early morning*
