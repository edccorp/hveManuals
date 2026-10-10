"""Build one print-ready HTML document per manual from the markdown sources."""
import os, re, sys, html as _html
import markdown
import latex2mathml.converter as L2M
from navparse import manuals, slug

DOCS = os.path.abspath('docs/manuals')
OUT  = sys.argv[1] if len(sys.argv) > 1 else 'html'
# Optional print-resolution image cache (JPEG); falls back to the repo PNGs.
IMGCACHE = os.environ.get('PDF_IMG_CACHE')
os.makedirs(OUT, exist_ok=True)

EXTS = ['admonition', 'pymdownx.details', 'pymdownx.superfences',
        'tables', 'attr_list', 'md_in_html', 'toc']

NAV_RE   = re.compile(r'<!--\s*NAV\s*-->.*?<!--\s*/NAV\s*-->', re.S)
BLOCK_RE = re.compile(r'(?<!\\)\$\$(.+?)(?<!\\)\$\$', re.S)
INLINE_RE= re.compile(r'(?<![\$\\])\$(?!\s)([^\$\n]+?)(?<![\s\\])\$(?!\$)')

ALIGNED_RE = re.compile(r'\\begin\{aligned\}(.*?)\\end\{aligned\}', re.S)

def _one(tex, display):
    try:
        return L2M.convert(tex.strip(), display='block' if display else 'inline')
    except Exception:
        return '<code>' + _html.escape(tex.strip()) + '</code>'

def to_mathml(tex, display):
    """Convert LaTeX to MathML.

    latex2mathml does not implement the `aligned` environment, so its rows would
    otherwise all collapse onto one line. Split such a block into one display
    equation per row, dropping the alignment markers.
    """
    m = ALIGNED_RE.search(tex)
    if m and display:
        rows = [r.strip() for r in re.split(r'\\\\', m.group(1)) if r.strip()]
        if len(rows) > 1:
            out = []
            for r in rows:
                parts = r.split('&')
                if len(parts) > 2:
                    # lhs & = rhs & tag  ->  lhs = rhs, then a wide gap before the tag
                    body = parts[0] + parts[1]
                    gap = '\\qquad '
                    tex = body + gap + gap.join(p.strip() for p in parts[2:])
                else:
                    tex = ''.join(parts)
                out.append('<div class="eqrow">' + _one(tex, True) + '</div>')
            return ''.join(out)
    return _one(tex, display)

def protect_math(md):
    """Replace math with placeholders; return (md, store)."""
    store = []
    def blk(m):
        store.append('<div class="eq">' + to_mathml(m.group(1), True) + '</div>')
        return f'\n\nMATHPLACEHOLDER{len(store)-1}ENDMATH\n\n'
    def inl(m):
        store.append(to_mathml(m.group(1), False))
        return f'MATHPLACEHOLDER{len(store)-1}ENDMATH'
    md = BLOCK_RE.sub(blk, md)
    md = INLINE_RE.sub(inl, md)
    return md, store

def restore_math(htm, store):
    return re.sub(r'MATHPLACEHOLDER(\d+)ENDMATH', lambda m: store[int(m.group(1))], htm)

def anchor_for(relpath):
    return 'ch_' + re.sub(r'[^A-Za-z0-9]+', '_', relpath[:-3]).strip('_')

def build(title, files):
    body, toc = [], []
    fileset = set(files)
    for relpath in files:
        src = os.path.join(DOCS, relpath)
        if not os.path.exists(src):
            print('  MISSING', relpath); continue
        md = open(src, encoding='utf-8').read()
        md = NAV_RE.sub('', md).rstrip()
        md, store = protect_math(md)

        base = os.path.dirname(relpath)
        # images -> absolute file paths
        def fiximg(m):
            p = m.group(2)
            if p.startswith(('http:', 'https:', 'data:', '/')): return m.group(0)
            full = os.path.normpath(os.path.join(DOCS, base, p))
            if IMGCACHE:
                rel = os.path.relpath(full, DOCS)
                jpg = os.path.join(IMGCACHE, os.path.splitext(rel)[0] + '.jpg')
                if os.path.exists(jpg):
                    full = jpg
            return f'{m.group(1)}{full}{m.group(3)}'
        md = re.sub(r'(!\[[^\]]*\]\()([^)]+)(\))', fiximg, md)
        md = re.sub(r'(<img[^>]+src=")([^"]+)(")', fiximg, md)

        # links to .md -> internal anchors when inside this manual, else plain text
        def fixlink(m):
            text, target = m.group(1), m.group(2)
            tgt = target.split('#')[0]
            if not tgt.endswith('.md'):
                return m.group(0)
            norm = os.path.normpath(os.path.join(base, tgt)).replace(os.sep, '/')
            if norm in fileset:
                return f'[{text}](#{anchor_for(norm)})'
            return text
        md = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', fixlink, md)

        conv = markdown.Markdown(extensions=EXTS)
        htm = restore_math(conv.convert(md), store)
        # demote heading levels so the manual title is the only h1
        htm = re.sub(r'<(/?)h([1-5])', lambda m: f'<{m.group(1)}h{int(m.group(2))+1}', htm)
        a = anchor_for(relpath)
        first = re.search(r'<h2[^>]*>(.*?)</h2>', htm, re.S)
        label = re.sub(r'<[^>]+>', '', first.group(1)).strip() if first else relpath
        label = re.sub(r'\s*¶\s*$', '', label)
        toc.append((a, label))
        body.append(f'<section class="chapter" id="{a}">\n{htm}\n</section>')

    toc_html = '\n'.join(f'<li><a href="#{a}">{_html.escape(t)}</a></li>' for a, t in toc)
    doc = TEMPLATE.format(title=_html.escape(title), toc=toc_html, body='\n'.join(body))
    path = os.path.join(OUT, slug(title) + '.html')
    open(path, 'w', encoding='utf-8').write(doc)
    return path, len(toc)

TEMPLATE = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template.html'), encoding='utf-8').read()

if __name__ == '__main__':
    only = sys.argv[2] if len(sys.argv) > 2 else None
    for name, files in manuals():
        if only and slug(name) != only: continue
        p, n = build(name, files)
        print(f'{name:<24} {n:>3} chapters -> {p}')
