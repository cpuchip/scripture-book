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
    text = re.sub(r'#(?!(link|margin-qr|align|text|v|pagebreak|set|hr|blockquote|binding-question|anchor-passage|import|show|let)\b)', r'\#', text)
    
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
        return f'#link("{resolved_url}")[{conv_text}]'
        
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
    typst_content.append(f'#import "template.typ": project, binding-question, anchor-passage, blockquote, hr, margin-qr')
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
            # Replace author
            md_content = md_content.replace('<div style="text-align: center; margin-top: 3in; font-size: 14pt;">\nMichael Stufflebeam\n</div>',
                                            '#v(2.5in)\n#align(center)[#text(size: 14pt)[Michael Stufflebeam]]\n')
            # Replace Consecration page and Colophon page blocks
            md_content = re.sub(r'<div style="page-break-before:\s*always;\s*margin-top:\s*1in;[^>]*?>\s*(.*?)\s*</div>',
                                r'#pagebreak()\n#v(1in)\n#set text(size: 10pt)\n\1', md_content, flags=re.DOTALL)
            # Replace headings inside frontmatter so they aren't processed as plain paragraphs
            md_content = md_content.replace('## Consecration', '== Consecration')
            md_content = md_content.replace('## Colophon', '== Colophon')
            
        ch_typst = markdown_to_typst(md_content, dist_dir)
        typst_content.append(ch_typst)
        typst_content.append("\n")
        
    with open(typ_out, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(typst_content))
        
    print(f"Generated Typst document: {typ_out}")

if __name__ == "__main__":
    build()
