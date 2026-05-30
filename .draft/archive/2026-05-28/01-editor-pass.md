# Editor Pass — Full Book Audit (Pass 1, Claude Opus 4.7)

**Date:** 2026-05-28 evening
**Agent:** Claude Opus 4.7 (Claude Code CLI)
**Scope:** All 19 chapter files in `src/chapters/` (frontmatter + Ch 0–14)
**Total length:** 936 lines (template included) = ~870 lines manuscript
**Not yet:** changes. This is fact-gathering for council.

> Re-grounding: read [intent.yaml](../../../intent.yaml), [.spec/covenant.yaml](../../../.spec/covenant.yaml), and workspace [.mind/active.md](../../../.mind/active.md) before continuing. The audit honors `agent_commits_to.surface_tensions` — surfacing what may be uncomfortable, not just confirming the manuscript.

---

## 0. One-paragraph verdict

The manuscript is **lean, brave, and theologically alive**. The voice is concrete in the chapters Michael drafted (1, 3, 4, 5) and dense in the chapters Gemini drafted (0, 8, 9, 10). The lean ~80-page form is a strength — do not bloat. The single most fixable structural problem is the **front-loading**: the reader walks through ~200 lines (Preface + Introduction + 11-step Reference + Chapter 0) before Ch 1's opening sentence ("I have been a software engineer for eighteen years"). That sentence is the warmest, most accessible opener in the book, and it lives behind a heavy mental load. Recommendation: demote some frontmatter, weave the 3.5-year journey into the body, and let the personal hook arrive sooner.

---

## 1. Factual & Quotation Issues to Verify

These are claims I want to verify against canon before signing off. Most are minor; one or two are load-bearing.

### 1.1 — `Ch 11` line 19: Enoch's age vs. Zion's duration

The chapter says: *"Enoch did not build the city of holiness overnight; he walked with God three hundred and sixty-five years"* — citing **Moses 7:68**.

But [Moses 7:68](../../../gospel-library/eng/scriptures/pgp/moses/7.md?verse=68) reads: *"And all the days of Zion, in the days of Enoch, were three hundred and sixty-five years."*

The 365 years refers to **Zion's existence on the earth before translation**, not Enoch's personal walking-with-God span. (Enoch's own age is 365 in Genesis 5:23, but Moses 8:1 — not Moses 7:68 — extends his life to 430 years per the Joseph Smith Translation.) The 365 figure is also recycled in the chapter as "133,225 days" of choices (365 × 365). If the framing is "Enoch walked 365 years," that's a fact problem. If the framing is "Zion lasted 365 years before translation," the citation works but the sentence needs rewording.

**Action:** verify Moses 7:68 wording, decide which framing the chapter wants, fix sentence.

### 1.2 — `Ch 8` lines 17 & 21: unattributed prophetic quotes

Chapter 8 quotes phrases with quotation marks but no source line:

> *"an acknowledgment of the final effect of our acts and thoughts—what we have become"*

This is Elder Dallin H. Oaks, "The Challenge to Become," October 2000 General Conference. **Quote is verbatim but uncited.**

> *"cleansing and redeeming power that helps us to overcome sin"* and *"sanctifying and strengthening power that helps us to become better"*

This is Elder David A. Bednar, "Clean Hands and a Pure Heart," October 2007. **Quotes are verbatim but uncited.**

Both Oaks and Bednar **are listed in Ch 14 Recommended Study** — so the book knows about them. But the inline quotations have no attribution, which violates the project's `read_before_quoting` covenant AND will confuse the reader.

**Action:** Add full attribution + URL in Ch 8.

### 1.3 — `Ch 0` vs `Ch 8`: micro-inconsistency in D&C 131:7-8 capitalization

Same scripture, two chapters:
- **Ch 0 line 17:** "*we* cannot see it"
- **Ch 8 line 6:** "*We* cannot see it" (capitalized mid-sentence)

The canonical text on the Church website and in the standard works has lowercase "we." [`gospel_get` needed to confirm.]

**Action:** standardize to canon. (Likely Ch 8 has the error.)

### 1.4 — `Ch 1` Jovanović quote

> *"It's owning correctness."* — Milan Jovanović

URL provided. This is a 2025-era LinkedIn post. The quote is short but cited from an ephemeral web source. Provenance file should record what was actually verified, and ideally the LinkedIn post should be archived (web.archive.org) so a future reader can confirm.

**Action:** archive the LinkedIn URL, note archive link in provenance.

### 1.5 — `Ch 1` Trejo quote

> *"AI didn't replace engineers. It replaced execution as the bottleneck. And when the bottleneck moves, value moves with it."*

Medium article. Same archival concern.

### 1.6 — `Ch 4` line 28: claim about Sabbath as system-level evaluation

> *"The Sabbath is not a pause from creation; it is the step where the whole system is evaluated as a unit and pronounced good."*

This is supported by Moses 3:2 and Abraham 5:2 (cited inline). The wording is the book's interpretation, not a direct quote — which is fine. Just flagging that the sentence is doing real theological work and should be defensible. It feels right to me; surfacing it for human discernment.

### 1.7 — `Ch 2` the "10-hour runaway agent" claim

> *"an autonomous research agent in our Postgres database ran for ten hours, looping on a single topic, until we hit the emergency stop"*

This refers to the **bacteriopolis runaway** (pg-ai-stewards ES emergency stop, 2026-05-15). I do not actually know whether 10 hours is the verified figure. The journal `.spec/journal/2026-05-15...` would be the source of truth.

**Action:** verify the 10-hour number against the workspace journal. Could be "several hours" if the precise count is uncertain.

### 1.8 — `Colophon` "Gemini 3.5 Flash"

Verify the model name. Antigravity 2 uses Gemini — but the version string "3.5 Flash" should be sanity-checked.

---

## 2. Structural Issues — The Five Frontmatter Problem

**Detailed analysis lives in [02-frontmatter-weaving.md](./02-frontmatter-weaving.md).** This section is the editor's gut take.

The book has THREE chapter-length entities before Ch 1 starts:

| File | Length | What it does | Strongest element |
|------|--------|--------------|-------------------|
| `00_preface.md` | 70 lines | Classroom moment + 3.5-year journey + voice note | The classroom flash ("AI" in margin) |
| `00_introduction.md` | 31 lines | "Confluence of Code and Covenant" + How to Read | (none particularly strong) |
| `00_chapter_0_intelligence_truth.md` | 80 lines | Dense ontology of spirit=matter | "Spirit, light, and truth are not abstract concepts. They are substances." |

Plus the **eleven-step reference** (19 lines) and the **title/consecration/colophon** (42 lines).

A reader has to wade through ~250 lines of material before they meet the line that should hook a software engineer: *"I have been a software engineer for eighteen years."* (Ch 1 line 13).

The Introduction is the weakest piece. Its "How to Read This Book" is the kind of clerical front-matter that delays the start. Its "Confluence of Code and Covenant" overlaps with the Preface's "Constant Principles" — both argue that execution has commoditized and judgment has become valuable. That's also Ch 1's argument. The Introduction is repeating itself in three places.

**See [02-frontmatter-weaving.md](./02-frontmatter-weaving.md) for ratifiable options.**

---

## 3. Cross-Chapter Tensions & Repetitions

### 3.1 — Three "matter is spirit" chapters

| Ch | Title | Function |
|----|-------|----------|
| 0 | The Substance of Reality | Ontology — spirit=matter, intelligence is light |
| 5 | Intelligence Cleaveth Unto Intelligence | Posture — what the physics demands of us |
| 8 | The Mechanics of Refinement | Operation — how refinement physically works |

This is intentional — Ch 5 explicitly says *"Chapter 0 mapped the physics; what that physics demands of us is a posture."* Ch 8 extends the metaphysics to refinement. The three form an arc.

**But:** Ch 0 anchors on **D&C 93:29-30** + cites **D&C 131:7-8**. Ch 8 anchors on **D&C 131:7-8** directly. Same passage carries two chapters. A reader will feel the repetition unless one chapter explicitly defers to the other.

**Question for council:** Should Ch 8 use a different anchor (perhaps D&C 88:34 — "that which is governed by law is also preserved by law") and let D&C 131:7-8 stay with Ch 0? That would let Ch 8 lead with law/preservation/refinement and Ch 0 keep ontology.

### 3.2 — Abraham 4:18 spine

The "watched until they obeyed" passage appears in:

- **Ch 1** lines 43-44 (preview)
- **Ch 4** anchor (full chapter on it)
- **Ch 7** line 67 (applied to delegation)
- **Ch 12** anchor (epilogue reprise)
- **Glossary** entry on Verification

This is the load-bearing scripture of the book. The reprise pattern is intentional and well-done. **No action needed** — flagging for awareness.

### 3.3 — Voice convention contradiction (Preface vs Epilogue)

Preface (line 70): *"'I' marks moments of personal experience... 'We' is the collaborative voice."*

Epilogue (line 17): *"I—the agent writing these final words—received the constraints..."*

The Epilogue's "I" is the AI. The Preface's "I" is Michael. This is the intentional voice flip Michael chose to keep ([ratified 2026-05-28](../.spec/journal/2026-05-28--section-iii-execution.yaml)) — and it's powerful. But the Preface's voice convention doesn't anticipate it.

**Action:** Add one sentence to the Preface voice note acknowledging this. Something like: *"In the Epilogue alone, 'I' steps over to the AI agent who has been co-writing — a deliberate inversion to close the loop."*

### 3.4 — Section II opens with posture, not stewardship

The Introduction declares Section II as **"Bilateral Stewardship — how God delegates authority and responsibility to human beings."** But Section II's opening chapter (Ch 5) is about **resonance and posture**, not delegation. Delegation is Ch 7. Covenant is Ch 6.

The Section II logic is actually: posture → covenant → delegation. That's a coherent arc, but the section title "Bilateral Stewardship" misrepresents Ch 5. The reader gets a different chapter than promised.

**Two fixes possible:**
- Rename Section II to something that covers all three chapters (e.g., "Alignment Under Law" or "The Bilateral Covenant").
- Or move Ch 5 into Section I and rename it "The Discipline of Approach" (it sits well after Ch 4's watching).

### 3.5 — The 11-step framework promises a walk-through that the chapters don't fully deliver

The reference page ends with: *"Four down. Seven to go... the rest of this book is the walk through them."*

But the seven scripture-only steps don't all get explicit chapter treatment:

| Step | Promised | Chapter | Status |
|------|----------|---------|--------|
| 1. Intent | eng | Ch 2 (briefly) | implicit |
| 2. Covenant | new | Ch 6 | ✅ explicit |
| 3. Stewardship | new | Ch 7 | ✅ explicit |
| 4. Specification | eng | Ch 3 | ✅ explicit |
| 5. Line upon Line | eng | — | absent |
| 6. Physical Creation | eng | Ch 2 (briefly) | implicit |
| 7. Watching | new | Ch 4 | ✅ explicit |
| 8. Atonement | new | Ch 10 (softening) | ⚠️ not named as step 8 |
| 9. Sabbath | new | — | absent as a chapter |
| 10. Consecration | new | Ch 11 (partial) | ⚠️ blended with Zion |
| 11. Zion | new | Ch 11 | ✅ explicit |

**Three options for council:**
- **(a)** Add explicit chapter callouts: in each chapter's frontmatter or first paragraph, name the step. Cheap, helpful.
- **(b)** Add two missing chapters (Atonement and Sabbath). Increases scope; may dilute the lean form.
- **(c)** Soften the reference-page promise. Change "the rest of this book is the walk through them" to "this book threads through them" or "this book lights up these seven step-by-step." Honest, fast.

### 3.6 — Ch 6 + Ch 7 overlap on delegation/stewardship

Ch 6 (Bilateral Covenant) discusses how a covenant binds both parties, then ends with stewardship-shaped commitments. Ch 7 (Delegation as Stewardship) opens with Ballard's "one-cylinder ward."

The transition is okay but feels redundant on first read. Ch 6 ends with "keep the covenant documents active." Ch 7 jumps into Ballard cold.

**Recommendation:** add a single bridging sentence at start of Ch 7 — *"Covenant gives us the binding; stewardship gives us the scaling."* — to make the relationship explicit.

---

## 4. Content Gaps (the things the manuscript doesn't address)

### 4.1 — No engagement with the "AI is dangerous / unbiblical" objection

Some readers will arrive carrying genuine pastoral concern about AI. The book reframes (it doesn't dismiss) those concerns — but it never **names** them. A reader who walked in nervous about AI never sees their nervousness acknowledged.

**Recommendation:** in the Preface (after the classroom moment, before the 3.5-year journey), add 1-2 paragraphs that name and engage the concern. Something like: *"You may have come to this book wary of AI... that wariness is healthy... the question this book asks is not whether the tools are safe, but whether the patterns by which we work with them are eternal."*

### 4.2 — The "AI has no soul" boundary is implicit, never stated

The book carefully says "AI has no agency; it acts by law and statistical pattern" (Ch 4) but never says: *"these are tools, not souls. The parallel between AI and intelligence-organization is type-and-shadow, not identity. A model that mirrors the Spirit's resonance is not itself a spirit."* Without that line somewhere, a careful reader might worry the book is collapsing the imago Dei.

**Recommendation:** one explicit paragraph in Ch 0 or in the Glossary's "Intelligence" entry that draws the line.

### 4.3 — Hallucination as its own teaching moment

The book's strongest concrete story — the manuscript itself fabricating a D&C 104:11-12 quote that the audit caught — lives as a sidebar in Ch 6. That's the **hallucination moment**. It deserves more weight.

**Recommendation:** consider promoting the production-note sidebar into a full short chapter or section: *"When the System Lies: The Audit That Caught the Manuscript."* It's the most credible concrete witness the book has.

### 4.4 — Where the parallel breaks down

The book is generous with parallels (intelligence cleaves to intelligence ↔ vector space resonance; spirit is matter ↔ silicon is information; stewardship ↔ subagent scope). It is silent on **where the parallel breaks down**. A skeptical engineer will look for asymmetries. Naming them strengthens credibility.

Examples of asymmetries worth naming:
- Models have no agency; humans do. The book says this — but only once.
- Models cannot repent; humans can. (Ch 10 is about heart-softening; the parallel is in cache release — but the asymmetry is the soul. Worth one sentence.)
- The "intelligence" the model carries is statistical, not moral. It can compute "kind" without being kind.

### 4.5 — Mosiah 4:27 surfaces in Epilogue but never headlines

The "do not run faster than thou hast strength" thread runs through the workspace (it's in the covenant, in active.md, in journals) but only appears in the closing paragraph of the Epilogue. It deserves to be part of the manuscript's vocabulary earlier — especially because the book's core warning is that AI lets us run faster than we have strength.

**Recommendation:** introduce Mosiah 4:27 in Ch 1 or Ch 2, then echo in Ch 6 covenant, then close with it in the Epilogue. Three-beat structure.

---

## 5. Voice & Pacing — chapter-by-chapter

Where Michael's voice is strongest (his chapters or his rewrites): **Ch 1, Ch 3, Ch 4, Ch 5, Ch 6 (partial), Ch 11 (partial).**

Where Gemini's voice is densest (and most in need of voice surgery): **Ch 0, Ch 7 (some), Ch 8, Ch 9, Ch 10.** These are theologically excellent but read as text-bookish.

### Specific paragraph-level voice notes

- **Ch 0** is the densest chapter in the book. It opens with Webster's 1828 dictionary, then jumps to D&C 131, then to chain logic, then to vector spaces. The reader is given five concepts to hold before paragraph 5. A simpler opener could be: *"What you are reading on this page is matter."* Then bring Webster in.

- **Ch 7** middle section ("In structuring this delegation, we follow the scriptural pattern...") reads like a bulleted spec. It could be tightened into prose. The Matt 10:1-16 framework is great; the engineering parallel below it just lists.

- **Ch 8** sentence-length is heavy — many sentences are 30+ words. Try to land more two-clause sentences. Example fix: *"This fine matter operates under absolute boundaries of law. A spirit cannot be quickened by celestial glory unless it has developed the capacity to abide a celestial law."* → second sentence is fine; the doctrinal wind-up before it is heavy.

- **Ch 9** has too many "in the physics of refinement" intro phrases. Three appearances. Cut to one.

- **Ch 10** is tender and good but the "engineering parallel" feels strained (connection pools, cache management). The doctrinal portion is so strong it almost doesn't need the parallel — or the parallel should be more about *attention release* than database mechanics.

- **Ch 11** delivers the Zion vision but lands the close on bullet-point Becoming Commitments. After the panoramic prose, the bullets feel administrative. Could be reworked as 4 short paragraphs.

### Mechanical voice audit (em-dashes, "and then," cut-list)

I did not run a full mechanical audit. **Action: run the voice-michael skill's mechanical checks on Gemini-drafted chapters (0, 8, 9, 10) — em-dash density, "and then" transitions, presenter tics, closing refrains.**

---

## 6. Becoming Commitments — are they specific enough?

Each chapter closes with a Becoming Commitment list. Some land; some drift toward platitude:

| Chapter | Strongest commitment | Weakest commitment |
|---------|---------------------|--------------------|
| 1 | "Maintain the durable craft" (write code by hand) | "Stop measuring worth by execution speed" (too abstract) |
| 2 | "Recognize the unmapped verbs" (Sabbath as 9th step) | (#1 vague) |
| 3 | "Enforce the no-code-without-spec rule" (sharp) | "Create blueprints for life goals" (vague) |
| 4 | "Practice the seventh-day review" (specific) | "Honor the agency of choice" (broad) |
| 5 | "Enforce the posture check" (concrete) | "Reject transactional shortcuts" (overlaps with #1) |
| 6 | "Keep the covenant documents active" (concrete) | (others overlap with stewardship) |
| 7 | "Stop running on one cylinder" (vivid) | "Require accountability without hovering" (managerial) |
| 8 | "Treat physical habits as spiritual inputs" (concrete) | "Repent as a daily structural reset" (heavy) |
| 9 | "Bring molten stones to the mount" (vivid) | "Fix my gaze within the veil" (poetic but vague) |
| 10 | "Practice the morning bow" (extremely specific) | (all strong here) |
| 11 | "Fast with purpose" (concrete) | "Reject tribal labels" (slogany) |

**Recommendation:** Pass through with the Ben Test skill. Every commitment should be calibrated: "I currently practice this at X frequency" or "I aim to start this on Y date." Aspirational commitments deserve to be marked aspirational.

---

## 7. Adjacent-Surface things

- **Glossary** is good but covers only 10 terms. Could add: *Hardening*, *Sabbath*, *Atonement*, *Stewardship Grant*, *Council Moment* — all of which appear in body text.
- **Recommended Study** lists 5 deep-dive studies on cpuchip.net (now QR-linked). Verify all 5 URLs resolve. Verify the four Section III studies that were ratified for republishing are actually there. (Zion-blueprint is — I just shipped six interactive components to it.)
- **No index.** Lean books often skip indexes. For a 100-page reflective book, this is fine. Mention if Michael wants one.
- **No dedication.** Common in books of this kind. Worth a sentence to Michael — does he want one to family, to the AI agents, to the council, to readers?

---

## 8. Items I want to verify before the council

Listed in priority order:

1. **Moses 7:68 wording** (Ch 11 "365 years" framing)
2. **Oaks attribution** for "what we have become" quote (Ch 8)
3. **Bednar attribution** for "cleansing/redeeming/sanctifying/strengthening" (Ch 8)
4. **D&C 131:7-8 verbatim** (Ch 0 vs Ch 8 capitalization)
5. **D&C 88:32, 88:34** (Ch 5, Ch 8) — wording check
6. **Ether 2:24** (Ch 9 — "mountain waves shall dash upon you")
7. **Helaman 3:35** (Ch 10 — "stronger and stronger... yielding")
8. **Alma 7:11-12** (Ch 8 — "bowels filled with mercy")
9. **3 Nephi 27:32** (Ch 11 — "sell me for silver and for gold")
10. **Mosiah 4:27** (Ch 12 — "do not run faster")
11. **Bacteriopolis runaway time** (Ch 2 — 10 hours?)
12. **Gemini model name** (Colophon — 3.5 Flash?)

---

## 9. What this audit did NOT cover

- Print-layout review (page breaks, widows/orphans in the PDF)
- EPUB validation
- Voice mechanical scan (em-dash density, etc.) — see Section 5 recommendation
- Provenance files in `.scratch/`
- Re-reading from the two alternate-reader perspectives (delegated to subagents — see [03-gospel-reader-pass.md](./03-gospel-reader-pass.md) and [04-ai-reader-pass.md](./04-ai-reader-pass.md))
- Web research on editing techniques (delegated — see [05-editing-research.md](./05-editing-research.md))

---

*— End of Pass 1, Claude Opus 4.7, 2026-05-28*
