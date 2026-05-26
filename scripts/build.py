#!/usr/bin/env python3
"""
Self-contained build script to compile "Beyond the Prompt" Markdown files
into a print-ready HTML file (for PDF conversion) and an EPUB book.
No external dependencies.
"""

import os
import re
import uuid
import zipfile

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

# Convert local gospel-library relative links to absolute online LDS.org links
def convert_gospel_links(html_content):
    def replace_link(match):
        text = match.group(1)
        path = match.group(2)
        if "gospel-library" in path:
            # Extract subpath after gospel-library/eng/
            sub_match = re.search(r'gospel-library/eng/(.*?)(?:\.md)?(?:#|$)', path)
            if sub_match:
                subpath = sub_match.group(1)
                base_url = f"https://www.churchofjesuschrist.org/study/{subpath}"
                
                # Check for verse anchor in link text (e.g. "Moses 6:59-60" or "D&C 93:36")
                verse_match = re.search(r':(\d+)(?:[-–](\d+))?', text)
                if verse_match:
                    start_v = verse_match.group(1)
                    end_v = verse_match.group(2)
                    if end_v:
                        return f'<a href="{base_url}?lang=eng&amp;id=p{start_v}-p{end_v}#p{start_v}">{text}</a>'
                    else:
                        return f'<a href="{base_url}?lang=eng&amp;id=p{start_v}#p{start_v}">{text}</a>'
                return f'<a href="{base_url}?lang=eng">{text}</a>'
        return match.group(0)

    # Match markdown link: [text](path)
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, html_content)

# Simple Markdown to XHTML parser
def markdown_to_html(md_text, is_epub=False):
    # Escape HTML special chars (excluding block elements we wrap)
    md_text = md_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    
    # Temporarily restore specific HTML blocks we put in templates
    md_text = md_text.replace('&lt;blockquote&gt;', '<blockquote>').replace('&lt;/blockquote&gt;', '</blockquote>')
    md_text = md_text.replace('&lt;div class="binding-question"&gt;', '<div class="binding-question">').replace('&lt;/div&gt;', '</div>')
    md_text = md_text.replace('&lt;div class="anchor-passage"&gt;', '<div class="anchor-passage">')
    # Restore general div and br tags with attributes
    md_text = re.sub(r'&lt;div(.*?)&gt;', r'<div\1>', md_text)
    md_text = md_text.replace('&lt;/div&gt;', '</div>')
    md_text = md_text.replace('&lt;br&gt;', '<br />').replace('&lt;br/&gt;', '<br />').replace('&lt;br /&gt;', '<br />')
    
    # Process code blocks
    code_blocks = []
    def code_repl(match):
        code_blocks.append(match.group(1))
        return f"<!--CODEBLOCK_{len(code_blocks)-1}-->"
    md_text = re.sub(r'```(?:[a-zA-Z0-9_-]+)?\n(.*?)\n```', code_repl, md_text, flags=re.DOTALL)

    # Headers
    md_text = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', md_text, flags=re.MULTILINE)
    
    # Blockquotes (gospel style)
    md_text = re.sub(r'^&gt;\s?(.*?)$', r'<blockquote><p>\1</p></blockquote>', md_text, flags=re.MULTILINE)
    # Merge consecutive blockquotes
    md_text = md_text.replace('</blockquote>\n<blockquote>', '\n')
    
    # Horizontal rule
    md_text = re.sub(r'^---$', r'<hr />', md_text, flags=re.MULTILINE)

    # Lists
    # Unordered Lists
    md_text = re.sub(r'^\- (.*?)$', r'<li>\1</li>', md_text, flags=re.MULTILINE)
    def wrap_ul(match):
        return '<ul>\n' + match.group(0) + '\n</ul>'
    md_text = re.sub(r'(?:<li>.*?</li>\n?)+', wrap_ul, md_text)
    
    # Bold and Italics
    md_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', md_text)
    md_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', md_text)
    
    # Normalize block-level tag boundaries with double newlines so they split into separate blocks
    for tag in ['h1', 'h2', 'h3', 'blockquote', 'div', 'ul', 'ol', 'pre', 'hr']:
        md_text = md_text.replace(f'<{tag}', f'\n\n<{tag}')
        md_text = md_text.replace(f'</{tag}>', f'</{tag}>\n\n')
        
    # Paragraphs (lines separated by double newlines, not starting with tags)
    blocks = md_text.split('\n\n')
    for i, block in enumerate(blocks):
        block_stripped = block.strip()
        if not block_stripped:
            continue
        # If it doesn't start with a structural tag, wrap in <p>
        if not re.match(r'^</?(?:h1|h2|h3|ul|ol|li|blockquote|div|hr|pre|code|!--)', block_stripped):
            # If we're inside a div or blockquote, be careful
            blocks[i] = f'<p>{block_stripped}</p>'
            
    md_text = '\n\n'.join(blocks)
    
    # Restore code blocks
    for idx, code in enumerate(code_blocks):
        esc_code = code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        md_text = md_text.replace(f"<!--CODEBLOCK_{idx}-->", f"<pre><code>{esc_code}</code></pre>")
        
    # Convert local/relative markdown links to online LDS.org links
    md_text = convert_gospel_links(md_text)
    
    return md_text

def build():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    print(f"Building book from config in {project_root}")
    config = parse_yaml(os.path.join(project_root, "book.yaml"))
    
    dist_dir = os.path.join(project_root, "dist")
    os.makedirs(dist_dir, exist_ok=True)
    
    title = config.get("title", "Beyond the Prompt")
    author = config.get("author", "Michael Stuffleberry")
    language = config.get("language", "en-US")
    chapters_list = config.get("chapters", [])
    
    # Process Chapters
    parsed_chapters = []
    for chapter_path in chapters_list:
        full_path = os.path.join(project_root, chapter_path)
        if not os.path.exists(full_path):
            print(f"Warning: Chapter file not found: {chapter_path}")
            continue
            
        with open(full_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        # Parse chapter Title from first H1
        title_match = re.search(r'^# (.*?)$', md_content, re.MULTILINE)
        ch_title = title_match.group(1) if title_match else os.path.basename(chapter_path)
        
        html_body = markdown_to_html(md_content)
        parsed_chapters.append({
            "title": ch_title,
            "filename": os.path.basename(chapter_path).replace('.md', '.xhtml'),
            "body": html_body
        })
    
    # 1. Output Print-Ready combined HTML
    html_out = os.path.join(dist_dir, "manuscript.html")
    with open(os.path.join(project_root, "src", "style.css"), 'r', encoding='utf-8') as f:
        css_style = f.read()
        
    combined_body = ""
    for ch in parsed_chapters:
        combined_body += f"<div class=\"chapter\">\n{ch['body']}\n</div>\n"
        
    html_manuscript = f"""<!DOCTYPE html>
<html lang="{language}">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
    {css_style}
    </style>
</head>
<body>
    {combined_body}
</body>
</html>
"""
    with open(html_out, 'w', encoding='utf-8') as f:
        f.write(html_manuscript)
    print(f"Compiled print-ready manuscript: {html_out}")
    
    # 2. Output EPUB
    epub_out = os.path.join(dist_dir, "beyond_the_prompt.epub")
    book_uuid = str(uuid.uuid4())
    
    # Create temp files for zip packaging
    temp_dir = os.path.join(dist_dir, "epub_temp")
    os.makedirs(temp_dir, exist_ok=True)
    os.makedirs(os.path.join(temp_dir, "META-INF"), exist_ok=True)
    os.makedirs(os.path.join(temp_dir, "OEBPS"), exist_ok=True)
    
    # Write mimetype
    with open(os.path.join(temp_dir, "mimetype"), 'w', encoding='utf-8') as f:
        f.write("application/epub+zip")
        
    # Write container.xml
    container_xml = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>"""
    with open(os.path.join(temp_dir, "META-INF", "container.xml"), 'w', encoding='utf-8') as f:
        f.write(container_xml)
        
    # Write OEBPS/style.css (simplified for digital)
    epub_css = """body { font-family: Georgia, serif; line-height: 1.6; margin: 5%; }
h1 { text-align: center; margin-top: 10%; margin-bottom: 5%; }
h2, h3 { margin-top: 5%; margin-bottom: 2%; }
p { text-indent: 1.5em; margin: 0; }
h1+p, h2+p, h3+p, blockquote+p { text-indent: 0; }
blockquote { margin: 5% 10%; font-style: italic; }
.binding-question { border-left: 3px solid #333; padding-left: 5%; margin-bottom: 5%; font-style: italic; }
"""
    with open(os.path.join(temp_dir, "OEBPS", "style.css"), 'w', encoding='utf-8') as f:
        f.write(epub_css)
        
    # Write chapter XHTML files
    manifest_items = ""
    spine_items = ""
    nav_points = ""
    
    for idx, ch in enumerate(parsed_chapters):
        ch_filename = ch['filename']
        ch_title = ch['title']
        
        ch_xhtml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="{language}">
<head>
    <title>{ch_title}</title>
    <link rel="stylesheet" href="style.css" type="text/css" />
</head>
<body>
    {ch['body']}
</body>
</html>
"""
        # Ensure self-closing tags in strict XHTML
        ch_xhtml = ch_xhtml.replace('<hr>', '<hr />').replace('<br>', '<br />')
        
        with open(os.path.join(temp_dir, "OEBPS", ch_filename), 'w', encoding='utf-8') as f:
            f.write(ch_xhtml)
            
        manifest_items += f'    <item id="ch_{idx}" href="{ch_filename}" media-type="application/xhtml+xml"/>\n'
        spine_items += f'    <itemref idref="ch_{idx}"/>\n'
        nav_points += f"""    <navPoint id="ch_{idx}" playOrder="{idx+1}">
      <navLabel><text>{ch_title}</text></navLabel>
      <content src="{ch_filename}"/>
    </navPoint>\n"""

    # Write content.opf
    content_opf = f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookID" version="2.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
    <dc:title>{title}</dc:title>
    <dc:creator opf:role="aut">{author}</dc:creator>
    <dc:language>{language}</dc:language>
    <dc:identifier id="BookID">urn:uuid:{book_uuid}</dc:identifier>
  </metadata>
  <manifest>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
    <item id="style" href="style.css" media-type="text/css"/>
{manifest_items}  </manifest>
  <spine toc="ncx">
{spine_items}  </spine>
</package>"""
    with open(os.path.join(temp_dir, "OEBPS", "content.opf"), 'w', encoding='utf-8') as f:
        f.write(content_opf)
        
    # Write toc.ncx
    toc_ncx = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE ncx PUBLIC "-//NISO//DTD NCX V1.0//EN" "http://www.daisy.org/z3986/2005/ncx-1.0.dtd">
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx-1.0.dtd" version="2005-1">
  <head>
    <meta name="dtb:uid" content="urn:uuid:{book_uuid}"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle>
    <text>{title}</text>
  </docTitle>
  <navMap>
{nav_points}  </navMap>
</ncx>"""
    with open(os.path.join(temp_dir, "OEBPS", "toc.ncx"), 'w', encoding='utf-8') as f:
        f.write(toc_ncx)
        
    # Package to ZIP (EPUB format)
    with zipfile.ZipFile(epub_out, 'w') as z:
        # Write mimetype first without compression
        z.write(os.path.join(temp_dir, "mimetype"), "mimetype", compress_type=zipfile.ZIP_STORED)
        
        # Write META-INF
        z.write(os.path.join(temp_dir, "META-INF", "container.xml"), "META-INF/container.xml", compress_type=zipfile.ZIP_DEFLATED)
        
        # Write OEBPS
        z.write(os.path.join(temp_dir, "OEBPS", "style.css"), "OEBPS/style.css", compress_type=zipfile.ZIP_DEFLATED)
        z.write(os.path.join(temp_dir, "OEBPS", "content.opf"), "OEBPS/content.opf", compress_type=zipfile.ZIP_DEFLATED)
        z.write(os.path.join(temp_dir, "OEBPS", "toc.ncx"), "OEBPS/toc.ncx", compress_type=zipfile.ZIP_DEFLATED)
        
        for ch in parsed_chapters:
            filename = ch['filename']
            z.write(os.path.join(temp_dir, "OEBPS", filename), f"OEBPS/{filename}", compress_type=zipfile.ZIP_DEFLATED)
            
    # Clean up temp files
    for root, dirs, files in os.walk(temp_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(temp_dir)
    
    print(f"Generated EPUB book: {epub_out}")

if __name__ == "__main__":
    build()
