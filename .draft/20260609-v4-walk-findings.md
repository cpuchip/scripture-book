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
| p2_00 divider | ⬜ | |
| eleven-step ref | ⬜ | |
| Ch 0 intelligence/truth | ⬜ | |
| Ch 1 value shift | ⬜ | |
| Ch 2 four disciplines | ⬜ | |
| Ch 3 spiritual before temporal | ⬜ | |
| Ch 4 watched until they obeyed | ⬜ | |
| Ch 5 intelligence cleaveth | ⬜ | |
| Ch 6 bilateral covenant | ⬜ | |
| Ch 7 delegation as stewardship | ⬜ | |
| Ch 8 mechanics of refinement | ⬜ | |
| Ch 9 hope and the veil | ⬜ | |
| Ch 10 softening | ⬜ | |
| Ch 11 the seventh time | ⬜ | |
| Ch 12 conclusion zion | ⬜ | |
| Epilogue silent loop | ⬜ | |
| Afterword how I got here | ⬜ | |
| Glossary | ⬜ | |
| Further reading | ⬜ | |
