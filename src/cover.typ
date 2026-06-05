// Full-wrap paperback cover for "Beyond the Prompt" (6x9).
// Typographic baseline — swap the front panel for designed art when it arrives.
// IMPORTANT: rebuild spine + width AFTER the interior page count is final (post-v4).
// Render: docker run --rm -v "<repo>:/work" ghcr.io/typst/typst:latest compile /work/src/cover.typ /work/dist/cover.pdf

#let pages = 123                  // <-- update to final interior page count
#let paper-factor = 0.002252in    // white paper; cream = 0.0025in
#let trim-w = 6in
#let trim-h = 9in
#let bleed = 0.125in
#let safe = 0.5in
#let spine = pages * paper-factor
#let full-w = bleed + trim-w + spine + trim-w + bleed
#let full-h = bleed + trim-h + bleed

#let ink = rgb("#1f2630")
#let cream = rgb("#f4efe4")
#let gold = rgb("#a89968")
#let gold-lt = rgb("#cdbd92")
#let body-font = ("EB Garamond", "Garamond", "Georgia", "Libertinus Serif")

#set page(width: full-w, height: full-h, margin: 0pt)
#set text(font: body-font, fill: cream)

// background — fills the full bleed
#place(top + left, rect(width: full-w, height: full-h, fill: ink))

#let back-x = bleed
#let spine-x = bleed + trim-w
#let front-x = bleed + trim-w + spine

// ================= FRONT (right panel) =================
#place(top + left, dx: front-x + safe, dy: bleed + safe,
  box(width: trim-w - 2*safe, height: trim-h - 2*safe)[
    #set align(center)
    #v(1.1in)
    #text(size: 11pt, tracking: 4pt, fill: gold-lt)[GOSPEL · AI · CREATION]
    #v(0.55in)
    #text(size: 52pt, fill: cream)[Beyond\ the Prompt]
    #v(0.30in)
    #line(length: 28%, stroke: 0.75pt + gold)
    #v(0.30in)
    #text(size: 17pt, style: "italic", fill: gold-lt)[Discovering the Laws\ of Organized Intelligence]
    #v(1fr)
    #text(size: 14pt, tracking: 3pt, fill: cream)[MICHAEL STUFFLEBEAM]
    #v(0.15in)
  ]
)

// ================= SPINE =================
#place(top + left, dx: spine-x, dy: bleed,
  box(width: spine, height: trim-h)[
    #set align(center + horizon)
    #rotate(90deg, reflow: true,
      text(size: 10pt, tracking: 0.5pt, fill: cream)[
        Beyond the Prompt#h(0.9em)#text(fill: gold-lt)[·]#h(0.9em)Stufflebeam
      ]
    )
  ]
)

// ================= BACK (left panel) =================
#place(top + left, dx: back-x + safe, dy: bleed + safe,
  box(width: trim-w - 2*safe, height: trim-h - 2*safe)[
    #set par(justify: false, leading: 0.72em)
    #v(0.35in)
    #text(size: 12.5pt, fill: cream)[
      As artificial intelligence collapses the cost of execution, the hard part of creation is no longer writing the code — it is knowing what to build, saying it clearly, and judging whether the result is good.

      *Beyond the Prompt* argues this shift was mapped long ago. Read alongside the daily work of building with AI, the scriptural accounts of creation, covenant, stewardship, and rest reveal one pattern underneath both: a blueprint before the build, a watcher over the work, a council of many minds aligned to a single intent.

      Part field guide and part gospel study, it moves from ten hard-won practices for working with AI to the doctrine beneath them — and makes a quiet claim along the way: the laws that make a machine reliable are the laws that make a soul whole.
    ]
    #v(1fr)
    #text(size: 10.5pt, style: "italic", fill: gold-lt)[
      Michael Stufflebeam is an engineer of eighteen years. This book was written the way it describes: a human and an AI, working under covenant.
    ]
    #v(0.18in)
    // KDP prints the barcode at the back cover's bottom-RIGHT as the reader holds it
    // (free-edge side) = the OUTER/LEFT edge of the back panel on the flat wrap.
    #align(left, box(width: 2in, height: 1.2in, fill: white)[
      #set align(center + horizon)
      #text(size: 7pt, fill: rgb("#999999"))[barcode area (KDP)]
    ])
  ]
)
