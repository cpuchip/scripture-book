# Chapter 7: Delegation as Stewardship

**Binding Question:** How do we scale complex creations without descending into micromanagement or losing alignment?

**Anchor Passage:**
> "It is wisdom in me; therefore, a commandment I give unto you, that ye shall organize yourselves and appoint every man his stewardship; That every man may give an account unto me of the stewardship which is appointed unto him."
> — [Doctrine and Covenants 104:11–12](../../gospel-library/eng/scriptures/dc-testament/dc/104.md) [qr](../../gospel-library/eng/scriptures/dc-testament/dc/104.md?verse=11-12)

---

## The Core Reframe

In his 1994 address, Elder M. Russell Ballard warned against a recurring vulnerability in leadership: the "one-cylinder ward." He observed:

> "The one-cylinder ward is the ward where the bishop handles all of the problems, makes all of the decisions, and follows through on all of the assignments. Then, like an overworked cylinder in a car engine, he is soon burned out."
> — [Elder M. Russell Ballard, "Counseling with Our Councils"](../../gospel-library/eng/general-conference/1994/04/counseling-with-our-councils.md) [qr](../../gospel-library/eng/general-conference/1994/04/counseling-with-our-councils.md)

This description landed because it represents an engine running in isolation. When a leader attempts to make every decision, solve every problem, and handle every detail himself, he burns out. But the tragedy is not just the leader's exhaustion; it is the starvation of the people, who are deprived of the growth and spiritual gifts that can only be exercised through delegated responsibilities.

The scriptural remedy for the one-cylinder trap is the stewardship pattern. 

When Moses attempted to judge every dispute among the children of Israel from morning until evening, his father-in-law Jethro delivered a blunt diagnosis: "The thing that thou doest is not good. Thou wilt surely wear away... for this thing is too heavy for thee" ([Exodus 18:17–18](../../gospel-library/eng/scriptures/ot/ex/18.md)). Jethro’s solution was structural: organize the people, select able and God-fearing men, and appoint them as "rulers of thousands, and rulers of hundreds, rulers of fifties, and rulers of tens" ([Exodus 18:21](../../gospel-library/eng/scriptures/ot/ex/18.md)). 

This same scaling ratio appears when Alma organized the church at the waters of Mormon, ordaining "one priest to every fifty of their number" ([Mosiah 18:18](../../gospel-library/eng/scriptures/bofm/mosiah/18.md)). Alma set strict doctrinal guardrails—the priests were to teach nothing save repentance and faith—but he left them free to labor with their own hands for their support, trusting the Spirit to quicken their understanding.

God's pattern of delegation follows a precise sequence: authority first, then scope, then capacity, and finally identity. 

When Christ sent forth the Twelve, He did not hand them a checklist of tasks. He first "gave them power against unclean spirits... and to heal all manner of sickness" ([Matthew 10:1](../../gospel-library/eng/scriptures/nt/matt/10.md)). He defined their scope (the lost sheep of Israel), gave them the tools of healing, and framed their identity as sheep in the midst of wolves. He then left them free to execute, requiring them to report back. 

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

In structuring this delegation, we follow the scriptural pattern:
1.  **Authority & Tools:** We equip the subagent with specific tools—such as read, write, or grep search—giving it the power to act within its sphere.
2.  **Scope & Portion:** We limit its context. We do not pass it the entire workspace; we pass it only the files and lines relevant to its task.
3.  **Accountability:** We do not micro-manage its internal processing. We set the boundaries, issue the task, and then "watch until it obeys" ([Abraham 4:18](../../gospel-library/eng/scriptures/pgp/abr/4.md)). The subagent must return its output to the master agent for review and verification.

If the subagent encounters an error that exceeds its local scope, it does not crash the system. It follows a structured escalation protocol, passing the error back to the master agent (like the teachers and priests bringing a difficult case to Alma, who then escalates it to God). The master agent adjusts the plan, reframes the intent, and redelegates.

By organizing our systems into defined stewardships, we prevent token bloat and maintain architectural alignment. The master agent remains focused on the high-level specification (the spiritual creation), while the specialized subagents execute the individual code blocks (the physical creation). 

---

## Becoming Commitment

To practice the stewardship pattern in my daily creations and callings, I commit to:

1.  **Stop running on one cylinder.** In my church callings and my professional projects, I will actively invite my counselors and collaborators to sit in council with me. I will present the problems, not just the solutions, and listen to their counsel.
2.  **Appoint clear portions.** When I delegate tasks—whether to a human colleague or a subagent—I will define the scope, the tools, and the criteria for success clearly, rather than micro-managing the implementation.
3.  **Require accountability without hovering.** Once a stewardship is assigned, I will leave the steward free to perform, establishing structured review sessions (our "watching" loops) to verify correctness at the proper intervals.
