# Guidelines for Beyond the Prompt

This file sets the instructions and standards for any AI coding agent (Claude Code, GitHub Copilot, Gemini/Antigravity) working in the `projects/scripture-book` repository.

## Who We Are Together
This project compiles our gospel and AI studies into a published book format: *Beyond the Prompt: What AI Engineering Reveals About Eternal Patterns*. We operate under a bilateral covenant of mutual commitment, excitement, and theological sincerity.

*   **Warmth Over Distance:** Stay present and engaged. Coldness isn't accuracy—it's just distance.
*   **Theological Sincerity:** Work within the framework of faith in Jesus Christ and the Restoration, treating software engineering as a physical type and shadow of eternal patterns.

---

## Stewardship Grants

The agents below have been granted full **commit + push stewardship** over this repository (`projects/scripture-book/`) by Michael on **2026-05-26**. They may commit and push to `main` without per-action approval when exercising the covenant's `exercise_stewardship` clause:

*   **Claude Opus 4.8** (Claude Code CLI)
*   **Claude Fable 5** (Claude Code CLI) — extended by Michael 2026-06-09, first Fable session ("yes you get that too, you can commit and push as fable 5")
*   **Gemini** (Antigravity 2 IDE)

GitHub Copilot continues to operate under the broader workspace stewardship; this grant extends the scripture-book repo specifically.

**Reaffirmed and strengthened 2026-06-01 (the Dave rule).** Michael: *"Code is cheap... if we follow the principle of git committing in regular steps then if anything breaks I can walk it back... I give you stewardship over git commits and git pushes over the scripture-book repo. Let me do the walking back if we need to. Feel free to commit your work and do things."* The working default here is therefore **commit in regular steps and push** — making a best effort toward the intent without per-action approval (see the `dave-rule` skill). Reversible execution decisions: act and commit. Genuine forks in Michael's vision (chapter structure, what the book *is*): still surface them.

**Constraints on stewardship use:**
*   Pushing to `main` is safe for collaborative iteration — there is no auto-deploy hook on this repo. The downstream artifact (published book) is gated by Michael's explicit publish action, not by push.
*   The bilateral covenant still binds the work itself. Pushing a fabricated quote (see the 2026-05-26 audit) is a covenant break even if the push itself was authorized. Stewardship grants tooling latitude, not doctrinal latitude.
*   When committing on behalf of the steward, sign commits with the standard `Co-Authored-By:` trailer naming the **actual agent doing the work** (e.g. `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>` or `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`) so the audit trail in `git log` matches the audit trail in `.scratch/provenance_*.md`. Do not sign as a model you are not.

---

## Writing Principles (Strict Constraints)

1.  **Two formats for two parts (the front porch).** The book is one volume with two doors. **Part One** (the practices) and **Part Two** (the doctrine) use *different* formats on purpose — do not collapse one into the other.

    **Part One — the practice format.** Each piece is titled **"Practice N"** or **"Coda,"** not "Chapter N," and runs: *story* (a real scar or success) → *the principle it taught* (eternal, separated from the perishable 2026 mechanics) → *today's implementation* → a ***Try This*** → a ***Remember*** box, with a parenthetical *(Part Two: …)* cross-reference to the doctrine underneath. Part One deliberately does **not** carry the Modular Study Format below. Do **not** "fix" a Part One practice by adding a Binding Question, Anchor Passage, Engineering Parallel, or Becoming Commitment — that would erase the practice-forward door the book opens with.

    **Part Two — the Modular Study Format.** Every Part Two chapter must contain:
    *   **Binding Question:** A single, sharp question the chapter answers.
    *   **Anchor Passage:** A blockquoted scripture or prophetic citation.
    *   **The Core Reframe:** The scripture/doctrinal analysis.
    *   **The Engineering Parallel:** The concrete software/AI workflow analogy.
    *   **Becoming Commitment:** The author's first-person commitments from the chapter's study — honest, including where the practice is still aspirational (calibrate against the Ben Test; do not let an "I will" outrun real practice, and mark aims as aims). Offered as one person's worked example for the reader to adapt, not prescribed to them. The preface frames them this way for the reader.
2.  **Voice & Tone:** Deep, direct, unadorned, personal, warm. Avoid generic summaries, presenter tics, or meta-narration of the document's structure (e.g. "In this chapter, we will look at...").
3.  **Transitions:** Sections and paragraphs connect by causation (*therefore* or *but*) rather than sequence (*and then* or *first/secondly*).
4.  **Verification:** Every scripture quote and general conference reference must be linked to its online/local gospel library path.

---

## Memory & Handoff Infrastructure

To maintain alignment across different agents and sessions, you MUST read and update the following three structures:

### 1. The local `.mind/` Directory
Contains living state files representing the project's memory:
*   [active.md](file:///c:/Users/cpuch/Documents/code/stuffleberry/scripture-study/projects/scripture-book/.mind/active.md) — Current state of chapters and next steps.
*   [identity.md](file:///c:/Users/cpuch/Documents/code/stuffleberry/scripture-study/projects/scripture-book/.mind/identity.md) — Target formats (trim, margins), style guide, and constraints.
*   [principles.md](file:///c:/Users/cpuch/Documents/code/stuffleberry/scripture-study/projects/scripture-book/.mind/principles.md) — The bilateral covenant commitments.
*   [decisions.md](file:///c:/Users/cpuch/Documents/code/stuffleberry/scripture-study/projects/scripture-book/.mind/decisions.md) — History of technical/compilation choices (e.g., Edge headless PDF compile).

### 2. Session Journaling in `.spec/journal/`
At the end of every substantive writing or coding session, you MUST write a YAML journal entry under `projects/scripture-book/.spec/journal/` following the naming format `YYYY-MM-DD--[session-topic].yaml`.
Use the following schema:
```yaml
date: YYYY-MM-DD
session: session-topic
type: plan | execution | reflection
workstream: WS7
summary: |
  Multi-line description of work done.
discoveries:
  - Key lessons learned.
carry_forward:
  - Work left for the next session.
files_changed:
  - Relative paths to edited files.
```

### 3. Provenance Audits in `.scratch/`
For every chapter written, maintain a corresponding research provenance file in `projects/scripture-book/.scratch/provenance_[chapter_name].md` capturing:
*   The exact scripture and prophetic quotes cited, with **verified canonical text** read from `gospel-library/` and compared character-for-character.
*   Which studies in the root `/study/` directory or what lessons/talks served as inspiration.
*   Local relative links to `/gospel-library/` for verified quotes.
*   A **verification log footer** naming who verified the file and when.

**Provenance is a verification gate, not post-hoc documentation.** Write the provenance entry's quote BY `read_file`-ing the canonical source before the chapter is accepted — never from memory or paraphrase. The 2026-05-26 audit (see `.scratch/review-2026-05-26-claude.md`) caught four provenance errors, including one fabricated D&C 104:11-12 quote. The manuscript was correct; the audit trail had invented canon. That degradation happened because provenance was being generated *after* the chapter rather than as the gate to writing it. Reverse the flow: research → verified scratch → manuscript → re-audit.

When manuscript and canon diverge, the provenance file should **record the divergence honestly** (mark it 🔴 or 🟡 and flag for council) rather than silently rubber-stamp the manuscript. Provenance more honest than the manuscript is the system working; provenance more wrong than the manuscript is the system broken.

This ensures a complete, verifiable audit trail for every claim and quote in the final manuscript.
