# Note for the scripture-book agent — quote-audit classes from the workspace walk

*Left 2026-06-13 by the workspace `webster-1828` session, at Michael's request:
"we should probably double check on the book quotes too… leave a note for that
agent to do it, that way we're not stepping on its stewardship."*

**I did NOT touch the manuscript.** The book's quotes are your stewardship. This
note just hands you the error-classes the workspace **study-correctness walk**
(all 469 `study/` files, completed 2026-06-13) found most often, so you can run
the same checks on *Beyond the Prompt* yourself and decide what to fix.

## The walk's method (reusable here)
For every quote with quotation marks, open the actual source and compare
character-for-character. Training-memory paraphrase reads as exact and isn't.
The four discovery tools that caught the most:
- **Direct grep of the source file** for scripture (the gospel-library verse
  text is `**N.** text`; strip `<sup>` footnote markers before comparing).
- **The repaired Webster 1828 MCP** (`webster_define` / the dual-edition
  `define`) for any "Webster 1828 says…" citation — see the contamination class
  below; this is the one that bit us hardest.
- **The talk/Ensign file itself** for conference quotes, dates, and counted
  claims — never trust a remembered date or number.
- **BYU Citation Index / the source** for any statistical or biographical claim.

## The error-classes the walk found (in rough order of frequency)

1. **Webster 1913-as-1828 contamination.** For months the workspace's Webster
   tool unknowingly served the **1913** Revised Unabridged under an "1828"
   label. ~132 words across the corpus were quoted from the wrong edition — the
   senses, the illustrative quotes, and the synonym-notes differ. **If the book
   quotes Webster 1828 anywhere, re-verify every entry against the genuine 1828**
   (the workspace MCP is now repaired; webstersdictionary1828.com is the
   external authority). Tell: 1913 entries are longer, add synonym paragraphs,
   and sometimes invert the 1828 sense (e.g. WELD, CONSTRAINED).

2. **Confabulated "X says" attributions.** The single worst class. The walk
   found *fabricated* quotations attributed to real people — e.g. two "Todd
   says…" lines on a published study that were never said (one was actually the
   author's own prose, one was a scripture mis-attributed to the speaker). If
   the book quotes a podcast/interview/person, confirm the words exist in the
   actual transcript at the cited place. Paraphrase (indirect speech) is honest;
   quotation marks around unverified words are not.

3. **Dropped / added conjunctions and small word-swaps in scripture.** Real
   verses quoted *almost* right — a dropped "and," a "do"→"prepare for you," a
   pluralization, a "world"→"life." These pass a casual read. Grep the verse and
   diff it. (Examples the walk fixed: Alma 22:18 dropped "and" twice; Ether 2:25
   "do"→"prepare for you"; an Oaks quote "world"→"life".)

4. **Counted-number / date / biographical claims stated as fact.** "Cited in six
   talks," "the earliest reference is 1944," "33 times since Brigham Young,"
   "Sabbath Is a Delight, Oct 2015." These read as facts and get trusted as
   facts. Each needs a source checked *this pass*, not memory. The walk found
   several mis-dated talks (Nelson "Sabbath Is a Delight" was **April** 2015,
   not October) and several off-by-N counts. Treat every number as a citation.

5. **Phantom phrases / quote-continuations.** A real quote extended with words
   the source doesn't contain (e.g. an Ether 12:19-20 quote with an appended
   "because of his relation to the Lord" that isn't there). Verify where the
   quote actually *ends*.

6. **Broken/mis-targeted reference links.** Citation text correct, hyperlink
   pointing at the wrong chapter/section (the walk's one back-half fix: "D&C
   109:76" linked to section 76, not 109). Worth a link-target sweep if the book
   has live links.

## Where the workspace record lives (for cross-reference)
- Full per-file audit trail: `study/.audit/findings.md` (workspace).
- The Webster remediation incident + known-issues: the workspace data-integrity
  brief (`.spec/proposals/webster-1828-data-integrity.md`).
- The book already has a `v4-honesty-audit-plan.md` here — this quote-audit is a
  natural companion pass to that.

No rush, and no obligation to match the workspace's visible-dated-correction-note
convention — the published-face style is Michael's call for the book. This is
just the checklist, handed over so the same discipline reaches the manuscript.
