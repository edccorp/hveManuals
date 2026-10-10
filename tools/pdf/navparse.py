"""Group the mkdocs nav into one entry per printed manual."""
import re

def nav_files(path='mkdocs.yml'):
    lines = open(path, encoding='utf-8').read().split('\n')
    s = next(i for i, l in enumerate(lines) if l.startswith('nav:'))
    out = []
    for l in lines[s+1:]:
        if l.strip() == '':
            continue
        if l[0] not in ' \t':
            break
        st = l.strip()
        if not st.startswith('- '):
            continue
        body = st[2:].strip()
        # The path is the last whitespace-delimited token ending in .md,
        # so titles containing colons are handled correctly.
        m = re.search(r'([^\s:]+\.md)\s*$', body)
        if m:
            out.append(m.group(1))
    return out

PROGRAM_TITLES = {
    'EDCRASH': 'EDCRASH', 'EDGEN': 'EDGEN', 'EDHIS': 'EDHIS',
    'EDSMAC': 'EDSMAC', 'EDSMAC4': 'EDSMAC4', 'EDSVS': 'EDSVS',
    'EDVDS': 'EDVDS', 'EDVSM': 'EDVSM', 'EDVTS': 'EDVTS',
    'SIMON': 'SIMON', 'DyMESH': 'DyMESH', 'GATB': 'GATB',
    'RDF': 'RDF (ReadDataFile)', 'DamageStudio': 'Damage Studio',
}

def manuals(path='mkdocs.yml'):
    files = nav_files(path)
    buckets, order = {}, []
    def put(key, f):
        if key not in buckets:
            buckets[key] = []
            order.append(key)
        buckets[key].append(f)
    for f in files:
        if f in ('README.md', 'downloads.md'):
            continue
        if f.startswith('hve-users/'):
            put("HVE User's Manual", f)
        elif f.startswith('programs/'):
            parts = f.split('/')
            if len(parts) < 3:
                continue           # programs/README.md
            put(PROGRAM_TITLES.get(parts[1], parts[1]), f)
        else:
            put('HVE Dialog Reference', f)
    return [(k, buckets[k]) for k in order]

SLUG = {"HVE User's Manual": 'HVE-Users-Manual',
        'HVE Dialog Reference': 'HVE-Dialog-Reference',
        'RDF (ReadDataFile)': 'RDF',
        'Damage Studio': 'DamageStudio'}

def slug(title):
    return SLUG.get(title, title)

if __name__ == '__main__':
    tot = 0
    for n, fs in manuals():
        tot += len(fs)
        print(f"{n:<24} {len(fs):>4} files -> {slug(n)}.pdf")
    print(f"{'TOTAL':<24} {tot:>4} files")
