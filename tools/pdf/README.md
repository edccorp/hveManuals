# Manual PDF build

Builds one PDF per manual from the markdown in `docs/manuals/`, for shipping
with the application and for offline distribution.

## Running it

    pip install -r tools/pdf/requirements.txt
    tools/pdf/build.sh build/pdf

Run from the repository root. Chromium is used to render the PDFs; set the
`CHROME` path at the top of `print_pdf.py` if yours is somewhere else.

## Output

Sixteen PDFs, about 1900 pages and 65 MB in total. Thirteen of them are named
for the files the application's **Help > User Manuals** menu opens from the
`Manuals` folder:

| File | Opened by |
| --- | --- |
| `HVE-Users.pdf` | Help > User Manuals > HVE |
| `EDCRASH.pdf`, `EDGEN.pdf`, `EDHIS.pdf`, `EDSMAC.pdf`, `EDSMAC4.pdf`, `EDSVS.pdf`, `EDVSM.pdf`, `EDVTS.pdf`, `GATB.pdf`, `SIMON.pdf` | the matching menu entry |
| `DamageStudioV8.pdf` | Help > User Manuals > Damage Studio |
| `ReadDataFile.pdf` | Help > User Manuals > ReadDataFile |

Three have no menu entry:

- `EDVDS.pdf` — the menu item exists but its handler is empty, so nothing opens.
- `DyMESH.pdf` — no menu item.
- `HVE-Dialog-Reference.pdf` — the per-dialog reference, which is the same
  material the compiled help file covers.

## How it works

1. `mkimgcache.py` writes a print-resolution copy of every figure (capped at
   1400 px wide, JPEG). The repository keeps the lossless PNGs; only the PDF
   build uses the cache. This is what takes the output from 177 MB to 65 MB.
2. `build_html.py` concatenates each manual's chapters, in the order given by
   the `nav` in `mkdocs.yml`, into a single print-styled HTML document with a
   title page and a linked table of contents. Web-only navigation footers are
   dropped, links between chapters of the same manual become internal
   anchors, and links to other manuals become plain text.
3. `print_pdf.py` drives Chromium over the DevTools protocol to render each
   document, adding the running header and the "Page N of M" footer. The
   command-line `--print-to-pdf` flag cannot customise those, which is why the
   protocol is used instead.

## Math

Equations are converted to MathML by `latex2mathml` and rendered by Chromium's
native MathML support, so the build needs no network access and no MathJax.

`latex2mathml` does not implement the `aligned` environment, so `build_html.py`
splits those blocks into one display equation per row before conversion —
otherwise every row of a multi-line equation collapses onto a single line.
`cases`, `bmatrix` and `Bmatrix` convert correctly and are left alone.
