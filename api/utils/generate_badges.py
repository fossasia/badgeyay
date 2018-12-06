import os
import csv
import shutil
import html
from flask import current_app as app
from defusedxml.lxml import parse
from defusedxml.lxml import _etree as etree
from api.utils.dimen import badge_config


def remove_extra(badge_page, offset):
    tree = etree.parse(open(badge_page, 'r'))
    root = tree.getroot()
    children = root.findall('.//{http://www.w3.org/2000/svg}g')
    for i in range(offset, len(children)):
        children[i].getparent().remove(children[i])
    etree.ElementTree(root).write(badge_page, pretty_print=True)


class GenerateBadges:
    def __init__(self,
                 image_name,
                 csv_name,
                 paper_dimen,
                 badge_size):
        self.APP_ROOT = app.config.get('BASE_DIR')
        self.image_name = image_name
        self.image = os.path.join(app.config.get('BASE_DIR'), 'static', 'uploads', 'image', image_name)
        self.csv = os.path.join(app.config.get('BASE_DIR'), 'static', 'uploads', 'csv', csv_name)
        self.paper_size = {'A3': ['297mm', '420mm'], 'A4': ['210mm', '297mm'], 'A5': ['148mm', '210mm'], 'A6': ['105mm', '148mm']}
        self.paper_dimen = paper_dimen
        dimen = badge_config[paper_dimen][badge_size]
        self.NUMBER_OF_BADGES_PER_PAGE = dimen.badges
        self.svgPath = 'static/badges/' + badge_size + 'on' + paper_dimen + '.svg'
        self.wrap = True
        with open(os.path.join(self.APP_ROOT, self.svgPath), encoding="UTF-8") as f:
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
                content = content.replace('Person_{}_{}'.format(i + 1, j + 1), text)
            content = content.replace('Pictures/18033231.jpeg', os.path.join(self.folder, 'background.png'))
        with open(target, 'w', encoding='UTF-8') as f:
            f.write(content)
        remove_extra(target, len(rows) + 1)
        # self.configure_badge_page(target)

    def configure_badge_page(self, badge_page):
        paper_width = self.paper_size.get(self.paper_dimen)[0]
        paper_height = self.paper_size.get(self.paper_dimen)[1]
        tree = parse(open(badge_page, 'r'))
        root = tree.getroot()
        path = root.xpath('//*[@id="svg2"]')[0]
        path.set('width', paper_width)
        path.set('height', paper_height)
        etree.ElementTree(root).write(badge_page, pretty_print=True)


def make_initials(val):
    return val[0].capitalize()
