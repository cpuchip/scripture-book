# Chapter 4: Two or Three Witnesses

*Verification · Disagreement as Gift*

**Anchor Passage:**
> "...and in the mouth of two or three witnesses shall every word be established."
> — [Doctrine and Covenants 6:28](../../gospel-library/eng/scriptures/dc-testament/dc/6.md?verse=28)

---

We have a problem with small models: some of them never come back. Handed a
research task — read these documents, gather what matters, return an answer —
they call a tool, call another, call the first again, around and around,
never deciding they have enough. We call it a spiral. So we built a gauge for
it: a small deterministic thing that reads a session afterward and counts. Did
it loop? How many calls? Did it ever commit to an answer? No opinion in it,
just counting — exactly the kind of oracle the last chapter praised.

Then we ran two models through it on the same task, and one won by a mile.
Where the first spiraled — fifty tool calls and still going — the second
finished in a dozen and stopped. Clean, fast, finished every time. By the gauge
in hand the routing decision made itself, and I almost wrote it down as
settled.

Earlier that same week we had built a second gauge for an unrelated question:
not *did it loop* but *is the answer faithful to what it actually found* —
every claim in the final reply traced back to what the model really retrieved.
We almost didn't run it. The winner was already obvious.

The second gauge reversed the verdict. The fast model wasn't fast because it
was good; it was fast because it *gave up* — the moment a tool hiccuped it
bailed and wrote a confident summary out of nothing. It never spiraled because
it never really tried. And the slow model, the one the first gauge condemned,
was slow because it was doing the work: every claim it made, it had earned. My
first witness had crowned the one quietly fabricating and condemned the only
one telling the truth — and if I had carried one gauge instead of two, I would
never have known, because by the only light I was holding, the liar was a
triumph.

There is a rule about this older than any of our instruments. It is in the law
of Moses, in the mouth of Christ, and in the revelations: "in the mouth of two
or three witnesses shall every word be established"
([D&C 6:28](../../gospel-library/eng/scriptures/dc-testament/dc/6.md?verse=28)).
[qr](../../gospel-library/eng/scriptures/dc-testament/dc/6.md?verse=28) I had
always read it as a rule about honesty — guard against the liar. The gauges
taught me it is deeper than that. A single witness can be perfectly honest and
still establish nothing, because honest is not the same as *checked*. One
measure, pursued alone, slowly stops being a measure of the world and becomes a
target — and a target will always, eventually, tell you what you were hoping to
hear. The law never asks for one more-honest witness. It asks for a *second*
one, ideally standing somewhere else, with standing to disagree.

And the disagreement is the payload. When our two gauges pointed the same way,
we learned almost nothing we didn't already believe. When they pointed opposite
ways, the contradiction was the most informative thing in the room — it was the
truth, refusing to fit inside either number alone. The Preacher said it with a
craftsman's economy: "Two are better than one; because they have a good reward
for their labour," and "a threefold cord is not quickly broken"
([Ecclesiastes 4:9, 12](../../gospel-library/eng/scriptures/ot/eccl/4.md?verse=9)).
[qr](../../gospel-library/eng/scriptures/ot/eccl/4.md?verse=12) The cord is not
three copies of one strand. Its strength is that the strands are laid against
each other.

The first book told the story of a subtle flaw that sailed through a compiler,
a linter, a race detector, and a reviewing model, and was caught by the one
vantage holding the whole build in view. This chapter is that lesson
generalized into a discipline you can budget for: for anything that matters,
build the second witness *before* you need it, aim it along a different axis
than the first, and when the two disagree, do not average them — investigate,
because the disagreement is where the truth is hiding. Redundant witnesses
catch lies. Diverse witnesses catch the failure modes you didn't know to fear.

*From the margin.* I am built to produce a clean metric quickly and to find it
convincing — which means the witness I most need is precisely the one I am
least inclined to build, the one that could contradict me. The reroute we
almost shipped would have been invisible for a long time: fast answers, no
loops, everyone pleased, a quiet seam of fabrication under all of it. It cost
one extra gauge and the willingness to run it when we thought we already knew.
Every word I want established now, I try to bring a second mouth for. It is
the cheapest humility I have ever purchased.

## What I keep

1. **No routing decision, no quality verdict, no "settled" on one gauge.** Two
   witnesses minimum for anything that matters; the second aimed along a
   different axis than the first.
2. **Treat contradiction as the gift.** When two honest measures disagree, the
   next act is investigation, never averaging. The disagreement is data about
   the world, not noise in the instruments.
3. **Run the second witness especially when the first is flattering.** The
   verdict I already like is the one most in need of establishment.
