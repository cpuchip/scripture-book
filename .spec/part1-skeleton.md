# Part 1 — "The Front Porch": Skeleton (the bones)

*Built 2026-05-30 from the ratified plan (`.spec/part1-front-porch-plan.md`), the chat-log mining (`.draft/20260530-how-we-actually-work.md`), and git/journal history. Nine workflow-first practices + a closing coda, each scar-led (Agans format), each on an eternal principle, each cross-linked into Part 2 doctrine. Scars are pulled from real, dated project history — verify the details against source when drafting each chapter (the provenance discipline applies to scars too).*

*Nine practices echoes Agans' nine rules; the coda echoes his closing chapters. Not forced — it just landed there.*

## The recursion (Part 1's secret spine)
Most of these scars are from **building this very book and its workspace**. Part 1 teaches the practices *through its own making* — the reader watches the method produce the artifact they're holding. That's the authenticity the audit said the book lives on.

## The porch door (Part 1 intro — short)
- One audience, two parts. "Two doors, one house." Start where you are; the parts cross-link.
- Part 1's promise: **the tools change weekly; these principles don't.** Each practice separates the eternal principle from the 2026 implementation, so you can carry it to whatever model you're using next year.
- These are battle scars, not a manual. We learned each one by getting it wrong first.

---

## The practices (arc: vision → council → bounds → context → memory → delegate → honest → retro → build → rest)

### P1 — Talk, Don't Command *(find the vision in the conversation)*
- **Scar:** I started writing this book and didn't know what it actually *was* until we talked it into being — doctrine-heavy, not teaching AI — five months in (2026-05-30 pivot). I didn't have a question; I had a vision I couldn't see yet. The conversation found it.
- **Principle (eternal):** You don't start with the answer. You start with a vision — often just a direction — and the conversation is how you and the AI converge on it and sharpen it. Promptcraft *is* the conversation.
- **Today (2026):** conversational, iterative prompting; reverse yourself freely; spec-first for *code*, conversational for *meaning*.
- **→ Part 2:** Intent (Step 1) · Spiritual Creation (Moses 3:5) · counsel (Abraham 4:26).
- **Try this:** next build, don't write a spec first — open with "here's roughly where I want to go; help me find it," and let the vision sharpen in the back-and-forth.

### P2 — Council Before You Build *(we should have done this from the start)*
- **Scar:** Section VII of the stewardship study was *wrong* — it contradicted work we'd already done, because it was built without checking existing work or counseling. Michael caught it. That failure birthed the covenant. (And recursively: this book's whole identity pivot came from finally *counciling* about what it should be — "we should have done this from the start.")
- **Principle (eternal):** Council and ratify before you build. The plan is the spiritual creation; skipping it forces the AI to guess, and the guesses compound into structural bugs.
- **Today (2026):** AskUserQuestion ratification batches; plan-first; check existing work before claiming.
- **→ Part 2:** Covenant/Council (Abraham 4:26, Mosiah 18) · Spiritual Creation (Ch 3).
- **Try this:** before your next big task, make the AI surface 2–3 options and the tradeoffs, and ratify one — out loud — before a line is written.

### P3 — Set the Bounds, Then Let Go *(intent · covenant · stewardship)*
- **Scar:** An autonomous research agent looped on one topic and burned **230 million tokens** before we hit the emergency stop (bacteriopolis runaway, 2026-05-15). No watchdog, no budget, no bound. (Also: the Gemini prepaid spend-cap we had to *enforce* after the fact, J.11.)
- **Principle (eternal):** Bounded authority + a budget + an account. Set intent, covenant, and stewardship up front; they do the heavy lifting so you watch *less* as they mature. (Watching fades as the upstream structures hold.)
- **Today (2026):** `intent.yaml`, `covenant.yaml`, per-agent scope + token budget + a watchman/check-in.
- **→ Part 2:** Intent · Covenant (D&C 82:10) · Stewardship (D&C 104) · Watching (Abraham 4:18).
- **Try this:** before delegating, write the bound: what it owns, what it must not touch, the budget, and when it reports back.

### P4 — Pack the Context, Waste Nothing *(layering through files & memory — what goes IN)*
- **Scar:** A fan-out where 4 of 6 agents died on the token limit (J.3) because we packed the window with noise — which forced us to build engram compaction (Batch K).
- **Principle (eternal):** Curate what the model has in view; build understanding line upon line. The context window is sacred space — fill it with what matters, not everything.
- **Today (2026):** filesystem layering, knowledge stores/MCP, retrieval, engram compaction.
- **→ Part 2:** Line upon Line (Step 5) · the house of order (D&C 88:119).
- **Try this:** before a long task, ask the AI what it needs *in view* to do it well — then give it exactly that, no more.

### P5 — Make It Portable *(have the agent journal its work — what comes OUT)*
- **Scar:** This book was drafted across **three different AI tools** — GitHub Copilot, then Claude Code, then Gemini — over months. It only held together because the memory lived in the *workspace* (the `.mind/` files, the journals, `MEMORY.md`), not in any one tool's chat. Every session that skipped the journal arrived as a stranger and re-derived — or contradicted — what we'd already settled. (Michael flagged memory gaps more than once; that's why `update_memory` is in the covenant.)
- **Principle (eternal):** Have the agent write its work down — what was done, decided, and learned — into memory that lives in *your workspace*, not the chat. Portable memory survives context loss, session boundaries, and tool/model switches. *The shortest pencil is longer than the longest memory.*
- **Today (2026):** `.mind/active.md`, `.spec/journal/`, `MEMORY.md`; the covenant's `update_memory` clause; portable across Copilot / Claude Code / Gemini.
- **→ Part 2:** Line upon Line (continuity built over time) · Consecration (the record persists and is shared).
- **Try this:** end every session by having the AI write a short journal entry + update one memory file *in your repo*. Next session, have it read those first.

### P6 — Let It Carry What You Can't *(research · tools · delegation)*
- **Scar:** pg-ai-stewards is built in Rust + SQL — languages Michael *doesn't write*. He delegated work beyond his own competence, with verification as the safety rail, and it built a working substrate (2026-05; "trust beyond competence"). The inverse scar: keyword search missed 2 Peter 1:4 until we let it use the semantic tool.
- **Principle (eternal):** Let the AI do the heavy lifting — research, tool use, work you can't or shouldn't do by hand — and verify the fruit. Stewardship scales what one person can do.
- **Today (2026):** sub-agents, MCP tools, semantic search, multi-model division of labor (Claude=fidelity/logic, Gemini=voice, cheap panel=brainstorm).
- **→ Part 2:** Stewardship (Jethro, Ex 18; Matt 10) · Physical Creation.
- **Try this:** name one task you've been doing by hand that the AI could carry — hand it over with a clear bound and a verification step.

### P7 — Assume It Will Lie to You *(skills · MCPs · provenance against hallucination)*
- **Scar:** A draft of *this book* fabricated a D&C 104:11–12 quote — the manuscript was right, but the audit-trail file had *invented canon* (2026-05-26 audit). A book about AI and the gospel nearly shipped a fabricated scripture. (Also: a shell-grep probe falsely concluded glm-5 "streams empty"; the real parser proved it streams fine — *verify via the real path*, 2026-05-29.)
- **Principle (eternal):** AI confabulates with confidence. Build verification gates — read before quoting, provenance as a gate not a footnote, verify via the real path — and encode them in skills/MCPs so the discipline survives time pressure.
- **Today (2026):** provenance scratch files, `gospel_get` verification, skills, MCP servers, the cite-count rule.
- **→ Part 2:** Watching (Abraham 4:18) · Atonement (re-aiming) · false revelation vs. tools-failing-under-law (Ch 6).
- **Try this:** pick one claim the AI made today and trace it to the actual source. Build a habit (or a skill) that makes that automatic.

### P8 — Ask What's in the Way *(the retro that changed everything)* — RETRO THREAD anchor 1
- **Scar:** Michael's coworker Ben, March 19 2026: *"Your AI is very complimentary. Perhaps too complimentary?"* That one question triggered an honest self-assessment — we were practicing our own principles at ~33%. The Ben Test was born. The retro is the single biggest thing that improved the work.
- **Principle (eternal):** Periodically stop and ask the AI: what's working, what could be better, what tools would help, what's getting in the way? Honesty over flattery. This is re-aiming — the practical face of Atonement.
- **Today (2026):** the every-few-weeks retro prompt; the Ben Test; honest metrics.
- **→ Part 2:** Atonement (Ch 8) · Sabbath/seventh-day review (Ch 11).
- **Try this:** end your next session by asking the AI those four questions — and write down the honest answer, even the uncomfortable one.

### P9 — When You Hit a Wall, Build the Door *(your workspace · workflows · your own harness)* — RETRO THREAD anchor 2
- **Scar:** This week the substrate couldn't read the manuscript to redline it, and the `agy` CLI hung headless — two walls in one session. Instead of stopping, we built the door: a substrate `redline` pipeline (`panel_redline`) and the `agy-cli` recipe/skill. The far end of this instinct is pg-ai-stewards itself — a whole harness built because the off-the-shelf tools didn't fit our intent.
- **Principle (eternal):** When the tool doesn't exist, build it *with* the AI. The retro tells you what's in the way; this is how you remove it. Build your workspace, your workflows, and — at the far end — your own opinionated harness.
- **Today (2026):** custom skills, MCP servers, agent modes, pg-ai-stewards.
- **→ Part 2:** Consecration (giving what you made) · Zion (many agents, one intent).
- **Try this:** the next time you hit the same friction twice, stop and build the smallest workflow/skill that removes it — with the AI's help.

### Coda — Go Touch Some Grass *(let the ideas stew)*
- **Scar / proof:** The two-book clarity arrived while Michael was **away from screens for a few hours**; the third witness (his daughter Leah) came in conversation away from the keyboard. The inverse: the times we ground at a wall for cycles — flailing at the substrate's filesystem, retrying probes — were the times we hadn't stepped back. The vision sharpens in the gap.
- **Principle (eternal):** Rest and incubation are part of the loop, not a break from it. Stop. Go outside. Let your brain work on it while you're not. The answer often arrives when you're not at the keyboard — and rest is what closes one cycle and seeds the next vision (back to P1).
- **Today (2026):** the pauses between sessions; a real day off; literally, go touch grass.
- **Bridge scripture → Part 2 (Mosiah 4:27, verified 2026-05-30):** *"And see that all these things are done in wisdom and order; for it is not requisite that a man should run faster than he has strength. And again, it is expedient that he should be diligent, that thereby he might win the prize; therefore, all things must be done in order."* This is the hinge between the two parts: it holds **both** halves — *rest* (don't outrun your strength) **and** *diligence* (be diligent to win the prize), so the coda is not an excuse for laziness — and *"wisdom and order"* opens directly into Part 2's doctrine of ordered creation. It's already quoted in the **Epilogue**, which reinforces the hand-off.
- **→ Part 2:** Sabbath (Ch 11) — the seventh time; the cessation that makes the work nameable and the rest that remains. The Mosiah 4:27 hinge is the doorway in.
- **Try this:** when you're stuck or spinning, stop and step away. Come back and see what your brain did while you were gone.

---

## Open while drafting
- Exact scar details (dates, numbers, names) verified against source per chapter — provenance discipline.
- Ch 8's kept engineering parallel ("what's refined is the developer") — does it migrate into a P1 practice (P6? P7?) or stay in Part 2? Decide with prose in front of us.
- The recurring connective analogy (Agans had the food-allergy diary) — candidate for Part 1: "the workspace as a house you build together."
- Title slogans per chapter (the *italic* sub-titles above are working slogans).
- Part 1 ↔ Part 2 cross-link mechanics in print (part/chapter refs) vs. a later digital graph view.
- Coda placement: closing chapter of Part 1, or a hinge between Part 1 and Part 2 (rest → the deeper "why")?
