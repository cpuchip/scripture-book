"""QR-collision detector for dist/manuscript.pdf.

QR codes render as ~0.85in (≈61pt) bordered boxes in the page margins. Two QRs
whose vertical extents overlap on the same page are a collision (they print on
top of each other). This walks every page, finds QR-sized rects via
get_drawings, and flags vertical overlaps.

Usage:  python scripts/check_qr_collisions.py [path/to.pdf]
Exit 0 = no collisions; exit 1 = collisions found (listed on stdout).

(Rewritten 2026-06-11 for the v4 walk — the original detector from the
2026-06-03 QR pass lived in a gitignored dist/ scratch and was lost with its
session. This one is committed.)
"""
import sys

import fitz  # PyMuPDF


def find_qr_rects(page):
    """QR border boxes: square-ish rects 50-75pt a side."""
    rects = []
    for d in page.get_drawings():
        r = d["rect"]
        if 50 <= r.width <= 75 and 50 <= r.height <= 75:
            rects.append(r)
    # Dedupe near-identical rects (stroke + fill layers of the same box)
    out = []
    for r in sorted(rects, key=lambda r: (round(r.y0), round(r.x0))):
        if not any(abs(r.y0 - o.y0) < 3 and abs(r.x0 - o.x0) < 3 for o in out):
            out.append(r)
    return out


def main(pdf_path="dist/manuscript.pdf"):
    doc = fitz.open(pdf_path)
    collisions = []
    qr_pages = 0
    total_qrs = 0
    for pno, page in enumerate(doc, start=1):
        rects = find_qr_rects(page)
        if not rects:
            continue
        qr_pages += 1
        total_qrs += len(rects)
        rects.sort(key=lambda r: r.y0)
        for a, b in zip(rects, rects[1:]):
            if b.y0 < a.y1 - 1.0:  # 1pt tolerance
                collisions.append((pno, a, b))
    print(f"{len(doc)} pages · {total_qrs} QR boxes across {qr_pages} pages")
    if collisions:
        for pno, a, b in collisions:
            print(f"COLLISION p{pno}: y[{a.y0:.0f}-{a.y1:.0f}] overlaps y[{b.y0:.0f}-{b.y1:.0f}]")
        print(f"VERDICT: {len(collisions)} collision(s)")
        return 1
    print("VERDICT: 0 collisions")
    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
