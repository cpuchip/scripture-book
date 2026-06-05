# Cover print spec — *Beyond the Prompt* (hand this to your artist)

**Computed 2026-06-04 from KDP's formula for our book. Verify against KDP's official
Cover Calculator (kdp.amazon.com/cover-calculator) once the interior page count is FINAL.**

> ⚠️ **One caveat that matters:** the **spine width and full-wrap width depend on the
> page count**, and the interior is not final yet (a v4 audit + voicing pass come first).
> The **front cover is page-count-independent** — commission that now, safely. The spine
> and the assembled full wrap get locked *after* the interior page count is final. Numbers
> below are at the current **123 pages, white paper**; treat them as provisional until then.

---

## TL;DR for the artist
**Design the FRONT COVER at 6.25 in × 9.25 in, 300 DPI (1875 × 2775 px).** That's the
6 × 9 in trim plus 0.125 in bleed on all four sides. Keep all text and anything you can't
afford to lose **at least 0.5 in inside the edges** (the safe zone). Deliver a flattened
**PDF or PNG/TIFF at 300 DPI**, with fonts embedded or outlined. CMYK is ideal for print
(sRGB is accepted and auto-converted). Send it to me and I'll drop it into the full wrap.

---

## The exact numbers (6 × 9 in, 123 pp, white paper — PROVISIONAL on final page count)

### Front cover (commission this now)
| Spec | Value |
|---|---|
| Trim size | 6.0 × 9.0 in |
| **Art canvas (with full bleed)** | **6.25 × 9.25 in** |
| At 300 DPI | **1875 × 2775 px** |
| Bleed | 0.125 in all four sides |
| Safe zone (keep text inside) | 0.5 in from each trimmed edge → a ~5.0 × 8.0 in live area |
| Resolution | 300 DPI minimum (≤ 600 DPI) |
| Color | CMYK preferred; sRGB accepted (KDP converts) |
| Format | PDF (preferred), or PNG/TIFF, flattened, fonts embedded/outlined |

### Spine (I finalize after page count locks)
| Spec | Value (123 pp, white) |
|---|---|
| Spine width (white paper) | 0.002252 × pages = **0.277 in** |
| Spine width (cream paper) | 0.0025 × pages = 0.308 in |
| Spine text | Allowed (we're well over the 79-page minimum), but **0.277 in is thin** — keep spine type small and centered with ≥ 0.0625 in clear on each side. If you'd rather not risk it, we leave the spine blank. |

### Full wrap (the file KDP actually ingests — I assemble this)
| Spec | Value (123 pp, white) |
|---|---|
| Layout (L→R) | bleed · **back 6.0** · **spine 0.277** · **front 6.0** · bleed |
| **Full width** | 0.125 + 6 + 0.277 + 6 + 0.125 = **12.527 in** (3758 px @ 300 DPI) |
| **Full height** | 0.125 + 9 + 0.125 = **9.25 in** (2775 px @ 300 DPI) |
| Single PDF | back + spine + front as one image; < 650 MB; 300 DPI |
| Barcode | **Leave a clear ~2.0 × 1.2 in space, white, in the bottom-right of the BACK cover** — KDP prints its barcode there automatically. Don't add your own. |

---

## How the pieces come together
1. **You** get front-cover art at **6.25 × 9.25 in / 300 DPI** and send it to me.
2. **I** build the full wrap in Typst: your front art on the right, a typographic spine in
   the middle, and a back panel (the book description + a clear barcode zone) on the left —
   sized to the final page count. Output: one print-ready `cover.pdf`.
3. If you don't get art in time, I ship the **all-typographic** wrap I'm building now (title
   set in the interior's type) — honest, consistent, upgradeable later.

## What I need from you for the back cover
- The **description/blurb** (I can draft 2–3 options for your pick).
- Optional: a 1–2 sentence author line.
- Paper choice (**white** or cream) — it changes the spine width slightly.

*Authoritative source: KDP Cover Calculator + "Create a Paperback Cover" help. Re-run the
calculator with the final page count before we submit.*
