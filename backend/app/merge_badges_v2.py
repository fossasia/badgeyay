#!usr/bin/python3
import os
import argparse
import subprocess
from .generate_badges import GenerateBadges
from PyPDF2 import PdfFileMerger
from .exceptions import PackageNotFoundError

parser = argparse.ArgumentParser(description='Argument Parser for merge_badges')
parser.add_argument('-p', dest='pdf', action='store_true')
parser.set_defaults(pdf=False, zip=False)
arguments = parser.parse_args()
_pdf = arguments.pdf

if subprocess.run('which rsvg-convert') != 0:
    raise PackageNotFoundError("Package rsvg-convert not found")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
BADGES_FOLDER = os.path.join(APP_ROOT, 'static/badges')

badge_generator = GenerateBadges()
badge_generator.run_generator()

input_folders = [file for file in os.listdir(BADGES_FOLDER) if file.lower().endswith(".badges")]


def generate_pdfs(folder_path):
    """
    Generate PDF at the passed folder path
    :param `folder_path` - Folder path
    """
    svgs = [file for file in os.listdir(folder_path) if file.lower().endswith('.svg')]
    for svg in svgs:
        svg_path = os.path.join(folder_path, svg)
        pdf_path = os.path.splitext(svg_path)[0] + '.pdf'
        print('svg: {}'.format(svg_path))
        print('pdf: {}'.format(pdf_path))
        subprocess.run('rsvg-convert -f pdf -o {} {}'.format(pdf_path, svg_path))


# Generating PDF files from svg.
if _pdf:
    for folder in input_folders:
        folder_path = os.path.join(BADGES_FOLDER, folder)
        generate_pdfs(folder_path)

# Merge badges of different types
input_folders = [file for file in os.listdir(BADGES_FOLDER) if file.lower().endswith(".badges")]

print('Merging badges of different types.')

for folder in input_folders:
    folder_path = os.path.join(BADGES_FOLDER, folder)
    merger = PdfFileMerger()
    pdfs = [file for file in os.listdir(folder_path) if file.lower().endswith('.pdf')]
    for pdf in pdfs:
        merger.append(open(os.path.join(folder_path, pdf), 'rb'))
    out = folder + '.pdf'
    out_path = os.path.join(BADGES_FOLDER, out)
    with open(out_path, 'wb') as fout:
        merger.write(fout)

final_path = os.path.join(BADGES_FOLDER, 'all-badges.pdf')
pdfs = [file for file in os.listdir(BADGES_FOLDER) if file.lower().endswith('.pdf')]
merger = PdfFileMerger()
for pdf in pdfs:
    merger.append(open(os.path.join(BADGES_FOLDER, pdf), 'rb'))

with open(final_path, 'wb') as fout:
    merger.write(fout)
