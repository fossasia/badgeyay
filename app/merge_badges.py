#!usr/bin/python3
import os
import argparse
import subprocess
from exceptions import PackageNotFoundError
from cairosvg import svg2pdf
from PyPDF2 import PdfFileMerger

parser = argparse.ArgumentParser(description='Argument Parser for merge_badges')
parser.add_argument('-p', dest='pdf', action='store_true')
parser.set_defaults(pdf=True)
arguments = parser.parse_args()
_pdf = arguments.pdf

if subprocess.call(['which', 'python3']) != 0:
    raise PackageNotFoundError("Package python3 not found")
if subprocess.call(['which', 'pdftk']) != 0:
    raise PackageNotFoundError("Package pdftk not found")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# Get root folder
BADGES_FOLDER = os.path.join(APP_ROOT, 'static/badges')
# Get badges folder
subprocess.call(['python3', APP_ROOT + '/generate-badges.py'])
# execute the generate-badges.py via subprocess

input_folders = [file for file in os.listdir(BADGES_FOLDER) if file.lower().endswith(".badges")]
# check for .badges files in BADGES_FOLDER

def generate_pdfs(folder_path):
    """
    Function to generate the PDF for the badge
    :param `folder_path` - Path of the folder for saving of the PDF's
    """
    svgs = [file for file in os.listdir(folder_path) if file.lower().endswith('.svg')]
    # check for .svg files in folder_path
    for svg in svgs:
        svg_path = os.path.join(folder_path, svg)
        pdf_path = os.path.splitext(svg_path)[0] + '.pdf'
        print('svg: {}'.format(svg_path))
        print('pdf: {}'.format(pdf_path))
        try:
            svg2pdf(url=svg_path, write_to=pdf_path)
        except Exception as e:
            pass


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
