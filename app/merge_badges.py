#!usr/bin/python3
import os
import argparse
import zipfile

parser = argparse.ArgumentParser(description='Argument Parser for merge_badges')
parser.add_argument('-p',dest='pdf',action='store_true')
parser.add_argument('-z',dest='zip',action='store_true')
parser.set_defaults(pdf=False,zip=False)
arguments = parser.parse_args()
_pdf = arguments.pdf
_zip = arguments.zip

if os.system('which rsvg-convert') != 0:
	os.system('sudo apt-get -y install librsvg2-bin')
if os.system('which python3') != 0:
	os.system('sudo apt-get -y install python3')
if os.system('which pdftk') != 0:
	os.system('sudo apt-get -y install pdftk')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
BADGES_FOLDER = os.path.join(APP_ROOT, 'static/badges')

os.system('python3 ' + APP_ROOT + '/generate-badges.py')

input_folders = [file for file in os.listdir(BADGES_FOLDER)
               if file.lower().endswith(".badges")]

def _zipFile(src,dst,allowed):
    zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            if filename != dst + ".zip" and filename.split('.')[-1] in allowed:
                absname = os.path.abspath(os.path.join(dirname, filename))
                arcname = absname[len(abs_src) + 1:]
                zf.write(absname, arcname)
    zf.close()

def generate_pdfs(folder_path):
	svgs = [file for file in os.listdir(folder_path)
		  if file.lower().endswith('.svg')]
	for svg in svgs:
		svg_path = os.path.join(folder_path, svg)
		pdf_path = os.path.splitext(svg_path)[0] + '.pdf'
		print('svg: {}'.format(svg_path))
		print('pdf: {}'.format(pdf_path))
		os.system('rsvg-convert -f pdf -o {} {}'.format(pdf_path, svg_path))

# Generating PDF files from svg.
if _pdf:
	for folder in input_folders:
		folder_path = os.path.join(BADGES_FOLDER, folder)
		generate_pdfs(folder_path)

# Merge badges of different types
input_folders = [file for file in os.listdir(BADGES_FOLDER)
               if file.lower().endswith(".badges")]

print ('Merging badges of different types.')

for folder in input_folders:
	folder_path = os.path.join(BADGES_FOLDER, folder)
	out = folder.replace('.','-') + '.pdf'
	out_path = os.path.join(BADGES_FOLDER, out)
	os.system('pdftk ' + folder_path + '/*.pdf cat output ' + out_path)

final_path = os.path.join(BADGES_FOLDER, 'all-badges.pdf')
os.system('pdftk ' + BADGES_FOLDER + '/*.pdf cat output ' + final_path)

if _zip:
	print ("Created {}".format(final_path))
	print ("Generating ZIP file")

	_zipFile("static/badges", "static/badges/all-badges", ["svg", "pdf"])

	print ('Generating ZIP of SVG files')

	input_folders = [file for file in os.listdir(BADGES_FOLDER)
	               if file.lower().endswith(".badges")]

	for folder in input_folders:
		folder_path = os.path.join(BADGES_FOLDER, folder)
		file_name = folder_path.replace('.','-') + '-svg'
		_zipFile(folder_path, os.path.join(folder_path, file_name), ["svg"])
