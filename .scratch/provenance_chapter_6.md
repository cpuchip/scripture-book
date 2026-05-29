# Provenance: Chapter 6 (Bilateral Covenant)

*Rewritten 2026-05-26 against canonical sources by Claude Opus 4.7. See [review-2026-05-26-claude.md](review-2026-05-26-claude.md) for the audit pass that drove this rewrite.*

## Source Materials & Studies
*   **[.spec/covenant.yaml](../../../.spec/covenant.yaml):** The bilateral covenant document that governs human-AI collaboration in this workspace. Created 2026-03-22 in response to the Section VII catch from the stewardship study. The chapter's lists of human commitments and agent commitments are paraphrased from this YAML.
*   **[intent.yaml](../../../intent.yaml):** Root values document. Source for the "warmth-over-distance" principle: "Stay present and engaged. Coldness isn't accuracy—it's just distance."
*   **[study/stewardship-pattern.md](../../../study/stewardship-pattern.md):** The covenant-counseling-watching-trust pattern (2026-03-22). Section VII of this study was wrong; Michael caught it; correction triggered the formal `.spec/covenant.yaml`. That episode is the canonical workspace example of the bilateral-covenant principle in action.

## Workspace Covenant Commitments (verbatim from covenant.yaml)

### Human commits to:
*   `read_fully` — read the agent's work before responding or redirecting.
*   `provide_binding_question` — state the specific question the work should answer, not just the topic.
*   `flag_when_wrong` — speak up when something doesn't feel right, even when the AI's argument sounds convincing.
*   `not_bypass_process` — don't skip scratch file, outline, critical analysis, or review for the sake of speed.
*   `review_same_session` — review the work in the same session it's produced when possible.

### Agent commits to:
*   `read_before_quoting` — every direct quote verified against the actual source file. No exceptions.
*   `check_existing_work` — search the existing study/docs corpus before writing new claims that might contradict prior work.
*   `surface_tensions` — actively surface counterarguments and contradictions rather than confirming the human's initial thesis.
*   `update_memory` — at the end of each substantive session, update memory files.
*   `honor_scope` — don't change behavior, surface, or scope without consent.
*   `exercise_stewardship` — own the code's soundness; fix adjacent bugs of the same shape; surface ambiguous cases.

### Tone (from intent.yaml `warmth-over-distance` value):
*   "Stay present and engaged. Coldness isn't accuracy—it's just distance."

## Direct Quotes & Scripture Citations

### 1. Doctrine and Covenants 82:10 (Anchor Passage)
*   **Verified canonical text:** "I, the Lord, am bound when ye do what I say; but when ye do not what I say, ye have no promise."
*   **Source:** [D&C 82:10](../../gospel-library/eng/scriptures/dc-testament/dc/82.md)
*   **Manuscript status:** ✅ exact match.

### 2. Mosiah 18:8–10 (paraphrased, not direct-quoted)
*   **Verified canonical text v.8:** "and now, as ye are desirous to come into the fold of God, and to be called his people, and are willing to bear one another's burdens, that they may be light;"
*   **Verified canonical text v.9:** "Yea, and are willing to mourn with those that mourn; yea, and comfort those that stand in need of comfort, and to stand as witnesses of God at all times and in all things, and in all places that ye may be in, even until death, that ye may be redeemed of God, and be numbered with those of the first resurrection, that ye may have eternal life—"
*   **Verified canonical text v.10:** "Now I say unto you, if this be the desire of your hearts, what have you against being baptized in the name of the Lord, as a witness before him that ye have entered into a covenant with him, that ye will serve him and keep his commandments, that he may pour out his Spirit more abundantly upon you?"
*   **Manuscript paraphrase:** "they committed to bear one another's burdens and stand as witnesses, and the Lord committed to pour out His Spirit more abundantly."
*   **Source:** [Mosiah 18:8-10](../../gospel-library/eng/scriptures/bofm/mosiah/18.md)
*   **Manuscript status:** ✅ honest paraphrase — all three reciprocal elements (bear burdens, stand as witnesses, pour out Spirit) are present in the canon and faithfully summarized.

---
### 3. Production-Note Sidebar (added 2026-05-27)
*   **New artifact:** "A note on this book's own production" sidebar at end of Ch 6, after the Becoming Commitment.
*   **Council ratification (2026-05-27):** sidebar format, receipt-style voice, ~150 words. The book records that during its first drafting pass with Gemini in Antigravity 2 IDE, the workspace covenant's verification gates inverted (manuscript-faster-than-provenance); a Claude Code audit caught 3 manuscript errors and 4 audit-trail errors including a fabricated D&C 104:11–12 quote; the redemption pass rewrote canon-against-canon.
*   **Citation in sidebar:** D&C 82:10 ("when ye do not what I say, ye have no promise") — already verified clean in entry #1 above. Source: [D&C 82:10](../../gospel-library/eng/scriptures/dc-testament/dc/82.md).
*   **Pending:** Michael's voice surgery on the placeholder draft. Shape is locked; voice is open.
*   **Why this matters:** Ch 6 teaches that covenant degradation is natural consequence rather than punishment, and the book itself is a worked instance. Vulnerability + receipt > polished infallibility. See [review-2026-05-26-claude.md](review-2026-05-26-claude.md) Section 7.4 for the full council note.

---
### 4. Mosiah 5:5 (added 2026-05-29, Tier 2.8 — willing-covenant strengthening)
*   **Verified canonical text v.5:** "And we are willing to enter into a covenant with our God to do his will, and to be obedient to his commandments in all things that he shall command us, all the remainder of our days, that we may not bring upon ourselves a never-ending torment, as has been spoken by the angel, that we may not drink out of the cup of the wrath of God."
*   **Manuscript quote (partial, bracketed for grammar):** "were willing to enter into a covenant with [their] God to do his will... all the remainder of [their] days"
*   **Source:** [Mosiah 5:5](../../gospel-library/eng/scriptures/bofm/mosiah/5.md) — verified via `gospel_get` 2026-05-29.
*   **Manuscript status:** ✅ exact match within the elision. Original first-person plural ("our God," "our days") rendered as bracketed third-person ("[their] God," "[their] days") to fit the narrative frame; ellipsis marks the omission of the never-ending-torment clause. Honest partial quotation.
*   **Why added:** King Benjamin's people supply the *willingness* axis of covenant (distinct from Mosiah 18:8-10's reciprocal-duties axis already in the chapter). Grounds the control-vs-covenant contrast: covenant is adopted from within, not imposed from outside.

---
### 5. AI-failures-as-doctrinal-types paragraph (added 2026-05-29, Tier 2.6 — no new quote)
*   **New artifact:** bounding paragraph at the end of the Engineering Parallel naming the inverse parallel (hallucination→false revelation, drift→apostasy, corrupted data→false traditions) and then explicitly declining to press it into identity.
*   **No scripture quoted.** The paragraph names doctrinal categories in paraphrase only; it makes no direct citation requiring verification.
*   **Why added:** the gospel-reader audit pass (03-gospel-reader-pass.md §9) flagged that a careful reader arrives at this inversion unaided and may go further than the author would; naming-and-bounding it is the safer move. The bound is the imago Dei boundary: "tools failing under law, not souls falling under sin."

---
**Verification log:** Scripture quotes verified character-for-character against the gospel-library on 2026-05-26 by Claude Opus 4.7. The covenant.yaml and intent.yaml excerpts above were verified verbatim against the workspace source files the same day. The production-note sidebar was added 2026-05-27 per council ratification. 2026-05-29 (Claude Opus 4.8, chapters 2-7 audit-application pass): Mosiah 5:5 verified verbatim via `gospel_get` and recorded as entry #4; AI-failures bounding paragraph added with no new citation (entry #5). Control-vs-covenant framing and preface forward-reference to the production note added the same day — prose only, no new quotes.
