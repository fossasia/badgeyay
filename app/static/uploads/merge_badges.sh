#!/bin/bash
set -e

cd "`dirname \"$0\"`"

# https://superuser.com/a/381128
if [ -z "`which rsvg-convert`" ]; then
  sudo apt-get -y install librsvg2-bin
fi
if [ -z "`which python3`" ]; then
  sudo apt-get -y install python3
fi
if [ -z "`which pdftk`" ]; then
  sudo apt-get -y install pdftk
fi

python3 generate-badges.py

echo "Generating PDF files from svg."

for svg in `find | grep -E '\.svg$'`; do
  pdf="${svg%.svg}.pdf"
  echo "svg: $svg"
  echo "pdf: $pdf"
  rsvg-convert -f pdf -o "$pdf" "$svg"
done

echo "Merging badges of different types."

all=""
for folder in *.badges; do
  out="${folder}.pdf"
  echo "merging $folder to $out"
  pdftk "$folder"/*.pdf cat output "$out"
  all="$out $all"
done

final="all-badges.pdf"
pdftk $all cat output "$final"
echo "Created $final"

echo "Generating ZIP file"
find . \( -iname \*.svg -o -iname \*.pdf \) | zip  -@ all-badges.zip

echo "Generating ZIP of SVG files"
for folder in $(ls -d */); do
    filename="${folder%%/}.svg.zip"
    find ./${folder%%/} -type f -name "*.svg" | zip  -@ $filename
done
