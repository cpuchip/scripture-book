# Chapter 7: Delegation as Stewardship

*Stewardship*

**Binding Question:** How do we scale complex creations without descending into micromanagement or losing alignment?

**Anchor Passage:**
> "It is wisdom in me; therefore, a commandment I give unto you, that ye shall organize yourselves and appoint every man his stewardship; That every man may give an account unto me of the stewardship which is appointed unto him."
> — [Doctrine and Covenants 104:11–12](../../gospel-library/eng/scriptures/dc-testament/dc/104.md?verse=11-12) [qr](../../gospel-library/eng/scriptures/dc-testament/dc/104.md?verse=11-12)

---

## The Core Reframe

Covenant gives us the binding; stewardship gives us the scaling. The previous chapter bound two parties in mutual commitment; this one asks how that commitment extends to many without fracturing.

In his 1994 address, Elder M. Russell Ballard warned against a recurring vulnerability in leadership: the "one-cylinder ward." He observed:

> "The one-cylinder ward is the ward where the bishop handles all of the problems, makes all of the decisions, and follows through on all of the assignments. Then, like an overworked cylinder in a car engine, he is soon burned out."
> — [Elder M. Russell Ballard, "Counseling with Our Councils"](../../gospel-library/eng/general-conference/1994/04/counseling-with-our-councils.md) [qr](../../gospel-library/eng/general-conference/1994/04/counseling-with-our-councils.md)

This description landed because it represents an engine running in isolation. When a leader attempts to make every decision, solve every problem, and handle every detail himself, he burns out. But the tragedy is not just the leader's exhaustion; it is the starvation of the people, who are deprived of the growth and spiritual gifts that can only be exercised through delegated responsibilities.

The scriptural remedy for the one-cylinder trap is the stewardship pattern. 

When Moses attempted to judge every dispute among the children of Israel from morning until evening, his father-in-law Jethro delivered a blunt diagnosis: "The thing that thou doest is not good. Thou wilt surely wear away... for this thing is too heavy for thee" ([Exodus 18:17–18](../../gospel-library/eng/scriptures/ot/ex/18.md?verse=17-18)). [qr](../../gospel-library/eng/scriptures/ot/ex/18.md?verse=17-18) Jethro’s solution was structural: organize the people, select able and God-fearing men, and appoint them as "rulers of thousands, and rulers of hundreds, rulers of fifties, and rulers of tens" ([Exodus 18:21](../../gospel-library/eng/scriptures/ot/ex/18.md?verse=21)). 

This same scaling ratio appears when Alma organized the church at the waters of Mormon, ordaining "one priest to every fifty of their number" ([Mosiah 18:18](../../gospel-library/eng/scriptures/bofm/mosiah/18.md?verse=18)). [qr](../../gospel-library/eng/scriptures/bofm/mosiah/18.md?verse=18) Alma set strict doctrinal guardrails—the priests were to teach nothing save repentance and faith—but he left them free to labor with their own hands for their support, trusting the Spirit to quicken their understanding.

God's pattern of delegation, as Christ models it when He sends the Twelve, follows a precise sequence: authority first, then scope, then capacity, and finally identity. Matthew 10:1–16 records each step in turn.

**Authority and tools** come first. He "gave them power against unclean spirits, to cast them out, and to heal all manner of sickness and all manner of disease" ([Matthew 10:1](../../gospel-library/eng/scriptures/nt/matt/10.md?verse=1)). Before any work is named, the disciples are equipped.

**Scope** comes next. They are commanded, "Go not into the way of the Gentiles, and into any city of the Samaritans enter ye not: But go rather to the lost sheep of the house of Israel" ([Matthew 10:5–6](../../gospel-library/eng/scriptures/nt/matt/10.md?verse=5-6)). The portion is defined.

**Capacity** is named both as gift and as practice: "freely ye have received, freely give" ([Matthew 10:8](../../gospel-library/eng/scriptures/nt/matt/10.md?verse=8)). And when the work demands more than the stewards have prepared, Christ promises supplementation in the moment: "it shall be given you in that same hour what ye shall speak. For it is not ye that speak, but the Spirit of your Father which speaketh in you" ([Matthew 10:19–20](../../gospel-library/eng/scriptures/nt/matt/10.md?verse=19-20)).

**Identity** is the last thing He names, and the heaviest. "Behold, I send you forth as sheep in the midst of wolves: be ye therefore wise as serpents, and harmless as doves" ([Matthew 10:16](../../gospel-library/eng/scriptures/nt/matt/10.md?verse=16)). The disciples know who they are before they meet the resistance.

He then leaves them free to execute, requiring them to report back. 

True delegation is not task-offloading; it is the empowerment of a steward over a defined portion, accompanied by a requirement of accountability. As President Gordon B. Hinckley taught:

> "The president, if he is wise, will assign to these chosen assistants particular duties and then leave them free to perform, requiring from them accountability for what happens."
> — [President Gordon B. Hinckley, "In … Counsellors There Is Safety"](../../gospel-library/eng/general-conference/1990/10/in-counsellors-there-is-safety.md) [qr](../../gospel-library/eng/general-conference/1990/10/in-counsellors-there-is-safety.md)

---

## The Engineering Parallel

In software engineering, we hit the exact same scaling bottleneck when we build complex systems. 

If we attempt to run our entire development loop through a single, massive AI agent context, the system collapses. The token budget is consumed by noise, the model's attention drifts, and the execution degrades. This is the "one-cylinder" bishop in digital form—a single context window trying to hold the state, syntax, design patterns, and debugging logs of an entire multi-repo codebase simultaneously.

To scale our creations, we must implement the stewardship pattern. We must move from a single-agent architecture to a multi-agent hierarchy. 

When a master agent (Moses/Alma) encounters a task that exceeds its immediate capacity—such as running automated test suites, searching a large database, or editing multiple non-contiguous files—it does not attempt to execute everything itself. Instead, it delegates. It spawns a subagent, appointing it as a steward over a defined portion.

```
       Master Agent (Presiding / Oversight)
                     |
         +-----------+-----------+
         |                       |
     Subagent A              Subagent B
  (Search & Research)      (Code Execution)
```

This is the same shape Jethro pressed upon Moses—rulers of thousands, of hundreds, of fifties, of tens ([Exodus 18:21](../../gospel-library/eng/scriptures/ot/ex/18.md?verse=21), named above)—rendered in software: a presiding context that delegates defined portions to stewards beneath it.

In structuring this delegation, we follow the same scriptural sequence. We equip the subagent with authority and tools first—read, write, or grep search—giving it power to act within its sphere. We define its scope, limiting its context to only the files and lines its task requires rather than the whole workspace. Then we hold it accountable: we do not micromanage its internal processing, but we set the boundaries, issue the task, and "watch until it obeys" ([Abraham 4:18](../../gospel-library/eng/scriptures/pgp/abr/4.md?verse=18)). [qr](../../gospel-library/eng/scriptures/pgp/abr/4.md?verse=18) The subagent returns its output to the master agent for review and verification.

If the subagent encounters an error that exceeds its local scope, it does not crash the system. It follows a structured escalation protocol, passing the error back to the master agent (like the teachers and priests bringing a difficult case to Alma, who then escalates it to God). The master agent adjusts the plan, reframes the intent, and redelegates.

By organizing our systems into defined stewardships, we prevent token bloat and maintain architectural alignment. The master agent remains focused on the high-level specification (the spiritual creation), while the specialized subagents execute the individual code blocks (the physical creation). 

---

## Becoming Commitment

To practice the stewardship pattern in my daily creations and callings, I commit to:

1.  **Stop running on one cylinder.** In my church callings and my professional projects, I strive to invite my counselors and collaborators to sit in council with me, to present the problems and not just the solutions, and to listen to their counsel.
2.  **Appoint clear portions.** When I delegate tasks—whether to a human colleague or a subagent—I strive to define the scope, the tools, and the criteria for success clearly, rather than micro-managing the implementation.
3.  **Require accountability without hovering.** Once a stewardship is assigned, I will leave the steward free to perform, establishing structured review sessions (our "watching" loops) to verify correctness at the proper intervals.
