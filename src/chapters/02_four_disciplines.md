# Chapter 2: The Four Disciplines

*Creation · Context · Intent · Specification*

**Binding Question:** Prompt craft, context engineering, intent engineering, spec engineering—what does each one cover, and what do they leave for the work itself?

**Anchor Passage:**
> "Organize yourselves; prepare every needful thing; and establish a house, even a house of prayer, a house of fasting, a house of faith, a house of learning, a house of glory, a house of order, a house of God."
> — [Doctrine and Covenants 88:119](../../gospel-library/eng/scriptures/dc-testament/dc/88.md?verse=119) [qr](../../gospel-library/eng/scriptures/dc-testament/dc/88.md?verse=119)

---

> **For the reader who doesn't work in software:** You do not need to follow the technical names in this chapter to follow the book. Here is all you need to carry forward: the software industry has named four ways of working with AI, and we will see that they cover only four of the eleven steps in scripture's pattern for creation. The rest of this book is about the seven steps the industry has not named. If a term below is unfamiliar, let it pass—the doctrine does not depend on it.

## The Core Reframe

In [Doctrine and Covenants 88:119](../../gospel-library/eng/scriptures/dc-testament/dc/88.md?verse=119), the first verb the Lord commands is *organize*. 

Organization is not merely putting things in folders; it is the deliberate application of order to raw materials, aligning them with a specific purpose. The scripture instructs us to "prepare every needful thing" and "establish a house of order." 

When we look at the modern landscape of working with AI, we see that the single act of "prompting" has split into four distinct altitudes of organization:

1.  **Prompt Craft (Street Level):** The immediate, session-based request. It organizes the immediate interaction. You describe the task, the formats, and the direct constraints. This is table stakes—the professional equivalent of knowing how to type.
2.  **Context Engineering (Aerial Level):** Curation of the information environment. Since a prompt is only a tiny fraction of a model's context window, context engineering organizes the other 99.98%: the retrieved documents, the system files, the tool schemas, and the active session state. 
3.  **Intent Engineering (Orbital Level):** Encoding the purpose and values of the system. While context tells the model what to *know*, intent tells the model what to *want*. It establishes the decision boundaries and trade-offs the agent uses when instructions run out.
4.  **Specification Engineering (Architectural Level):** Designing a blueprint complete enough that an autonomous agent can build from it for hours without checking in. It requires completeness of thinking, anticipation of edge cases, and decomposing complex goals into executable components.

Each of these disciplines is a different altitude of the same scriptural verb: *organize*. Intent organizes the *why*. Spec organizes the *blueprint*. Context organizes the *environment*. Prompt organizes *this single step*.

When these four are aligned, they establish a "house of order" within our development projects. But organizing is only the beginning. The scripture commands us to "prepare every needful thing," and as we examine the limits of these four disciplines, we find that the most critical parts of creation are verbs that the framework does not reach.

---

## The Engineering Parallel

In practice, we discover the boundaries of the four disciplines when our systems fail. 

Prompt craft fails when the model lacks context. A perfect prompt in a blank chat session yields only generic, fluent output. 

Context engineering fails when the model knows everything but still chooses the wrong trade-off. It knows the code, but not what matters more. 

Intent engineering fails when real autonomy begins. An agent can understand its purpose and still get caught in an infinite loop. We saw this when an autonomous research agent in our Postgres database looped on a single topic and burned through 230 million input tokens before we hit the emergency stop. The agent's intent was defined, but intent alone did not prevent it from drifting.

Specification engineering fails in the same way. A precise spec allows an agent to work unattended, but the spec does not monitor the execution. 

If we map these four disciplines to the scriptural creation pattern, we find that they cover only four of the eleven steps:
- **Intent Engineering** is Step 1: *Intent* (the plan).
- **Specification Engineering** is Step 4: *Spiritual Creation* (the blueprint).
- **Context Engineering** is Step 5: *Line Upon Line* (layered understanding).
- **Prompt Craft** is Step 6: *Physical Creation* (the execution).

The other seven steps of the creation cycle—Covenant, Stewardship, Watching, Atonement, Sabbath, Consecration, and Zion—are left untouched by the four disciplines. 

For example, the runaway agent loop happened because nothing was *watching*. Watching—the feedback loop of Abraham 4:18—is the step where we observe the creation until it obeys. 

The industry has begun to feel how much the four disciplines leave out. In early 2026 a new phrase moved to the center of the conversation: *harness engineering*. Its slogan was *Agent = Model + Harness*. The model is the engine; the harness is everything else—the tools the agent may call, the guardrails that keep it safe, the feedback loops that let it self-correct, the observability that lets a human see what it did. Teams found they could lift an agent from the bottom of a benchmark to the top without touching the model at all, purely by building it a better harness. But a harness is not a fifth altitude of *organize*. It is not a sharper prompt, a richer context, or a cleaner spec. It is the wrapper around the model, and the wrapper is built from the verbs the four disciplines never named.

I have been building one, and it is not finished. The runaway loop ran *inside* it; those 230 million tokens taught me more than any clean success, because the gap was never a weaker model. It was a rung I had not yet built. So the substrate has grown toward the shape of the cycle, one rung at a time: every action an agent takes becomes a row—a covenant it works under, a tool it may call only where its stewardship allows, a watchman that records whether the work drifted, the lesson kept from a failure, the surplus returned to the work that still needs it, and a council where several agents reason toward one decision. I did not build those tables from a checklist of eleven steps; I built on the principles until they were habit, and only in hindsight saw what I had been transcribing: covenant, stewardship, watching, atonement, consecration, and the gathering of many into one.

Six of the seven. Sabbath, true cessation, is the rung I still have not made the system keep; rest stays my own discipline to remember, not the machine's to enforce, and that is the most honest thing the work has taught me. The hardest step to build is the one that tells you to stop. The field has named the need for a harness; scripture named what goes in it, and the rung I still cannot build, it wrote into the first week of the world.

---

## Becoming Commitment

To build a house of order in my work and life, I commit to the following:

1.  **Formally document intent.** For every major study or software project, I strive to write an explicit `intent` document stating the core purpose, values, and decision boundaries, so the system has a guide when instructions run out.
2.  **Establish watching mechanisms.** I strive to build monitoring and early-termination boundaries into my autonomous workflows, and not to delegate an execution task without a corresponding "watching" protocol to observe its output.
3.  **Recognize the unmapped verbs.** In my personal discipleship and daily habits, I strive to focus on the verbs of covenant, stewardship, and rest, and to treat the Sabbath not as a pause in execution, but as the essential ninth step of the creation cycle where we verify that the work is good.
