"""Build a print-resolution image cache: cap width at 1400px, save as JPEG.

The repository keeps the lossless PNGs; only the PDF build uses this cache.
"""
import glob, os, sys
from PIL import Image

SRC = os.path.abspath('docs/manuals')
DST = sys.argv[1]
MAXW = 1400
QUAL = 84

n = insize = outsize = 0
for f in glob.glob(os.path.join(SRC, '**', '*.png'), recursive=True):
    rel = os.path.relpath(f, SRC)
    out = os.path.join(DST, os.path.splitext(rel)[0] + '.jpg')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    insize += os.path.getsize(f)
    im = Image.open(f)
    if im.mode in ('RGBA', 'LA', 'P'):
        bg = Image.new('RGB', im.size, 'white')
        im = im.convert('RGBA')
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert('RGB')
    if im.width > MAXW:
        im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
    im.save(out, 'JPEG', quality=QUAL, optimize=True, progressive=True)
    outsize += os.path.getsize(out)
    n += 1
print(f'{n} images  {insize/1e6:.0f} MB -> {outsize/1e6:.0f} MB')
