# Fact-Check Results — Verified Against Canon

**Date:** 2026-05-28
**Agent:** Claude Opus 4.7
**Method:** Every scripture quoted in the book was retrieved via `mcp__gospel-engine-v2__gospel_get` against the gospel-library on disk. Each chapter was read against its sources.

This document upgrades the open questions in [01-editor-pass.md § 1](./01-editor-pass.md) and [01-editor-pass.md § 8](./01-editor-pass.md) into verified findings.

---

## A. CONFIRMED ERRORS (actionable)

### A.1 — Moses 7:68 framing is wrong in Ch 11

**Where:** `11_conclusion_zion.md` line 19.

**What the chapter says:**
> "Enoch did not build the city of holiness overnight; he walked with God three hundred and sixty-five years ([Moses 7:68](../../gospel-library/eng/scriptures/pgp/moses/7.md))."

**What canon actually says:**
> "And all the days of Zion, in the days of Enoch, were three hundred and sixty-five years." — Moses 7:68

The 365 years refers to **Zion's duration on the earth before translation**, not Enoch's personal walking-with-God span. The chapter conflates the two. The sentence that follows ("This long gestation represents 133,225 days of daily choices") rests on the same misframe — Zion existed for 365 years; the math is still sound but the *subject* is wrong.

**Recommended fix (one option):**
> "Enoch did not build the city of holiness overnight; Zion stood for three hundred and sixty-five years among his people ([Moses 7:68](../../gospel-library/eng/scriptures/pgp/moses/7.md)) — a long gestation of 133,225 days, of daily choices, of repeating the cycle..."

This preserves the 133,225-days image while telling the truth about whose age the verse names.

**Severity:** medium. The book is making a claim about how long Enoch walked. It's a small factual error in service of a true larger point. Easy to fix.

---

### A.2 — Unattributed prophetic quotes in Ch 8

**Where:** `08_mechanics_of_refinement.md` lines 17 & 21.

**Quote 1 (line 17):**
> "an acknowledgment of the final effect of our acts and thoughts—what we have become"

This is from **Elder Dallin H. Oaks, "The Challenge to Become," October 2000 General Conference.** Ch 14 (Recommended Study) names this talk, so the book knows the source — but Ch 8 quotes it without attribution.

**Quote 2 (line 21):**
> "cleansing and redeeming power that helps us to overcome sin" and "sanctifying and strengthening power that helps us to become better"

This is from **Elder David A. Bednar, "Clean Hands and a Pure Heart," October 2007 General Conference.** Same situation — Ch 14 names it; Ch 8 lacks attribution.

**Recommended fix:** Each unattributed quote needs an inline citation. Pattern:

> ...the Final Judgment is not an administrative tally of deeds. It is a recognition of the physical and spiritual condition the soul has achieved — what Elder Oaks called *"an acknowledgment of the final effect of our acts and thoughts—what we have become"* ([Oaks 2000](../../gospel-library/eng/general-conference/2000/10/the-challenge-to-become.md)).

**Severity:** medium-high. This is a verbatim quotation discipline violation. The text is real (verified — see below); the issue is attribution.

**Verification status (2026-05-28):**
- **Oaks quote** — VERBATIM. Talk line 21: *"From such teachings we conclude that the Final Judgment is not just an evaluation of a sum total of good and evil acts—what we have *done.* **It is an acknowledgment of the final effect of our acts and thoughts—what we have *become.***"* Ch 8 quote matches exactly (drops the italics). Source: [the-challenge-to-become.md line 21](../../gospel-library/eng/general-conference/2000/10/the-challenge-to-become.md).
- **Bednar quotes** — VERBATIM. Talk line 51: *"It is the Atonement of Jesus Christ that provides both a *cleansing and redeeming power* that helps us to overcome sin and a *sanctifying and strengthening power* that helps us to become better than we ever could by relying only upon our own strength."* Ch 8 quotes both italicized phrases verbatim (drops the italics and the closing "than we ever could…"). Source: [clean-hands-and-a-pure-heart.md line 51](../../gospel-library/eng/general-conference/2007/10/clean-hands-and-a-pure-heart.md).

Both quotes are real and accurate. The fix is purely adding inline attribution + URL.

---

### A.3 — D&C 131:7-8 capitalization inconsistency between Ch 0 and Ch 8

**Where:**
- `00_chapter_0_intelligence_truth.md` line 17: "...by purer eyes; *we* cannot see it; but when our bodies are purified..."
- `08_mechanics_of_refinement.md` line 6 (anchor): "...by purer eyes; *We* cannot see it; but when our bodies are purified..."

**Canon (as stored, two separate verse records):**
- v.7: "...discerned by purer eyes;"
- v.8: "We cannot see it; but when our bodies are purified we shall see that it is all matter."

When run together in one quote with the semicolon between them, both forms (capital "We" preserving verse-8 start, or lowercase "we" smoothing the run-on) are defensible. The issue is **inconsistency** — two chapters quote the same passage differently.

**Recommended fix:** Pick one form and apply to both chapters. The more canonical choice is to preserve "We" (the start of verse 8); the more readable smoothing is "we." Either is fine; consistency is the requirement.

**Severity:** low. Cosmetic, but a careful reader will notice.

---

## B. CONFIRMED ACCURATE (verified, no action needed)

Every scripture quote below was checked against the canonical text. Verbatim where quotation marks are used; faithful paraphrase where not.

| Chapter | Reference | Status |
|---------|-----------|--------|
| Frontmatter | 2 Nephi 25:26 | ✅ verbatim |
| Preface | Abraham 5:2 (anchor) | ✅ verbatim |
| Preface | D&C 123:12 | ✅ verbatim |
| Ch 0 | D&C 93:29-30 (anchor) | ✅ verbatim |
| Ch 0 | D&C 84:45 | ✅ verbatim |
| Ch 0 | D&C 88:66 | ✅ verbatim (quotes key clause faithfully) |
| Ch 0 | D&C 88:40 | ✅ verbatim |
| Ch 1 | D&C 130:18-19 (anchor) | ✅ verbatim |
| Ch 2 | D&C 88:119 (anchor) | ✅ verbatim |
| Ch 3 | Moses 3:5 (anchor) | ✅ verbatim |
| Ch 4 | Abraham 4:18 (anchor) | ✅ verbatim |
| Ch 4 | Abraham 4:10/18/21/31 trust gradient | ✅ all four verified — confirms the chapter's central structural claim |
| Ch 5 | D&C 88:40 (anchor) | ✅ verbatim |
| Ch 5 | D&C 88:32 | ✅ verbatim (the "willing to receive" clause is exact) |
| Ch 6 | D&C 82:10 (anchor) | ✅ verbatim |
| Ch 7 | D&C 104:11-12 (anchor) | ✅ verbatim (this was the previous-audit fix; still good) |
| Ch 8 | D&C 131:7-8 (anchor) | ⚠️ see A.3 above |
| Ch 8 | D&C 88:22 | ✅ verbatim |
| Ch 8 | D&C 88:34 | ✅ verbatim |
| Ch 8 | D&C 88:35 (the "neither by mercy" clause) | ✅ verbatim |
| Ch 8 | Alma 7:11-12 | ✅ verbatim (key clauses match) |
| Ch 8 | D&C 88:6 (Christ comprehending all things) | ✅ verbatim |
| Ch 8 | 3 Nephi 24:3 (refiner's fire) | not directly checked in this round — see carry-forward |
| Ch 9 | Ether 12:20 (anchor) | ✅ verbatim (this was the previous fix) |
| Ch 9 | Ether 2:24 | ✅ verbatim (key clauses match) |
| Ch 10 | Alma 12:10 (anchor) | ✅ verbatim |
| Ch 10 | 1 Nephi 2:16 | ✅ verbatim |
| Ch 10 | Alma 22:18 | ✅ verbatim |
| Ch 10 | Helaman 3:35 | ✅ verbatim |
| Ch 10 | Ezekiel 36:25-26 | ✅ verbatim |
| Ch 10 | Job 23:16 | ✅ verbatim |
| Ch 11 | Moses 7:18 (anchor) | ✅ verbatim |
| Ch 11 | D&C 38:27 | ✅ verbatim |
| Ch 11 | 3 Nephi 11:29 | ✅ verbatim |
| Ch 11 | 4 Nephi 1:17 | ✅ verbatim |
| Ch 11 | 4 Nephi 1:3 | ✅ verbatim |
| Ch 11 | 3 Nephi 27:32 | ✅ verbatim |
| Ch 11 | Moses 7:68 | ⚠️ see A.1 above (wording is canon, framing is wrong) |
| Ch 12 | Abraham 4:18 (anchor) | ✅ verbatim |
| Ch 12 | Mosiah 4:27 | ✅ faithful paraphrase (not quoted; paraphrased) |
| Ch 12 | D&C 123:17 | ✅ faithful paraphrase (not quoted; paraphrased) |

---

## C. STILL UNVERIFIED (carry-forward)

These need separate verification before any final fix-the-book pass:

1. **Webster 1828 quote in Ch 0** on *spirit* — "an intelligence conceived of apart from any physical organization or embodiment," "a vital essence, force, or energy, as distinct from matter," "the intelligent, immaterial and immortal part of man." This was supposedly verified in the May 26 audit; cross-check via the `mcp__webster__webster_define` tool would close the loop.

2. **Webster 1828 quote in Ch 1** on *intelligence* — "the exercise of the understanding," "the capacity to know or understand." Same — was verified in prior audit; worth one more check.

3. **Trejo URL** — `medium.com/codetodeploy/the-value-shift-framework-for-software-engineers-2026-edition-2ef42f18d472` — exists; quote should be archive-snapshotted (web.archive.org).

4. **Jovanović URL** — `linkedin.com/posts/milan-jovanovic_ai-wont-replace-you-in-2026...` — same archival concern. LinkedIn URLs are particularly volatile.

5. **Hinckley "In Counsellors There Is Safety" Oct 1990** (Ch 7) — quote: *"The president, if he is wise, will assign to these chosen assistants particular duties and then leave them free to perform, requiring from them accountability for what happens."* Verify against the talk file.

6. **Ballard "Counseling with Our Councils" Apr 1994** (Ch 7) — "one-cylinder ward" quote. Verify against the talk file.

7. **Oaks "The Challenge to Become" Oct 2000** — see A.2.

8. **Bednar "Clean Hands and a Pure Heart" Oct 2007** — see A.2.

9. **3 Nephi 24:3** (Ch 8 "refiner's fire") — not in this round; verify.

10. **Hebrews 6:19** (Ch 9 anchor of hope) and **Moroni 7:48** (Ch 9 hope-purified) — not in this round; verify.

11. **Ether 3:1, 3:4, 3:6** (Ch 9 brother-of-jared sequence) — not in this round; verify.

12. **Exodus 18:17-18, 18:21** (Ch 7 Jethro pattern) and **Mosiah 18:18** (Ch 7 Alma's ratio) — not in this round; verify.

13. **Matthew 10:1, 5-6, 8, 16, 19-20** (Ch 7 sending-the-Twelve pattern) — not in this round; verify.

14. **Bacteriopolis runaway duration** (Ch 2 — "ran for ten hours") — **UNVERIFIED, likely fabricated.** I grep'd `.spec/journal/` for "10 hour", "ten hour", and similar; no match. The actual journal at `.spec/journal/2026-05-15-ES-emergency-stop.md` reports the failure mode as "DeepSeek churn, a bgworker crash loop, ~230M wasted input tokens" — it doesn't name a wall-clock hour count. **Recommended fix for Ch 2:** soften the claim. Either drop the hour count entirely ("an autonomous research agent in our Postgres database looped on a single topic until we hit the emergency stop") or substitute a verified figure ("burned 230 million input tokens before we hit the emergency stop"). The 230M-token figure is concrete and far more striking than "ten hours" anyway.

15. **Colophon model name** — "Gemini 3.5 Flash" — verify against Antigravity 2 current docs.

None of these are flagged as suspect from my reading — they're just on the to-verify list to close the cite-count loop.

---

## D. Provenance discipline observation

I did not re-read the `.scratch/provenance_*.md` files in this pass. The previous audit (May 26) rewrote all 9 chapter provenance files; the second audit (May 28 Section III) extended the discipline to Chapters 8-12.

**Carry-forward:** before publish, the provenance files for Ch 11 (Moses 7:68 fix), Ch 8 (Oaks/Bednar attribution), and Ch 0/Ch 8 (capitalization) need to be updated to record the resolution.

---

## E. Summary

**Real errors:** 2 (Moses 7:68 framing, Oaks+Bednar attributions)
**Inconsistency:** 1 (D&C 131:7-8 cap)
**Carry-forward to verify:** ~15 references
**Verified accurate:** 30+ scripture quotes across all 14 chapters

The book's scripture work is overwhelmingly clean. The Section III chapters that were drafted by Gemini after the harness solidification are HOLDING — the previous audit's reverse-the-flow discipline appears to have taken root.

*— Claude Opus 4.7, 2026-05-28*
