#!/bin/sh
# Build one PDF per manual from docs/manuals/.
#
# Requires a Chromium build and the packages in requirements.txt. Set CHROME to
# the browser binary if it is not at the default path used by print_pdf.py.
#
# Usage:  tools/pdf/build.sh [output-dir]      (run from the repository root)
set -e
OUT=${1:-build/pdf}
WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT

echo "1/3  compressing figures for print"
python3 tools/pdf/mkimgcache.py "$WORK/img"

echo "2/3  building one HTML document per manual"
PDF_IMG_CACHE="$WORK/img" PYTHONPATH=tools/pdf python3 tools/pdf/build_html.py "$WORK/html"

echo "3/3  rendering to PDF"
mkdir -p "$OUT"
PYTHONPATH=tools/pdf python3 tools/pdf/print_pdf.py "$WORK/html" "$OUT"
