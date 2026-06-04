# Weave plan: the pg-ai-stewards audit lessons → the manuscript

**Drafted 2026-06-04 by Claude Opus 4.8 (Claude Code), for Michael to review.**
Then we walk it together, lesson by lesson, via AskUserQuestion — same cadence as the
condensation walk: I present the concrete edit + options, you gate each one.

## Where this comes from

The pg-ai-stewards session produced an honest audit of the substrate against the
11-step cycle, plus a lived case study of the critic-harness build:

- `projects/pg-ai-stewards/docs/work-with-ai/2026-06-04-blueprint-vs-implementation-audit.md`
- `projects/pg-ai-stewards/docs/work-with-ai/examples/2026-06-04-substrate-critic-harness-creation-cycle.md`

Both now carry the corrected floor-vs-ceiling framing (the full-context shepherd caught
glm's race, not "a human"). The audit hands six cross-cutting lessons, each mapped to a
chapter. This document turns each into a concrete proposed edit.

## The tension to hold (read this first)

**We just finished a condensation pass.** Every chapter below was tightened on purpose.
So the question for each lesson is not "is it true?" (they all are) but **"does this
lived substrate example earn its place, or is the chapter already complete?"** For each,
I give a *full* version and a *light* version, and an honest recommendation — including
where I think the honest answer is **skip**. Adding five new passages to a book we just
condensed would undo the work; the goal is to add only what genuinely deepens a chapter.

**Two global caveats** (apply wherever the substrate is cited):
1. **The bake-off is n=1.** "All four models passed / the model barely mattered" came
   from *one task*. Anywhere that reaches the page it needs "on one task" framing, or it
   becomes a 99%-style stat asserted as a law.
2. **Rhyme, not identity.** A capped revise-loop *rhyming* with the Atonement is fine; a
   revise-loop that *is* the Atonement overreaches — the same thing we softened in Ch
   9/10/12. Any atonement parallel must carry Ch 8's existing "the shape rhymes, the
   substance does not" humility.

---

## Lesson 1 — Floor vs. ceiling → Chapter 4 (*Watched Until They Obey*)

**The lesson:** automated gates (tests, evals, type checks, even a reviewing model)
raise the *floor*; full-context vigilance — whoever holds the whole arc — holds the
*ceiling*. glm-5.1's latent data race passed the compiler, vet, `-race`, *and* the
critic model, and the orchestrating Opus shepherd caught it. The axis is
full-context-vs-narrow-gate, **not** human-vs-AI; the human stays the **Hinge** (merge
authority).

**Where it lands:** Ch 4's Engineering Parallel. The chapter already lists the
instruments (¶40: "Test suites and evals… Observability traces… Watchdogs and
budgets…") and already closes on moral agency (¶48–50: "AI has no moral agency… Your
moral agency… is the irreplaceable element"). The cleanest home is a **bridge paragraph
inserted just before ¶48** — so the chapter climbs: narrow gate → full-context watcher →
moral agency. That ordering makes the new material *strengthen* the existing agency
close instead of competing with it.

**Current ¶48 (the bridge target):**
> "This feedback loop works because of the distinction in agency. As Doctrine and
> Covenants 93:30 states, 'All truth is independent in that sphere…'"

**Proposed edit (DRAFT) — insert before ¶48 — TWO paragraphs. Strengthened 2026-06-04
by Michael's "the ceiling moves" insight: the original draft only had one direction (the
AI caught what the human missed). We have now lived BOTH directions — so the lesson can
show the watching passing back and forth, which is what proves it isn't human-vs-AI:**
> Even so, every one of these instruments is a gate, and a gate sees only its slice: the
> tests see the paths they exercise, the budget sees tokens, even a second model reviewing
> a change sees only the change. None holds the whole. In one comparison of four models on
> a single task, a model's code cleared the compiler, the linter, the race detector, and a
> separate reviewing model — every automated gate — and still hid a subtle flaw none of
> them was positioned to catch, because no test exercised the path that exposed it. What
> caught it was the one vantage with the entire build in view. The narrow gates raise the
> floor; the watcher who holds the whole picture is the ceiling.
>
> And that vantage is not fixed to one side. It moves. The agent orchestrating a build
> once caught a flaw I had read past — it held the whole arc while I was looking at the
> parts. And the reverse happens just as often: a model hands me an answer that is fluent,
> confident, and wrong, and I catch it in a breath, because I am holding a piece of ground
> truth it never had. The ceiling is not the human and it is not the machine. It is
> whoever, in that moment, holds the whole, and the watching passes back and forth between
> us. The loop needs both, and neither can be retired from it. Above even that shared
> vantage sits the thing no instrument and no orchestrator supplies at all.

…which flows straight into the existing ¶48 ("…the distinction in agency"). "The thing no
instrument… supplies" = moral agency = the human's. The two lived cases — the orchestrating
agent catching glm's race (AI held the whole), and Michael catching the model's
confident-wrong tool name (human held the ground truth) — are the two directions of one
principle, which is exactly why this framing can't collapse into human-vs-AI.

**Notes / caveats:** carries the n=1 caveat inline ("four models on a single task").
Harmonizes with ¶50 rather than contradicting it (gate < full-context watcher < moral
agency). Ch 4 already references the Ch 2 runaway, so this keeps Ch 2 ↔ Ch 4 linked.

**Recommendation: ADD (full version).** This is the strongest of the six — it's the most
credible idea in the audit, it has a vivid lived example, and it threads *into* the
chapter's existing climax. The one I'd most want in the book.

---

## Lesson 2 — Acceptance criteria, not just a binding question → Chapter 3 (*Spiritual Before Temporal*)

**The lesson:** a thin spec (one binding question) is necessary but not sufficient. The
executable spec needs acceptance criteria a reviewer can check item-by-item. The
night-build gap (a presence tracker built *global* when the design implied *per-room*)
happened because the spec never said "room-scoped," so nothing required it.

**Where it lands:** Ch 3's Engineering Parallel, right after the 743-line-spec story
(¶35). **Note: this EP was condensed from ~10¶ to 3¶ this session** — adding back a full
paragraph partly undoes that. So I lean light here.

**Current ¶35 (end):**
> "…the foundation was sound from the start, because the design was sound first. Moses
> 3:5 had the pattern long before we did."

**Proposed edit (DRAFT):**

*Option A — light (1–2 sentences appended to ¶35):* **(recommended)**
> But length was not what made it work; checkability was. A specification earns its keep
> when every requirement in it is something a reviewer can later hold the finished work
> against, item by item — and the places a spec stays vague are exactly the places the
> build later drifts, because what the design does not require, the code does not deliver.

*Option B — fuller (new paragraph with the lived counter-example):*
> The cost of skipping that is concrete. An agent once built a feature of mine cleanly —
> it compiled, the tests passed — and shipped exactly the wrong thing: a tracker built to
> span everything when the design needed it scoped to a single room. The spec had never
> said "scoped to a room," so nothing required it, and the tests, written to the same
> thin spec, certified work that did the wrong job correctly. A complete spiritual
> creation is not just long; it names the constraints a reviewer can check, so that
> "correct" and "right" cannot drift apart.

**Notes / caveats:** Option B re-expands a chapter we just trimmed. Option A delivers the
insight (checkability > length) in two sentences and keeps the condensation intact.

**Recommendation: ADD (Option A).** The "checkability, not length" sharpening is a real
addition and costs almost nothing. Option B only if you want the lived counter-example.

---

## Lesson 3 — Granted-vs-earned context → Practice 4 (*Pack the Context, Waste Nothing*)

**The lesson:** the practice assumes the agent can *reach* the library. A sandboxed or
sub-agent can't — it sees one repo, not the workspace. So line-upon-line inverts: context
*earned* (the agent demonstrates readiness, gets more) flips to context *granted* (the
steward hands it what it cannot reach). Isolation decides which applies.

**Where it lands:** p1_04, after ¶11 (the "window half"). This is a Part One **practice**,
so the addition must stay in practice voice (first-person, concrete) — **not** doctrine.

**Proposed edit (DRAFT) — new paragraph after ¶11:**
> There is a sharp edge to this, and I found it the hard way. Both motions assume the
> agent can reach the shelf. Sometimes it can't. When I send an agent into a sandbox — an
> isolated copy of one repository, walled off from the rest — it cannot browse the
> library at all; it sees only what I packed into the box before I closed the lid. "Do it
> the way we did it on the other service" is then an instruction it literally cannot
> follow, because it cannot open the other service. When that happens the discipline
> flips: what the agent normally pulls for itself, I now have to hand it — the pattern,
> the contract, the example — placed in the box up front. Reaching for context is the
> agent's job when it can; granting it is mine when it can't.

**Optional Remember-box addition:** "…and when the agent is boxed in (a sandbox, a
sub-agent), it cannot reach the shelf at all — then you must hand it what it needs."

**Notes / caveats:** lengthens a tight practice. But it's genuinely the same practice's
missing half, and it's a lived scar (fits the practice format perfectly). Stays in Part
One register — no Binding Question / Modular elements.

**Recommendation: ADD (full).** It completes the practice rather than padding it.

---

## Lesson 4 — Atonement as forward-recovery → Chapter 8 (*The Mechanics of Refinement*)

**The lesson:** error-recovery in the pipeline doesn't revert → it names what's wrong
(the learning), injects it, and the next attempt *moves forward changed*. "Go thy way and
sin no more," not "retry from blank." The engineering shadow of repentance-as-re-aiming.

**Where it lands:** Ch 8's EP. **Caution:** Ch 8's EP is already complete and is *not*
about error-recovery — it's about the developer refined by the loop against the
Christ-prototype. It already contains repentance-as-re-aiming (¶43: "Repentance… is not
first a re-doing of behavior. It is a re-aiming of the eye") **and** the rhyme/substance
humility (¶45). So a full new beat risks both redundancy and re-bloat.

**Proposed edit (DRAFT):**

*Option A — light (append to ¶43, riding the existing re-aiming point):* **(recommended)**
> The engineering loop shows the same refusal to start over: when the output misses, you
> do not delete the work and begin from a blank page — you name what was wrong, carry the
> correction forward, and the next attempt is the same work moved on, changed by the
> correction rather than erased by it. Repentance is that motion, not the deletion of the
> self for a fresh one: the same soul, re-aimed, carrying the correction forward.

(¶45's existing "the shape rhymes, the substances do not" then covers the humility — no
new caveat sentence needed.)

*Option B — skip.* The chapter may already say everything this lesson would add.

**Notes / caveats:** this is the lesson with the **least room**. If added, Option A only,
and lean on ¶45's existing humility (do **not** write "the revise-loop is the Atonement").

**Recommendation: LIGHT or SKIP.** Honest read: Ch 8 is close to complete. I'd add
Option A only if it reads as a deepening when you see it in place; otherwise skip and let
the chapter stand. Your call when we walk it.

---

## Lesson 5 — Zion staffing = measured-gift council → Chapter 12 (*From Consecration to Zion*)

**The lesson:** a ward council is staffed by *gift* — and the engineering version makes
the discernment explicit by *measuring* the gift (the bake-off as the council interview)
before assigning a model to a pipeline role. Step 3 (stewardship by ability) meeting Step
11 (Zion). Assignment on evidence, not reputation.

**Where it lands:** Ch 12's EP, after the ward-council paragraph (¶35) or the
"pattern is older" paragraph (¶41). Ch 12's EP was just softened to first-person
aspiration ("the architecture I keep building toward") — this addition must stay in that
register.

**Proposed edit (DRAFT) — new short paragraph after ¶35:**
> A ward council is also staffed by gift. Callings are extended by discerning what each
> person is given to do — scripture is explicit that the gifts are distributed, that not
> everyone has every one, and that each is given a gift to profit the whole [D&C 46:11–12
> — verify and quote when we walk it]. The version I am building makes the discernment
> explicit: before I assign a model to a role in the pipeline, I measure its gift. I have
> run one task through several models side by side — not to crown a winner, but to see
> what each is actually good at: which writes the leanest correct code, which documents
> best, which is the sharpest critic. The council is staffed on evidence of the gift, not
> on reputation — assignment-by-measured-gift under a shared intent.

**Notes / caveats:** (1) the D&C 46:11–12 anchor is **unverified** — I have not read it
this session; I've paraphrased and flagged it. We verify and quote it during the walk
(read-before-quoting). (2) Keeps the n=1 caveat honest by making the point about the
*method* (measure, don't assume), not the result. (3) First-person, consistent with the
softened Ch 12.

**Recommendation: ADD (full), pending the D&C 46 verification.** It's a real extension of
the ward-council argument and a strong Step-3-meets-Step-11 bridge.

---

## What I'm NOT proposing
- Touching the Ch 2 harness beat again (just revised; it already carries the Sabbath
  honesty and the "six of seven").
- A new chapter or section. These are surgical additions to existing EPs / one practice.
- Anything that re-opens the condensation decisions.

## Proposed walk order (when you're ready)
1. **Ch 4** — floor/ceiling (the strongest; full).
2. **p1_04** — granted context (completes the practice; full).
3. **Ch 12** — measured-gift council (full; verify D&C 46 first).
4. **Ch 3** — acceptance criteria (light, Option A).
5. **Ch 8** — forward-recovery (light or skip — judge in place).

Verify-gated as before: diff-confirm no scripture/quote/doctrine lost; any new scripture
read from canon and quoted character-for-character before commit; rebuild + render-check;
0-collision check.

## Open questions for you
1. Any lesson here you'd rather **not** weave at all? (Ch 8 is my own candidate for skip.)
2. For Ch 3 and Ch 8: light versions, or the fuller lived counter-examples?
3. The bake-off result ("model barely mattered") — keep it out of the prose entirely
   (n=1), or include with the "on one task" hedge? I've kept it out of every draft above
   except as method; flag if you want it stated.
