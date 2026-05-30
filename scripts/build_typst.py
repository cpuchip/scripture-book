#!/usr/bin/env python3
"""
Build script to compile "Beyond the Prompt" Markdown files
into a Typst document (for PDF generation).
"""

import os
import re
import uuid
import hashlib
import sys
import shutil

# Helper to parse YAML-like book.yaml config
def parse_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    data = {}
    current_key = None
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith('- '):
            val = line[2:].strip().strip('"').strip("'")
            if current_key and isinstance(data[current_key], list):
                data[current_key].append(val)
        elif ':' in line:
            parts = line.split(':', 1)
            key = parts[0].strip()
            val = parts[1].strip().strip('"').strip("'")
            if not val:
                data[key] = []
                current_key = key
            else:
                if val.replace('.', '', 1).isdigit():
                    val = float(val) if '.' in val else int(val)
                data[key] = val
                current_key = None
    return data

def resolve_gospel_path(path):
    if "gospel-library" not in path:
        return path
    
    # Extract subpath after gospel-library/eng/
    sub_match = re.search(r'gospel-library/eng/([^?#]*?)(?:\.md)?(?:[?#]|$)', path)
    if not sub_match:
        return path
    subpath = sub_match.group(1)
    base_url = f"https://www.churchofjesuschrist.org/study/{subpath}"
    
    # Extract verse number from query parameter (?verse=18 or ?verse=17-18)
    # or from hash anchor (#p18 or #18)
    verse_match = re.search(r'(?:\?verse=|#p?)(\d+)(?:[-–](\d+))?', path)
    if verse_match:
        start_v = verse_match.group(1)
        end_v = verse_match.group(2)
        if end_v:
            return f"{base_url}?lang=eng&id=p{start_v}-p{end_v}#p{start_v}"
        else:
            return f"{base_url}?lang=eng&id=p{start_v}#p{start_v}"
            
    return f"{base_url}?lang=eng"

def generate_local_qr(url, dist_dir):
    # Ensure qrcode is installed
    try:
        import qrcode
        import qrcode.image.svg
    except ImportError:
        print("Installing required 'qrcode' library for local QR code generation...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "qrcode"])
        import qrcode
        import qrcode.image.svg

    qr_dir = os.path.join(dist_dir, "images", "qr")
    os.makedirs(qr_dir, exist_ok=True)
    
    # Generate a unique stable filename for this URL
    url_hash = hashlib.md5(url.encode('utf-8')).hexdigest()[:8]
    filename = f"qr_{url_hash}.svg"
    filepath = os.path.join(qr_dir, filename)
    
    # Generate SVG QR code if it doesn't exist
    if not os.path.exists(filepath):
        factory = qrcode.image.svg.SvgImage
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            image_factory=factory
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image()
        with open(filepath, 'wb') as f:
            img.save(f)
        print(f"Generated QR code: {filename} -> {url}")
        
    return f"images/qr/{filename}"

def convert_inline_markdown(text, dist_dir):
    # Escape at symbols (@) so they aren't parsed as Typst bibliography references
    text = text.replace('@', '\\@')
    
    # Escape any hash symbols in text so they don't break Typst syntax
    # (except when they represent headings or functions we emit)
    # We do a safe replacement of raw '#' that aren't heading indicators, code, or known Typst functions we emit
    text = re.sub(r'#(?!(link|margin-qr|align|text|v|pagebreak|set|hr|blockquote|binding-question|anchor-passage|production-note|cycle-step|import|show|let)\b)', r'\#', text)
    
    # Resolve and replace QR codes: [qr](url)
    def replace_qr(match):
        url = match.group(1)
        resolved_url = resolve_gospel_path(url)
        qr_path = generate_local_qr(resolved_url, dist_dir)
        return f' #margin-qr("{qr_path}") '
        
    text = re.sub(r'\[qr\]\(([^)]+)\)', replace_qr, text)

    # Convert standard links: [text](url) -> #link("url")[text]
    def replace_link(match):
        link_text = match.group(1)
        path = match.group(2)
        resolved_url = resolve_gospel_path(path)
        # Apply nested formatting inside the link text if needed
        conv_text = convert_inline_formatting(link_text)
        link_typst = f'#link("{resolved_url}")[{conv_text}]'
        # Prevent line-breaking inside email links so the address does not split
        # across lines (mailto links are otherwise broken by justified text)
        if resolved_url.startswith('mailto:'):
            link_typst = f'#box[{link_typst}]'
        return link_typst
        
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, text)

    # Apply bold/italic
    text = convert_inline_formatting(text)
    
    return text

def convert_inline_formatting(text):
    # Use temporary token for bold to avoid collision with italic replacement
    text = re.sub(r'\*\*(.*?)\*\*', r'__BOLD_TEMP__\1__BOLD_TEMP__', text)
    # Convert italic *text* -> _text_
    text = re.sub(r'\*(.*?)\*', r'_\1_', text)
    # Convert temporary bold token -> *text*
    text = text.replace('__BOLD_TEMP__', '*')
    return text

def preprocess_html_blocks(md_content):
    """Convert specific HTML markup patterns in the markdown source to Typst function calls.
    Handles:
      - <div class="production-note">...</div> -> #production-note[...]
      - <ol class="cycle-list">...<li class="eng-step|scripture-step">...</li>...</ol>
        -> series of #cycle-step(num, "name", "verb", "body", kind: "eng|scripture", eng: true|false)
    """
    # Production-note sidebar
    def replace_production_note(match):
        inner = match.group(1).strip()
        # Convert the ### heading inside to inline styled text (avoids breaking the chapter TOC)
        # Use rgb(r, g, b) integer components so the convert_inline_markdown # escape doesn't touch
        # the color value (rgb("#hex") would be mangled). #5a4d2a = (90, 77, 42).
        inner = re.sub(
            r'^###\s+(.+?)\s*$',
            r'#text(style: "italic", weight: "bold", fill: rgb(90, 77, 42), size: 11pt)[\1]\n',
            inner, count=1, flags=re.MULTILINE
        )
        return f'#production-note[\n{inner}\n]'

    md_content = re.sub(
        r'<div class="production-note">\s*\n(.*?)\n\s*</div>',
        replace_production_note,
        md_content,
        flags=re.DOTALL
    )

    # Eleven-step cycle list <ol class="cycle-list">
    def replace_cycle_list(match):
        inner = match.group(1)
        results = []
        item_num = 1
        # Each <li> spans one line with predictable structure
        # Match each <li> with flexible body capture. Some items have the period right
        # after the verb's closing span ("binding. A mutual agreement…"); others have
        # body content first and the period later ("naming the why."). Capture whatever
        # text follows the verb up to the optional eng-tag or the closing </li>, then
        # clean the body (strip leading period + whitespace, ensure trailing period).
        li_pattern = re.compile(
            r'<li class="(eng-step|scripture-step)">'
            r'<span class="cycle-step-name">([^<]+)</span>\s*[—-]\s*'
            r'<span class="cycle-step-verb">([^<]+)</span>'
            r'(.*?)'
            r'(?:\s*<span class="eng-tag">eng</span>)?\s*'
            r'</li>',
            re.DOTALL
        )
        for li_match in li_pattern.finditer(inner):
            kind_class = li_match.group(1)
            name = li_match.group(2).strip()
            verb = li_match.group(3).strip()
            # Body capture may start with a period (verb-immediately-followed-by-period
            # pattern) or with body text directly. Strip leading period + whitespace,
            # then trailing whitespace, then re-add a trailing period for sentence form.
            body = li_match.group(4).strip()
            body = body.lstrip('.').strip()
            body = body.rstrip('.').strip()
            if body:
                body_text = body + '.'
            else:
                body_text = ''
            is_eng = kind_class == 'eng-step'
            kind = "eng" if is_eng else "scripture"
            eng_flag = "true" if is_eng else "false"
            # Escape any embedded quotes in the body text
            body_escaped = body_text.replace('"', '\\"')
            results.append(
                f'#cycle-step({item_num}, "{name}", "{verb}", "{body_escaped}", '
                f'kind: "{kind}", eng: {eng_flag})'
            )
            item_num += 1
        return '\n\n'.join(results)

    md_content = re.sub(
        r'<ol class="cycle-list">\s*\n(.*?)\n\s*</ol>',
        replace_cycle_list,
        md_content,
        flags=re.DOTALL
    )

    return md_content


def markdown_to_typst(md_content, dist_dir):
    blocks = md_content.split('\n\n')
    typst_blocks = []
    
    in_anchor = False
    in_list = False
    
    for block in blocks:
        block_stripped = block.strip()
        if not block_stripped:
            continue
            
        # Handle Headings
        if block_stripped.startswith('# '):
            if in_anchor:
                typst_blocks.append(']')
                in_anchor = False
            title = block_stripped[2:].strip()
            typst_blocks.append(f'= {convert_inline_markdown(title, dist_dir)}')
            continue
        elif block_stripped.startswith('## '):
            title = block_stripped[3:].strip()
            typst_blocks.append(f'== {convert_inline_markdown(title, dist_dir)}')
            continue
        elif block_stripped.startswith('### '):
            title = block_stripped[4:].strip()
            typst_blocks.append(f'=== {convert_inline_markdown(title, dist_dir)}')
            continue
            
        # Handle horizontal divider
        if block_stripped == '---':
            typst_blocks.append('#hr()')
            continue
            
        # Handle Binding Question
        if block_stripped.startswith('**Binding Question:**'):
            question = block_stripped[len('**Binding Question:**'):].strip()
            typst_blocks.append(f'#binding-question[{convert_inline_markdown(question, dist_dir)}]')
            continue
            
        # Handle Anchor Passage Intro (which might contain the blockquote directly if separated by single newline)
        if block_stripped.startswith('**Anchor Passage:**'):
            in_anchor = True
            typst_blocks.append('#anchor-passage[')
            # Check if the blockquote is in the same block
            parts = block_stripped.split('\n', 1)
            if len(parts) > 1 and parts[1].strip().startswith('>'):
                quote_part = parts[1].strip()
                lines = []
                for line in quote_part.split('\n'):
                    line = line.strip()
                    if line.startswith('>'):
                        lines.append(line[1:].strip())
                    else:
                        lines.append(line)
                quote_content = '\n'.join(lines)
                conv_quote = convert_inline_markdown(quote_content, dist_dir)
                # Move margin-qr to the beginning of the blockquote to align with the first line
                qr_match = re.search(r'#margin-qr\("[^"]+"\)', conv_quote)
                if qr_match:
                    qr_str = qr_match.group(0)
                    conv_quote = conv_quote.replace(qr_str, '').strip()
                    conv_quote = re.sub(r'\s{2,}', ' ', conv_quote)
                    conv_quote = f'{qr_str} {conv_quote}'
                typst_blocks.append(f'  #blockquote[\n    {conv_quote}\n  ]\n]')
                in_anchor = False # closed anchor passage block
            continue
            
        # Handle Blockquotes
        if block_stripped.startswith('>'):
            lines = []
            for line in block_stripped.split('\n'):
                line = line.strip()
                if line.startswith('>'):
                    lines.append(line[1:].strip())
                else:
                    lines.append(line)
            quote_content = '\n'.join(lines)
            conv_quote = convert_inline_markdown(quote_content, dist_dir)
            # Move margin-qr to the beginning of the blockquote to align with the first line
            qr_match = re.search(r'#margin-qr\("[^"]+"\)', conv_quote)
            if qr_match:
                qr_str = qr_match.group(0)
                conv_quote = conv_quote.replace(qr_str, '').strip()
                conv_quote = re.sub(r'\s{2,}', ' ', conv_quote)
                conv_quote = f'{qr_str} {conv_quote}'
            
            if in_anchor:
                typst_blocks.append(f'  #blockquote[\n    {conv_quote}\n  ]\n]')
                in_anchor = False # closed anchor passage block
            else:
                typst_blocks.append(f'#blockquote[\n  {conv_quote}\n]')
            continue
            
        # Handle Code blocks
        if block_stripped.startswith('```'):
            # Pass code blocks straight through since Typst uses same syntax
            typst_blocks.append(block_stripped)
            continue
            
        # Handle standard paragraph or lists (parsed line-by-line to catch lists mixed inside paragraphs)
        lines = block_stripped.split('\n')
        parsed_lines = []
        for line in lines:
            line_stripped = line.strip()
            if not line_stripped:
                continue
            
            # Check if line is a list item
            list_match = re.match(r'^[\-\*\+]\s+(.*)', line_stripped)
            if list_match:
                item_text = list_match.group(1).strip()
                parsed_lines.append(f'- {convert_inline_markdown(item_text, dist_dir)}')
            else:
                parsed_lines.append(convert_inline_markdown(line_stripped, dist_dir))
                
        typst_blocks.append('\n'.join(parsed_lines))
        
    return '\n\n'.join(typst_blocks)

def build():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    print(f"Building Typst book source from config in {project_root}")
    config = parse_yaml(os.path.join(project_root, "book.yaml"))
    
    dist_dir = os.path.join(project_root, "dist")
    os.makedirs(dist_dir, exist_ok=True)
    
    title = config.get("title", "Beyond the Prompt")
    author = config.get("author", "Michael Stufflebeam")
    chapters_list = config.get("chapters", [])
    
    # Create the target Typst source file
    typ_out = os.path.join(dist_dir, "book.typ")
    
    # Copy template.typ to dist so it is local to compilation
    shutil.copy2(
        os.path.join(project_root, "src", "template.typ"),
        os.path.join(dist_dir, "template.typ")
    )
    
    typst_content = []
    # Setup document metadata and template import
    typst_content.append(f'#import "template.typ": project, binding-question, anchor-passage, blockquote, hr, margin-qr, production-note, cycle-step')
    typst_content.append(f'#show: project.with(title: "{title}", author: "{author}")\n')
    
    for chapter_path in chapters_list:
        full_path = os.path.join(project_root, chapter_path)
        if not os.path.exists(full_path):
            print(f"Warning: Chapter file not found: {chapter_path}")
            continue
            
        print(f"Converting chapter: {chapter_path}")
        with open(full_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        if "frontmatter.md" in chapter_path:
            # Replace subtitle
            md_content = md_content.replace('<div class="chapter-meta">\nWhat AI Engineering Reveals About Eternal Patterns\n</div>',
                                            '#align(center)[#text(size: 12pt, style: "italic")[What AI Engineering Reveals About Eternal Patterns]]\n')
            # Replace author. Margin-top is variable (3in originally; 1.5in once the
            # title-page epigraph was added). Use a regex with capture so both work.
            md_content = re.sub(
                r'<div style="text-align: center; margin-top: ([\d.]+in); font-size: 14pt;">\s*\nMichael Stufflebeam\s*\n</div>',
                lambda m: f'#v({m.group(1)})\n#align(center)[#text(size: 14pt)[Michael Stufflebeam]]\n',
                md_content
            )
            # Replace Dedication block (centered italic; opens the consecration page)
            md_content = re.sub(
                r'<div style="page-break-before:\s*always;\s*margin-top:\s*1\.5in;\s*text-align:\s*center;\s*font-style:\s*italic;[^>]*?>\s*(.*?)\s*</div>',
                r'#pagebreak()\n#v(1.5in)\n#align(center)[#text(style: "italic")[\n\1\n]]\n#v(0.4in)',
                md_content, flags=re.DOTALL
            )
            # Replace Consecration block (no page break -- shares the dedication's page)
            md_content = re.sub(
                r'<div style="margin-top:\s*1in;\s*font-size:\s*10pt;[^>]*?>\s*(.*?)\s*</div>',
                r'#set text(size: 10pt)\n\1', md_content, flags=re.DOTALL
            )
            # Replace Colophon page block (its own page)
            md_content = re.sub(r'<div style="page-break-before:\s*always;\s*margin-top:\s*1in;[^>]*?>\s*(.*?)\s*</div>',
                                r'#pagebreak()\n#v(1in)\n#set text(size: 10pt)\n\1', md_content, flags=re.DOTALL)
            # Replace headings inside frontmatter so they aren't processed as plain paragraphs
            md_content = md_content.replace('## Consecration', '== Consecration')
            md_content = md_content.replace('## Colophon', '== Colophon')
            
        # Preprocess any custom HTML patterns (production-note, cycle-list) before markdown conversion
        md_content = preprocess_html_blocks(md_content)

        ch_typst = markdown_to_typst(md_content, dist_dir)
        typst_content.append(ch_typst)
        typst_content.append("\n")
        
    with open(typ_out, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(typst_content))
        
    print(f"Generated Typst document: {typ_out}")

if __name__ == "__main__":
    build()
