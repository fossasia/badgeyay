import os
import csv
import shutil
import html
import json
import traceback

from defusedxml.lxml import parse
from defusedxml.lxml import _etree as etree


class GenerateBadges:
    def __init__(self):
        self.NUMBER_OF_BADGES_PER_PAGE = 8
        self.APP_ROOT = os.path.dirname(os.path.abspath(__file__))
        self.UPLOAD_FOLDER = os.path.join(self.APP_ROOT, 'static/badge_backgrounds')

        self.paper_sizes = {'A3': ['297mm', '420mm'], 'A4': ['210mm', '297mm']}

        self.input_files = [file for file in os.listdir(
            self.UPLOAD_FOLDER) if file.lower().endswith(".csv")]

        with open(self.APP_ROOT + "/../badges/8BadgesOnA3.svg", encoding="UTF-8") as f:
            self.CONTENT = f.read()

        self.font_choice = None
        if os.path.isfile(os.path.join(self.UPLOAD_FOLDER, 'fonts.json')):
            self.DATA = json.load(open(os.path.join(self.UPLOAD_FOLDER, "fonts.json")))
            self.font_choice = self.DATA['font']

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
                row = [""] * (5 - len(row)) + row
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
            config_json_uploaded = os.path.splitext(input_file)[0] + '.json'
            config_json_uploaded_path = os.path.join(
                self.UPLOAD_FOLDER, config_json_uploaded)
            if os.path.isfile(config_json_uploaded_path):
                config_json = config_json_uploaded
            config = json.loads(open(self.UPLOAD_FOLDER + '/' + config_json).read())
            options = config['options']

            picture = os.path.splitext(input_file)[0]
            picpath = self.UPLOAD_FOLDER + '/' + picture
            if not os.path.isfile(picpath):
                print("SKIP: {} has no picture {}".format(input_file, picture))
                continue
            print("READING: {}".format(input_file))
            folder = self.APP_ROOT + '/static/badges/' + input_file + ".badges"
            shutil.rmtree(folder, ignore_errors=True)
            try:
                os.makedirs(folder, exist_ok=True)
            except Exception:
                traceback.print_exc()
            ext = os.path.splitext(picpath)[1]
            badges_background = "badges_background{}".format(ext)
            shutil.copyfile(picpath, os.path.join(folder, badges_background))

            with open(os.path.join(self.UPLOAD_FOLDER, input_file), encoding="UTF-8") as f:
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
