# Fact-Check Pass — v2 Audit (2026-05-29)

*Verification of quoted scripture, Webster 1828 entries, and prophetic-talk attributions against canon, by Claude Opus 4.8. Method: every quote below was checked against the gospel-library via `mcp__gospel-engine-v2__gospel_get` (scripture), `mcp__webster__webster_define` (1828), or the local general-conference file (talks) THIS session. Priority was the rebuilt chapters (8, 9, 10, 12), whose provenance files predate the 2026-05-29 rebuilds, plus the never-filed glossary/further-reading citations. Chapter 11's seven quotes were re-verified earlier today (`provenance_chapter_11.md`); chapters 0–7 were verified in the completion + chapters-2-7 passes earlier today and are not re-listed exhaustively here.*

---

## Headline

The rebuilds introduced **no scripture quote drift.** Every one of the 28+ quotes checked this session matches canon character-for-character. Both Webster 1828 quotes are exact. This is the reassuring result: the heavy 2026-05-29 chapter rebuilds did not fabricate or corrupt a single verse. Three real errors surfaced, none of them a misquote — a wrong talk **date**, a wrong **word** (not in quotation marks), and an imprecise **number**.

---

## Tier 3 — Confirmed errors (actionable)

### FC-1 — Nelson talk date is wrong in Chapter 11
- `11_the_seventh_time.md:21` says Elder Nelson "built his **October 2015** talk around this distinction."
- `16_further_reading.md:24` lists "**The Sabbath Is a Delight (April 2015)**."
- **Verified:** the local file is `gospel-library/eng/general-conference/2015/04/the-sabbath-is-a-delight.md`. The talk is **April 2015 general conference.** Chapter 11 is the error; Further Reading is correct.
- **Fix:** change Chapter 11 "October 2015" → "April 2015."

### FC-2 — "molting / molted" should be "molten" (or "melted") in Chapter 9
- `09_hope_and_the_veil.md:23` "molting sixteen small stones out of a rock" and `:57` "molted sixteen small stones out of a rock."
- **Verified Ether 3:1:** "did **molten** out of a rock sixteen small stones." The scriptural verb is *molten* (archaic past of *melt*). *Molt/molted* means to shed (feathers, skin) — a different word. The manuscript narration (not a direct quote) uses the wrong verb, twice.
- **Fix:** "molten sixteen small stones out of a rock" or "melted sixteen small stones out of a rock." Low stakes, but a careful reader will catch it.

### FC-3 — "133,225 days" is imprecise in Chapter 12
- `12_conclusion_zion.md:21` "three hundred and sixty-five years—represents 133,225 days."
- 365 × 365 = 133,225, but 365 calendar **years** ≈ 133,316 days once leap years are counted. The figure silently treats a year as exactly 365 days. **Verified Moses 7:68:** "And all the days of Zion, in the days of Enoch, were three hundred and sixty-five years." (The 365-*year* figure is correct; the day-count is the rhetorical flourish that's off.)
- **Fix:** soften to "more than 133,000 days" or drop the day-count. Minor.

---

## Verified accurate (sample of the 28+ checked this session)

**Chapter 8 (rebuilt):** D&C 88:22 ✅, 88:34 (verified earlier) ✅, 88:6 ✅, 88:67 ✅ (accurate elision of the "no darkness" clause), Alma 7:11–12 ✅, 3 Nephi 24:3 ✅, Matthew 6:22 ✅. (LoF 7:16 "prototype of all saved beings" — Lectures on Faith, not in `gospel_get`; carry-forward to verify against `/books/lectures-on-faith/lecture-7.md`.)

**Chapter 9 (rebuilt, longest):** Ether 2:20 ✅, 2:23 ✅, 3:1 ✅ (text exact aside from FC-2 narration), 3:4 ✅, 1 Nephi 8:25 ✅, 8:30 ✅, Helaman 6:36 "easiness and willingness to believe" ✅, 15:5 "walk circumspectly before God" ✅, Hebrews 6:19 "entereth into that within the veil" ✅, Moroni 7:48 ✅. (1 Nephi 8:28, Helaman 3:33 / 4:13 / 4:26 / 6:32 / 7:6 not re-pulled this batch — high confidence, standard text; carry-forward for completeness.)

**Chapter 10 (rebuilt):** Alma 12:10 (anchor, verified earlier) ✅, 1 Nephi 2:16 ✅, Ezekiel 36:25–26 ✅ ("an heart of flesh" exact), Alma 22:18 "I will give away all my sins to know thee" ✅, Job 23:16 ✅, Mark 4:27 ✅, Helaman 3:35 (verified earlier) ✅.

**Chapter 12 (rebuilt):** Moses 7:18 (anchor) ✅, D&C 38:27 "be one; and if ye are not one ye are not mine" ✅, 3 Nephi 11:29 ✅, 4 Nephi 1:17 "-ites" ✅, 4 Nephi 1:3 "all things common" ✅, 3 Nephi 27:32 ✅, Moses 7:68 (365 years) ✅, Moses 7:69 ✅ (Zion received "into his own bosom" — supports Ch 12 `:21`).

**Webster 1828:**
- *spirit* (Ch 0 `:13`): "an intelligence conceived of apart from any physical organization or embodiment," "vital essence, force, or energy, as distinct from matter" (def 3), and "the intelligent, immaterial and immortal part of man" (def 4) — **all three exact.** ✅
- *intelligence* (Ch 1 `:23`): "the exercise of the understanding" (def 1) and "the capacity to know or understand" (def 2) — **both exact.** ✅

**Prophetic-talk attributions:**
- Oaks, "The Challenge to Become," **October 2000** ✅ (used Ch 8; quote "an acknowledgment of the final effect of our acts and thoughts—what we have become" — carry-forward to confirm verbatim against the talk file, but title/date/author correct).
- Bednar, "Clean Hands and a Pure Heart," **October 2007** ✅ (Ch 8 / Further Reading).
- Bednar, "In the Space of Not Many Years," **October 2024** ✅ (Ch 9 / Further Reading).
- Ballard, "Counseling with Our Councils," **1994** ✅ (Ch 7, link `/1994/04/`).
- Hinckley, "In … Counsellors There Is Safety," **1990** ✅ (Ch 7, link `/1990/10/`).
- Christofferson, "Come to Zion," **October 2008** ✅ (file present in `2008/10/`).
- Pearce, "Keep Walking, and Give Time a Chance," **April 1997** ✅ (file present in `1997/04/`).
- Nelson, "The Sabbath Is a Delight," **April 2015** ✅ (file in `2015/04/`) — see FC-1: Chapter 11 misdates it.

---

## Carry-forward (verify before print, not blocking)
- LoF 7:16 "prototype of all saved beings" — confirm against `/books/lectures-on-faith/lecture-7.md`.
- Verbatim text of the Oaks "what we have become" clause and the Bednar 2007 "cleansing/sanctifying" framing against the talk files (titles/dates/authors confirmed; exact wording is the remaining check).
- 1 Nephi 8:28; Helaman 3:33 / 4:13 / 4:26 / 6:32 / 7:6 (cited in Ch 9; standard text, not re-pulled this batch).
- The glossary's scripture citations (added this session) are references, not quotes — links resolve; no verbatim text to verify.

## For the synthesis
FC-1 (Nelson date) is a clean Tier 3 fix that ships without controversy. FC-2 and FC-3 are minor. The larger point for the COUNCIL: the provenance files for chapters 8/9/10/12 should now be **rewritten** to match the rebuilt text (they currently describe pre-rebuild drafts), and this session's verifications give the verified-text basis to do it. That closes the "rebuilt-chapter provenance predates rebuilds" gap logged in `.mind/active.md`.
