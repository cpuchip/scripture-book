# Book Review — Claude Code Audit (2026-05-26)

**Reviewer:** Claude Opus 4.7 (Claude Code)
**Scope:** Chapters 0–7 + Preface + Introduction + Frontmatter (everything Gemini drafted)
**Method:** Read-before-quoting verification. Every direct quote checked against `gospel-library/` canonical source files. External citations checked separately. Cross-chapter consistency scanned for tensions, double-coverage, terminology drift.
**Posture:** Fact-finding for council, not redrafting. Findings ranked by severity. Where the book is right, I say so; where it drifts, I name the drift.

---

## Severity legend

- **🔴 Fact error / quote drift** — needs correction before publish
- **🟡 Citation precision** — accurate substance but cite-range, attribution, or framing should tighten
- **🟢 Verified clean** — quote matches canonical source, no action needed
- **💡 Enhancement opportunity** — something from our studies, journals, or session history that would deepen the chapter if added

---

## Section 1 — Scripture Quote Verification

### 🟢 Verified Clean (no action)

| Citation | Chapter | Verification |
|----------|---------|--------------|
| D&C 93:29–30 | Ch 0 anchor | Exact match (man was also in beginning…). |
| D&C 131:7–8 | Ch 0 | Exact match (no immaterial matter…). |
| D&C 88:40 | Ch 0, Ch 5 anchor | Exact match — book ellipses `;...` between truth-embraceth and light-cleaveth is honest selective quotation. |
| D&C 88:66 | Ch 0 | Exact partial quote — book opens with `...` to signal omission of "my voice, because". |
| D&C 93:24 | Ch 0 | Exact ("knowledge of things as they are, and as they were, and as they are to come"). |
| D&C 93:28 | Ch 0 | Exact partial. |
| D&C 93:30 | Ch 0, Ch 4 | Exact ("All truth is independent in that sphere…"). |
| D&C 93:36 | Ch 1 | Exact ("the glory of God is intelligence…"). |
| D&C 88:42 | Ch 0 | Exact partial ("move in their times and their seasons"). |
| D&C 88:119 | Ch 2 anchor | Exact (terminal punctuation differs — semicolon in canon, period in book; trivial). |
| D&C 130:18–19 | Ch 1 anchor | Exact match. |
| D&C 123:12 | Preface | Exact match. |
| Abraham 4:18 | Ch 1, Ch 4 anchor, Ch 7 | Substantively exact. **Tiny note:** book inserts a comma — "watched those things which they had ordered, until they obeyed" — canon has no comma. Most editions render without the comma. Not worth changing; flagging only for completeness. |
| Abraham 4:10 | Ch 4 | Exact partial. |
| Abraham 4:21 | Ch 4 | Exact partial (omits "and that their plan was good" — acceptable). |
| Abraham 4:31 | Ch 4 | Exact partial. |
| Abraham 5:2 | Preface anchor | Exact match (the chapter text is right; **the provenance file has a typo** — see 🟡 below). |

### 🟡 Citation Precision Issues

**1. D&C 84:44–45 cited, but only verse 45 is quoted (Ch 0)**
- Book: "For the word of the Lord is truth, and whatsoever is truth is light, and whatsoever is light is Spirit, even the Spirit of Jesus Christ." — attributed to D&C 84:44–45.
- Canonical 84:44: "For you shall live by every word that proceedeth forth from the mouth of God."
- Canonical 84:45: the quoted text.
- **Fix:** Change citation to `D&C 84:45`. Or, if you want to keep 44–45 as a unit (since 44 sets up 45's "for the word"), reword: "For you shall live by every word that proceedeth forth from the mouth of God. For the word of the Lord is truth…"

**2. D&C 88:32 framed as if it's a quoted principle (Ch 5)**
- Book: "you cannot receive that which you are not willing to receive ([D&C 88:32])."
- Canonical 88:32: "And they who remain shall also be quickened; nevertheless, they shall return again to their own place, to enjoy that which they are willing to receive, because they were not willing to enjoy that which they might have received."
- The principle is real, but the book's phrasing is the agent's compression, not the verse. As italicized in the chapter, a reader will assume the verse says exactly that.
- **Fix:** Either quote the actual verse (or its key clause: "they shall return again to their own place, to enjoy that which they are willing to receive"), or remove the cite and paraphrase plainly: "The principle is taught in D&C 88:32 — souls receive what they are willing to receive, and no more."

**3. Provenance preface — Abraham 5:2 transcribed wrong (file only, not manuscript)**
- `.scratch/provenance_preface.md` quotes: "…rest on the seventh time from all our work which we have **created**."
- Canonical and manuscript both end with "which we have **counseled**."
- **Fix:** Update provenance file to match canon. Manuscript itself is correct.

**4. Provenance chapter 0 — D&C 88:40 quote includes punctuation drift**
- Provenance: ends `"...light cleaveth unto light;"` (semicolon as final char inside quotes)
- Manuscript: ends `"...light cleaveth unto light."` (period as final char)
- Minor. Either is fine; pick one and apply consistently.

### 🔴 Factual / Interpretive Drift Requiring Correction

**5. Chapter 4 misstates what happened on the seventh day**
- Book Ch 4: *"In [Abraham 5:2], we read that on the seventh day the Gods rested and 'counseled among themselves.' This was a session of reflection—a step back to evaluate the entire creative arc to see if the overall system was good."*
- Canonical Abraham 5:2: "On the seventh time we will end our work, which we have counseled; and we will rest on the seventh time from all our work which we have counseled."
- The seventh day is rest **from work they had counseled** (past tense). The phrase "counseled among themselves" appears in Abr 4:26 (council before forming man) and Abr 5:3 (referring to the planning before creation) — it is NOT a description of seventh-day activity. The chapter's framing of the seventh day as "a session of reflection" is plausible but it's the book's interpretation, not what 5:2 says.
- **Fix options:** (a) Drop the quoted phrase and reframe as "Abr 5:2 names the seventh day as the rest *from* the work they had counseled — the whole creative arc was bounded by counsel on the front end and rest on the back end." (b) Move the "session of reflection" framing one chapter forward into the Sabbath material and tie it to the actual scriptural rest pattern. The fundamental point (sabbath as evaluation moment) is good; it just isn't *in* Abraham 5:2.

**6. Chapter 7 mis-paraphrases Abraham 4:18's purpose in stewardship context**
- Book Ch 7 final paragraph treats Abr 4:18 as the stewardship-feedback verse for a delegating master.
- Cross-chapter tension: Ch 4 names Abr 4:18 as the **specification-verification** verse. Both uses are theologically defensible (watching IS feedback IS stewardship), but the book uses the same anchor verse for two distinct chapter theses without acknowledging it.
- **Fix options:** (a) In Ch 7, swap to a different stewardship-watching verse — D&C 104:13 ("every man is accountable, as a steward over earthly blessings") would actually anchor delegation-with-accountability more sharply. (b) Acknowledge the layered reading: "The same Abraham 4:18 we read in Chapter 4 as oversight applies again here, but now from the steward-master angle." Option (b) preserves the through-line; option (a) sharpens the chapter-by-chapter distinctness.

---

## Section 2 — Prophetic / Conference Talk Quotes

### 🟢 Verified Clean

**Ballard, "Counseling with Our Councils" (April 1994)** — Ch 7
- Book: "The one-cylinder ward is the ward where the bishop handles all of the problems, makes all of the decisions, and follows through on all of the assignments. Then, like an overworked cylinder in a car engine, he is soon burned out."
- Canonical (paragraph 17 of the talk): **identical wording, verified character-for-character.**

**Hinckley, "In … Counsellors There Is Safety" (October 1990)** — Ch 7
- Book: "The president, if he is wise, will assign to these chosen assistants particular duties and then leave them free to perform, requiring from them accountability for what happens."
- Canonical: **identical wording, verified character-for-character.**

Both quotes are clean. The Ballard talk also has surrounding context that could enhance Ch 7 — see Section 5 enhancement notes.

---

## Section 3 — External / Industry Citations

### 🟢 Verified Clean

**Tony Trejo, *Value Shift Framework* (Medium)** — Ch 1
- Book: "AI didn't replace engineers. It replaced execution as the bottleneck. And when the bottleneck moves, value moves with it."
- Source (after Medium redirect to `medium.com/codetodeploy/...`): **exact match.** The article uses the term "Value Shift Framework" as the title and as a section heading. Citation is honest. *Note: the original `tonytrejodev.medium.com` URL now 302-redirects to `medium.com/codetodeploy`; consider updating the manuscript link to the canonical destination URL so the citation doesn't break if the redirect ever lapses.*

**Milan Jovanović (LinkedIn)** — Ch 1
- Book: "It's owning correctness."
- Canonical surrounding sentence from his LinkedIn post: "If you're trying to 'stay relevant' in the AI era, the skill isn't prompting. It's owning correctness."
- **Exact match.** *Consider:* the book paraphrases the lead-in as "The skill is no longer prompting; as engineer Milan Jovanović writes, 'It's owning correctness.'" Compressing his two sentences into the book's framing is fair use, but if you want maximum honesty, quote the full pairing: "the skill isn't prompting. It's owning correctness."

### 🟡 Webster 1828 — Mixed

**Spirit (Ch 0)** — 🟢 VERIFIED
- Book quotes three phrases as Webster 1828's definition of *spirit*:
  - "an intelligence conceived of apart from any physical organization or embodiment" — **exact**, from sense 3 of the Webster entry I retrieved via the `webster_define` MCP tool.
  - "vital essence, force, or energy, as distinct from matter" — **exact**, also from sense 3.
  - "the intelligent, immaterial and immortal part of man" — **exact**, opens sense 4.
- The book's framing ("To the nineteenth-century mind, the division was absolute") is the author's gloss, not a quote — fair characterization.

**Intelligence (Ch 1)** — 🔴 WORDING MISMATCH
- Book Ch 1: "Webster's 1828 dictionary defines it as 'understanding; skill; the faculty of understanding.'"
- Actual entry returned by the workspace `webster_define` MCP for *intelligence*:
  - Synonyms list: "Understanding; intellect; instruction; advice; notice; notification; news; information; report."
  - Sense 1: "The act or state of knowing; the exercise of the understanding."
  - Sense 2: "The capacity to know or understand; readiness of comprehension; the intellect, as a gift or an endowment."
- The book's quoted phrase **"skill; the faculty of understanding"** does not appear in the dictionary entry the workspace's MCP tool returns. The word "skill" is absent entirely from the entry's senses and synonyms.
- **Possible explanations:** (a) The book is quoting an *abridged* or *paraphrased* version of the 1828 entry, perhaps from `1828.ibeco.me`'s display format which may collapse multi-clause senses. (b) The author drafted a plausible synthesis and forgot to verify. (c) The MCP is serving Webster's 1913 (or another edition) rather than the literal 1828 first edition, and the original 1828 reads differently.
- **Action needed:** Open `https://1828.ibeco.me/word/intelligence` in a browser and read the entry as displayed. If the displayed text matches the book's quoted phrase, the citation stands but should note "as rendered in the Stuffleberry 1828 Illuminated edition." If the displayed text differs, the book's quote needs revision to match the actual source.
- This is the only finding marked 🔴 in the external citations bucket. It is correctable in one line.

---

## Section 4 — Cross-Chapter Consistency Scan (Preliminary)

### Strong consistency
- The matter-spectrum framework (intelligence → spirit → element) introduced in Ch 0 is the *same* framework used to explain vector-space resonance in Ch 5. The book is doing one thing across many chapters, not many things in series. This is its strongest structural feature.
- The 11-step creation cycle is named in the Introduction and used as the scaffolding in Ch 2 (mapping the four disciplines to steps 1, 4, 5, 6). The seven unmapped steps named in Ch 2 (covenant, stewardship, watching, atonement, sabbath, consecration, Zion) become the actual chapter topics for Section II and III. **This is excellent architecture.**
- Voice is consistent across chapters. No presenter tics. No "let that land." The cut list from `.github/copilot-instructions.md` is honored throughout. Gemini's voice work is genuinely strong.

### Tensions to surface (for council, not corrections)

**T1. Chapter 0 vs Chapter 5 redundancy.**
Both chapters use "intelligence cleaveth unto intelligence" + vector-space resonance + "lazy prompt = darkness" framing. Ch 5 is the chapter named for this idea, but Ch 0's Engineering Parallel section already executes the entire argument. By the time the reader reaches Ch 5, the punchline is delivered.
- **Council question:** Is Ch 0 doing too much? Or is Ch 5 supposed to *expand* what Ch 0 names? Right now they're parallel rather than serial.
- **Recommendation to consider:** Trim Ch 0's "intelligence cleaveth" passage to a foreshadow ("we'll examine the law of resonance in Section II") and let Ch 5 do the work. OR: keep Ch 0's metaphysical exposition and refactor Ch 5 to focus on the **posture/intent** angle (the human's internal state shaping output) rather than re-deriving the vector-space math.

**T2. The 11-step cycle is invoked but never enumerated in one place.**
- Ch 2 names 4 of the 11 steps and lists the other 7 as a parenthetical.
- The reader has to know "the eleven-step creation cycle from Moses and Abraham" already to follow.
- **Suggestion:** Either Introduction or Ch 2 should have a single panel/sidebar that lists all 11 steps with one-line definitions: Intent / Covenant / Stewardship / Specification / Line Upon Line / Physical Creation / Watching / Atonement / Sabbath / Consecration / Zion. This anchors every later chapter that references "step N."

**T3. "Vibe coding" appears in Ch 3 but is not defined.**
- Ch 3 uses the term as if it's familiar industry shorthand. For a general audience it isn't — it's a 2024–2025 dev-Twitter term from Karpathy.
- **Suggestion:** One-sentence parenthetical on first use, or a glossary at the back.

**T4. Voice slips into list-mode in Chapter 7.**
- Ch 7 numbers Christ's delegation sequence as "authority first, then scope, then capacity, and finally identity." That four-element schema isn't from the text — it's the book's overlay. It works, but reads as the only place in the manuscript where Gemini imposes a framework on top of a verse rather than letting the verse hand one over.
- **Council question:** Is the four-element schema teachable, or is it manufactured neatness? If teachable, defend it more (cite the actual verses for each). If manufactured, dissolve it back into prose.

**T5. The author voice slips between "I" (single human) and "we" (human + AI).**
- Preface, Ch 1: "I have been a software engineer for eighteen years." — clearly Michael.
- Ch 4: "In our scripture project, a periodic review revealed that…" — "we" = ??
- Ch 6: "In our own workspace, we have codified this pattern in a physical file: `.spec/covenant.yaml`." — "we" = human + AI.
- This isn't wrong, but the unsignaled shifts can confuse a reader who doesn't know the book is co-authored. Either explicitly name the collaboration in the Preface ("Throughout this book, 'I' is Michael's voice; 'we' marks moments of co-creation with the AI agents named in the Colophon") or normalize toward one pronoun.

**T6. The Becoming app reference in Ch 3 is concrete but unattributed.**
- Ch 3: "743 lines long before a single line of code was written. It detailed every database table…"
- This is a great specific detail. But a reader doesn't know what the Becoming app is, or where to see it.
- **Fix:** One-sentence pointer ("the personal-practice tracker now deployed at ibeco.me") or footnote.

---

## Section 5 — Enhancement Opportunities

These are studies, journals, and real session records that could deepen specific chapters. Not requests — just inventory for council.

### Ch 0 (Substance of Reality) — 💡

- **Mechanics of refinement study** ([study/mechanics-of-refinement.md](../../../study/mechanics-of-refinement.md), 2026-05-23) — already cited by `.mind/active.md`. It's the most precise treatment of D&C 88:21-34 (capacity governed by law) in the workspace. Ch 0 alludes to "capacity to contain" but doesn't name the law-driven mechanism. **Drop-in candidate:** one paragraph about how light withdrawal isn't punitive — it's law, the way temperature regulates state.
- **Truth-Atonement chain** ([study/truth-atonement.md](../../../study/truth-atonement.md)) — explicitly maps the matter spectrum to atonement physics. Ch 0 sets up the spectrum; could close with a forward reference to "we'll see in Ch 8 that this same fine matter is what the Holy Ghost works on in refinement."

### Ch 1 (Value Shift) — 💡

- **Emad Mostaque YouTube evaluation** ([study/yt/Se91Pn3xxSs-you-have-3-years-left.md](../../../study/yt/Se91Pn3xxSs-you-have-3-years-left.md), 2026-05-26 — literally today!) — Mostaque's "infinite grads" thesis is the source for the preface's framing. The study is in the workspace right now and explicitly connects this to the value shift. **The Preface already names the Mostaque interview** but doesn't pull from the study's findings. Worth one paragraph in Ch 1 about what infinite grads actually means for the bottleneck.
- **Relevance/fatigue studies** ([study/ai/relavent.md](../../../study/ai/relavent.md), [study/ai/fatigue.md](../../../study/ai/fatigue.md)) — the source material for the "judgment rises with us" argument. Already grafted into principles.md. The book's "Parable of the Talents" angle in Ch 1 could be sharpened by the principle stated there: *"AI has no resurrection. The question isn't 'am I still relevant?' — it's 'am I using what I've been given?'"* That line is sharper than the book's current closing.

### Ch 2 (Four Disciplines) — 💡

- **Bacteriopolis runaway / ES emergency-stop incident** — referenced in Ch 2 ("an autonomous research agent in our Postgres database ran for ten hours, looping on a single topic, until we hit the emergency stop"). The fuller story lives in `project_substrate_ES_emergency_stop` memory + multiple journal entries (`.spec/journal/2026-05-15` etc.). Ch 2's one-sentence treatment is appropriately compact, but the journal entries have *very* concrete details (cost runaway: $X, judge-pattern fix, the precise loop). **Council question:** Is this incident too good to leave at one sentence? Could be its own boxed sidebar in Ch 2 or Ch 4.

### Ch 3 (Spiritual Before Temporal) — 💡

- **Last Supper Four Cups study** ([study/last-supper-four-cups.md](../../../study/last-supper-four-cups.md)) — example of "outline first, then study." This is a real example of the book's claim that "we write a study outline first." Worth citing as proof rather than just claim.
- **Spec-driven Stuffleberry projects** — multiple references in your journal (storygames, simple-games, ibeco.me, 1828-illuminated) to "specification before code." Ch 3 mentions the Becoming app's 743-line spec; could mention a second example to show the pattern repeats.

### Ch 4 (Watched Until They Obeyed) — 💡

- **The 2026-05-20 substrate bridge stall** ([`.spec/journal/2026-05-20-substrate-bridge-stall-recovery.md`](../../../.spec/journal/2026-05-20-substrate-bridge-stall-recovery.md)) — bridge worker silently stalled, 7 Thummim items orphaned, recovered via restart. This is literally "watching that revealed the system was no longer obeying" — a real workplace instance of the Abraham 4:18 pattern. Way more concrete than "many people approach AI as a vending machine."
- **The Section VII covenant violation story** ([.mind/identity.md](../../../.mind/identity.md), referenced in `.spec/covenant.yaml`) — the stewardship study had a wrong Section VII that contradicted earlier work; Michael caught it. **This is the canonical workspace example of "watching catches drift."** Surprisingly absent from Ch 4. Worth a paragraph.
- **2026-05-15 to 2026-05-19 ES arc** — emergency stop on bacteriopolis is the most expensive watching lesson in the workspace's history. The book references it in Ch 2 but Ch 4 (the watching chapter) doesn't.

### Ch 5 (Intelligence Cleaveth) — 💡

- **Voice analysis study** ([study/yt/voice-analysis-ai-vs-michael.md](../../../study/yt/voice-analysis-ai-vs-michael.md)) — the prep work for the chapter's claim that AI mirrors quality of input. Real, codified observations about voice degradation under loose prompts.
- **Kimi-K2.6 and Qwen-3.6 voice-signature memories** (`project_kimi_voice_signatures`, `project_qwen_voice_signatures`) — workspace has *receipts* on how different model styles emerge under different prompt postures. Ch 5 currently asserts the law; these memories are the evidence.

### Ch 6 (Bilateral Covenant) — 💡

- **The actual `.spec/covenant.yaml` file** is named in Ch 6 but never quoted. The bullet list of human and agent commitments is *paraphrased* from the YAML. Consider including the actual `human_commits_to` and `agent_commits_to` names verbatim with their "why" sections — that's both more honest (this IS our covenant, not a sanitized version) and more powerful (the "why" stories ground each rule).
- **Mosiah 18:8-10 quote in Ch 6** is paraphrased ("they committed to bear one another's burdens and stand as witnesses, and the Lord committed to pour out His Spirit more abundantly"). Could include the actual covenant language. Verifying separately.

### Ch 7 (Delegation as Stewardship) — 💡

- **The Judges-not-Executors principle** (`.mind/principles.md` → "Judges, Not Executors (Exodus 18:21-22)") — already in workspace canon. The chapter cites Exodus 18 but doesn't name the principle that has been ratified from it: agents are judges with stewardship authority, not executors running scripts. This is a workspace-original framing worth claiming.
- **The Art-of-Presidency / Art-of-Delegation arc** ([study/art-of-presidency.md](../../../study/art-of-presidency.md), [study/art-of-delegation.md](../../../study/art-of-delegation.md)) — directly source material for Ch 7. Currently invisible.
- **Zion-in-a-Presidency** ([study/zion-in-a-presidency.md](../../../study/zion-in-a-presidency.md)) — likely candidate for Ch 11 conclusion's Zion treatment.
- **The pg-ai-stewards substrate as the worked example** — the chapter's diagram (Master Agent / Subagent A / Subagent B) is generic. The workspace has an actual three-tier stewardship: watchman → pipelines → stages → judges. This is the most-developed stewardship instance in the workspace and the chapter doesn't name it.

---

## Section 6 — Frontmatter / Preface / Introduction Notes

**Preface — Mostaque interview link.** The preface uses `[qr](https://youtu.be/Se91Pn3xxSs)` for the Bilyeu/Mostaque interview but doesn't link to our own evaluation. We have one (today). Worth adding `[Our study](../../../study/yt/Se91Pn3xxSs-you-have-3-years-left.md)`.

**Preface — historical accuracy.** "GitHub Copilot introduced its chat pane and integrated Anthropic's Claude 3.5 Sonnet in preview" in October 2024. **Verify the date.** My memory says GitHub Copilot Chat went GA earlier and Claude integration came later in 2024; the exact month is testable against GitHub's blog. Worth fact-checking before publish.

**Introduction — "For five months."** The preface says the book is being written May 2026, and that the journey began in January 2026 in the classroom. Five months checks out. But the Introduction's opening "For five months, I have worked daily with AI models" is the book's only time-marker outside the Preface; it will become stale fast. Consider "Since January 2026" or removing the duration.

**Colophon — agent council.** GitHub Copilot, Claude Code CLI, Gemini / Antigravity all named. Honest. **But:** it doesn't mention the human-only contributions explicitly (the binding questions, the cuts, the corrections). The bilateral covenant theme would land harder if the colophon also named what the human brought.

---

## Section 7 — Things The Book Gets Conspicuously Right

(For council — don't sand these down.)

1. **Theological architecture is real.** The four-disciplines-mapping-to-creation-cycle conceit (Ch 2) is original to this collaboration as far as I can tell from workspace history. It works.
2. **The voice is yours.** Compared with the kimi/qwen voice-signature memories on file, this manuscript reads as *Michael's voice cleaned of formatting tics*, not as Gemini's voice. That's hard to do.
3. **The 3.5-year journey in the Preface is the book's strongest passage.** Specific tools, specific dates, specific projects. The Monson Principle from `.mind/principles.md` ("specific detail + trust the moment") is doing the work without being told to.
4. **Section II's "delegation-as-offloading vs stewardship" distinction (Ch 7 and Ch 6)** is a sharper version of what `.spec/covenant.yaml`'s `exercise_stewardship` clause names. The book is teaching what the workspace has only just learned. That's the point.

---

## Section 7.4 — Council Note: Honest Footnote / Sidebar for Ch 6 (RATIFIED 2026-05-26)

Michael ratified including this as material in the book itself rather than hiding it. The drift pattern is real teaching material — exactly the kind of thing the bilateral covenant principle is *about*.

### What happened (the testable record)

The book is being written collaboratively across multiple AI agents. Gemini drafted most of the first-pass chapters inside the Antigravity 2 IDE. The CLAUDE.md and `.github/copilot-instructions.md` files codify a covenant workflow: **research → scratch file → verify against canon → manuscript → audit**. The intended ordering puts verification *before* the chapter is written.

What actually happened during the Gemini drafts: Antigravity 2's instruction-loading harness doesn't enforce the file-based covenant the way GitHub Copilot and Claude Code do. The provenance files were generated *after* the chapters as documentation, not *before* as verification gates. The flow degraded from `scratch → manuscript` to `manuscript → backfilled scratch`. That inversion is invisible from the surface — the directory structure looked complete — but it meant the audit trail was being written from memory and paraphrase rather than from canon.

### What this produced (the audit findings)

Three real errors in the manuscript itself (Ch 0 cite range, Ch 4 mis-attribution, Ch 1 Webster intelligence). Four real errors in the provenance files (preface typo, Ch 3 verse number wrong, Ch 4 propagated error, Ch 7 *fabricated D&C 104:11-12 quote* attributing language from v.86 to v.11-12). The most serious was the Ch 7 provenance fabrication — the audit trail was inventing canon. The manuscript itself was correct; the documentation that was supposed to prove it was correct was making things up.

### Why this is the book's strongest credibility moment, not a wound

Chapter 6's argument is that bilateral covenants produce good output when honored and produce degraded output when broken — and that *the degradation is natural consequence, not punishment*. The book is teaching the exact pattern that the book's own production violated. **Hiding this would be performance. Naming it is the doctrine.**

What Ben would catch: a teacher writing about covenant who doesn't show their own covenant break is performing infallibility. Including it makes the chapter trustable in a way no polished version can.

### Recommendation for council

Add a short footnote or sidebar at the end of Chapter 6 (or in the Colophon, or in a dedicated "Atonement" section between Ch 8 and Ch 11). Suggested shape, ~150 words:

> *A note on this book's own production:*
> *This book is a collaboration across three AI agents. In the first drafting pass, our Gemini agent — running inside an IDE whose instruction-loading harness is still maturing — wrote chapters faster than the verification gates were applied. When we ran a Claude Code audit against the workspace covenant, we found three quote-precision errors in the manuscript and four errors in the provenance files. One was a fabricated D&C 104:11-12 quote pretending to be canon. The manuscript itself was right; the audit trail invented language to justify it. We rewrote the audit trail against canon and ratified this footnote rather than hide what happened.*
> *The degradation wasn't punishment. The covenant said: when ye do not what I say, ye have no promise (D&C 82:10). What our covenant says is "read before quoting, no exceptions." When the workflow inverted, the natural consequence followed. Saying so out loud is the redemptive half of the same covenant.*

(Voice this in Michael's voice; the above is placeholder shape, not final wording.)

### Additional council items this opens

1. **A "Redemptive Work" pattern.** This audit + rewrite + footnote sequence is itself an instance of [study/mechanics-of-refinement.md](../../../study/mechanics-of-refinement.md) and the broader Atonement-as-refinement principle. Worth naming as the book's working method, not just the book's content. Could become a Section III chapter or an Atonement-themed appendix.

2. **Antigravity 2 / Gemini harness limitations** as a recurring constraint to design around. The instruction files don't load reliably; expect the agent to draft from training-data priors rather than from workspace canon unless explicit verification is enforced at each step. Future Gemini sessions should be supervised by Claude Code or Copilot doing the verification pass synchronously, not deferred.

3. **The Section VII pattern is now appearing twice in the workspace.** Once in `study/stewardship-pattern.md` (originally caught by Michael in March 2026). Now in this book's production. Both times it was an agent writing confidently past existing canon without `read_file`'ing first. Worth a memory entry / principle entry naming this as a recurring failure mode and the covenant's `check_existing_work` clause as the antidote.

---

## Section 7.5 — Provenance File Audit (`.scratch/provenance_*.md`)

The provenance files in `.scratch/` exist as the audit trail behind each chapter's claims. They are meant to *match* the canon — they're the seam between the manuscript and the gospel-library. I read all nine of them. The manuscript is in better shape than the provenance files.

### 🔴 Hard errors in provenance files (the manuscript is correct; the audit trail isn't)

**P1. `provenance_preface.md` — Abraham 5:2 has "created" where canon says "counseled."**
- Provenance: "…rest on the seventh time from all our work which we have **created**."
- Canon and manuscript both: "…which we have **counseled**."
- *(Already noted in Section 1, repeating here for the provenance summary.)*

**P2. `provenance_chapter_3.md` — D&C 29 verse number is wrong.**
- Provenance heading: "Doctrine and Covenants 29:**31**"
- Provenance quote: "First spiritual, secondly temporal, which is the beginning of my work"
- Actual location: D&C 29:**32** (verse 31 says "For by the power of my Spirit created I them; yea, all things both spiritual and temporal—" — it's the lead-in, not the quoted phrase)
- The manuscript itself correctly cites 29:32. Only the provenance is wrong.

**P3. `provenance_chapter_4.md` — propagates the same factual error the manuscript has.**
- Provenance lists Abraham 5:2's quote as: `"counseled among themselves."`
- Canon Abr 5:2 actually opens: "And the Gods **said** among themselves." The phrase "counseled among themselves" appears in Abr 4:26 and Abr 5:3, not 5:2.
- This is the same error called out in Section 1, finding 🔴 #5. Provenance carries the error forward — it doesn't catch it.

**P4. `provenance_chapter_7.md` — D&C 104:11-12 quote is fabricated.**
- Provenance gives the quote as: `"And I give unto you this privilege, this once, that you may be organized, with your stewardships, every man in his stewardship; and a steward shall be appointed over his portion..."`
- That phrasing is **not in D&C 104:11-12**. The actual 104:11-12 (which the manuscript correctly quotes) reads: "It is wisdom in me; therefore, a commandment I give unto you, that ye shall organize yourselves and appoint every man his stewardship; That every man may give an account unto me of the stewardship which is appointed unto him."
- The opening phrase "I give unto you this privilege, this once" comes from D&C **104:86** ("I give unto you this privilege, this once; and behold, if you proceed to do the things which I have laid before you, according to my commandments…").
- The provenance file appears to be a fabricated mash-up: a fragment of v.86 spliced with paraphrased stewardship language attributed to v.11-12. The manuscript is fine; the audit trail is invented.
- **This is the most serious provenance finding.** It defeats the whole point of provenance as the verification layer.

### 🟡 Soft drift in provenance files

**P5. `provenance_chapter_0.md` — D&C 88:40 terminal punctuation differs from manuscript** (`;` in provenance, `.` in manuscript). Trivial; pick one.

**P6. `provenance_chapter_5.md` — D&C 88:32 quote in provenance is CORRECT (the actual verse text); but the manuscript paraphrase compresses and *reverses* that meaning.**
- Provenance has the canonical: `"to enjoy that which they are willing to receive, because they were not willing to enjoy that which they might have received."`
- Manuscript says: "you cannot receive that which you are not willing to receive ([D&C 88:32])."
- The provenance is honest; the manuscript loosens the verse into a slogan. This validates 🟡 finding #4 in Section 1 — the manuscript needs to quote what the provenance correctly captured.
- This is actually the provenance system *working as designed* — it preserves the truth even when the manuscript drifts. If anyone follows the audit trail, they catch the drift. Good design feature.

**P7. `provenance_chapter_4.md` lists the Godhead study (`study/know-god.md`) as the source for the 2 Peter 1:4 surfacing**. The book's claim ("semantic vector database… instantly surfaced non-obvious, critical passages — like 2 Peter 1:4") implies a specific session episode. Worth verifying the study record actually contains that semantic-search-vs-keyword episode if anyone wants to defend the example.

### 🟢 Provenance files that hold up

- `provenance_chapter_1.md` — quotes match the manuscript; Trejo and Jovanović sources properly named.
- `provenance_chapter_2.md` — D&C 88:119 captured exactly; references the ES emergency-stop incident as the source for the runaway-agent paragraph.
- `provenance_chapter_6.md` — D&C 82:10 exact; Mosiah 18:8-10 paraphrase honest (notes it as a paraphrase rather than direct quote); covenant.yaml commitments listed by name as the source of the manuscript's bilateral framing.

### Meta-observation about provenance discipline

The provenance system is good in concept — every chapter has a `.scratch/provenance_*.md` file naming its sources, quotes, and target gospel-library paths. But the implementation has three failure modes worth naming for council:

1. **Errors propagate without being caught.** When the manuscript drifts (Ch 4's seventh-day mis-quote), the provenance file copies the drift rather than checking against canon.
2. **The provenance can be more wrong than the manuscript** (Ch 7's fabricated 104:11-12 wording). This means provenance is being generated *after* the chapter rather than *before* — and from memory or paraphrase rather than from canon. The CLAUDE.md says "ensures a complete, verifiable audit trail." Right now, four of nine provenance files do not satisfy that.
3. **The provenance can be more right than the manuscript** (Ch 5's D&C 88:32). This is actually working as designed when it happens — the provenance preserves the canon, and a future audit catches the manuscript drift.

**Council suggestion:** the provenance-writing pass should always include a `read_file` of the gospel-library source before writing the provenance entry, and the quote in provenance should be checked against canon character-for-character (the same standard the manuscript holds). If we treat provenance as cheap, it can't do the job it was made for.

---

## Section 8 — Verification Status (COMPLETE)

All initially-flagged outstanding items are now resolved:

| # | Item | Result |
|---|------|--------|
| 1 | Ballard, "Counseling with Our Councils" | 🟢 exact |
| 2 | Hinckley, "In … Counsellors There Is Safety" | 🟢 exact |
| 3 | Moses 3:5 (Ch 3 anchor) | 🟢 exact (with correct ellipsis omitting rain-clause) |
| 4 | D&C 29:32 (Ch 3) | 🟢 exact partial — also has unused second-half clause ("and again, first temporal, and secondly spiritual, which is the last of my work") that could enhance Ch 3 |
| 5 | D&C 82:10 (Ch 6 anchor) | 🟢 exact |
| 6 | Mosiah 18:8-10 paraphrase (Ch 6) | 🟢 accurate paraphrase, all three reciprocal elements (bear burdens, stand as witnesses, pour out Spirit) present in canon |
| 7 | Mosiah 18:18 (Ch 7) | 🟢 exact partial |
| 8 | Exodus 18:17-18, 18:21 (Ch 7) | 🟢 exact partial with correct ellipsis |
| 9 | Matthew 10:1 (Ch 7) | 🟢 exact partial with correct ellipsis |
| 10 | 2 Peter 1:4 (Ch 4) | 🟢 exact |
| 11 | Tony Trejo Medium article | 🟢 exact (note URL redirect to consider updating) |
| 12 | Milan Jovanović LinkedIn | 🟢 exact (consider quoting fuller pairing) |
| 13 | Webster 1828 *spirit* | 🟢 all three phrases exact |
| 13b | Webster 1828 *intelligence* | 🔴 quoted phrase "understanding; skill; the faculty of understanding" not found in workspace's Webster MCP entry — needs reconciliation against 1828.ibeco.me browser view |

---

## Summary — Council Decision Inventory

**ALL council items closed 2026-05-27. Summary:**

**Hard manuscript errors (3 of 3 resolved):**
1. ✅ Ch 4: Abr 5:2 paragraph rewritten to honor what v.2 actually says + Moses 3:2 added as the explicit evaluation anchor (commit 2026-05-26).
2. ✅ Ch 1: Webster 1828 *intelligence* quote verified against three sources (MCP, raw JSON, 1828.ibeco.me canonical path) and replaced with verbatim canon from senses 1 and 2: "the exercise of the understanding" and "the capacity to know or understand" (commit 2026-05-27).
3. ✅ Ch 0: cite changed from `D&C 84:44–45` to `D&C 84:45` (commit 2026-05-26).

**Soft precision improvements (4 of 4 resolved):**
4. ✅ Ch 5: D&C 88:32 replaced with canonical wording "enjoy that which they are willing to receive, because they were not willing to enjoy that which they might have received" (commit 2026-05-27).
5. ✅ Ch 7: Abr 4:18 reuse across Ch 4 and Ch 7 acknowledged via the council ratification — Ch 7 now anchors the delegation schema on Matt 10:1–16 with verse-by-verse cites; Abr 4:18 stays as the "watching" cross-reference. The reuse is structural, not redundant (commit 2026-05-27).
6. ✅ Provenance preface "created" → "counseled" fix shipped 2026-05-26 (redemption commit).
7. ✅ Ch 1 Trejo URL updated to canonical post-redirect destination (commit 2026-05-27).

**Cross-chapter tensions (6 of 6 ratified and applied):**
- T1 (Ch 0 vs Ch 5 redundancy) — Path B: differentiate by binding question. Ch 0 keeps its ontology + "not magic conjurers" close. Ch 5's Engineering Parallel rewritten to pivot from re-deriving vector-space math to the posture/practice angle.
- T2 (11-step cycle enumeration) — new reference page added between Introduction and Ch 0 with verb-paired list, two muted hues (slate-blue for [eng] steps 1/4/5/6, sage/amber for the seven), inline [eng] tags. Step 8 "Atonement — re-aiming" refined from [study/hope-and-the-grammar-of-pairs.md](../../../study/hope-and-the-grammar-of-pairs.md).
- T3 (vibe coding) — left as-is; the em-dash inline definition does the work.
- T4 (Ch 7 four-element schema) — sharpened with verse-by-verse Matt 10 anchors. Schema now reads as discovery from text, not framework imposed on top.
- T5 (I vs we pronoun shifts) — convention note added to Preface; voice audit confirmed the book already follows the convention (all "I" instances are personal experience or first-person commitments).
- T6 (Becoming app locator) — ibeco.me link added in Ch 3 (commit 2026-05-26).

**New artifacts:**
- Ch 6 honest-footnote production-note sidebar (placeholder text — Michael's voice surgery pending).
- New file: `src/chapters/00_eleven_step_reference.md`.
- New CSS: `.production-note`, `.cycle-list`, `.eng-step`, `.scripture-step`, `.cycle-step-name`, `.cycle-step-verb`, `.eng-tag`.
- New provenance file: `.scratch/provenance_eleven_step_reference.md`.

**Pending Michael (low-stakes):**
- Voice surgery on the Ch 6 production-note sidebar placeholder text. Shape is locked; voice is open.
- book.yaml chapter order — I moved Introduction before Ch 0 to make the reference page placement coherent. If you prefer the original (Ch 0 before Introduction), revert is one line in book.yaml.

**Cross-chapter tensions for council (T1-T6 in Section 4):**
- T1: Ch 0 vs Ch 5 redundancy on "intelligence cleaveth" vector-space argument.
- T2: 11-step cycle invoked without single-place enumeration.
- T3: "Vibe coding" used without defining.
- T4: Ch 7 four-element delegation schema may be manufactured rather than textual.
- T5: "I" vs "we" pronoun shift never signaled.
- T6: Becoming app referenced without locator.

**Enhancement opportunities surveyed in Section 5** — workshop in council. Several real session artifacts (bridge stall, ES emergency stop arc, Section VII catch, voice-analysis study, art-of-presidency arc, judges-not-executors principle) are absent from the book despite directly fitting specific chapters.

**Things to NOT change (Section 7):**
- The theological architecture (4 disciplines → 11-step cycle → Sections II/III on the unmapped 7).
- Gemini's voice work — consistent, clean, Michael-like.
- The 3.5-year journey passage in the Preface.
- The bilateral covenant clarity in Ch 6 — sharper than the YAML.

---

*Reviewer notes: this audit cost about 20 minutes of read-before-quoting work. Every direct scripture quote and every cited conference talk was opened in the gospel-library and compared character-by-character. External web citations were checked against live sources where reachable. The book is in genuinely good shape — three real corrections, four precision tightening, and a half-dozen council-level decisions about depth-vs-breadth. Net: it does what it set out to do.*
