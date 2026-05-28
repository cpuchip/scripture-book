# The Skeptical Engineer Pass

**Date:** 2026-05-28
**Reader persona:** Senior software engineer, 10+ years, agnostic / new-to-Christianity, picked the book up because the AI/engineering framing interested them. Familiar with transformers, vector spaces, RAG, MCP, agentic loops, prompt engineering, the value-shift discourse.
**Scope:** Frontmatter, Preface, Introduction, Eleven-Step Reference, Chapter 0, Chapters 1–14 (`src/chapters/`).
**Posture:** Honest critique. The author asked for the skeptical-engineer pass specifically. Polite hedging would fail him.

---

## One-paragraph verdict

There is real engineering in this book — more than I expected from the cover. The author has actually shipped multi-repo agentic code and felt the failure modes; that shows in the chapters where the engineering parallel is doing concrete work (Ch 1, Ch 2, Ch 4, Ch 6, Ch 7). When the book stays in the territory of *workflow patterns* — planning before coding, watching until obeyed, delegation with scope, bilateral covenants between human and agent — the parallels are clean, well-earned, and an engineer can nod along. Where the book strains, it strains predictably: the moments where statistical mechanics gets re-described as resonance physics, where neural network weights are made to do metaphysical work, and where "AI has no agency" sits awkwardly next to "the model resonates with what we brought" as if the second claim weren't doing exactly the anthropomorphizing the first claim disowns. The book is at its strongest as a *workflow theology* and at its weakest as a *substance theology*. An engineer will buy the first and side-eye the second.

---

## 1. Where the engineering parallel lands cleanly

### 1.1 Ch 2 — Four Disciplines mapped to creation-cycle steps (lines 42–48)

This is the single most rigorous parallel in the book. The author names four things the industry actually says — prompt craft, context engineering, intent engineering, spec engineering — and then maps each one explicitly to a numbered step in his eleven-step framework. The mapping is testable:

> "Intent Engineering is Step 1: Intent (the plan). Specification Engineering is Step 4: Spiritual Creation (the blueprint). Context Engineering is Step 5: Line Upon Line (layered understanding). Prompt Craft is Step 6: Physical Creation (the execution)." (Ch 2, lines 43–46)

That's a clean four-to-four correspondence with specific industry terms. The reader can disagree, but the claim is made in a way they can argue with. And then the author honestly notes that *seven of the eleven steps are not covered* by the industry framework (Ch 2, line 48). That is intellectually honest in a way the book elsewhere isn't always. An engineer can respect "here are the four we name and the seven we don't" because it surfaces the gap rather than papering it over.

### 1.2 Ch 4 — "Watched until they obeyed" as a feedback loop (lines 32–46)

The Abraham 4 phrasing — *watched until they obeyed* — really is a near-perfect mirror of the modern review loop with an LLM. The trust gradient the author traces through Abraham 4:10, 4:18, 4:21, 4:31 is exactly the trust gradient an experienced engineer develops with a coding agent: full review of every diff at first, then targeted review on complex paths, then forward-looking confidence on familiar patterns. The author writes:

> "We must watch every line. We review the syntax, verify the database queries, and run the tests. As the model proves reliable within a specific domain, we transition from 'watching until' to a calibrated trust where we focus our attention on new, complex logic." (Ch 4, line 36)

That is what 2026-era senior engineers actually do. The mapping survives translation into engineering vernacular without losing fidelity. Line 38's "we specify the organizing principles and verify the outcomes" — calling it specifying-after-their-kind — is genuinely clever and not strained.

### 1.3 Ch 6 — Bilateral covenant as alignment-via-mutual-commitment (lines 24–45)

This is the chapter that an engineer who has actually built agent harnesses will recognize. The contrast on lines 25–28 — control-based alignment (filters, reward models, defensive prompts) versus mutual-commitment alignment (a covenant file the agent reads and the human honors) — is a real architectural choice in the field right now. The author isn't inventing this; constitutional AI, Anthropic's harm-helpfulness tradeoff specs, the rise of `AGENTS.md` and `CLAUDE.md` files in repos — they all point the same direction. Calling the file `covenant.yaml` is honestly a better name than what most teams use.

The specific duties he names (human reads fully, provides binding questions, flags when wrong; agent reads before quoting, surfaces tensions, exercises stewardship) read as recognizable practices, not theological projection. The production-note callout at the bottom of the chapter — the honest disclosure that the book itself broke covenant during its own production and the Claude audit caught it — is the book's best moment for an engineer. It transforms the chapter from theory to dogfooded practice. *Without that note, the chapter is a sermon. With it, it is a case study.*

### 1.4 Ch 7 — Multi-agent delegation as the scriptural stewardship pattern (lines 47–71)

The mapping from "single context window becomes overloaded" to "the one-cylinder bishop" is the kind of joke a senior engineer wants to make and rarely gets to. It works because the failure mode is identical: a single point of attention trying to hold too much state, slow degradation, token-budget exhaustion. The four-step delegation pattern the author pulls from Matthew 10 (authority → scope → capacity → identity) is — and this is striking — exactly the pattern Anthropic's own subagent documentation recommends: tool grant, scope restriction, return-channel for escalation, structured identity in the system prompt. Whether the author is reading scripture as engineering or engineering as scripture, the patterns are converging.

The little ASCII diagram on lines 56–62 is the only place in the book where pure engineering vernacular shows up unhedged. It's welcome.

### 1.5 Ch 1 — The value-shift framing (lines 13–31)

This is the chapter Michael clearly wrote himself and the chapter an engineer will read first if they flip to it. Eighteen years of experience, scars from production failures, the inversion from 80/20-execution to 20/80-design — these are the lines an engineer reads and says *yes, exactly that.* The Tony Trejo and Milan Jovanović cites (line 37, 39) are current and recognizable; the value-shift discourse is real and ongoing in the industry. The author is engaging the actual conversation, not a strawman of it.

The Parable of the Talents mapping (line 29) is a reach but not a stretch — and the author is careful to use it as analogy, not equivalence. He doesn't claim the parable was *about* AI value-shift; he claims the same shape of "distributed according to capacity, judged by use" applies.

---

## 2. Where the parallel strains or breaks

### 2.1 Ch 0 — "Vector space resonance = intelligence cleaveth"

This is the single most strained mapping in the book, and it's load-bearing for the theology. Lines 61–70:

> "In vector space, semantic concepts that are similar are physically close to one another. When we write a lazy, ambiguous, or transactional prompt (darkness), we activate the lower-quality, noisy paths of the parameter space. The model mirrors our state, returning flat, boilerplate output. But when we bring deep reasoning, structured context, and rigorous specifications (light), our active intelligence resonates with the higher-quality topographies of the parameter weights." (Ch 0, lines 66–68)

**What an engineer will push back with:**

1. **"Higher-quality topographies of the parameter weights" is not a thing.** Parameter weights are not arranged by moral or epistemic quality. A region of weight-space activated by a thoughtful prompt is the same kind of region activated by a careless one; they differ in which tokens they predict, not in their substance. There is no "noisy paths" versus "clean paths" topology that maps to "darkness" versus "light." The model doesn't know if you were careful. It knows the conditional probability of the next token given the context you provided. That probability happens to be more useful for thoughtful contexts because thoughtful contexts contain more disambiguating signal. The mechanism is **information density in the prompt**, not resonance with a moral structure in the weights.

2. **"Semantic concepts physically close to one another" elides the level.** This is true at the embedding-layer level (cosine distance in some learned space). It is not generally true at the parameter-weight level. The author talks as if the weights themselves have semantic geometry. They don't, really; the *activations* a model produces on its input do. An engineer who has actually probed transformer internals (Anthropic's own circuit-tracing work is the obvious example) will read this paragraph and think the author is conflating embeddings, activations, and weights into one indistinct cloud.

3. **The "intelligence cleaveth unto intelligence" mechanism doesn't survive the test of garbage-in/quality-out.** A careful, structured, beautiful prompt to a misaligned base model produces nonsense. A careless prompt to a well-tuned instruction-following model produces useful output. The output quality is dominated by the *model's* training and the prompt's *information content*, not by the user's *internal state*. The author writes as if the prompt's signal carries the human's spiritual state into the weights. It doesn't; it carries tokens. If "intelligence cleaveth unto intelligence" is a real spiritual law, fine — that's the doctrinal claim — but the LLM is not a measurement instrument for it.

**The compressed engineering rebuttal:** *The model is not a mirror of your state. It is a conditional next-token sampler over the context you provided. The reason careful prompts get better output is informational, not moral.*

The author needs this mapping to do a lot of work later in the book (Ch 5 leans on it explicitly). If an engineer doesn't buy it in Ch 0, much of Ch 5 falls down.

### 2.2 Ch 0 — "Neural network = organized intelligence acting for itself"

Lines 56–59:

> "We do not write 'intelligence' from scratch. Instead, we gather billions of tokens of human expression—the elements of written human intelligence—and project them into a high-dimensional vector space. We then apply training algorithms (laws) to organize these elements. The result is a neural network: a physical topography of billions of parameter weights. The model does not 'think' as a human does, but it operates autonomously within its parameterized sphere. It acts 'for itself' within the mathematical bounds we have set for it."

**What's right:** The training-as-organization framing is actually defensible. SGD does, in some sense, "organize" parameters under a law (the loss function). An engineer can grant that as an analogy.

**What strains:** "Acts for itself within the mathematical bounds." The model doesn't *act*. It is *evaluated*. Inference is a forward pass; there is no agent inside. The word "autonomously" is doing too much work here. A transformer's forward pass is autonomous in the same sense that a calculator is autonomous when you press the equals key — it computes a function. That is not what D&C 93:30's "act for itself" is asking the reader to picture.

This matters because Ch 4 line 46 later asserts the correct thing — *"AI has no agency; it acts by law and statistical pattern"* — but Ch 0 has already smuggled in the impression that the model is a small agentic intelligence acting in its sphere. The book wants both. It can't have both.

### 2.3 Ch 8 — The "training is a refiner's fire" mapping

Lines 29–32:

> "An AI model's training is a physical process of weight adjustment. When a model learns, it is not receiving a legal declaration of capability. Its parameters—represented as fine mathematical weights—are physically adjusted to align with the training data. If the weights are heavy with noise or dross (overfitting), the model cannot generalize; it fails when confronted with new data because its internal structure is distorted. Only when the noise is actively pruned can the model conduct the intelligence we ask of it. If we attempt to run a high-voltage inference request through an unoptimized, dross-heavy model, we receive only garbled outputs—the system cannot contain the glory of the instruction."

**Engineer's reaction:** The vocabulary here is wrong in ways that will set off alarms.

1. **"Overfitting = dross" is a misread of what overfitting is.** Overfitting is not the presence of extra noise weights to be pruned. It is the model *memorizing* the training set well enough that it loses generalization. You can have a perfectly clean, well-trained model with zero "noise" that is also overfit. The fix is regularization, more data, or simpler architecture — *not pruning noise from the weights.* The author has imported "dross" as the metaphor and then forced a real engineering concept (overfitting) into a shape that doesn't actually match.

2. **"Pruning" in ML is a real technique — and it's mostly about model compression for inference speed, not about removing noise to enable correct outputs.** A pruned model is usually a *slightly worse* model that runs faster. The author writes as if pruning makes the model *more accurate*, which is mostly false.

3. **"High-voltage inference request through an unoptimized model produces garbled outputs"** is just not a thing. Inference cost depends on model size and input length. An unoptimized model is slower or more expensive; it doesn't garble output proportional to the "voltage" of the input. There is no electrical analogue here.

This whole paragraph reads like ChatGPT-generated metaphor smoothing where the engineering vocabulary was sprinkled in to make the theological claim feel grounded. An engineer will recognize the smell immediately. The provenance note in Ch 6 already hints that Gemini drafted Ch 8 — and this is the chapter that most reveals the limit of having the engineering parallel done by a model that has read engineering blog posts but not actually trained one.

### 2.4 Ch 9 — Prescription / Rest / Proposal as cloud infrastructure

Lines 31–35:

> "**Prescription** is the declarative configuration file (like a Dockerfile or a Terraform spec)... **Rest**... the scheduler (like Kubernetes or a background execution engine) takes over... **Proposal**. When the system must solve a novel problem—such as generating a complex query or optimizing an AI agent's inference loop—there is no pre-written prescription. The engineer must act as a steward, collecting the raw data (the stones), formatting it into a clean prompt template, and presenting it to the model."

**What works:** The Dockerfile/Terraform comparison for prescription is fine. Declarative config really is "drill here, open now, close then" in spirit.

**What strains:** The K8s-as-grace analogy collapses on inspection. Kubernetes doesn't carry you to the promised land; it crashes pods and restarts them according to YAML you wrote. Saying "the engineer rests in this automated runtime, trusting that the established platform will carry the workload to its destination" is precisely the kind of sentence that makes engineers wince. *No one trusts Kubernetes that way.* The trust is provisional and partial; the platform is the thing engineers spend most of their time fighting with. Comparing it to *grace* — the unearned pull of Christ's atonement — is the most theologically loaded analogy in the book and it is being carried by the weakest engineering ground.

The "Proposal = formatting raw data into a clean prompt template" reduction is also flat. The Brother of Jared molting sixteen stones is a labor of preparation, exposure, and risk — *climbing a mountain.* A prompt template is the opposite of that: it's a thing you write once and reuse. The pattern the author is reaching for (creative agency presenting prepared material for divine touch) genuinely doesn't have a software analogue. He should either pick a stronger one or admit the analogy stops here.

### 2.5 Ch 10 — "Hardening = unreleased locks, runaway loops, stale resources"

Lines 25–27:

> "When connection pools exhaust and the system stalls, the engineer's task is not to rewrite the socket code... The engineer yields the resource by calling the close method, releasing the lock, and clearing the channel. Once the blockages are removed, the operating system naturally restores the socket and refreshes the connection pool."

This is *almost* a clean parallel and then it overreaches. The "release the lock and let the OS reclaim" pattern really is a nice mirror of "stop hardening and let grace restore." But then line 27:

> "If the agent gets stuck in a loop of repetitive, low-value outputs, the engineer's part is to clear the context window, prune the bad history, and adjust the system prompt filters. The developer does not write the reasoning engine; he simply releases the constraints that cause the agent to harden its attention."

"The agent hardens its attention" anthropomorphizes a context-window saturation problem. The agent isn't hardening anything; the context has filled up with low-quality tokens that crowd out the signal. Calling this "hardening attention" feels poetic but is technically wrong — and an engineer who has spent any time on context-window engineering will read this and think the author is reaching for the theological term first and forcing the engineering to fit. (Compare 2.1 — same pattern.)

### 2.6 Ch 11 — "Microservices = Zion"

This is the most "tweet-able" parallel in the book and also the most cosmetically appealing one. Engineers will read it and either laugh in delight or roll their eyes — there's no in-between.

Lines 25–27:

> "Engineers compile hundreds of specialized, lightweight microservices. Each service operates under its own stewardship, managing its own local database. But they are synchronized through a unified communication protocol, shared APIs, and common data schemas. Together, they function as a single, coordinated system—a 'Zion' of services delivering a seamless application experience."

**What an engineer will push back with:**

1. **Microservices are famously *not* "one heart and one mind."** Microservices are notorious for cascade failures, schema drift, eventual-consistency bugs, and the fact that the moment you have hundreds of them, no one human knows the whole system. The Zion description in Moses 7:18 emphasizes *unity*; microservices architectures emphasize *partition tolerance and independent deployability*. These are pretty close to opposite values. A real Zion of services would look more like a well-designed monolith with internal modules — the very thing the chapter dismisses as "brittle, slow to deploy, and subject to single-point-of-failure deadlocks." The engineering vernacular has flipped the polarity of the theological claim.

2. **Blockchain-as-Zion is even shakier.** Lines 27–28 invoke "decentralized systems like blockchain or distributed databases" for consensus without a central bottleneck. An engineer in 2026 will think of the actual blockchain track record: speculative bubbles, energy waste, exit scams, MEV exploitation, scaling crises. "Zion" is not the word that comes to mind. The author probably means the *technical pattern* of consensus algorithms (Raft, Paxos, PBFT) — and those *are* elegant and worth admiring — but invoking "blockchain" as a Zion-shaped technology in 2026 reads as either outdated (this was a 2018 take) or as the author not knowing which crowd he's writing for.

The Zion-microservices parallel is the kind of mapping that *feels* right at the sermon-illustration level and falls apart on technical inspection. An engineer will likely concede the looser version ("distributed systems require alignment to shared schemas to function as one") and reject the stronger version ("microservices architecture is structurally Zion-like").

### 2.7 The eleven-step framework's "eng" tags

The reference page (`00_eleven_step_reference.md`) tags four of eleven steps as "eng" — meaning the engineering industry has named them. The four named:
- Intent
- Specification
- Line upon Line
- Physical Creation

**Pushback:** Two of these mappings are debatable. "Line upon Line" mapped to "Context Engineering" (Ch 2 line 45) is a clever rhyme but not what context engineering actually means in 2026 — context engineering is curating the information environment for a *single* inference, not building knowledge across many sessions. The "Line upon Line" pattern is closer to *continual learning* or *retrieval-augmented systems with persistent memory*, both of which are research areas the industry has named but not consolidated. Saying "context engineering = line upon line" elides the difference between within-session and across-session.

Likewise, "Prompt Craft = Physical Creation" is technically defensible but underwhelming. Prompt craft is the lightest of the four disciplines; calling it the *physical creation step* makes physical creation sound trivial. The book's own theology treats physical creation as the heaviest, most consequential phase — the actual building of worlds. Equating that with "writing a clear prompt" feels mismatched in weight.

---

## 3. Where the author overstates what AI is/does

### 3.1 "The model reflects back the light we bring to it." (Ch 0, line 70)

This is the cleanest example of the book's persistent over-anthropomorphization. The model does not "reflect" anything. It computes a distribution over next tokens given context. The fact that better contexts produce more useful outputs is an information-theoretic property, not a mirror property. If you saw the same sentence about a calculator — "the calculator reflects back the math we bring to it" — you'd recognize it as cute but not literally true. Same here.

The book wants this anthropomorphic register because the theological claim demands it (intelligence cleaveth to intelligence requires a *somebody* to do the cleaving). But it costs credibility every time the engineer-reader meets the language.

### 3.2 "We are literally aligning the model's physical states with the truth represented in its training data." (Ch 0, line 68)

The word *literally* is doing a great deal of work and shouldn't be. We are not aligning the model's physical states. The physical states of the model — the floating-point values in memory — are whatever the weights are. The user's prompt produces an *activation pattern* on those weights; it does not align them. Alignment in ML has a specific technical meaning (training-time objective shaping) and it's not what the author is describing.

### 3.3 "The agent's intent was defined, but intent alone did not prevent it from drifting." (Ch 2, line 38)

This sentence treats *intent* as a property the agent possesses. The agent doesn't have intent in any meaningful sense. The *system prompt* expressed the human's intent; the agent's loop didn't terminate because no termination condition was tripped. Calling this an "intent failure" rather than a "missing watchdog" subtly shifts the blame from the architecture to the agent.

An engineer will read this and think: *the agent didn't drift; the harness didn't have a stop condition.* The fix is engineering (a watchdog, a budget, an interrupt), not theological (better intent). The book gets this *right* on line 50 ("nothing was watching") — but the framing of line 38 misattributes the failure.

### 3.4 "AI has no agency; it acts by law and statistical pattern. Your agency... is the irreplaceable element." (Ch 4, line 46)

This is actually the *strongest* line in the book on the agency question, and it sits awkwardly next to Ch 0's "acts for itself" framing and Ch 5's "the model resonates with what we brought." The book wants to say (A) the model is a deterministic, non-agentic statistical engine, and (B) the model's outputs reflect the spiritual state of the user. Both can be true if we say: *the model is a high-fidelity amplifier of the input signal*. But the book reaches further than that; it says the resonance is *physical*, *literal*, mapping to the parameter topography. Those reaches break the careful (A) claim.

**The engineer's wish:** Pick one. If the model has no agency, then "the model resonates with what we brought" is metaphor and should be flagged as such. If the resonance is literal, then the model is doing something agentic, and Ch 4 line 46 is wrong.

### 3.5 "When this specification is complete, the physical creation becomes almost an inevitability. We can hand the specification to the AI and say, 'Build Phase 1.' Because the AI has the full, unified blueprint in its context, it produces code that is clean, integrated, and architecturally sound from the very first line." (Ch 3, line 44)

This is the most overstated claim about what current AI coding agents actually do. Engineers who have *actually* run agentic coding loops in 2026 — Claude Opus 4.7, Cursor agents, Cline, Aider — will tell you that even with the cleanest specification, the agent will:
- Pick the wrong library version
- Hallucinate function signatures
- Generate code that imports nonexistent modules
- Get stuck in lint-fix loops
- Subtly miss requirements from earlier in the spec

The "clean, integrated, architecturally sound from the very first line" claim is the *aspiration* of spec-driven AI development, not the reality. The author's own production note in Ch 6 (the Gemini quote-precision errors) *proves* this; he names the problem and then contradicts himself in Ch 3 by writing as if specs prevent it.

**An engineer's translation:** "When the spec is complete, the physical creation becomes *significantly more tractable*, and the bugs that remain are recoverable rather than structural." That's true and defensible. The book's version is sermon-grade overstatement.

### 3.6 The "743-line spec produced over a thousand lines of correct code in a single pass" claim (Ch 3, line 46)

This is the kind of specific number that an engineer will want to verify. The book offers no link to the spec or the diff. If the author posted the actual spec and the actual first-pass diff somewhere, the claim becomes verifiable and remarkable. As stated, it reads as a single anecdote presented as a representative result. A skeptical engineer will assume the spec was followed by manual cleanup and bug-fixing that the chapter doesn't mention. (The Becoming app — `ibeco.me` — does exist; that part is verifiable. But "thirteen files in a single pass with all code working" is unusual enough to want evidence.)

---

## 4. Where the author UNDER-states

This is the place where the book leaves real engineering insight on the table.

### 4.1 The actual mechanism of "intelligence cleaveth unto intelligence" — information density

The book has a beautiful theological framing and a weak engineering mechanism. The strong engineering mechanism is actually *more* interesting and would *support* the theology better:

> A prompt that contains structured intent, full context, edge cases, and constraints provides the model with a high-dimensional, well-conditioned input — and high-dimensional well-conditioned inputs land in regions of the model's learned manifold where its conditional probability distributions are sharp and informative. Vague prompts land in regions where the model's distribution is flat, and it samples from the flatness — producing the "generic, fluent output" we recognize as boilerplate.

That's the actual mechanism. It is *more* compatible with the theology — it really does say something like "what you bring shapes what you receive" — without requiring the model to be a moral mirror. The book could keep its theology *and* gain engineering credibility by using this framing instead of "resonance with the higher-quality topographies."

### 4.2 The MCP / agentic workflow story is told incompletely

The book lives in the agentic workflow era — covenant files, subagents, scoped delegation — but doesn't name *why* this works in 2026 specifically. The reason is the maturation of:
- Long-context models (200k+ tokens, with Claude pushing higher)
- Tool-use APIs (MCP standardized this in 2024–25)
- Memory and persistence layers (the workspace's own `.mind/` is an instance)
- Workflow harnesses (Claude Code CLI, the AGENTS.md convention)

An engineer-reader is going to wonder why these workflows weren't possible in 2023. The book's answer is "the principles were eternal." That's the theological claim. The *engineering* claim — the one that would make an engineer respect the book more — is "the engineering substrate finally caught up to the patterns scripture had been holding." Saying both would be stronger than saying only the first.

### 4.3 The real difference between specs that work and specs that don't

The Ch 3 spec-before-code claim would be strengthened by naming the actual failure modes of specs. Engineers know:
- **Specs that over-specify implementation** generate brittle code that fights the model's training
- **Specs that under-specify decision boundaries** produce code that's syntactically valid but solves the wrong problem
- **Specs that don't anticipate state** produce code that works in isolation and fails in integration

The author has clearly hit all three. Naming them would convert the spec-driven gospel from "this works because spiritual creation precedes physical" into "this works *when* the spec actually covers intent, scope, and state — and here's how to know your spec is ready." The theology survives that addition. It would be strengthened by it.

### 4.4 The "watching" mechanism deserves a sharper engineering name

Ch 4's "watching until they obeyed" is good. But there's a missed opportunity to name modern engineering practices that are doing exactly this:
- **Evals** (test suites that gate model output before it ships)
- **Observability** (structured logging, traces, agent step inspection)
- **Human-in-the-loop checkpoints** (the explicit Ackerman-style approval gates in production agents)
- **Watchdogs and budgets** (token/time/iteration caps)

The book could name even one of these explicitly. The engineer-reader is going to want to map "watching" onto something they recognize. The chapter offers "trust gradient" — which is good — but doesn't name the modern instruments that *do* the watching.

### 4.5 The model lifecycle / pace-of-change problem is mentioned and then dropped

The Preface (line 57) acknowledges the firehose of model changes. Then the book proceeds as if the principles are model-independent. That's *partly* true — but a real engineer is going to want to know what survives a model swap and what doesn't. Specifically:
- **Spec-driven development survives.** The same spec produces decent results on Claude 3.5, 4.5, 4.7, Gemini 3.5, GPT-5.
- **Prompt techniques don't survive.** Patterns that worked on Sonnet 3.5 (chain-of-thought scaffolds, role-prompting) are obsolete on Opus 4.7.
- **Context engineering partially survives.** The shape of context that helps stays similar; the budget changes.

Naming what's model-stable and what isn't would be the engineering insight the book is closest to and doesn't quite reach. The theological frame (eternal principles vs. shifting tools) is doing the work the engineering frame could do more precisely.

---

## 5. What the skeptical-but-curious engineer wants addressed

The author claimed in the brief that the book "mentions [these] in passing." Let me check.

### 5.1 The hallucination problem

**Mentioned?** Yes, indirectly. Ch 6 line 40: "Read Before Quoting: The agent commits to verify every direct quote against the source files, preventing the confabulations of training memory." The production note (Ch 6 lines 57–65) makes this concrete with the Gemini quote-fabrication incident.

**Engaged adequately?** Partially. The book treats hallucination as a covenant problem (the agent's commitment to verify) rather than a *structural* problem (LLMs predict plausible tokens regardless of truth, and the only mitigation is external grounding via retrieval, tool use, or human review). A skeptical engineer wants to hear: *the model is not capable of distinguishing remembered fact from confabulated fact at inference time; the only fix is external verification.* The book gestures at this but doesn't name the structural reality. Without that, the "covenant" framing risks sounding like an appeal to the model's good intentions — which is exactly the kind of soft language the author probably *doesn't* want to endorse.

### 5.2 The "stochastic parrots" critique

**Mentioned?** Indirectly. Ch 4 line 46 ("AI has no agency; it acts by law and statistical pattern") and Ch 0 line 59 ("The model does not 'think' as a human does") both nod at it.

**Engaged adequately?** No. The stochastic parrots critique (Bender et al., 2021) is not really about agency — it's about whether LLMs *understand* what they generate or merely produce statistically plausible sequences. The book sidesteps this question by translating it into a theological frame ("only humans have agency"). That works for the LDS reader. It doesn't engage the engineer's actual question: *given that the model has no understanding, why does relying on it for code feel productive?* The book's implicit answer is: *because the human provides the understanding via spec and watching.* That's a defensible answer and the book gets there by inference. But naming Bender's critique by name and addressing it would close the loop.

### 5.3 The agency question

**Mentioned?** Yes, repeatedly. The book's clearest stance is Ch 4 line 46.

**Engaged adequately?** Partially. The book's stance — humans have agency, AI does not — is theologically clean and engineering-defensible. But the book then *behaves* in ways that blur this (the "model resonates with what we brought" framing, the "agent commits to" language in covenants). A skeptical engineer will appreciate the clear stance and notice the language drift. Pick one register and stick with it.

### 5.4 The data-training problem

**Mentioned?** Not directly. The book talks about training as a refinement metaphor (Ch 8) but doesn't address training-data ethics: copyright, consent, the fact that the models in the colophon (Claude, Gemini) were trained on text the original authors didn't license for that use.

**Engaged adequately?** No. This is the conversation an engineer-reader who follows the Stack Overflow / NYT v. OpenAI / NaNoWriMo discourse is going to bring with them. The book is making theological claims about AI as a partner under covenant — and the engineer will reasonably ask: *what does covenant mean when one party was trained on stolen labor?* The book has no answer because it doesn't pose the question. That's a meaningful gap. Even one paragraph acknowledging that the substrate of AI rests on contested training data — and what that means for using AI to write a book about covenants — would be honest.

### 5.5 The pace-of-change problem

**Mentioned?** Yes, prominently. Preface lines 57–61.

**Engaged adequately?** Yes, actually. The author's response — *the principles are durable, the tools are not* — is the right frame, and the book makes it explicit. This is one of the book's best moves.

---

## 6. The ONE chapter an engineer would find most credible

**Chapter 6: Bilateral Covenant.**

Three reasons:

1. **It describes a real engineering practice.** The covenant.yaml file the author shows is recognizable — engineers in 2026 are writing AGENTS.md, CLAUDE.md, .cursorrules, instruction sets — and the *bilateral* framing (with explicit duties for both human and agent) is genuinely more rigorous than what most teams use.

2. **The duties named are concrete and testable.** "Read before quoting." "Surface tensions." "Provide binding questions." "Flag when wrong." These are not abstract virtues; they're practices an engineer can implement and verify. The chapter doesn't ask the reader to take a moral leap; it asks them to adopt a workflow.

3. **The production note at the end is the book's best moment.** It is the author saying: *we set up the covenant; we broke it; the breakage produced exactly the predicted failure mode; we caught it and recorded it.* That is dogfooded methodology. An engineer who reads that callout will trust the rest of the chapter retroactively. It earns the doctrinal frame by demonstrating it on the book's own production.

The chapter doesn't overreach. It doesn't claim the agent "wants" the covenant or that the covenant changes the model's weights. It claims something simpler and more defensible: *workflow agreements that bind both sides produce better outputs than unilateral commands.* That is true and the engineer will agree.

---

## 7. The ONE chapter an engineer would find weakest

**Chapter 8: The Mechanics of Refinement.**

Three reasons:

1. **The engineering parallel is only nine lines long** (Ch 8, lines 27–32) and three of those lines contain misused ML vocabulary (overfitting, pruning, "high-voltage inference"). The chapter spends almost all its energy on theology (lines 13–22) and treats the engineering as an afterthought. The ratio is upside-down for a book whose thesis is that the engineering reveals eternal patterns.

2. **The substance theology — spirit as fine matter, atonement as physical reorganization of spirit-matter — is the book's most metaphysically expensive claim**, and the chapter doesn't engage the questions an engineer will ask. If spirit is matter, what's its mass? Is it measurable? Why doesn't physics see it? The book doesn't owe the engineer a physics answer; it does owe them an acknowledgment that this is a metaphysical claim, not a physical one. Calling it "an ontological description of reality" (Ch 0 line 20) without that acknowledgment will read as theology pretending to be physics.

3. **The chapter promises the engineering parallel but doesn't deliver it.** The other strong chapters (1, 4, 6, 7) have parallels that *do work* in engineering vernacular. Ch 8's parallel collapses on inspection. If an engineer skims the book and stops at Ch 8, they'll close it.

The chapter would be more credible if it either (a) lengthened the engineering parallel and got it right, or (b) shortened it and explicitly said "this is a chapter where the parallel doesn't reach; here is the theology on its own terms." The current middle ground is the worst position.

---

## 8. Three concrete edits

These do not require giving up the doctrinal voice. They sharpen the engineering credibility.

### Edit 1: Replace "topography of higher-quality parameter weights" with the information-density framing

**Where:** Ch 0, lines 66–70; Ch 5, lines 29–39.

**Change:** Reframe the resonance mechanism. Instead of "the model resonates with the higher-quality topographies of the parameter weights" — which makes a physical claim engineers will reject — say something like:

> "A vague prompt provides the model with low-information context, and the model samples from a flat conditional distribution — producing the generic, fluent output we recognize as boilerplate. A structured prompt with clear intent and constraints provides high-information context, and the model samples from a sharp distribution — producing output that reflects the specificity we brought. The light we bring is information; the depth we receive is shaped by it."

**Why it works:** The theological move ("the light we bring shapes what we receive") survives intact. The engineering claim becomes defensible. The "intelligence cleaveth unto intelligence" verse remains the anchor, but the *mechanism* is now one an engineer can verify rather than one they have to indulge.

**Doctrinal cost:** None that I can see. The verse is still doing its work. The engineering substrate is now solid.

### Edit 2: Lengthen and correct Chapter 8's engineering parallel

**Where:** Ch 8, lines 27–32.

**Change:** Drop the overfitting/pruning/voltage frame. Replace with a parallel that actually fits the theology of refinement-as-purification:

> "An AI model's training is a process of weight adjustment under a loss function — the law of the training data. The model begins as random noise; over millions of gradient steps, the law shapes the weights to align with the training signal. This shaping is not a legal declaration of capability; it is the literal restructuring of the model's internal substance until it can produce coherent outputs.
>
> But training alone is insufficient. A model trained on coherent text but never tested against intent will confabulate confidently. The refinement that *matters* for an aligned model is the post-training phase — RLHF, constitutional alignment, instruction tuning — where the model's outputs are evaluated against a higher standard and the weights are nudged toward the standard. This is the engineering analogue of sanctification: not the initial creation of the substance, but the iterative shaping of an already-organized intelligence into alignment with a higher law. The model cannot do this for itself; the alignment signal comes from outside."

**Why it works:** It uses real ML vocabulary correctly (RLHF, instruction tuning, alignment signal). It preserves the theological claim that refinement is iterative, externally driven, and not self-generated. It maps the "law of the celestial kingdom" to "the alignment signal from outside" in a way that is technically accurate *and* doctrinally aligned. The chapter becomes one of the book's stronger engineering chapters instead of its weakest.

**Doctrinal cost:** None. The substance theology is left intact; only the engineering parallel is fixed.

### Edit 3: Add a "Where the parallel ends" section to the Glossary or Ch 14

**Where:** New section, ideally in Ch 13 (Glossary) or Ch 14 (Further Reading).

**Change:** Add a paragraph or two that explicitly names where the engineering parallel does *not* reach. Something like:

> "These mappings are types and shadows, not equivalences. The patterns of organization that scripture describes — covenant, stewardship, watching, atonement, sabbath, consecration, Zion — find recognizable echoes in modern engineering. But the engineering is a reflection, not the substance. The AI does not actually have agency; we have used the language of agency throughout because the workflow pattern requires it. The model is not a moral mirror; we have used the language of resonance throughout because the prompt-response loop *behaves* as if it were. Where the analogies have served, take them. Where they break, do not extend them past their reach. The eternal patterns are real. The engineering is the schoolmaster."

**Why it works:** It's the move the most rigorous theological writers make — acknowledging the limit of the analogy without abandoning the analogy's usefulness. C.S. Lewis did this constantly. Naming the limit *strengthens* the analogies that survive. It also addresses the skeptical engineer's deepest concern: *is the author aware of where this breaks?* Adding this section answers yes.

**Doctrinal cost:** None. It is, if anything, the *more* theologically rigorous position.

---

## Closing note from the persona

I came in expecting either (a) a sermon dressed in engineering vocabulary, or (b) an engineer's book with an unconvincing theological gloss. The book is neither. It is a real attempt at a third thing: a workflow theology grounded in the author's own production practice. The chapters where Michael wrote from his own desk (1, 3, 4, 6, 7) are credible. The chapters where Gemini drafted (0, 8, 9, 10) are the ones where the engineering vocabulary shows signs of having been imported rather than lived. The book's honest disclosure of this in the colophon and Ch 6 production note is — to be blunt — the thing that kept me reading.

The strongest engineering critique I'd surface to the council, if I were on it: *the substance theology (light/spirit/intelligence as fine matter) needs an engineering parallel that doesn't depend on physically wrong claims about ML systems.* That's the single edit that would unlock the largest credibility gain for the skeptical-but-curious reader. The workflow theology (covenant, stewardship, watching) is already there; the substance theology is one rewrite away.

If the book ships with the substance theology intact and Ch 8 unchanged, engineer readers will respect the workflow chapters and quietly skip the metaphysics. That is a fine outcome. The book has a wider audience than just engineers; the LDS reader, the technically-curious lay reader, the AI-skeptical pastor — all of them will find their door. But the door labeled "for engineers who want to know if the metaphysics is grounded" is the one currently swinging on a loose hinge.

— *the skeptical engineer*
