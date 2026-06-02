// Typst Template for "Beyond the Prompt" Book Typesetting

#let body-font = ("EB Garamond", "Garamond", "Georgia", "Libertinus Serif")
#let heading-font = ("Georgia", "Libertinus Serif")

// Per-chapter kicker shown above a chapter title (e.g. "PRACTICE 1" / "CODA").
// Set just before a Part One heading and cleared after, so the chapter title
// itself (the heading body) stays a clean single line for the running header.
#let practice-kicker = state("practice-kicker", none)

#let project(title: "", author: "", body) = {
  // Page Configuration (6x9 inch trade paperback)
  set page(
    width: 6in,
    height: 9in,
    margin: (
      inside: 0.8in,
      outside: 1.2in,
      top: 0.8in,
      bottom: 0.8in,
    ),
    binding: left,
    
    // Alternating Headers
    header: context {
      let page-num = counter(page).get().first()
      // Suppress the running header on chapter-opening pages (any level-1 heading
      // begins here) and on part-divider half-titles (marked with metadata) — as in
      // standard trade typography. The previous query used .before(here()), which
      // never saw the heading that opens the current page (it sits below the header),
      // so chapter openers were wrongly getting a running head.
      let h1-here = query(heading.where(level: 1)).filter(h => h.location().page() == page-num)
      let div-here = query(metadata).filter(m => m.value == "part-divider" and m.location().page() == page-num)
      let suppress = h1-here.len() > 0 or div-here.len() > 0

      if page-num > 1 and not suppress {
        if calc.even(page-num) {
          // Verso: short book title on the outer (left) edge
          align(left, text(size: 8.5pt, font: heading-font, style: "italic", fill: rgb("#555555"), title.split(":").at(0)))
        } else {
          // Recto: active chapter title (last heading at or before this page)
          let prior = query(heading.where(level: 1)).filter(h => h.location().page() <= page-num)
          let active-chapter = if prior.len() > 0 { prior.last().body } else { [] }
          align(right, text(size: 8.5pt, font: heading-font, style: "italic", fill: rgb("#555555"), active-chapter))
        }
        v(-0.3em)
        line(length: 100%, stroke: 0.5pt + rgb("#dddddd"))
      }
    },
    
    // Alternating Page Numbers in Footer
    footer: context {
      let page-num = counter(page).get().first()
      if page-num > 1 {
        if calc.even(page-num) {
          // Even page: number on left (outside)
          align(left, text(size: 9pt, font: heading-font, str(page-num)))
        } else {
          // Odd page: number on right (outside)
          align(right, text(size: 9pt, font: heading-font, str(page-num)))
        }
      }
    }
  )

  // Typography & Paragraphs
  set text(
    font: body-font,
    size: 11pt,
    fill: rgb("#111111"),
    lang: "en",
  )
  
  set par(
    justify: true,
    leading: 0.65em,
    first-line-indent: 1.5em,
  )
  
  // No indent for paragraphs immediately following headings
  show heading: it => {
    it
    v(0.5em)
  }

  // Heading Styling
  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    v(1.5in)
    align(center, block(width: 100%)[
      #context {
        let k = practice-kicker.at(it.location())
        if k != none {
          text(size: 13pt, weight: "regular", font: heading-font, tracking: 3pt, fill: rgb("#999999"))[#upper(k)]
          linebreak()
          v(0.18in, weak: true)
        }
      }
      #text(size: 22pt, weight: "regular", font: heading-font, it.body)
    ])
    v(1.5in)
  }

  show heading.where(level: 2): it => {
    v(1.5em)
    text(size: 13pt, weight: "regular", font: heading-font, it.body)
    v(0.8em)
  }

  show heading.where(level: 3): it => {
    v(1.2em)
    text(size: 11pt, weight: "bold", font: heading-font, it.body)
    v(0.6em)
  }

  // Blockquote Styling helper
  // We will define it as a global let binding below, but here we can define show rules if any.


  // Horizontal Rule (divider) helper
  // We will define it as a global let binding below.


  body
}

// Custom margin note function to place QR codes in the outside margins dynamically
#let margin-qr(svg-path) = context {
  let page-num = counter(page).get().first()
  let is-even = calc.even(page-num)
  
  // Left page (even) -> outside is left margin (negative dx offset)
  // Right page (odd) -> outside is right margin (positive dx offset)
  let dx-val = if is-even { -1.05in } else { 1.05in }
  let side = if is-even { left } else { right }
  
  place(
    side,
    dx: dx-val,
    dy: -10pt, // subtle vertical align adjustment
    block(
      width: 0.85in,
      align(center)[
        #rect(
          stroke: 0.5pt + rgb("#eeeeee"),
          inset: 2pt,
          fill: white,
          image(svg-path, width: 0.75in)
        )
      ]
    )
  )
}

// Special layout helper for Binding Questions
#let binding-question(body) = {
  set par(first-line-indent: 0pt)
  rect(
    width: 100%,
    stroke: (left: 2.5pt + rgb("#222222")),
    inset: (left: 1.2em, y: 0.8em),
    fill: rgb("#fafafa"),
    text(style: "italic", size: 10.5pt, body)
  )
  v(1em)
}

// Special layout helper for Anchor Passages
#let anchor-passage(body) = {
  block(width: 100%, inset: (bottom: 1em))[
    #set par(first-line-indent: 0pt)
    #body
  ]
}

// Special layout helper for Blockquotes
#let blockquote(body) = {
  set par(first-line-indent: 0pt)
  rect(
    width: 100%,
    stroke: (left: 1.5pt + rgb("#333333")),
    inset: (left: 1em, right: 0.8em, y: 0.7em),
    fill: rgb("#f0f5fa"),
    text(style: "italic", body)
  )
}

// Special layout helper for Horizontal Rules (dividers)
#let hr() = {
  align(center, block(width: 25%, pad(y: 1.5em, line(length: 100%, stroke: 0.5pt + rgb("#dddddd")))))
}

// Production-note sidebar (used in Ch 6 honest footnote)
#let production-note(body) = {
  set par(first-line-indent: 0pt, leading: 0.65em)
  v(1em)
  rect(
    width: 100%,
    stroke: (left: 3pt + rgb("#a89968"), rest: 0.5pt + rgb("#d4cfc0")),
    inset: (x: 1.2em, y: 1em),
    fill: rgb("#f8f6f0"),
    radius: 2pt,
    text(size: 10pt, body)
  )
  v(1em)
}

// Part-divider half-title page (opens "Part One" / "Part Two").
// label = small kicker ("Part One"); title = the big word ("How"); subtitle = the gloss.
// A half-title gets its own page, larger and quieter than a chapter opening,
// so the two-part structure (the "two doors, one house") reads at a glance.
#let part-divider(label, title, subtitle) = {
  pagebreak(weak: true)
  metadata("part-divider")  // page marker so the running header is suppressed here
  v(2.4in)
  align(center)[
    #text(size: 12pt, font: heading-font, tracking: 4pt, fill: rgb("#999999"))[#upper(label)]
    #v(0.55in)
    #text(size: 44pt, weight: "regular", font: heading-font, fill: rgb("#111111"))[#title]
    #v(0.32in)
    #line(length: 18%, stroke: 0.5pt + rgb("#cccccc"))
    #v(0.32in)
    #text(size: 13pt, style: "italic", fill: rgb("#555555"))[#subtitle]
  ]
  pagebreak(weak: true)
}

// Table-of-contents helpers (manual TOC — gives full control over the
// Part One / Part Two grouping that the auto-outline can't express, since the
// part dividers are not headings). Page numbers are resolved from labels placed
// on each chapter heading via counter(page).at(<label>).
#let toc-part(title) = {
  v(1.4em)
  text(size: 11pt, weight: "bold", font: heading-font, tracking: 2pt, fill: rgb("#333333"))[#upper(title)]
  v(0.35em)
}

#let toc-line(body, target) = context {
  let pg = counter(page).at(target).first()
  pad(left: 0.3in, top: 0.3em, bottom: 0.3em,
    grid(
      columns: (auto, 1fr, auto),
      align: (left + bottom, left + bottom, right + bottom),
      box[#body],
      box(width: 100%, inset: (x: 0.4em))[#text(fill: rgb("#cccccc"))[#repeat[.]]],
      box[#text(size: 10pt)[#pg]],
    )
  )
}

// Eleven-step cycle list step item.
// kind = "eng" (slate-blue) or "scripture" (warm sage/amber).
// eng = true adds an inline ENG tag.
#let cycle-step(num, name, verb, body, kind: "scripture", eng: false) = {
  let bg = if kind == "eng" { rgb("#eef2f6") } else { rgb("#f4f0e6") }
  let accent = if kind == "eng" { rgb("#4a6480") } else { rgb("#998b5e") }

  block(
    width: 100%,
    inset: (left: 0.9em, right: 0.7em, y: 0.45em),
    fill: bg,
    stroke: (left: 3pt + accent),
    radius: 2pt,
    above: 0.3em,
    below: 0.3em,
  )[
    #set par(first-line-indent: 0pt, leading: 0.6em)
    #text(weight: "bold", fill: rgb("#555555"))[#str(num).]
    #text(weight: "bold")[#name] —
    #text(style: "italic")[#verb].
    #body
    #if eng [#h(0.3em)#box(
      stroke: 0.7pt + accent,
      inset: (x: 0.4em, y: 0.1em),
      radius: 1.5pt,
      baseline: 0.1em,
    )[#text(size: 7pt, fill: accent, weight: "regular", tracking: 0.5pt)[ENG]]]
  ]
}


