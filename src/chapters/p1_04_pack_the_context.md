# Practice 4 · Pack the Context, Waste Nothing

The first instinct, when you want a good answer, is to give the model everything. The whole codebase. All the docs. The entire history. It feels generous, and it is exactly wrong. I learned this when I fanned a job out to six agents at once and packed each one's window full of context I thought might be useful. Four of the six died on the spot, hitting the token limit before they could do any work. I'd confused *having* the information with *using* it, and I'd drowned the very agents I was trying to equip. We ended up building a whole compaction layer just to dig back out.

So the fourth practice has two motions, and the trick is never to confuse them. **Build the agent a library it can explore. Then pull only what the task needs into view.**

The library is vast and lives on disk. The window is small and must be curated. Those are different jobs.

Here's the library half, and it's the single most useful thing I do at work. I download *all* of it into one folder the agent can read: every git repository I have access to, and at work that is over three hundred interconnected microservices. Not into the prompt. Into a place it can *explore*. When I need to change something, I don't paste in what I think is relevant; I point the agent at the folder and let it go find the truth: which services call this one, what breaks if I change this contract, where the pattern I need already exists. A second folder holds external repositories we don't own but want to learn from. The agent pulls from these the way you pull a book off a shelf: the shelf holds thousands; you open one.

Looking back, my very first real project with AI was a small tool to search video transcripts and hand back a quote with a link straight to its source. I never finished it, but I see now what I was actually building: a way to find the *right* context and bring it forward without dragging the rest along. I was curating context before I had the word for it.

That's the window half. Once the library exists, the discipline flips. Into any given task's window goes only what that task needs: the two files, the one contract, the relevant prior decision. Everything else stays on the shelf. The context window is precious. The skill is not stuffing it; the skill is choosing what goes in.

The scripture names both halves in one verse. "Organize yourselves; *prepare every needful thing*; and establish a house... a house of order" ([D&C 88:119](../../gospel-library/eng/scriptures/dc-testament/dc/88.md)). [qr](../../gospel-library/eng/scriptures/dc-testament/dc/88.md) *Prepare every needful thing* is the library: make it ready and available. The *house of order* is the window, with everything in its place, nothing crowding what matters. Understanding then comes the way scripture says it always comes: a little at a time, line upon line, drawn from a prepared store. (Part Two: Line upon Line — the doctrine under this practice.)

Today this is a `./context` folder of work repos, a `./external_context` folder of references, knowledge stores wired in over a protocol, and a compaction step for when a window fills anyway. The mechanics will date fast — windows may grow so large that "waste nothing" stops biting the way it does now. But the deeper move won't: prepare a store the agent can draw from, and bring forward only what the moment needs.

**Try this.** Before your next big task, build the library: clone the repos the agent might need into one folder it can read, instead of pasting snippets into the chat. Then, for the task itself, name what to pull into view — and trust the shelf for the rest.

> **Remember:** Two motions, never confused. Build the agent a *library* it can explore — prepare every needful thing — then curate the *window* to only what this task needs. The shelf is vast and on disk; the window is small and sacred. Don't starve the agent, and don't drown it.
