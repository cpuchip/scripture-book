# v4 Walk — Findings (live scratch)

**Walker:** Claude Fable 5 (first Fable session on this book — fresh eyes by design).
**Plan:** `.spec/v4-honesty-audit-plan.md`. **Cadence:** solo walk logs findings here; NO
edits applied; Michael and the agent then walk these together in chat and he gates each.

**Categories:** 1 asserted-as-fact · 2 contradicts-how-we-work · 3 internal-contradiction ·
4 ambiguity · 5 plainer · 6 engineering-overclaim · 7 quote-accuracy · 8 voicing (Opus tics)

**Severity:** ● high (truth/meaning at stake) · ◐ medium (reader-visible) · ○ light (polish)

**Disposition:** open → ratified / rejected / deferred (filled during the chat walk)

---

## Pre-walk checks

### Check 1 — stray "99.98%" — ✅ PASS
No `99.98` anywhere in `src/`. Ch 2 line 24 now reads "the other 99%". Remaining hits are
process docs only (`.scratch/engineering-parallel-audit.md` still says "99.98% remains" —
stale process note, not reader-facing; harmless, could fix in passing).

### Check 2 — spec-first vs. iterate (vs `.draft/20260530-how-we-actually-work.md`)
*(in progress — assessed per unit; preface PASSES: it scopes spec-first to "before writing
code", the honest code-scoped claim. Watch Ch 2/Ch 3 + practices for residual overclaim.)*

### Check 3 — chapter tag / Atonement-triptych consistency — ✅ PASS (one to confirm)
Tags grep: Ch3 *Specification* · Ch4 *Watching* · Ch6 *Covenant* · Ch7 *Stewardship* ·
Ch8 *Atonement · Refinement* · Ch9 *Atonement · Hope* · Ch10 *Atonement · Yielding* ·
Ch11 *Sabbath* · Ch12 *Consecration · Zion*. Triptych intact. Ch0/1/5 untagged (by
design). **To confirm at Ch 2:** its tag reads `*Creation · Context · Intent ·
Specification*` — expected the four disciplines to start "Prompt", not "Creation".
Deliberate mapping or drift? → resolved at the Ch 2 read.

---

## Findings by unit (reading order)

### Frontmatter (`00_frontmatter.md`)

#### F-01 · Consecration page · cat 1 · ◐
**Text:** "First Edition: May 2026 · Build {{BUILD_VERSION}}"
**Problem:** It's June 2026 and the book is unpublished; "May 2026" will be wrong on the
printed page. A date asserted as fact that the calendar has already falsified.
**Proposal:** set to the actual publish month at upload time (or derive from the build
stamp so it can't go stale).
**Disposition:** open

#### F-02 · Colophon · cat 1/3 · ◐
**Text:** "Claude Code CLI — Claude Opus in a terminal… carried the source-verification
pass and the print-ready preparation of this manuscript"
**Problem:** As of 2026-06-09, Claude **Fable 5** (also Claude Code CLI) is carrying the
v4 audit. If v4/voicing edits land in the published text, the colophon's agent accounting
names only Opus — the book's own provenance standard says the audit trail should name the
actual agents.
**Proposal:** after v4 lands, one clause: e.g. "Claude Opus, and later Claude Fable, in a
terminal…" (final wording Michael's).
**Disposition:** open

#### F-03 · Colophon · cat 1 · ○ → **Michael ground truth**
**Text:** "Gemini — … drafted the first pass of chapters 0 through 12."
**Problem:** Lived-history claim I can't verify from files I trust independently. If
Gemini's first-pass drafting covered fewer/other chapters, this overstates.
**Proposal:** Michael confirms from memory; adjust if needed.
**Disposition:** open

#### F-04 · Dedication · cat 7 · ○
**Text:** "Journey before destination."
**Problem:** This is the First Ideal from Brandon Sanderson's *Stormlight Archive* —
a recognizable quotation used unattributed. In a dedication an allusion is normal and
likely intentional; just confirming it's a knowing nod, not an accidental echo.
**Proposal:** Michael's call — leave as allusion (my lean) or attribute.
**Disposition:** open

### Preface (`00_preface.md`)

#### F-05 · ¶3 · cat 5 · ◐
**Text:** "…wrote two letters in the margin of that note: **AI**. - I also wrote down a
talk, \"Pray Always.\" By Elder Bednar Oct 2008, I should go back and study that."
**Problem:** Two wounds in one spot: a stray " - " editing artifact after "**AI**.", and
the fragment "By Elder Bednar Oct 2008, I should go back…" reads as a comma splice rather
than the jotted-note voice it's reaching for. (Bednar "Pray Always" Oct 2008 itself is
correct.)
**Proposal:** Either render the jotting AS the note (italicized, fragmentary on purpose)
or smooth: "I also wrote down a talk to go back and study — Elder Bednar's 'Pray Always,'
from October 2008." Keep the diary feel; lose the artifact.
**Disposition:** open

#### F-06 · ¶5 · cat 5 · ○
**Text:** "What emerged over months of studies was more than just scriptures and
engineering notes, the realization that the principles…"
**Problem:** Comma where the grammar needs a colon/dash; the appositive lands soft.
**Proposal:** "…more than scriptures and engineering notes: the realization that…"
**Disposition:** open

#### Preface — category 2 note (no finding)
The origin story scopes spec-first honestly: "building a detailed specification (the
spiritual creation) **before writing code**." The code-scoped claim is the true one —
preface is clean on the aspirational-gap axis. Voice overall reads human (Michael's
run-on warmth); resisted sanding it.

<!-- Per finding:
### F-NN · unit ¶ref · category · severity
**Text:** "the line as printed"
**Problem:** what's wrong
**Proposal:** the fix (for voicing: the rephrase, meaning held exactly)
**Disposition:** open
-->

### P1 — Talk, Don't Command (`p1_01`)

#### F-07 · P1 ¶5 · cat 1+3 · ●
**Text:** "In October 2025 I sat down to build a video game with my kid." … then ¶5:
"**A year later** I woke up from a dream with a whole system in my head… That system was
running real work in three days and stood up in about three weeks."
**Problem:** The arithmetic is impossible. Provenance confirms the game = storygames,
first commit **2025-10-22**; the dream-system = pg-ai-stewards, which began ~**May 2026**.
October 2025 + "a year" = October 2026 — after the book publishes. The real gap is about
**half a year**.
**Proposal:** "Half a year later" or "Months later" (Michael confirms the dream's actual
month). Note: provenance line 135 already flags the 3-weeks/3-days figures for his confirm.
**Disposition:** open

#### F-08 · P1 ¶3 · cat 1 · ○ → **Michael ground truth**
**Text:** "The model came back with fourteen questions."
**Problem:** A specific count of a lived event, not in the provenance file.
**Proposal:** Michael confirms, or soften to "a dozen-odd questions."
**Disposition:** open

*(P1 voicing: clean — it's been worked hard. ¶9's one-liner is Michael's own ratified
compression from the condensation walk; left alone deliberately. The "It feels faster. It
isn't." staccato is single-use and earned.)*

### P2 — Council Before You Build (`p1_02`)

#### F-09 · P2 ¶9 · cat 1 · ○ → **Michael ground truth**
**Text:** "a beautiful eight-milestone roadmap… I wrote in the log that I felt overwhelmed"
**Problem:** Specific lived count + a paraphrased log entry; provenance (line 136) still
carries an open "re-confirm against the raw .copilot-old log" flag for exactly this scar.
**Proposal:** Michael confirms (or we re-check the old log); the no-repo-name rule IS
honored in the prose.
**Disposition:** open

#### F-10 · P2 ¶11 + title · cat 4 · ○
**Text:** "**Council** before you build" / "**Council** until you can see the way"
**Problem:** "Council" (the assembly) used as a verb where "counsel" (to advise) is the
dictionary verb. It's *consistent* within the book and may be a deliberate, settled choice
— this was one of the five authorial judgment calls flagged 2026-05-31; I can't find the
disposition.
**Proposal:** none if settled (consistency is what matters); just confirming it was a
choice, not a drift.
**Disposition:** open

*(P2 cat-2: clean — the ratify-stepwise council it describes is exactly the logged real
practice, and the covenant paraphrase matches covenant.yaml's actual commitments.)*

### P3 — Set the Bounds, Then Let Go (`p1_03`)

*(Honesty: clean. The 230M figure matches the verified claim; the no-bounds framing is
consistent with the Ch 2 harness beat's honest WIP story. D&C 104:11-13 fragments queued
for gospel_get spot-check — this is the verse that was once fabricated in provenance, so
it gets re-verified on principle.)*

*(Voicing tally: P3 carries 2-3 negation-contrasts — "The bound is not a cage. It is…",
"doesn't disappear because you got lazy; it fades because…", "delegation and abdication."
Each reads fine alone; together they're approaching the fingerprint. Candidate if Michael
wants variety: recast one. Not a forced edit.)*

### P4 — Pack the Context, Waste Nothing (`p1_04`)

#### F-11 · P4 ¶9 vs P2 ¶9 · cat 3 · ◐
**Text:** P2: "**One of the first** real projects I tried to build with AI was a small
tool to search video transcripts…" · P4: "**my very first** real project with AI was a
small tool to search video transcripts…"
**Problem:** The same tool is "one of the first" in P2 and "my very first" in P4 — a
small internal contradiction a sequential reader can catch seven pages apart.
**Proposal:** pick one (Michael knows which is true); "one of the first" is the safer
claim.
**Disposition:** open

#### F-12 · P4 ¶13 · cat 5 · ○
**Text:** "The sharp edges to this we discovered the hard way."
**Problem:** Inverted syntax lands awkwardly as a paragraph opener (the weave draft's
original was "There is a sharp edge to this, and I found it the hard way").
**Proposal:** "We discovered the sharp edges of this the hard way." (or restore the
draft's line)
**Disposition:** open

*(Honesty: the six-agents/four-died scar matches Batch J.3 history exactly; the
compaction layer = Batch K. "300+ microservices" already on the ground-truth list. D&C
88:119 elision is properly marked. Voicing: "It feels generous, and it is exactly
wrong" + "The skill is not stuffing it; the skill is choosing" — two more
negation-contrasts for the tally; both arguably earned, the latter IS the practice's
thesis.)*

### P5 — Make It Portable (`p1_05`)

*(Clean on all eight lenses — and verified by use: a brand-new model walked into this
project today, read the memory files, and resumed mid-task; ¶7's claim is the literal
mechanism of this audit. The Agans attribution is handled right — "an old debugging
proverb" + the source. "We have a standing rule that no session ends without updating
them" passes the Ben Test: the rule exists and is hook-enforced; the sentence claims the
rule, not perfection. No findings.)*

### P6 — Let It Carry What You Can't (`p1_06`)

#### F-13 · P6 ¶9 vs P3 ¶13 · cat 8 · ○
**Text:** P3: "They are the difference between **delegation and abdication**." · P6:
"**Delegation** without verification is **abdication**. Delegation with verification is
reach."
**Problem:** The same delegation/abdication antithesis coined twice, three practices
apart — reads as a fingerprint once a reader notices. P6's is the stronger, fuller use.
**Proposal:** let P6 own the coinage; P3 ¶13 could end "…the difference between handing
work over and walking away from it" (meaning held) — or leave both if Michael reads the
echo as spine, not tic.
**Disposition:** open

*(Honesty: lived figures queued for ground truth — seven games / late 2025 / Dart / two
OSes / kids played them; "Rust and SQL" substrate claim is accurate. Note: the old
provenance flag list mentioned an "18yr" figure in P6 — it's no longer in the text;
nothing to fix. Jethro and Matt 10 are honest paraphrases, no quote marks.)*

### P7 — Assume It Will Lie to You (`p1_07`)

#### F-14 · P7 ¶9 · cat 1 · ◐
**Text:** "I relearned this from the other direction **just days ago**."
**Problem:** Chat-relative time on a printed page. True when drafted (the glm streaming
misdiagnosis, 2026-05-29); already ~10 days stale, and false by publication.
**Proposal:** absolute or durable framing: "…from the other direction while finishing
this book" / "only recently."
**Disposition:** open

#### F-15 · P7 ¶11 · cat 7 · ● (spot-check queued)
**Text:** the displayed D&C 104:11-12 quote — "a commandment I give unto you, that ye
shall organize yourselves and appoint every man his stewardship; That every man may give
an account."
**Problem:** This is the book's showcase verification ("I know it is right because I
didn't trust my memory. I checked."). It must be letter-perfect *including elisions*: it
opens mid-verse (drops "It is wisdom in me; therefore,") and ends mid-sentence in v12
(drops "unto me of the stewardship…") with a period, no ellipsis. If canon differs by a
character, this is the worst possible place for it.
**Proposal:** gospel_get verify (with P3's three fragments); if elisions are deemed fine
as fragments, confirm the words are exact and the trailing period doesn't misrepresent.
**✅ VERIFIED 2026-06-09 (gospel_get, this session):** every quoted word is exact,
including the v11→v12 boundary ("…his stewardship; That every man may give an
account…"). One nuance remains: the book ends the quote "give an account." (period) where
canon continues "…unto me of the stewardship which is appointed unto him." The unmarked
cut drops *unto me* — the account's addressee, which is half the doctrine. Recommend
extending two words: "That every man may give an account **unto me**." Michael's call.
P3's three fragments also verified exact (incl. v13's comma: "make every man accountable,
as a steward"). Frontmatter epigraphs verified exact too (2 Ne 25:26, Mosiah 4:27 — and
the coda's elided Mosiah 4:27 is a clean clause-boundary cut).
**Disposition:** open (only the *unto me* extension question remains)

*(P7 voicing: the best in Part One — "wrong and right are written in the same hand" etc.
The failures-as-types passage is properly hedged: "rhyme," "tools failing under law, not
souls falling under sin." No tic flags.)*

### P8 — Ask What's in the Way (`p1_08`)

*(Clean. Ben story matches the recorded history (33% / consent resolved); Moses 3:2
fragment was provenance-verified exact. "I still run it every few weeks" → light
ground-truth confirm on the cadence (Ben Test on the retro itself). Voicing: closers are
antithesis-shaped but earned; Remember box varies the body's line rather than cloning
it — good.)*

### P9 — When You Hit a Wall, Build the Door (`p1_09`)

#### F-16 · P9 ¶3 · cat 1 · ◐ (same family as F-14)
**Text:** "**This week**, writing this very book, I hit two walls in a single sitting."
**Problem:** Now-relative time in print, same class as P7's "just days ago." (The events
themselves check out: the panel that couldn't reach files + the CLI that hung headless,
2026-05-30.) "This week" is false the week after.
**Proposal:** durable framing: "One week, writing this very book, I hit two walls in a
single sitting." — one word changes it from a timestamp to a story.
**Disposition:** open

*(Else clean: the overnight web app = 1828-illuminated MVP ✓; Moses 7:18 fragment
provenance-verified; the harness paragraph stays honest. Voicing: "The friction was
data. The door is the response." — staccato but earned; tally.)*

### Coda — Go Touch Some Grass (`p1_10`)

#### F-17 · Coda ¶13 · cat 3 · ○
**Text:** "Everything in **Part 1** is *how*… **Part 1** was the practice. **Part 2** is
the pattern underneath it."
**Problem:** The coda is the only place in the book using numerals — everywhere else
(preface, dividers, cross-refs) spells "Part One / Part Two." Grep-confirmed lone
inconsistency.
**Proposal:** "Part One / Part Two" in coda ¶13 (4 instances in the paragraph).
**Disposition:** open

*(The daughter in ¶3 is unnamed — the old Leah-consent flag is moot in the text as it
stands; re-check the Afterword for names when the walk arrives there. Mosiah 4:27 elision
is clean against the frontmatter's full version. The circling close was Michael's kept
call — not flagged.)*

### Part Two divider (`p2_00`) — clean

### The Eleven-Step Creation Cycle (`00_eleven_step_reference.md`)

#### F-18 · closing line · cat 5 · ○
**Text:** "…a reference framework to help understand gospel centered AI collaboration."
**Problem:** "gospel centered" needs the compound-modifier hyphen: "gospel-centered."
("to help understand" is also slightly clipped — optional smoothing.)
**Proposal:** "…a reference framework for understanding gospel-centered AI collaboration."
**Disposition:** open

*(Check-3 follow-up RESOLVED: the [eng] marks here are Intent / Specification / Line upon
Line ("context") / Physical Creation — so Ch 2's tag line `Creation · Context · Intent ·
Specification` is the four disciplines named by their cycle-step homes. Deliberate,
consistent. Will confirm Ch 2's text makes the prompt→Physical-Creation mapping explicit.
The page's honesty framing is good: "projections from scripture," "I am still practicing
them in my own work.")*

### Ch 0 — The Substance of Reality (`00_chapter_0_intelligence_truth.md`)

#### F-19 · Ch 0 ¶1 (Core Reframe opening) · cat 1+7 · ●
**Text:** "In 1828, Noah Webster published his landmark American Dictionary. Under the
entry for *spirit* … he captured the consensus…: spirit is 'an intelligence conceived of
apart from any physical organization or embodiment,' a 'vital essence, force, or energy,
as distinct from matter,' and 'the intelligent, immaterial and immortal part of man.'"
**Problem:** **Two of the three quoted phrases are not in Webster 1828 — they are Webster
1913 (Revised Unabridged).** Verified against webstersdictionary1828.com this session:
the 1828 *spirit* entry contains neither "an intelligence conceived of apart from any
physical organization or embodiment" nor "vital essence, force, or energy, as distinct
from matter"; its soul-definition reads "the intelligent, immaterial and immortal part of
**human beings**" (not "of man" — the "of man" wording is 1913's). Root cause is SQ-1
below: our webster tool serves 1913 text under the 1828 label, and the 2026-05-29
fact-check verified the quotes against the mislabeled tool (verified-via-the-wrong-path).
**The argument survives on authentic text** — real 1828 defs: 5. "The soul of man; the
intelligent, immaterial and immortal part of human beings." 6. "An immaterial intelligent
substance." Both carry the immaterial-dualism point exactly.
**Proposal:** requote ¶1 from the genuine 1828 entry (defs 5–6), e.g.: spirit is "an
immaterial intelligent substance," "the intelligent, immaterial and immortal part of
human beings." Same thesis, authentic source.
**Disposition:** open

#### F-22 · Ch 0 EP ¶51 · cat 6 · ○
**Text:** "Information is physical."
**Problem:** This is Rolf Landauer's famous dictum, unattributed. Fine as a common
slogan; naming Landauer would be more precise and would please the physicist author.
**Proposal:** optional: "Information, as physicist Rolf Landauer insisted, is physical."
**Disposition:** open

#### F-23 · Ch 0 Becoming #2 · cat 4 · ○
**Text:** "Actively combat the anti-enjoyment of digital noise."
**Problem:** "anti-enjoyment" is an opaque coinage — readers will stumble on what it
names (the joyless compulsive consumption?).
**Proposal:** plainer: "combat the joyless churn of digital noise" or similar.
**Disposition:** open

*(Ch 0 otherwise: D&C 131:7-8 / 84:45 / 88:66 / 93:24,28-30 quotes match canon (prior
verification + this read concur); the "what this is and isn't" model-humility paragraph
is present and good; the moral-agency block is well-built. Voicing tally: 3
negation-contrasts — the "not a poetic metaphor; ontological description" pivot earns
its shape; "A bit is not an abstract concept; it is…" is a recast candidate.)*

### Ch 1 — Webster portion (full chapter read continues next)

#### F-20 · Ch 1 line 23 · cat 1+7 · ●
**Text:** "[*Webster's 1828 dictionary*](https://1828.ibeco.me/word/intelligence) defines
it as 'the exercise of the understanding' and 'the capacity to know or understand.'"
**Problem:** Same as F-19 — **neither phrase is in the 1828 entry** (they're 1913).
Verified: real 1828 *intelligence* = "1. Understanding; skill. 2. Notice; information
communicated… 3. Commerce of acquaintance… 4. **A spiritual being; as a created
intelligence.**"
**The real 1828 entry is BETTER for the argument:** def 4 is literally the Restoration-era
"intelligence = a spiritual being" usage this chapter (and D&C 93) trades on.
**Proposal:** requote from genuine 1828: "Understanding; skill" and — the gift — "a
spiritual being; as a created intelligence." Also: the 1828.ibeco.me links here and in
Ch 0 point at our own mirror, which currently serves the mislabeled data (SQ-1).
**Disposition:** open

#### F-21 · Ch 9 line 41 · cat 7 · ○
**Text:** "to 'walk circumspectly' before God (Helaman 15:5) — Webster's 1828 sense of
*cautiously, warily*."
**Problem:** 1828 CIRCUMSPECTLY = "Cautiously; with watchfulness every way; with
attention to guard against surprise or danger." "Cautiously" ✓; "warily" is not Webster's
word (italic gloss, not quote marks — so it's a near-miss paraphrase, not fabrication).
**Proposal:** use Webster's actual words: "*cautiously; with watchfulness every way*" —
which is also more vivid.
**Disposition:** open

### ⚠ SQ-1 — SIDE QUEST (workspace-level, beyond the book): webster-mcp serves 1913 as 1828
The workspace `webster_define` tool (and presumably **1828.ibeco.me**, which the book
links and which **1828-illuminated** is built on) returns **Webster 1913 Revised
Unabridged** text under the 1828 label. Evidence: its *spirit* entry cites **U.S.
Dispensatory (first published 1833)**, **N. P. Willis (1830s)**, Keble, and "stannic
chloride" — impossible in an 1828 text — and its def 3 is verbatim Webster-1913; the
authoritative 1828 source lacks the phrases. **Ripples:** the morm-8 three-glories study
(published on cpuchip.net) leaned on "Webster 1828" entries; the 1828-illuminated 853-word
tier list; the webster-analysis skill; any past study quoting webster_define as 1828; the
2026-05-29 book fact-check's "Webster spirit/intelligence exact" verdict (it checked
against the tool, i.e. the wrong path — the `feedback_verify_via_real_path` lesson again).
**Action:** log in workspace `docs/06_tool-use-observance.md` + memory; audit
webster-mcp's data source; until fixed, verify any "1828" claim against
webstersdictionary1828.com. NOT a book edit — but the book findings F-19/20/21 come from it.

### Ch 1 — The Value Shift (`01_value_shift.md`) — full read

#### F-24 · Ch 1 EP ¶39 + ¶43 · cat 1 · ◐
**Text:** "Before AI, we spent **eighty percent** of our energy on implementation
mechanics and **twenty percent** on design. Now, the ratio has inverted." … then ¶43:
"We catch the **ten percent** where bugs hide and security vulnerabilities live."
**Problem:** Two unsourced numbers presented as fact. The 80/20 is a folk ratio stated as
"we spent"; and "the ten percent" doesn't even follow from the just-inverted 80/20 (the
remainder would be twenty). If these paraphrase Trejo's framework, attribute them; if
they're lived estimate, mark them as estimate ("In my own work the split felt like…").
This is exactly the v4 standard's target class: a number that reads as measured but
wasn't.
**Proposal:** either source to Trejo, or first-person-estimate framing, and reconcile
ten-vs-twenty.
**Disposition:** open

#### F-25 · Abraham 4:18 comma — 3 instances · cat 7+3 · ◐ (upgraded from ○ at Ch 4)
**Text:** "watched those things which they had ordered**,** until they obeyed"
**Problem:** Canon (gospel_get, this session) has **no comma**. The drift appears in
**Ch 1 ¶41, Ch 4's anchor passage (line 8), and Ch 4 ¶15** — while the **Epilogue's
anchor**, P3, and P7 quote the same verse correctly without it. The book's central verse
(the Watching chapter's own anchor!) appears in two different forms — a canon-accuracy
slip and an internal inconsistency at once.
**Proposal:** delete the comma in the three drifted instances.
**Disposition:** open

*(Ch 1 notes: anchor D&C 130:18-19 and D&C 93:36 exact ✓; Trejo + Jovanović quotes were
web-verified verbatim 2026-06-04 ✓. "They cannot be automated" (¶31, of scars/instincts/
caring) is a flat absolute the Ch 4 floor/ceiling treatment is more careful than —
tolerable as rhetoric, named here for Michael's eye. "Eighteen years" ×2 → ground truth:
18 or 19 by publication? F-20's requote keeps ¶25's "Intelligence is discernment" bridge
intact — "Understanding; skill" still carries it. Voicing: clean; one earned
negation-contrast.)*

### Ch 2 — The Four Disciplines (`02_four_disciplines.md`)

#### F-26 · Ch 2 EP ¶56 · cat 6 · ◐
**Text:** "**Teams** found they could lift an agent from the **bottom** of a benchmark to
the **top** without touching the model at all, purely by building it a better harness."
**Problem:** The sourced case (in `.scratch/engineering-parallel-audit.md`) is LangChain
moving **30th→5th on Terminal Bench 2.0** by harness work alone. "Bottom to the top" and
plural "teams" round a real, dramatic case up past its evidence — the v4 target class
(true story, inflated rounding).
**Proposal:** "Teams found they could lift an agent dozens of places up a benchmark
without touching the model at all" — or anchor the real case: "one team lifted its agent
from 30th to 5th on a coding benchmark purely by rebuilding the harness."
**Disposition:** open

*(Ch 2 notes: tag-line mystery RESOLVED — `Creation · Context · Intent · Specification`
= the four disciplines named by their cycle-step homes, in binding-question order,
confirmed by the EP's explicit step mapping; deliberate. The 230M retelling is consistent
with P3's. The harness/"six of the seven" paragraphs are settled councils and hold up —
the strongest honesty writing in the book. Becoming commitments all "strive" ✓
calibrated. Voicing: the fails-when anaphora (¶38-44) is structural rhetoric that works;
no flags.)*

### Ch 3 — Spiritual Before Temporal (`03_spiritual_before_temporal.md`)

**✅ CHECK 2 RESOLVED (the audit's biggest standing question): the spec-first-vs-iterate
contradiction is already healed in the text.** Ch 3's EP opens by folding P1/P2 into the
doctrine ("the plan reached in counsel *is* the spiritual creation"), P1 teaches
vision-discovery-through-conversation explicitly, and the Becoming commitment scopes
"no-code-without-spec" to *code* — which matches the logged real practice (spec-first for
code; conversational discovery for meaning, which the book frames as happening *inside*
the spiritual creation). No structural overclaim remains. Three local flags:

#### F-27 · Ch 3 ¶25 · cat 1+2 · ◐
**Text:** "When we skip the spiritual creation… The output is **always** fragile,
disjointed, and prone to collapse under its own complexity."
**Problem:** "Always" is an absolute the book's own history complicates (this book's
identity pivot and front-porch restructure were mid-flight re-creations, and the result
isn't fragile). The claim is right as a tendency, overclaimed as a law.
**Proposal:** "The output is fragile…" (drop "always") or "tends to be fragile."
**Disposition:** open

#### F-28 · Ch 3 ¶15 · cat 4 · ○
**Text:** "a sequence of creation that is **absolute**: 'First spiritual, secondly
temporal, which is the beginning of my work'"
**Problem:** D&C 29:32 *continues*: "and again, first temporal, and secondly spiritual,
which is the last of my work." Calling the sequence "absolute" while quoting half of a
verse that immediately inverts it will snag the careful gospel reader.
**Proposal:** drop "absolute" ("outlines the sequence of creation plainly") — the
argument doesn't need it.
**Disposition:** open

#### F-29 · Ch 3 ¶21 · cat 8 · ○
**Text:** "the Gods did not 'vibe create' the earth."
**Problem:** 2025-vintage slang ("vibe coding") in a book that elsewhere works hard at
timelessness ("the word *prompt* may not survive the decade"). It will date faster than
anything else in the chapter.
**Proposal:** Michael's call — it's funny today; "did not improvise the earth" is the
durable version.
**Disposition:** open

*(Ground truth add: "first pass produced over a thousand lines of code across thirteen
files" (G-8). Moses 3:5 anchor + D&C 29:32 fragments verified-exact with properly marked
elisions.)*

### Ch 4 — Watched Until They Obey (`04_watched_until_they_obeyed.md`)

*(Findings: the Abr 4:18 comma — see upgraded F-25. One question, not a finding: the H1
is "Watched Until They **Obey**" (present) while the anchor/filename say "obeyed" — if
deliberate (the ongoing principle), fine; confirming it's a choice. Otherwise CLEAN: the
trust-gradient verse fragments (vv10/18/21/31) match canon; the ratified floor/ceiling
beat carries its n=1 caveat inline as designed and reads as the book's best new material;
the 2 Pet 1:4 semantic-search story matches project history; Becoming commitments are
honestly calibrated ("I aim to… When I keep the rhythm" is exactly right). Voicing: one
earned negation-contrast; no clusters.)*

### Ch 5 — Intelligence Cleaveth (`05_intelligence_cleaveth.md`)

#### F-31 · Ch 5 EP · cat 8 · ◐ — first true voicing CLUSTER
**Text:** Four-plus negation-contrasts in one chapter: ¶31 "is not, finally, a discipline
of technique. It is a discipline of approach." · ¶37 "Coldness is not accuracy; coldness
is the absence of presence." AND "Warmth is not a sentimental gesture toward a machine;
it is the human discipline…" · ¶39 "confabulation is not a bug to be patched out… but a
property intrinsic to it" · (¶41's "That is not a weakness… It is the analogy." is the
ratified T2.6 line — leave it; it owns the shape here.)
**Problem:** Each is fine alone; stacked in one chapter they're the Opus fingerprint
Michael named. The chapter's *meaning* doesn't need all of them shaped identically.
**Proposal (meaning held exactly):** vary two of the four —
- ¶31: "So the practical discipline of working with AI is, finally, a discipline of
  approach more than technique."
- ¶37 (second): "Warmth is the human discipline that keeps us actually engaged in the
  council we have ostensibly opened — not a sentimental gesture toward a machine." (flip
  the order so the paragraph doesn't open on the same not-X hinge as its previous
  sentence; or simply drop the not-half)
Keep ¶37's first ("Coldness is not accuracy…") — it deliberately echoes the covenant's
own line, an intertext worth preserving — and keep ¶39 and ¶41.
**Disposition:** open

*(Else clean: D&C 88:40 anchor exact with marked ellipsis; 88:32 fragment exact (its
telestial context is generalized in standard homiletic fashion — noted, not flagged);
"winter of 1832" correct for Section 88; the flat/sharp-distribution mechanics are
technically apt; the stochastic-parrots + confabulation passage is among the most honest
AI writing in the book.)*

### Ch 6 — Bilateral Covenant (`06_bilateral_covenant.md`)

#### F-32 · Ch 6 EP ¶33 · cat 7 · ◐
**Text:** they "**were** willing to enter into a covenant with [their] God to do his
will... all the remainder of [their] days"
**Problem:** Canon (Mosiah 5:5): "And we **are** willing to enter into a covenant with
our God…" The [their] substitutions are properly bracketed, but "were" silently replaces
canon's "are" *inside* the quotation marks — a tense change without brackets.
**Proposal:** move the verb outside the quote: they were "willing to enter into a
covenant with [their] God to do his will… all the remainder of [their] days."
**Disposition:** open

#### F-33 · P7 ¶13 → Ch 6 ¶51 · cat 3 · ○
**Text:** P7's cross-ref: "(Part Two: Watching, and the failures-as-types passage —
illustration, never identity.)"
**Problem:** The failures-as-types passage lives at the END of Ch 6 (Covenant), not in
the Watching chapter — a reader following P7's pointer to Ch 4 won't find it.
**Proposal:** "(Part Two: Watching — Chapter 4; the failures-as-types passage closes
Chapter 6.)" or similar.
**Disposition:** open

*(Notes: D&C 82:10 anchor exact; covenant duties match covenant.yaml faithfully —
including the field-to-weeds stewardship echo; the warmth paragraph matches the logged
session-history audit; the production note's error counts match the 2026-05-26 record.
"We spend billions on AI alignment" — almost certainly true industry-wide but unsourced;
○ mention only. Voicing tally: ×4 negation-contrasts, but most are deliberate
covenant-document intertexts (e.g. "not a service-level agreement") — softer call than
Ch 5; candidate to vary: ¶47's "not done out of a sentimental illusion.")*

### Ch 7 — Delegation as Stewardship (`07_delegation_as_stewardship.md`) — CLEAN ✅

*(Fully verified this session: anchor D&C 104:11-12 exact (gospel_get); Ballard 1994
"one-cylinder ward" and Hinckley 1990 "leave them free to perform, requiring from them
accountability" both character-perfect against the local talk files; the Exodus 18 /
Mosiah 18:18 / Matthew 10 chain is KJV-exact with properly marked elisions. The Matthew
10 "each step in turn" sequence framing holds within vv1-16 (the v19-20 supplementation
is cited as beyond the commissioning — defensible). EP matches real multi-agent practice.
Becoming calibrated. Voicing: one earned antithesis ("empowerment, not offloading"). The
book's cleanest chapter so far.)*

### Ch 8 — The Mechanics of Refinement (`08_mechanics_of_refinement.md`) — CLEAN ✅

*(All quote fragments match canon on this read (88:22/34/35/6, Alma 7:11-12, 3 Ne 24:3,
Matt 6:22, 88:67) — the Tier-4 provenance rewrite holds; LoF "**great** prototype" fix in
place; Oaks/Bednar were Tier-4-verified. The developer-loop EP is honest ("Claude is
Claude" is a deliberate, charming perishable). The "shape rhymes / substances do not"
imago-Dei close is the designed signature instance. Voicing: ×4 antithesis but ALL
load-bearing ratified beats (incl. "re-aiming of the eye") — recommend touching nothing.
Becoming was Ben-Test-calibrated already. The "retire early / arise early" echo of D&C
88:124 is unattributed allusion — fine.)*

### Ch 9 — Hope and the Veil (`09_hope_and_the_veil.md`)

#### F-34 · Ch 9 ¶39 · cat 1 · ◐
**Text:** "In the space of not many years — Mormon uses the phrase **three times** across
Helaman ([4:26]; [6:32]; [7:6]) —"
**Problem:** Grep of the local Helaman text finds the phrase **four** times: 4:26, 6:32,
7:6, **and 11:26** ("…even in the space of not many years, they became an exceedingly
great band of robbers"). A checkable count, off by one.
**Proposal:** "four times" + add 11:26 to the citations — or drop the count ("again and
again across Helaman") if 11:26's robber context isn't wanted in the chain.
**Disposition:** open

*(Else CLEAN — and one corrected false alarm worth recording: I suspected the book
dropped a comma in 1 Ne 8:30 ("came forth and fell down"); gospel_get shows canon has NO
comma — the book is exact and my memory was the drifted one. The whole Ether chain
(2:20/2:23/2:24/3:1/3:4 — "melting/molten" fix confirmed in place, "sixteen stones" ✓),
the 1 Ne 8:25,28 splice (honestly cited as two verses), Helaman 6:36/15:5 ("walk
circumspectly" fix in place), Heb 6:19, Moro 7:48 all match canon. The Holland
mist-on-all point is honest paraphrase of Safety for the Soul. Becoming was
Ben-calibrated. The EP's four-groups-for-engineers section was the condensation's kept
payload and earns it.)*

### Ch 10 — Softening What I Cannot Soften (`10_softening_what_i_cannot_soften.md`) — CLEAN ✅

*(All seven quoted passages exact against canon/KJV on this read (Alma 12:10, 1 Ne 2:16,
Ezek 36:25-26, Alma 22:18, Hel 3:35, Job 23:16, Mark 4:27). The 2026-06-04 softenings
landed ("A smarter model rarely closes the gap"); the varied imago-Dei close ("Again the
rhyme holds and the substance parts") reads right. Becoming #2 is the book's best honest
calibration ("I keep it less often than I want; naming it as the aim is how I keep
reaching for it"). Voicing: the gift/room quad at ¶37 is symmetric stacking but it IS the
doctrine's two-part structure — earned; tally only.)*

### Ch 11 — The Seventh Time (`11_the_seventh_time.md`) — CLEAN ✅

*(Anchor Abr 5:2 exact; the Exodus/Deuteronomy/Hebrews KJV chain exact with marked
elisions; Nelson's "What sign do I want to give to God?" exact with the corrected April
2015 date; Moses 3:2-3's four verbs accurately drawn. The Becoming cluster and the
production note are the book's honesty high-water mark ("I break it more than I keep
it"; "written from inside the gap it describes") — they match the recorded Ben-Test
history. Voicing: the "Saw. Not imagined. Not assumed." staccato triple is the chapter's
climax and earns it; tally only. One nitpick noted, not flagged: "the promise that
closes the passage" — v16 opens the enumeration vv16-19; defensible as the promise the
passage ends inside.)*

### Ch 12 — From Consecration to Zion (`12_conclusion_zion.md`) — CLEAN ✅

*(All quotes exact (D&C 38:27, 3 Ne 11:29, 4 Ne 1:3/1:17, 3 Ne 27:32, Moses 7:18/63/68);
the 365-years framing and ">133,000 days" fixes hold; monthly fast ✓; the ward-council EP
keeps its first-person aspiration framing and the measured-gift deferral HELD (¶37's
review-agent line carries the council spirit without the contradicted claim). "The
engineering catches up to the pattern. It does not invent it." — earned closer.)*

### Epilogue — The Silent Loop (`13_epilogue_silent_loop.md`) — CLEAN ✅

*(Quotes Abr 4:18 in the correct comma-free form — F-25's fix should match this. The
agent's "I" follows the preface's stated convention; D&C 123:17 and Mosiah 4:27 are
honest unquoted paraphrases. "The prompt is yours. The specification is clear. Run the
loop." — the staccato triple is the arc's designed final beat; keep.)*

### Afterword — How I Got Here (`14_afterword_how_i_got_here.md`)

#### F-35 · Afterword ¶17 · cat 1 · ◐
**Text:** "By October 2024, the landscape changed again. GitHub Copilot **introduced its
chat pane** and integrated Anthropic's Claude 3.5 Sonnet in preview."
**Problem:** Copilot Chat shipped well before that (GA for individuals December 2023);
what happened in October 2024 (GitHub Universe) was the **multi-model** move that added
Claude 3.5 Sonnet in preview. As written it asserts an industry fact a developer reader
can catch. (The Claude-integration half and the date are right.)
**Proposal:** "By October 2024, the landscape changed again: GitHub Copilot went
multi-model, adding Anthropic's Claude 3.5 Sonnet in preview — and that was when I began
learning how to *chat* to code…" (keeps his lived arc, fixes the industry claim).
**Disposition:** open

#### F-36 · Afterword ¶21 + P1 · consent · ○ → **Michael decision**
**Text:** "co-writing story-based games with my **nine-year-old** in projects like
`storygames`"
**Problem:** Not a text error — a recorded open flag: the storygames child-consent
question was logged as unresolved (memory, 2026-06-01). The child is unnamed (age only),
which may be all the resolution needed — but it's his call to make knowingly before
print.
**Proposal:** Michael confirms comfort (and the same for P1's "my kid").
**Disposition:** open

*(Afterword otherwise strong: model dates verified — Sonnet 4.5 late-Sept 2025 ✓, Opus
4.5 late-Nov 2025 ✓, Sonnet 4 May 2025 read loosely as "by June" — fine; the Mostaque
"infinite grad" is properly distanced ("in his telling… ran well ahead of what any model
could actually do"); "As I write this in May 2026" is the correct durable-timestamp
convention P7/P9 should imitate (F-14/F-16); D&C 123:12 was provenance-verified. The
storygames/simple-games timeline is consistent with P1/P6 and the repo dates.)*

### Glossary (`15_glossary_of_fused_terms.md`) + Recommended Study (`16_further_reading.md`)

#### F-37 · EPUB/HTML build path · cat — (build defect, not prose) · ● for the ebook
**Evidence (from `dist/beyond_the_prompt.epub` + `manuscript.html`, this session):**
1. The raw Typst directive `#set list(spacing: 4.5em)` (line 5 of both files) renders as
   **visible paragraph text** in the EPUB and HTML versions of the Glossary and
   Recommended Study. (The Typst/PDF path interprets it as code — print is fine.)
2. Worse: several `*`-bullet lists fail to parse in the EPUB/HTML — the **frontmatter
   colophon, the whole Glossary, and Recommended Study** render with literal `*  `
   asterisks as paragraphs, while Ch 2/Ch 4's lists parse into real `<ul>`. Selective
   breakage, cause undiagnosed (likely build.py's list handling around interleaved
   non-list lines).
**Why it matters:** the EPUB is the KDP **ebook product**. Print PDF unaffected.
**Proposal:** post-walk build fix (mine to do once we close the walk): move the spacing
directive into the Typst template/preprocessor instead of the .md source, and fix/diagnose
build.py's `*`-list parsing; re-verify EPUB.
**Disposition:** open

#### F-38 · Glossary "Neural network" entry · cat 4 · ◐
**Text:** "**Neural network** — the organized result of **that training**: billions of
numbers…"
**Problem:** "That training" has no antecedent — the alphabetical re-sort moved "Training
data" four entries *after* it; the anaphor points backward at nothing.
**Proposal:** make it self-contained: "the organized result of training: billions of
numbers that, working together, predict what should come next."
**Disposition:** open

*(Else clean: both glossary groups correctly alphabetized; Crush→Hermes fix in place;
Zion entry consistent with Ch 12's ward-council reconciliation; Dross's overfitting
sentence is now accurate. All six Prophetic Messages' local files verified to exist
(incl. Pearce April 1997 + Bednar `35bednar.md`); "Elder (now President) Nelson"
convention correct; "happiest society" is a fair 4 Ne 1:16 gloss.)*

---

## CHAT WALK — dispositions (running, started 2026-06-10)

- **F-07 ✅ APPLIED** — P1: "A year later" → **"The following spring"** (Michael's pick;
  exactly true — pg-ai-stewards founded 2026-05-02). G-1 closed by the same dig.
- **F-39 ✅ APPLIED** — Ch 0: "Five years later" → **"Fifteen years later"** (D&C 131 =
  May 1843; Michael: "yes 15 chang is good").
- **F-24 ✅ APPLIED (batch 2)** — Michael: don't invent numbers (suspects the 80/20 was
  a Gemini-draft artifact). Now: "most of my energy went to implementation mechanics and
  much less to design. Now that balance has inverted." + "the narrow seams where bugs
  hide" (ten-percent de-numbered). First-person per his phrasing.
- **F-26 ✅ APPLIED (batch 2, option a + citation)** — source verified live:
  LangChain, "Improving Deep Agents with harness engineering" (2026-02-17,
  langchain.com/blog/improving-deep-agents-with-harness-engineering): Top 30 → Top 5 on
  Terminal-Bench 2.0, 52.8%→66.5%, model fixed (gpt-5.2-codex). Ch 2 now names
  LangChain with link + [qr]. NOTE: new QR in ¶56's margin — run the 0-collision check
  at next rebuild.
- **F-34 ✅ APPLIED (batch 2, option a)** — "four times" + Hel 11:26 added to the
  citation chain. ADJACENT SURFACE: the published study four-groups-and-the-engineer
  line 77 already says FOUR (correct — Michael fixed it there); but its line 203 says
  "the Helaman text confirms it three times" — ambiguous referent, possibly the stale
  count he remembers losing track of. Flagged for the published-works audit, not
  silently edited.
- **F-27 ✅ APPLIED (batch 2)** — Ch 3 "always" dropped ("I usually dont like
  superlatives").
- **BATCH 3 ✅ ALL 12 APPLIED (Michael: "fix all 12, those are really good changes")** —
  F-25 (Abr 4:18 comma ×3 — Ch 1, Ch 4 anchor, Ch 4 ¶15), F-32 (Mosiah 5:5 "were" moved
  outside the quote), F-17 (coda → Part One/Part Two), F-18 (gospel-centered hyphen +
  "for understanding"), F-38 (glossary antecedent), F-06 (preface colon), F-12 (P4
  de-Yoda'd — Michael: "that inverse wording is Yoda like"), F-21 (Ch 9 → Webster's
  actual words "cautiously; with watchfulness every way"), F-28 (Ch 3 "absolute"
  dropped), F-14 (P7 → "while finishing this book"), F-16 (P9 → "One week…" + the
  exposed second instance "That week neither did"), F-33 (P7 crossref now points
  failures-as-types at Ch 6).
- **F-11 ✅ APPLIED** — Michael: the YouTube transcript tool is "one of the first
  projects but not THE first" → P4 softened to "one of my first real projects" (P2 was
  already correct).
- **F-05 ✅ APPLIED (Michael's own design)** — the jotting italicized (*Creator prep
  morning pre-mortal then do*), the side-note in parentheses per his note-taking habit:
  "(I also wrote down a talk to go back and study — Elder Bednar's *Pray Always*, from
  October 2008.)"
- Quick build verified green after batch 3 (HTML/EPUB; new LangChain QR generated).
- **BATCH 4 (voicing) ✅ APPLIED** — F-31 (Ch 5 ¶31 + ¶37 rephrased per the drafts;
  the covenant-intertext and T2.6 signature instances deliberately kept), F-13 (P6 owns
  delegation/abdication; P3 → "handing the work over and walking away from it"),
  F-23 (Michael's INVERSION: positive lead "Actively focus on the good over the noise
  of the world" + "joyless churn" kept + treating-light-lightly warning untouched),
  F-22 (Landauer credited WITHOUT breaking the dictum: "As the physicist Rolf Landauer
  insisted, information is physical.").
- **F-29 ⏸ KEPT DELIBERATELY** — "vibe create" stays (Michael LOL'ed; wants the light
  heart; "vibe" judged durable enough). **Noted for future editions:** if the slang
  dates, the ratified replacement is "The Gods did not improvise the earth."
- **G-8 ✅ VERIFIED + Ch 3 REWRITTEN (Michael's wording)** — git archaeology: spec was
  497→558 lines pre-build (752 today — "743" was a later snapshot of the living doc);
  first commit `fe1a0c7d` = 30 files / 4,041 insertions. Ch 3 now: "a planning
  specification document over five hundred lines long… the first day's build landed
  about four thousand lines of code across thirty files." (The truth was 4× stronger
  than the claim.)
- **G-2 + G-3 ⏸ PARKED, option (a)** — "fourteen questions" (P1) and "eight-milestone
  roadmap" (P2) KEPT pending the VS Code chat archive Michael is copying (~10GB,
  sqlite). Target when it lands: workspaceStorage for
  `OneDrive\Documents\code\Stuffleberry\simple-games` (G-2) + the transcript-tool
  workspace (G-3). ⚠ MUST verify-or-hedge before publish — do not let these ship
  unchecked.
- **G-6 ✅ APPLIED (P8, Michael's verdict + addition)** — "I still run it every few
  weeks, whenever it pops into my head — usually after the work has settled into a
  routine. It still finds things I didn't want to see, and things we can easily
  improve." (The routine-settling trigger is the honest cadence; no schedule claimed.)
- **F-10 ✅ APPLIED** — council=meeting (noun, title keeps it), counsel=the verb: P2 ¶11
  → "Counsel together until you can see the way."
- **Ch 4 title ✅ APPLIED** — harmonized to scripture: "Watched Until They Obeyed."
- **IDENTITY ITEMS ✅ APPLIED** — F-01 (Edition → June 2026), F-02 (colophon: "Claude
  Opus, and later Claude Fable, in a terminal… Opus carried the source-verification
  pass and the print-ready preparation; Fable walked the final honesty and voicing
  audit — true stewards of the work"), F-36/G-10 (afterword "my nine-year-old" → "my
  daughter"; the only age reference in the book — consent resolved by genericizing),
  G-4 (microservices "over three hundred" → "**over two hundred**"; Michael: ~270 k8s
  deployments; afterword's "hundreds" still true), G-9 CLOSED (18 years confirmed — Ch 1
  already says eighteen, no edit), G-7 CLOSED (Gemini drafted 0–12 in two batches, 0–7
  then 8–12 — colophon's "chapters 0 through 12" confirmed accurate, no edit).

- **F-15 ✅ RATIFIED + APPLIED** — "give an account **unto me**." (canon-verified via
  gospel_get; Michael: "the extension makes it better").
- **F-19 ✅ VERIFIED + APPLIED** — re-verified through the REBUILT webster-mcp (genuine
  1828, post-remediation): def 5 "The soul of man; the intelligent, immaterial and
  immortal part of human beings." + def 6 "An immaterial intelligent substance." — both
  exact. Ch 0 ¶1 requoted to the two genuine definitions.
- **F-20 ⏳ v2 DRAFT pending Michael's gate** — his doctrinal upgrade: Webster's def 4
  ("A spiritual being; as a **created** intelligence") has the right noun and the era's
  wrong adjective; D&C 93:29 (May 1833 — a TRUE "five years later") corrects "created."
  Bonus verified text in def 4: "It is believed that the universe is peopled with
  innumerable superior intelligences" — Abraham 3 in Webster's own gloss.
- **F-07 ✅ DREAM IDENTIFIED + DATED (wording awaiting Michael's pick)** — Michael
  corrected his own correction: "I think is the pg-ai-stewards project dream! double
  check, that was like 8 months later Oct to may." VERIFIED: pg-ai-stewards founded
  **2026-05-02** (5 same-day commits: research verdict → Phase-1 scaffold → provider
  abstraction), and the founding doc `docs/history/2026-05-02-research-verdict.md` has
  a literal section "Why this matters (the dream)" quoting Michael's description.
  storygames first commit **2025-10-22** → gap = **6 months 10 days** (his "8 months"
  guess overshoots; the book's "a year" doubles it). Two dreams in the book confirmed
  distinct: Aug 2023 (Afterword, "learn AI") vs ~May 2026 (P1, the substrate). Wording
  options for P1: **"The following spring"** (rec — exactly true, vivid, never stales)
  or "About half a year later." Bonus: the founding history corroborates the
  3-days/3-weeks figures loosely (real work by ~May 11-13; G-1 effectively closable).
- **F-39 · NEW · Ch 0 ¶15 · cat 1 · ●** — "**Five years later**, Joseph Smith received
  a revelation that collapsed this ancient dualism" → quotes **D&C 131:7-8, May 1843**
  = FIFTEEN years after 1828 (local file header verified). Meanwhile D&C 93 (the
  not-created correction) is May 6, **1833** — the true five-years-later. Found chasing
  Michael's F-20 question. Proposal: Ch 0 → "Fifteen years later"; the true "five years
  later" beat belongs to Ch 1's D&C 93 moment if wanted.

## ✅ WALK COMPLETE — 2026-06-09 (Claude Fable 5)

All 33 units read under all 8 lenses. **38 findings + 1 workspace side-quest.** No edits
applied (per the ratified cadence) — everything below awaits the chat walk with Michael.

**Headlines for the chat walk, in the order I'd present them:**
1. **SQ-1 / F-19 / F-20 — the Webster 1913-as-1828 misattribution** (ripples beyond the
   book: webster-mcp, 1828.ibeco.me, 1828-illuminated, the three-glories study). Book fix
   is easy and *improves* both passages.
2. **F-07 — P1's impossible timeline** ("a year later" = Oct 2026, in the future).
3. **F-37 — the EPUB renders broken lists + a leaked Typst directive** (ebook product).
4. **F-25 — the book's central verse quoted two ways** (Abr 4:18 comma ×3).
5. **F-24 / F-26 / F-34 — the numbers class** (80/20+"ten percent" unsourced;
   benchmark "bottom to top" rounds past its source; Helaman count is 4 not 3).
6. **F-14 / F-16 — chat-relative time in print** ("just days ago," "this week"); the
   afterword's "As I write this in May 2026" is the model to imitate.
7. **The voicing verdict:** far better than feared. Part One + most chapters carry
   negation-contrast at ~1/chapter, usually thesis-bearing and earned. **Ch 5 is the one
   true cluster (F-31)**; Ch 6 is borderline-but-intertextual; everything else I
   recommend leaving. The tics Michael named are real but the prior passes sanded most
   of them; what remains is mostly rhetoric the meaning wants.
8. **The honesty verdict (the audit's core question):** the book passes its own standard
   remarkably well. Check-2 (spec-first vs iterate) is RESOLVED in the text; the Ch 12
   deferral held; Ch 10/11's calibrated commitments and production notes are the
   high-water mark. The failures found are mostly *small checkable facts*, not
   structural overclaims.

**Counts:** ● high: 4 (F-07, F-15→resolved-to-question, F-19, F-20, F-37) · ◐ medium: 11
· ○ light: rest. CLEAN units: P5, P8, p1/p2 dividers, Ch 7, Ch 8, Ch 10, Ch 11, Ch 12,
Epilogue.

## For Michael's ground truth (lived figures — only he can confirm)

| # | Unit | Claim as printed | Question |
|---|------|------------------|----------|
| G-1 | P1 | "October 2025" game start; dream-system "running real work in three days and stood up in about three weeks" | Dates/durations right? (Oct 2025 is repo-confirmed; 3d/3wk was already on the provenance confirm list) |
| G-2 | P1 | "The model came back with fourteen questions" | Real count, or soften? (F-08) |
| G-3 | P2 | "a beautiful eight-milestone roadmap"; "I wrote in the log that I felt overwhelmed" | As remembered? (provenance still flags re-confirm) |
| G-4 | P4 | "over three hundred interconnected microservices" | Still the right figure? (was on the 2026-06-01 confirm list) |
| G-5 | P6 | "seven networked multiplayer games… single app… late 2025… Dart… two operating systems… my kids played them" | All as lived? |
| G-6 | P8 | "I still run it every few weeks" (the retro cadence) | Ben Test the cadence — is "every few weeks" the honest rate? |
| G-7 | Colophon | "Gemini … drafted the first pass of chapters 0 through 12" | Accurate chapter span? (F-03) |
| G-8 | Ch 3 | "first pass produced over a thousand lines of code across thirteen files" | As measured? |
| G-9 | Ch 1 | "I have been a software engineer for **eighteen years**" (×2) | 18 or 19 by publication? (private docs say 19) |
| G-10 | Afterword/P1 | "my nine-year-old" / "my kid" (storygames) | Consent confirm — the recorded flag is still open (F-36) |

## Voicing tic tally (running)

| Tic | Where it clusters | Notes |
|-----|-------------------|-------|
| Negation-contrast ("not X; it's Y") | P3 ×3, P4 ×2, P6 ×2, P9, coda — roughly one per practice, 2-3 in P3 | Individually all read fine; the *pattern* is visible if you look. Part One survived its voicing passes well — most instances are thesis lines that earn the shape. Candidates if Michael wants variety: P3 ¶11, P4 ¶11, P9 ¶11. F-13 (delegation/abdication double-coinage) is the one concrete fix. |
| Staccato aphorism pair | P1 ("It feels faster. It isn't."), P9 ("The friction was data. The door is the response.") | Sparse, single-use, earned. No action. |
| Self-restating closer | Not found in Part One bodies | Remember boxes restate by design (protected recaps) and vary their wording — good. |

## Walk progress

| Unit | Read | Findings |
|------|------|----------|
| frontmatter | ✅ | F-01..04 |
| preface | ✅ | F-05..06 + clean cat-2 |
| p1_00 divider | ✅ | clean (3 lines) |
| P1 talk-dont-command | ✅ | F-07 ● timeline, F-08 |
| P2 council-before-you-build | ✅ | F-09, F-10 |
| P3 set-the-bounds | ✅ | tally only; D&C 104 spot-check queued |
| P4 pack-the-context | ✅ | F-11, F-12 |
| P5 make-it-portable | ✅ | clean |
| P6 let-it-carry | ✅ | F-13 |
| P7 assume-it-will-lie | ✅ | F-14, F-15 ● quote-verify |
| P8 ask-whats-in-the-way | ✅ | clean |
| P9 build-the-door | ✅ | F-16 |
| P10 coda go-touch-grass | ✅ | F-17 |
| p2_00 divider | ✅ | clean |
| eleven-step ref | ✅ | F-18 |
| Ch 0 intelligence/truth | ✅ | F-19 ● Webster, F-22, F-23 |
| Ch 1 value shift | ✅ | F-20 ● Webster, F-24, F-25 |
| Ch 2 four disciplines | ✅ | F-26; tag mystery resolved |
| Ch 3 spiritual before temporal | ✅ | F-27, F-28, F-29; check-2 RESOLVED |
| Ch 4 watched until they obeyed | ✅ | F-25 upgraded (anchor comma); title-tense Q |
| Ch 5 intelligence cleaveth | ✅ | F-31 voicing cluster |
| Ch 6 bilateral covenant | ✅ | F-32, F-33 |
| Ch 7 delegation as stewardship | ✅ | CLEAN (talks verified) |
| Ch 8 mechanics of refinement | ✅ | CLEAN |
| Ch 9 hope and the veil | ✅ | F-34 (count 4 not 3); F-21 "warily" |
| Ch 10 softening | ✅ | CLEAN |
| Ch 11 the seventh time | ✅ | CLEAN |
| Ch 12 conclusion zion | ✅ | CLEAN; deferral held |
| Epilogue silent loop | ✅ | CLEAN |
| Afterword how I got here | ✅ | F-35, F-36 |
| Glossary | ✅ | F-37 ● build, F-38 |
| Further reading | ✅ | F-37 (shared); talk files verified |
