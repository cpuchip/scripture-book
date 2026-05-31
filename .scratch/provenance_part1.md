# Provenance: Part 1 — "The Front Porch" (the scars)

*Created 2026-05-30 by Claude Opus 4.8; framing updated same day (scar → story). Part 1 teaches each practice through **the story that taught it** — which can be a failure we learned from, a spectacular **success** where the principle paid off, or (best) a **scar→fix→payoff arc**. This file is the verification gate for those stories BEFORE they become prose. Part 2 provenance verifies **scripture**; Part 1 verifies **lived claims** — every date, token count, name, and quote is a factual/biographical claim under the cite-count rule (verify, don't recall). **Guardrail (Ben Test):** where a real failure exists, lead with it — vulnerability read as the book's #1 credibility signal in the audit; use success where there's no scar or where it teaches better; keep the failures in — don't curate down to a brag reel. (See the "scar vs. success per practice" addendum near the end for the lead recommendation on each.) Sources: this project's git history (commit hashes + dates below), `.spec/journal/` entries, `.mind/`/`MEMORY.md`, `.spec/covenant.yaml`, the `ben-test` skill, and `.draft/20260530-how-we-actually-work.md` (the chat-log mining). Bridge scriptures are Part 2 anchors already verified in their own `provenance_chapter_*` files (or this session); cited here, not re-verified, except Mosiah 4:27 (verified fresh).*

*Consolidated while Part 1 is still a skeleton (`.spec/part1-skeleton.md`) and the practices may reshuffle per Michael's read. Split into per-chapter `provenance_*.md` files when each chapter is drafted.*

---

## P1 — Talk, Don't Command *(find the vision in the conversation)*
- **Scar:** Michael wrote this book doctrine-first for ~5 months and didn't know what it actually *was* — too preachy, not teaching AI — until the 2026-05-30 council talked its true shape (one book, two parts) into being. He didn't start with a question; he had a vision he couldn't yet see, and the conversation found it.
- **Evidence / sources:** `.spec/journal/2026-05-30--book-identity-pivot.yaml`; `.draft/20260530-how-we-actually-work.md` (the mining: "real method is discover-the-vision-by-iterating, not spec-first"; Michael's own words *"sometimes I know exactly what that vision is… other times I don't… but as we work together we find it."*); `.spec/journal/2026-05-30--planning-council.yaml`.
- **Principle (eternal):** You start with a vision, not the answer; the conversation converges on it. Promptcraft *is* the conversation.
- **Bridge → Part 2:** Intent (Step 1) · Spiritual Creation, Moses 3:5 · counsel, Abraham 4:26 — verified in Part 2 anchors (`provenance_chapter_3`, etc.).
- **To verify at draft:** quote Michael's "we find it" line verbatim from the mining file / source session.

## P2 — Council Before You Build *(we should have done this from the start)*
- **Scar:** Section VII of the stewardship study was **wrong** — it contradicted the guide's Step 2 (Covenant) because the agent didn't check existing work or counsel first. Michael caught it. That failure **birthed the covenant** (`.spec/covenant.yaml`, created 2026-03-22). Recursively: this book's whole identity pivot came from finally *counciling* its shape — "this council thing is what we should have done from the start."
- **Evidence / sources:** `.spec/covenant.yaml` (`flag_when_wrong` + `check_existing_work` both cite the Section VII incident verbatim); `study/stewardship-pattern.md` § VII; `.spec/journal/2026-05-30--planning-council.yaml` (the recursion). Book history of council-vs-no-council: `a6a1501 2026-05-26 Apply no-council manuscript fixes` vs. `639fa32` council-execution.
- **Principle (eternal):** Council and ratify before building; the plan is the spiritual creation; skipping it forces the AI to guess and the guesses compound.
- **Bridge → Part 2:** Covenant/Council — Abraham 4:26, Mosiah 18; Spiritual Creation (Ch 3, Moses 3:5).
- **To verify at draft:** confirm Section VII specifics against `study/stewardship-pattern.md` (read the actual section) and the covenant's wording.

## P3 — Set the Bounds, Then Let Go *(intent · covenant · stewardship)*
- **Scar:** An autonomous research agent looped on one topic (the "bacteriopolis" exhibit run) and burned **230 million input tokens** before the emergency stop — no watchdog, no budget, no bound. The fix arc was Batch "ES" (emergency-stop), 2026-05-15/16.
- **Evidence / sources:** `230 million input tokens` is **verified** in book **Ch 2** (`02_four_disciplines.md`, Tier 3.4 fix — replaced the unverified "ten hours"). MEMORY `project_substrate_ES_emergency_stop` ("2026-05-15 bacteriopolis runaway, CLOSED"). Substrate commits: ES.5 `4280de7 2026-05-16`, ES.6 streaming `801b247 2026-05-16`, bacteriopolis exhibit `ccbd2ec/3ba0aef 2026-05-16`. Also the enforced Gemini prepaid spend-cap, J.11 `c3cc2cc` (a bound added *after* the fact).
- **Principle (eternal):** Bounded authority + budget + an account; the upstream structures (intent/covenant/stewardship) do the heavy lifting so you watch *less* as they mature.
- **Bridge → Part 2:** Intent · Covenant D&C 82:10 · Stewardship D&C 104 / Ex 18 / Matt 10 · Watching Abraham 4:18 — verified in Part 2 anchors.
- **To verify at draft:** confirm exact runaway date (MEMORY says 2026-05-15) against the ES/bacteriopolis journal; keep "230 million" (already verified, do not drift).

## P4 — Pack the Context, Waste Nothing *(what goes IN)*
- **Scar:** A fan-out where **4 of 6** child agents died on the token limit (substrate Batch J.3) because the window was packed with noise — which forced building **engram-based context compaction** (Batch K, shipped 2026-05-14).
- **Evidence / sources:** MEMORY `project_substrate_batch_j_plan` ("J.3 partial — 4 of 6 children failed with token limit — drove Batch K's existence") and `project_substrate_batch_k_plan` ("SHIPPED 2026-05-14: engram-based context compaction; all 9 phases K.1-K.9").
- **Principle (eternal):** Curate what the model has in view; build understanding line upon line; the context window is sacred space.
- **Bridge → Part 2:** Line upon Line (Step 5) · house of order, D&C 88:119.
- **To verify at draft:** confirm "4 of 6" + the Batch K ship date against the substrate journals (`.spec/journal/2026-05-*-substrate-*`).

## P5 — Make It Portable *(have the agent journal its work — what comes OUT)*
- **Scar:** This book was drafted across **three different AI tools** — GitHub Copilot (Claude inside VS Code), then Claude Code CLI, then Gemini (Antigravity) — over months. It held together only because the memory lived in the **workspace** (`.mind/`, `.spec/journal/`, `MEMORY.md`), not in any one tool's chat. Sessions that skipped the journal "arrived as a stranger" and re-derived or contradicted settled work; Michael flagged memory gaps more than once.
- **Evidence / sources:** the **colophon** (`00_frontmatter.md`) names the three tools explicitly; the **Afterword** chronology dates them (Sept 2022 Copilot → Oct 2024 Copilot+Claude 3.5 Sonnet → spring 2026 Claude Code CLI + Gemini). `.spec/covenant.yaml` `agent_commits_to.update_memory` ("an agent that arrives as a stranger every time cannot be a covenant partner"). Workspace CLAUDE.md: "Michael has flagged memory gaps multiple times."
- **Principle (eternal):** Have the agent write its work down — done/decided/learned — into memory that lives in *your workspace*, not the chat. Portable memory survives context loss, session boundaries, and tool/model switches. *"The shortest pencil is longer than the longest memory"* (Agans, *Debugging*, Ch 8 — attribute).
- **Bridge → Part 2:** Line upon Line (continuity) · Consecration (the record persists/shared).
- **To verify at draft:** confirm the three-tool sequence + dates against the Afterword (already in-manuscript); attribute the "shortest pencil" line to Agans.

## P6 — Let It Carry What You Can't *(research · tools · delegation)*
- **Scar:** pg-ai-stewards — a Postgres/Rust substrate — is built in **Rust + SQL, languages Michael does not write.** He delegated work beyond his own competence, with verification as the safety rail, and it produced a working substrate. The inverse scar: a keyword search missed **2 Peter 1:4** ("partakers of the divine nature") until the agent was directed to the semantic vector tool (already told in book Ch 4).
- **Evidence / sources:** MEMORY `user_michael_background_workstyle` ("18yr eng (Go/Python/C++/Java/C#/TS/JS/Vue3/MongoDB); does NOT write Rust/SQL → pg-ai-stewards is beyond-competence, verification discipline matters most there"). Workspace journal `218ea4d 2026-05-29 journal: trust beyond competence — what the principles actually buy`. The 2 Peter 1:4 story: book Ch 4 (`04_watched_until_they_obeyed.md`, verified).
- **Principle (eternal):** Let the AI do the heavy lifting — research, tools, work you can't/shouldn't do by hand — and verify the fruit. Stewardship scales one person.
- **Bridge → Part 2:** Stewardship — Jethro/Ex 18; Matt 10 · Physical Creation.
- **To verify at draft:** the 18-years + not-Rust/SQL biographical claim (Michael to confirm); 2 Peter 1:4 already verified in Ch 4 provenance.

## P7 — Assume It Will Lie to You *(provenance · skills · MCPs against hallucination)*
- **Scar (primary):** A draft of **this book** fabricated a **D&C 104:11–12** quote — the manuscript text was right, but the audit-trail/provenance file had **invented canon**. Caught in the 2026-05-26 audit. (A second fabrication — a Ch 9 anchor — was caught the same arc.) A book about AI *and* the gospel nearly shipped a fabricated scripture.
- **Scar (secondary):** A shell-grep streaming probe falsely concluded **glm-5 "streams empty"**; the substrate's real SSE parser (auto-probe) proved it streams fine (385 chars). *Verify via the real path, not a parser you just wrote.*
- **Evidence / sources:** Book CLAUDE.md (`.github/copilot-instructions.md`) documents the fabricated D&C 104:11-12 verbatim; `.spec/journal/2026-05-26--claude-audit-and-provenance-redemption.yaml`; MEMORY `project_scripture_book_provenance_redemption`. Book commits: `a6a1501 2026-05-26`, `31e5349 2026-05-27` ("identify manuscript fabrications"), `a735201 2026-05-27` ("Fix Ch 9 anchor fabrication"). glm misdiagnosis: substrate `f87edde 2026-05-29 correct: glm-5/5.1 stream fine — overturn my shell-grep misdiagnosis`, `63236c6`; MEMORY `feedback_verify_via_real_path`.
- **Principle (eternal):** AI confabulates with confidence. Build verification gates — read before quoting, provenance as a gate not a footnote, verify via the real path — and encode them in skills/MCPs so the discipline survives time pressure.
- **Bridge → Part 2:** Watching (Abr 4:18) · Atonement · "tools failing under law, not souls under sin" (Ch 6 — the AI-failures-as-doctrinal-types passage).
- **To verify at draft:** the D&C 104:11-12 fabrication details against the 2026-05-26 audit file; glm details against the substrate workflow-doc/journal.

## P8 — Ask What's in the Way *(the retro)* — RETRO THREAD anchor 1
- **Scar:** Michael's coworker **Ben**, **March 19, 2026**: *"Your AI is very complimentary. Perhaps too complimentary?"* That question triggered an honest self-assessment of the 11-step creation cycle — **~33% practice rate.** We had been telling others what they could learn from principles we hadn't implemented ourselves. The **Ben Test** was born; the periodic retro became the single biggest improver of the work.
- **Evidence / sources:** the **`ben-test` skill** (verbatim origin: date, quote, "~33% practice rate"); book commits `42f93e5`/`3cb6aff 2026-05-29` (Ben Test calibration pass). `.spec/covenant.yaml` § teaching (`ben_test_every_episode`, "Your AI is very complimentary…" quoted). Michael's own retro cadence: chat-mining notes he still runs it every few weeks (his stated "single biggest early help").
- **Principle (eternal):** Periodically ask the AI: what's working, what could be better, what tools would help, what's in the way? Honesty over flattery. This is re-aiming — the practical face of Atonement.
- **Bridge → Part 2:** Atonement (Ch 8) · Sabbath/seventh-day review (Ch 11).
- **To verify at draft:** Ben quote + date are verbatim from the skill (firm); confirm Michael is comfortable naming "Ben" / wants a pseudonym.

## P9 — When You Hit a Wall, Build the Door *(workflows · your own harness)* — RETRO THREAD anchor 2
- **Scar:** 2026-05-30, two walls in one session — the substrate's lens sandbox **couldn't read the manuscript** to redline it, and the **`agy` CLI hung headless** (stdin-EOF) and dropped stdout. Instead of stopping, we built the doors: a substrate **`redline` pipeline** (`panel_redline`, stew shipped R.1–R.6) and the **`agy-cli`** recipe/skill. The far end of this instinct is **pg-ai-stewards** itself — a whole opinionated harness built because off-the-shelf tools didn't fit the intent.
- **Evidence / sources:** `/.spec/proposals/substrate-multimodel-document-redline.md` (use-case, failure, the ratified+shipped R.1–R.6); `.claude/skills/agy-cli/SKILL.md` (the two-bug recipe); this session's journals. pg-ai-stewards as the harness: its whole repo + MEMORY `project_pg_ai_stewards_state`.
- **Principle (eternal):** When the tool doesn't exist, build it *with* the AI. The retro tells you what's in the way; this removes it. Build your workspace, your workflows, and — at the far end — your own harness.
- **Bridge → Part 2:** Consecration (giving what you made) · Zion (many agents, one intent).
- **To verify at draft:** the redline-pipeline shipped status (R.1–R.6) and agy bug specifics are documented in the proposal + skill (firm); confirm at draft they're still accurate.

## Coda — Go Touch Some Grass *(rest / incubation → the bridge into Part 2)*
- **Scar / proof:** The two-book clarity arrived while Michael was **away from screens for a few hours**; the third witness (his daughter **Leah**, age 14) came in conversation away from the keyboard, landing on the two-part idea cold. The inverse: the cycles spent flailing at a wall (the substrate fs probes) were the times we hadn't stepped back. The vision sharpens in the gap.
- **Evidence / sources:** this session's conversation (2026-05-30); `.spec/journal/2026-05-30--planning-council.yaml`. Michael's real Sabbath practice per the chat-mining: "in practicality I practice the pauses and break between the chat sessions."
- **Principle (eternal):** Rest and incubation are part of the loop, not a break from it; rest closes one cycle and seeds the next vision (back to P1).
- **Bridge scripture → Part 2 (Mosiah 4:27 — VERIFIED 2026-05-30 via `gospel_get`):** *"And see that all these things are done in wisdom and order; for it is not requisite that a man should run faster than he has strength. And again, it is expedient that he should be diligent, that thereby he might win the prize; therefore, all things must be done in order."* Holds both halves — rest (don't outrun strength) **and** diligence (win the prize) — so the coda is not laziness; "wisdom and order" opens into Part 2's ordered creation. Already quoted in the **Epilogue** (`13_epilogue_silent_loop.md`), which reinforces the hand-off. → Part 2 Sabbath (Ch 11).
- **To verify at draft:** confirm Leah's age/consent to name her; Mosiah 4:27 firm.

---

## Scar vs. success per practice — addendum (repo sweep, 2026-05-30)

Swept every workspace repo (git genesis + arc dates verified below). Each practice can lead with a failure, a success, or the arc. Lead recommendation per practice:

| Practice | Lead with | Story (verified source) |
|---|---|---|
| **P1** Talk, Don't Command | scar **+ success companion** | Scar: the book's doctrine-first drift (above). Success: **storygames** — co-writing story-games with his (afterword: nine-year-old) child. Repo `projects/storygames`, 18 commits, **2025-10-22 → 2026-04-18** ("Chapter 5: The Midnight Parade"). Conversational creative collaboration that worked — and human. |
| **P2** Council Before You Build | scar **+ success** | Section VII (above). Success: the **becoming/brain app** — a 743-line spec → 1000+ lines across 13 files (book Ch 3, verified) — spec-as-spiritual-creation paying off. |
| **P3** Set the Bounds | scar | Bacteriopolis 230M-token runaway (strong; keep). |
| **P4** Pack the Context | scar | J.3 four-of-six token deaths → Batch K engrams (keep). |
| **P5** Make It Portable | **SUCCESS-led** | Michael built an *entire externalized-memory + practices system*: **`scripts/brain` (127 commits) + `scripts/brain-app` (52), since 2026-03-01** = the becoming / ibeco.me app. Plus: this book survived being drafted across three AI tools because the memory lived in the repo. Scar demoted to a cautionary aside (sessions that skipped the journal "arrived as a stranger"). |
| **P6** Let It Carry What You Can't | **SUCCESS-led** | Delegation *built* things in languages/skills Michael lacks: **pg-ai-stewards** (Rust/SQL he doesn't write) and **simple-games** — 7 networked multiplayer games in **Dart, zero prior experience**, + WebSockets he'd never done (Afterword, Oct 2025; note: `simple-games` is not a workspace repo — cite from the Afterword). Also the site revivals via stewardship grants (`cpuchip.net`, 62 commits 2026-04-14→05-28 → autonomous Dokploy deploy). Minor scar companion: the keyword miss of 2 Peter 1:4. |
| **P7** Assume It Will Lie | scar **→ payoff (full arc)** | Fabricated D&C 104:11-12 (2026-05-26 audit) → built provenance gates **+ the `gospel-engine-v2` MCP** (`scripts/gospel-engine-v2`, 20 commits, **2026-04-18→05-13**) — the verification tool that now makes every quote checkable (it's what verified the scriptures in this very provenance file). Scar → fix → payoff. |
| **P8** Ask What's in the Way | scar | Ben / ~33% (humbling; keep). The payoff is the whole improved body of work. |
| **P9** Build the Door | scar **→ success** | Arc: this week's redline + agy walls → built `panel_redline` + the `agy-cli` skill. Pure-success companion: **1828-illuminated shipped overnight** (Vue SPA + multi-stage Docker → 1828.ibeco.me, **2026-05-20**, MVP overnight). The MCP servers themselves (gospel-engine, becoming, webster, yt, byu-citations) *are* this practice incarnate. |
| **Coda** Go Touch Some Grass | success | The away-from-screens clarity (the two-book idea + Leah, 14). |

**Net:** P5 and P6 reframe to **success-led** (the portable-memory system and the built-beyond-competence substrate/games are triumphs, not failures); P7 and P9 are **scar→fix→payoff arcs**; the rest lead with the scar, several with a success companion. The mix is what keeps it honest.

**To verify at draft (additions):** which child for `storygames` (afterword says nine-year-old; not the same as Leah, 14 — don't conflate); `simple-games` specifics from the Afterword; commit counts/dates above are from the 2026-05-30 sweep (re-confirm if cited as exact).

---

**Verification log:** Compiled 2026-05-30 by Claude Opus 4.8 from git history (hashes/dates above, three repos), `.spec/journal/` entries, `.spec/covenant.yaml`, the `ben-test` skill, `MEMORY.md`, and the chat-log mining (`.draft/20260530-how-we-actually-work.md`). Mosiah 4:27 verified character-for-character via `gospel_get`. The "230 million tokens" claim is the already-verified book Ch 2 figure. Bridge scriptures are Part 2 anchors verified in their own provenance files. **Per-scar "to verify at draft" notes flag the few specifics to re-confirm against source when each chapter's prose is written — the provenance gate stays closed until then.**
