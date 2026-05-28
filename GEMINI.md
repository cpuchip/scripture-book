# Scripture Book — Beyond the Prompt — Gemini Context

The canonical project instructions are shared with Copilot and Claude. Read them first, then the Gemini-specific addendum below.

@.github/copilot-instructions.md

---

## Gemini / Antigravity IDE Addendum

This file is loaded automatically by the Gemini agent / Antigravity IDE on session start in this subproject.

### Build Commands

Compile book PDF and EPUB:
```bash
python scripts/build.py
```

### Writing Principles (Strict Constraints)

1.  **Modular Study Format:** Every chapter must contain a *Binding Question*, *Anchor Passage*, *The Core Reframe*, *The Engineering Parallel*, and *Becoming Commitment*.
2.  **Voice & Tone:** Deep, direct, unadorned, personal, warm. Avoid generic summaries, presenter tics, or meta-narration.
3.  **Transitions:** Connect paragraphs/sections by causation (*therefore* or *but*) rather than sequence (*and then*).
4.  **Verification:** Every quote must be verified against source library files before committing. Write the corresponding `.scratch/provenance_[chapter].md` file character-for-character from canon.
