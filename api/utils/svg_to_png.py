import os
import uuid
from defusedxml.lxml import _etree as etree
from defusedxml.lxml import parse
from cairosvg import svg2png
from flask import current_app as app
from api.utils.dimen import badge_config
from api.config import config


class SVG2PNG:

    def __init__(self):
        self.APP_ROOT = app.config.get('BASE_DIR')
        self.ids = ['text4611', 'text4585', 'text4559', 'text4533', 'text4399', 'text4373', 'text4347', 'text4313']

    def do_text_fill(self, filename, font_color_1, font_color_2, font_color_3, font_color_4, font_color_5, badge_size, paper_size):
        """
        Module to change color of badge's details
        :param `filename` - svg file to modify.
        :param `fill` - lis of color to be applied on each line
        """
        fill = [1, font_color_1, font_color_2, font_color_3, font_color_4, font_color_5]
        dimensions = badge_config[paper_size][badge_size]
        if config.ENV == 'LOCAL':
            filename = 'static/badges/' + dimensions.badgeSize + 'on' + dimensions.paperSize + '.svg'
        else:
            filename = os.getcwd() + '/api/static/badges/' + dimensions.badgeSize + 'on' + dimensions.paperSize + '.svg'
        tree = etree.parse(open(os.path.join(self.APP_ROOT, filename), 'r'))
        element = tree.getroot()

        for idx in range(1, dimensions.badges + 1):

            for row in range(1, 6):
                _id = 'Person_color_{}_{}'.format(idx, row)
                path = element.xpath(("//*[@id='{}']").format(_id))[0]
                style_detail = path.get("style")
                style_detail = style_detail.split(";")

                if style_detail[7].split(':')[0] == 'fill':
                    style_detail[7] = "fill:" + str(fill[row])
                    print(style_detail[7])

                elif style_detail[6].split(':')[0] == 'fill':
                    style_detail[6] = "fill:" + str(fill[row])
                    print(style_detail[6])

                else:
                    for ind, i in enumerate(style_detail):
                        if i.split(':')[0] == 'fill':
                            style_detail[ind] = "fill:" + str(fill[row])
                style_detail = ';'.join(style_detail)
                text_nodes = path.getchildren()
                path.set("style", style_detail)

                for t in text_nodes:
                    text_style_detail = t.get("style")
                    text_style_detail = text_style_detail.split(";")
                    for ind, i in enumerate(text_style_detail):
                        if i.split(':')[0] == 'fill':
                            text_style_detail[ind] = "fill:" + str(fill[row])

                    text_style_detail = ";".join(text_style_detail)
                    t.set("style", text_style_detail)

        etree.ElementTree(element).write(filename, pretty_print=True)
        print("Text Fill saved!")

    def change_font_size(self,
                         filename,
                         badge_size,
                         paper_size,
                         font_size_1,
                         font_size_2,
                         font_size_3,
                         font_size_4,
                         font_size_5):

        """
            Module to change size of each badge lines
                :param `filename` - svg file to modify.
                :param `font_size_1` - Size to be applied on first line
                :param `font_size_2` - Size to be applied on Second line
                :param `font_size_3` - Size to be applied on Third line
                :param `font_size_4` - Size to be applied on Fourth line
                :param `font_size_5` - Size to be applied on Fifth line
        """

        font_size = [1, font_size_1, font_size_2, font_size_3, font_size_4, font_size_5]
        dimensions = badge_config[paper_size][badge_size]
        if config.ENV == 'LOCAL':
            filename = 'static/badges/' + dimensions.badgeSize + 'on' + dimensions.paperSize + '.svg'
        else:
            filename = os.getcwd() + '/api/static/badges/' + dimensions.badgeSize + 'on' + dimensions.paperSize + '.svg'
        tree = etree.parse(open(os.path.join(self.APP_ROOT, filename), 'r'))
        element = tree.getroot()

        for idx in range(1, dimensions.badges + 1):

            for row in range(1, 6):
                _id = 'Person_color_{}_{}'.format(idx, row)
                path = element.xpath(("//*[@id='{}']").format(_id))[0]
                style_detail = path.get("style")
                style_detail = style_detail.split(";")

                for ind, i in enumerate(style_detail):
                    if i.split(':')[0] == 'font-size':
                        style_detail[ind] = "font-size:" + font_size[row]
                style_detail = ';'.join(style_detail)
                text_nodes = path.getchildren()
                path.set("font-size", style_detail)

                for t in text_nodes:
                    text_style_detail = t.get("style")
                    text_style_detail = text_style_detail.split(";")
                    text_style_detail[-1] = "font-size:" + font_size[row]
                    text_style_detail = ";".join(text_style_detail)
                    t.set("style", text_style_detail)

        etree.ElementTree(element).write(filename, pretty_print=True)
        print("Font Size Saved!")

    def change_font_family(self,
                           filename,
                           badge_size,
                           paper_size,
                           font_1,
                           font_2,
                           font_3,
                           font_4,
                           font_5):

        """
            Module to change Font Family of each badge lines
                :param `filename` - svg file to modify.
                :param `font_1` - Family to be applied on first line
                :param `font_2` - Family to be applied on Second line
                :param `font_3` - Family to be applied on Third line
                :param `font_4` - Family to be applied on Fourth line
                :param `font_5` - Family to be applied on Fifth line
        """

        font = [1, font_1, font_2, font_3, font_4, font_5]
        dimensions = badge_config[paper_size][badge_size]
        if config.ENV == 'LOCAL':
            filename = 'static/badges/' + dimensions.badgeSize + 'on' + dimensions.paperSize + '.svg'
        else:
            filename = os.getcwd() + '/api/static/badges/' + dimensions.badgeSize + 'on' + dimensions.paperSize + '.svg'
        tree = etree.parse(open(os.path.join(self.APP_ROOT, filename), 'r'))
        element = tree.getroot()

        for idx in range(1, dimensions.badges + 1):

            for row in range(1, 6):
                _id = 'Person_color_{}_{}'.format(idx, row)
                path = element.xpath(("//*[@id='{}']").format(_id))[0]
                style_detail = path.get("style")
                style_detail = style_detail.split(";")

                for ind, i in enumerate(style_detail):
                    if i.split(':')[0] == 'font-family':
                        style_detail[ind] = "font-family:" + font[row]
                style_detail = ';'.join(style_detail)
                text_nodes = path.getchildren()
                path.set("font-family", style_detail)

                for t in text_nodes:
                    text_style_detail = t.get("style")
                    text_style_detail = text_style_detail.split(";")
                    text_style_detail[-1] = "font-family:" + font[row]
                    text_style_detail = ";".join(text_style_detail)
                    t.set("style", text_style_detail)

        etree.ElementTree(element).write(filename, pretty_print=True)
        print("Font Family Saved!")

    def change_text_align(self,
                          filename,
                          badge_size,
                          paper_size,
                          align_1,
                          align_2,
                          align_3,
                          align_4,
                          align_5):

        """
            Module to change Text Alignment of each badge line
                :param `filename` - svg file to modify.
                :param `align_1` - Text Alignment to be applied on first line
                :param `align_2` - Text Alignment to be applied on Second line
                :param `align_3` - Text Alignment to be applied on Third line
                :param `align_4` - Text Alignment to be applied on Fourth line
                :param `align_5` - Text Alignment to be applied on Fifth line
        """

        align = [1, align_1, align_2, align_3, align_4, align_5]
        dimensions = badge_config[paper_size][badge_size]
        if config.ENV == 'LOCAL':
            filename = 'static/badges/' + dimensions.badgeSize + 'on' + dimensions.paperSize + '.svg'
        else:
            filename = os.getcwd() + '/api/static/badges/' + dimensions.badgeSize + 'on' + dimensions.paperSize + '.svg'
        tree = etree.parse(open(os.path.join(self.APP_ROOT, filename), 'r'))
        element = tree.getroot()

        for idx in range(1, dimensions.badges + 1):

            for row in range(1, 6):
                _id = 'Person_color_{}_{}'.format(idx, row)
                path = element.xpath(("//*[@id='{}']").format(_id))[0]
                style_detail = path.get("style")
                style_detail = style_detail.split(";")

                for ind, i in enumerate(style_detail):
                    if i.split(':')[0] == 'text-align':
                        style_detail[ind] = "text-align:" + align[row]
                style_detail = ';'.join(style_detail)
                text_nodes = path.getchildren()
                path.set("text-align", style_detail)

                for t in text_nodes:
                    text_style_detail = t.get("style")
                    text_style_detail = text_style_detail.split(";")
                    text_style_detail[-1] = "text-align:" + align[row]
                    text_style_detail = ";".join(text_style_detail)
                    t.set("style", text_style_detail)

        etree.ElementTree(element).write(filename, pretty_print=True)
        print("Text Alignment Saved!")

    def do_svg2png(self, opacity, fill):
        print(str(fill))
        """
        Module to convert svg to png
        :param `opacity` - Opacity for the output
        :param `fill` -  Background fill for the output
        """

        filename = os.path.join(self.APP_ROOT, 'svg', 'user_defined.svg')
        tree = parse(open(filename, 'r'))
        element = tree.getroot()
        # changing style using XPath.
        path = element.xpath('//*[@id="rect4504"]')[0]
        style_detail = path.get("style")
        style_detail = style_detail.split(";")
        style_detail[0] = "opacity:" + str(opacity)
        style_detail[1] = "fill:" + str(fill)
        style_detail = ';'.join(style_detail)
        path.set("style", style_detail)
        # changing text using XPath.
        path = element.xpath('//*[@id="tspan932"]')[0]
        # Saving in the original XML tree
        etree.ElementTree(element).write(filename, pretty_print=True)
        print("done")
        png_name = os.path.join(self.APP_ROOT, 'static', 'uploads', 'image', str(uuid.uuid4())) + ".png"
        svg2png(url=filename, write_to=png_name)

        return png_name
