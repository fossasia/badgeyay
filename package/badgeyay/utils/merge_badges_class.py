import os
from cairosvg import svg2pdf
from PyPDF2 import PdfFileMerger


class MergeBadges:
    """docstring for MergeBadges"""

    def __init__(self, app_root=None):
        if app_root:
            self.APP_ROOT = app_root
            self.BADGES_FOLDER = os.path.join(self.APP_ROOT, 'static/badges')
        else:
            self.APP_ROOT = os.path.dirname(os.path.abspath(__file__))
            self.BADGES_FOLDER = os.path.join(self.APP_ROOT, 'static/badges')

        self.input_folders = [file for file in os.listdir(self.BADGES_FOLDER) if file.lower().endswith(".badges")]
        print("Initialised")

    @staticmethod
    def generatePDFS(folder_path):
        svgs = [file for file in os.listdir(folder_path) if file.lower().endswith('.svg')]
        for svg in svgs:
            svg_path = os.path.join(folder_path, svg)
            pdf_path = os.path.splitext(svg_path)[0] + '.pdf'
            print('svg: {}'.format(svg_path))
            print('pdf: {}'.format(pdf_path))
            try:
                svg2pdf(url=svg_path, write_to=pdf_path)
            except Exception as e:
                print(e)

    def mergePDFS(self):
        for folder in self.input_folders:
            folder_path = os.path.join(self.BADGES_FOLDER, folder)
            self.generatePDFS(folder_path)

        # Merge badges of different types
        self.input_folders = [file for file in os.listdir(self.BADGES_FOLDER) if file.lower().endswith(".badges")]

        print('Merging badges of different types.')

        for folder in self.input_folders:
            folder_path = os.path.join(self.BADGES_FOLDER, folder)
            merger = PdfFileMerger()
            pdfs = [file for file in os.listdir(folder_path) if file.lower().endswith('.pdf')]
            for pdf in pdfs:
                merger.append(open(os.path.join(folder_path, pdf), 'rb'))
            out = folder + '.pdf'
            out_path = os.path.join(self.BADGES_FOLDER, out)
            with open(out_path, 'wb') as fout:
                merger.write(fout)

        final_path = os.path.join(self.BADGES_FOLDER, 'all-badges.pdf')
        pdfs = [file for file in os.listdir(self.BADGES_FOLDER) if file.lower().endswith('.pdf')]
        merger = PdfFileMerger()
        for pdf in pdfs:
            merger.append(open(os.path.join(self.BADGES_FOLDER, pdf), 'rb'))

        with open(final_path, 'wb') as fout:
            merger.write(fout)
