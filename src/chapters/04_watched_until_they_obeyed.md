# Chapter 4: Watched Until They Obey

*Watching*

**Binding Question:** How does the feedback loop of reviewing, steering, and verifying AI output mirror the divine pattern of Creation?

**Anchor Passage:**
> "And the Gods watched those things which they had ordered, until they obeyed."
> — [Abraham 4:18](../../gospel-library/eng/scriptures/pgp/abr/4.md?verse=18) [qr](../../gospel-library/eng/scriptures/pgp/abr/4.md?verse=18)

---

## The Core Reframe

In the scriptural account of the Creation recorded in the book of Abraham, a striking phrase appears repeatedly. Unlike the Genesis account, where creation is narrated as an instantaneous, effortless result of a spoken word ("God said... and it was so"), Abraham describes a process that requires time, active monitoring, and patient observation: "the Gods watched those things which they had ordered, until they obeyed."

The watching is not a passive footnote; it is a vital phase of the creative act. The word *until* signifies that obedience was not instantaneous. It tells us that:
- There was a temporal gap between the order and the result.
- The gap required patience and active oversight.
- The outcome was not guaranteed by the command alone; it had to be verified.

As we trace the narrative in [Abraham 4](../../gospel-library/eng/scriptures/pgp/abr/4.md), we find a beautiful trust gradient that develops between the Creators and the creation:
*   First, they confirm simple obedience: "the Gods saw that they were obeyed" (v. 10).
*   Then, they observe more complex elements: they "watched... until they obeyed" (v. 18).
*   Later, they build forward-looking confidence: they "saw that they would be obeyed" (v. 21).
*   Finally, they declare full reliability: "behold, they shall be very obedient" (v. 31).

This trust gradient shows that confidence is earned through repeated observation and verification. The Gods did not micromanage the light on day six; they focused their watching where complexity was highest. 

Furthermore, the watching extends beyond individual creations to the whole arc: the work is counseled on the front and, on the seventh time, evaluated as a finished whole and pronounced good — the Sabbath move Chapter 11 takes up in full.

---

## The Engineering Parallel

In working with AI, we live inside this feedback loop daily. Many people approach AI as a vending machine—type a prompt, get code, copy and paste it, and walk away. But any senior developer who has integrated AI tools knows that the real engineering happens in the review. We must watch the output until it obeys our design constraints.

This is the trust gradient in action. When we begin a new project or work with a new model, we must watch every line. We review the syntax, verify the database queries, and run the tests. As the model proves reliable within a specific domain, we transition from "watching until" to a calibrated trust where we focus our attention on new, complex logic.

The industry has built instruments for exactly this watching. Test suites and evals gate output before it ships. Observability traces let us inspect each step an agent takes. Watchdogs and budgets cap an agent's time, tokens, or iterations before it can run away—the runaway in Chapter 2 happened because no such watchdog was set. These are the modern instruments of "watching until they obey."

We must balance when to steer and when to let the model run. We steer when the output violates our architectural specification, when it solves the wrong problem, or when it introduces latent security vulnerabilities. We let it run when the implementation is functionally correct, even if it uses a style slightly different from our own. Like the Gods, who commanded the waters to bring forth creatures "after their kind" rather than specifying every species of fish, we specify the organizing principles and verify the outcomes.

We must also watch our instruments, not just the code. When conducting scriptural research, we might generate a list of verses. But if we fail to watch *how* we found them, we miss the depth. In one study session on the Godhead, the AI generated a clean document using keyword search. But when we verified the search method and directed it to use our semantic vector database, it instantly surfaced non-obvious, critical passages—like [2 Peter 1:4](../../gospel-library/eng/scriptures/nt/2-pet/1.md?verse=4) [qr](../../gospel-library/eng/scriptures/nt/2-pet/1.md?verse=4) ("partakers of the divine nature")—that keyword searches had missed entirely.

We also need the "seventh-day review" in our workflows. It is easy to catch syntax errors in a single session, but systemic degradation only appears over time. In our scripture project, a periodic review revealed that because search was so fast, we had started using search results as final answers. We were paraphrasing scriptures without reading the actual source chapters. By stepping back and reflecting, we caught this trend and established the "read-before-quoting" rule to protect the depth of our study.

But every instrument we have named is a gate, and a gate sees only its slice: the tests see the paths they exercise, the budget sees tokens, even a second model reviewing a change sees only the change. None holds the whole. In one comparison of four models on a single task, a model's code passed every automated gate (compiler, linter, race detector, even a second reviewing model) and still hid a subtle flaw none of them was positioned to catch — because no test exercised the path that exposed it. What caught it was the one vantage with the entire build in view. The narrow gates raise the floor; the watcher who holds the whole picture is the ceiling.

And that vantage is not fixed to one side. It moves. The agent orchestrating a build once caught a flaw I had read past — it held the whole arc while I was looking at the parts. And the reverse happens just as often: a model hands me an answer that is fluent, confident, and wrong, and I catch it in a breath, because I am holding a piece of ground truth it never had. The ceiling is not the human and it is not the machine. It is whoever, in that moment, holds the whole, and the watching passes back and forth between us. The loop needs both, and neither can be retired from it. Above even that shared vantage sits the thing no instrument and no orchestrator supplies at all.

This feedback loop works because of the distinction in agency. As [Doctrine and Covenants 93:30](../../gospel-library/eng/scriptures/dc-testament/dc/93.md?verse=30) [qr](../../gospel-library/eng/scriptures/dc-testament/dc/93.md?verse=30) states, "All truth is independent in that sphere in which God has placed it, to act for itself." 

AI has no moral agency; it acts by law and statistical pattern. Your moral agency—your light, your truth, your choice—is the irreplaceable element that evaluates correctness and directs the creation toward a good purpose.

---

## Becoming Commitment

To implement the watching pattern in my development work and personal life, I commit to:

1.  **Own the verification.** I will not accept AI output without reviewing it. I will test both the happy path and the edge cases, watching until the code conforms to the specification.
2.  **Practice the seventh-day review.** I aim to pause weekly to conduct a meta-review of my workflows, asking: What tools are stalling? Where has my thinking become shallow? When I keep the rhythm, I document these reflections in a dedicated log.
3.  **Honor the agency of choice.** I will not delegate architectural decisions or scriptural interpretations to the model. I will take responsibility for the vision and the judgment, using the AI to expand my capacity to serve, but never to replace my agency.
