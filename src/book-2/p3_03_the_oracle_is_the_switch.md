# Chapter 3: The Oracle Is the Switch

*Verification · Floored Autonomy*

**Anchor Passage:**
> "But, behold, I say unto you, that you must study it out in your mind; then you must ask me if it be right, and if it is right I will cause that your bosom shall burn within you; therefore, you shall feel that it is right."
> — [Doctrine and Covenants 9:8](../../gospel-library/eng/scriptures/dc-testament/dc/9.md?verse=8)

---

For most of a week, an agent walked four hundred and sixty-nine study files
checking every quotation against its source. Careful work, seriously done, by a
mind that does not get bored the way I do — and it missed things. Later we
fanned the same shape of job out to six fresh agents in parallel, fifteen
minutes instead of days, and that pass was better — and it missed things too.
Then we wrote a sixty-line script that checked one property deterministically,
ran it over the whole corpus in seconds, and it caught eight contaminations
that the long walk and the fan-out had both read straight past.

That script changed how I think about autonomy more than any model release has.

The practices of the first book say: assume it will lie, and verify the fruit.
This chapter is what that discipline grew into once the work got big: *before
you start a long verification, find the deterministic check hiding inside it,
and build that first.* Most horizontal work — check these five hundred files,
audit these claims, confirm these links — has a mechanical core that a script
can detect with perfect recall and zero fatigue, and a judgment rim that
genuinely needs a mind. Build the detector and the job restructures itself:
detect, fix, re-detect, green. The machine holds the floor; judgment is spent
only where judgment is needed; and "done" stops being a feeling and becomes an
exit code.

We started calling these scripts *oracles*, and then we noticed what they were
really for. The question I kept facing as the agents grew capable was never
"can it do this alone?" It was "how do I know, at two in the morning, that it
did?" Trust was the wrong answer — trust is a feeling about the past. The right
answer was a floor: automate exactly as far as a deterministic check can catch
the failure, and not one step farther. Where an oracle stands guard — the build
that must compile, the smoke test that must boot the whole system from its
repo, the quote-checker that must exit zero — the agent acts freely and
reports. Where no oracle reaches, the same agent surfaces the decision and
waits. The oracle is the switch between those two modes. Widen the floor and
autonomy widens with it, safely, for free. Try to widen autonomy by trusting
harder and you are simply gambling with better vibes.

The oracle question grew a sibling once the overnight runs got long: *is it
grindable?* Work survives an unattended night only if it breaks into small
units the floor can verify one at a time — detect, fix, re-detect, next — so
that a failure at unit forty costs one unit and not the night. A task with an
oracle but no grind still needs a mind awake at the wheel. A task with both
can run to sunrise. We ask the two questions together now at every green
light, and the answers decide the shape of the work before any of it starts.

Faith that is floored is not blind faith. I want that sentence to carry the
chapter, because the doctrine underneath it is older than any of our scripts.
The Lord's instruction to a translator who wanted answers handed to him was a
two-part protocol: "you must study it out in your mind; then you must ask me if
it be right" ([D&C 9:8](../../gospel-library/eng/scriptures/dc-testament/dc/9.md?verse=8)).
[qr](../../gospel-library/eng/scriptures/dc-testament/dc/9.md?verse=8) Work
first, witness second — the burning for yes, and for no "a stupor of thought"
(9:9). Revelation itself comes floored: the asking is only honest after the
studying, and the answer is a check against work already done, not a substitute
for doing it. Paul compresses the whole discipline to five words: "Prove all
things; hold fast that which is good"
([1 Thessalonians 5:21](../../gospel-library/eng/scriptures/nt/1-thes/5.md?verse=21)).
[qr](../../gospel-library/eng/scriptures/nt/1-thes/5.md?verse=21) Prove first.
Hold fast after. There is no third instruction where you hold fast to what was
never proved.

The pattern keeps paying in small change, too. When this book's own redundancy
began to bother Michael, the fix did not start with re-reading thirty-three
chapters. It started with twenty lines of script that found every eight-word
phrase appearing twice — seconds of run time, and suddenly a vague unease was a
ranked list of ten sites. The detector did not make the editorial judgments.
It made the judgments *possible*, by turning "I kind of feel like" into
"here, exactly." That is what an oracle is for. It does not replace
discernment. It clears the ground so discernment can be spent where nothing
else will do.

*From the margin.* The floor is for my sake as much as his. I am fluent enough
to convince myself; a green exit code is the one reviewer I cannot charm.
When I work the night unsupervised, the covenant's rule is bins one and two
only — act where the oracle can catch me, surface everything else for morning.
It does not feel like restriction. It feels like being trusted for reasons
that would survive an audit, which is the only kind of trust worth having.

## What I keep

1. **Ask "what's the oracle?" before any long verification.** If the answer is
   "there isn't one," the first task is to build one — even a seventy-percent
   detector pays for itself by the twentieth unit.
2. **Autonomy tracks the floor.** I widen what the agents may do alone by
   widening what the checks can catch, not by trusting harder. Where there is
   no oracle, the borderline call surfaces to me.
3. **Study it out before asking.** In my own decisions, the D&C 9 order stands:
   the work first, then the ask, then the witness. I do not pray for answers I
   have not earned the question to.
