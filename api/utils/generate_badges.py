import os
import csv
import shutil
import html
from flask import current_app as app
from defusedxml.lxml import parse
from defusedxml.lxml import _etree as etree


class GenerateBadges:
    def __init__(self, image_name, csv_name, badge_size, font_size, font_choice):
        self.APP_ROOT = app.config.get('BASE_DIR')
        self.image_name = image_name
        self.image = os.path.join(app.config.get('BASE_DIR'), 'static', 'uploads', 'image', image_name)
        self.csv = os.path.join(app.config.get('BASE_DIR'), 'static', 'uploads', 'csv', csv_name)
        self.paper_size = {'A3': ['297mm', '420mm'], 'A4': ['210mm', '297mm'], 'A5': ['148mm', '210mm'], 'A6': ['105mm', '148mm']}
        self.badge_size = badge_size
        self.wrap = True
        self.font_size = font_size
        self.font_choice = font_choice
        self.NUMBER_OF_BADGES_PER_PAGE = 8
        with open(os.path.join(self.APP_ROOT, 'static/badges/8BadgesOnA3.svg'), encoding="UTF-8") as f:
            self.CONTENT = f.read()

    def run_generator(self):
        self.folder = os.path.join(self.APP_ROOT, 'static', 'temporary', os.path.splitext(self.image_name)[0])
        try:
            os.makedirs(self.folder)
        except Exception as e:
            print(e)

        shutil.copyfile(self.image, os.path.join(self.folder, 'background.png'))
        shutil.copyfile(self.csv, os.path.join(self.folder, 'data.csv'))

        with open(os.path.join(self.folder, 'data.csv'), encoding='UTF-8') as f:
            rows = []
            i = 1
            for row in csv.reader(f):
                rows.append(row)
                if self.wrap:
                    rows.append(row)
                if len(rows) == self.NUMBER_OF_BADGES_PER_PAGE:
                    self.generate_badges(rows, i)
                    rows = []
                    i += 1
            if rows:
                self.generate_badges(rows, i)

    def generate_badges(self, rows, index):
        target = os.path.join(self.folder, 'badges_{}.svg'.format(index))
        content = self.CONTENT
        if self.font_choice:
            content = content.replace("font-family:sans-serif", "font-family:" + self.font_choice)
            content = content.replace("inkscape-font-specification:sans-serif", "inkscape-font-specification:" + self.font_choice)
            content = content.replace("font-family:ubuntu", "font-family:" + self.font_choice)
            content = content.replace("inkscape-font-specification:ubuntu", "inkscape-font-specification:" + self.font_choice)
        if self.font_size:
            content = content.replace("font-size:31.25px", "font-size:" + str(self.font_size) + "px")
        for i, row in enumerate(rows):
            row = [entry for entry in row if not entry.isspace()]
            if len(row) == 0:
                row = ["", "", "", ""]
            if len(row) == 1:
                row = ["", ""] + row + [""]
            else:
                row = [""] * (5 - len(row)) + row

            for j, text in enumerate(row):
                text = html.escape(text)
                content = content.replace(
                    'person_{}_line_{}'.format(i + 1, j + 1), text)
            content = content.replace('badge_{}.png'.format(i + 1), os.path.join(self.folder, 'background.png'))
        with open(target, 'w', encoding='UTF-8') as f:
            f.write(content)
        self.configure_badge_page(target)

    def configure_badge_page(self, badge_page):
        paper_width = self.paper_size.get(self.badge_size)[0]
        paper_height = self.paper_size.get(self.badge_size)[1]
        tree = parse(open(badge_page, 'r'))
        root = tree.getroot()
        path = root.xpath('//*[@id="svg2"]')[0]
        path.set('width', paper_width)
        path.set('height', paper_height)
        etree.ElementTree(root).write(badge_page, pretty_print=True)
