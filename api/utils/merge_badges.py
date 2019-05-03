import os
from flask import current_app as app
from api.utils.generate_badges import GenerateBadges
from cairosvg import svg2pdf
from PyPDF2 import PdfFileMerger


class MergeBadges:
    def __init__(self,
                 image_name,
                 csv_name,
                 paper_size,
                 badge_size):
        self.APP_ROOT = app.config.get('BASE_DIR')
        self.badge_generator = GenerateBadges(image_name,
                                              csv_name,
                                              paper_size,
                                              badge_size)
        self.badge_generator.run_generator()
        self.folder = os.path.join(self.APP_ROOT, 'static', 'temporary', os.path.splitext(image_name)[0])

    def merge_pdfs(self):
        self.generate_pdfs(self.folder)
        pdf_files = [file for file in os.listdir(self.folder) if file.endswith('.pdf')]
        merger = PdfFileMerger()
        for pdf in pdf_files:
            merger.append(open(os.path.join(self.folder, pdf), 'rb'))
        outfile = 'all-badges.pdf'
        out_path = os.path.join(self.folder, outfile)
        with open(out_path, 'wb') as fout:
            merger.write(fout)

    @staticmethod
    def generate_pdfs(folder_path):
        svgs = [file for file in os.listdir(folder_path) if file.endswith('.svg')]
        for svg in svgs:
            svg_path = os.path.join(folder_path, svg)
            pdf_path = os.path.splitext(svg_path)[0] + '.pdf'
            try:
                svg2pdf(url=svg_path, write_to=pdf_path)
            except Exception:
                print('')
        print("done")
