import os
import csv
import shutil
import html
import json
import traceback
import tempfile

from defusedxml.lxml import parse
from defusedxml.lxml import _etree as etree


class GenerateBadges:
    def __init__(self):
        self.NUMBER_OF_BADGES_PER_PAGE = 8
        self.IMG = None
        self.CONFIG = None
        self.NAMES = None
        self.TEMP_DIR = tempfile.gettempdir() + "/"
        self.APP_ROOT = os.getcwd()
        self.LIB_ROOT = os.path.abspath(os.path.join(os.path.abspath(os.path.join(__file__, os.pardir)), os.pardir))
        self.UPLOAD_FOLDER = os.path.join(self.LIB_ROOT, 'static/badges')

        self.paper_sizes = {'A3': ['297mm', '420mm'], 'A4': ['210mm', '297mm']}

        self.input_files = [file for file in os.listdir(
            self.TEMP_DIR) if file.lower().endswith(".csv")]

        with open(self.LIB_ROOT + "/static/8BadgesOnA3.svg", encoding="UTF-8") as f:
            self.CONTENT = f.read()

        self.font_choice = None

    def override_param(self, font, img, config, names):
        self.font_choice = font
        self.IMG = img
        self.CONFIG = config
        self.NAMES = names

    def configure_badge_page(self, badge_page, options):
        """
        Configure the badge page according to the page
        options as passed in the function
        :param `badge_page` - Single Badge Sheet
        :param `options` - Options for the page
        """
        if options.get('width') and options.get('height'):
            paper_width = options.get('width')
            paper_height = options.get('height')
        else:
            paper_size_format = options.get('paper_size_format')
            paper_width = self.paper_sizes[paper_size_format][0]
            paper_height = self.paper_sizes[paper_size_format][1]
        tree = parse(open(badge_page, 'r'))
        root = tree.getroot()
        path = root.xpath('//*[@id="svg2"]')[0]
        path.set('width', paper_width)
        path.set('height', paper_height)
        etree.ElementTree(root).write(badge_page, pretty_print=True)

    def generate_badges(self, aggregate, folder, index, picture, paper_size):
        """
        Generate the badges
        :param `aggregate` - Aggregate collection of details of badge holders
        :param `folder` - Destination folder to save
        :param `index` - Index number for generating the image
        :param `picture` - Picture file for background
        :param `paper_size` - Size of the paper
        """
        target = os.path.join(folder, "badges_{}.svg".format(index))
        print("Generating {}".format(target))
        content = self.CONTENT
        if self.font_choice:
            content = content.replace("font-family:sans-serif",
                                      "font-family:" + self.font_choice)
            content = content.replace("inkscape-font-specification:sans-serif",
                                      "inkscape-font-specification:" + self.font_choice)
            content = content.replace("font-family:ubuntu",
                                      "font-family:" + self.font_choice)
            content = content.replace("inkscape-font-specification:ubuntu",
                                      "inkscape-font-specification:" + self.font_choice)
        for i, row in enumerate(aggregate):
            row = [entry for entry in row if not entry.isspace()]
            if len(row) == 0:
                row = ["", "", "", ""]
            if len(row) == 1:
                row = ["", ""] + row + [""]
            else:
                row = [""] * (4 - len(row)) + row
            for j, text in enumerate(row):
                text = html.escape(text)
                content = content.replace(
                    "person_{}_line_{}".format(i + 1, j + 1), text)
            content = content.replace("badge_{}.png".format(i + 1), picture)

        with open(target, "w", encoding="UTF-8") as f:
            f.write(content)
        self.configure_badge_page(target, paper_size)

    def run_generator(self):
        """
        Run this class
        """
        for input_file in self.input_files:
            config_json = 'default.config.json'

            # check if custom config.json is present for the file
            if self.CONFIG is not None:
                config = json.loads(open(os.path.join(self.APP_ROOT, self.CONFIG)).read())
            else:
                badges_config_json = 'static/badges/' + config_json
                config = json.loads(open(os.path.join(self.LIB_ROOT,
                                                      badges_config_json)).read())
            options = config['options']

            picpath = os.path.join(self.APP_ROOT, self.IMG)
            if not os.path.isfile(picpath):
                print("SKIP: {} no picture found.".format(input_file))
                continue
            print("READING: {}".format(input_file))
            folder = self.TEMP_DIR + 'static/badges/' + input_file + ".badges"
            shutil.rmtree(folder, ignore_errors=True)
            try:
                os.makedirs(folder, exist_ok=True)
            except Exception:
                traceback.print_exc()
            ext = os.path.splitext(picpath)[1]
            badges_background = "badges_background{}".format(ext)
            shutil.copyfile(picpath, os.path.join(folder, badges_background))

            data_file_path = os.path.abspath(os.path.join(self.APP_ROOT, self.NAMES))
            with open(data_file_path, encoding="UTF-8") as f:
                aggregate = []
                i = 1
                for row in csv.reader(f):
                    aggregate.append(row)
                    if options['badge_wrap']:
                        aggregate.append(row)
                    if len(aggregate) >= self.NUMBER_OF_BADGES_PER_PAGE:
                        self.generate_badges(aggregate, folder, i,
                                             badges_background, options)
                        aggregate = []
                        i += 1
                if aggregate:
                    self.generate_badges(aggregate, folder, i,
                                         badges_background, options)
