from defusedxml.lxml import _etree as etree
import os
from flask import current_app as app


class SVG2PNG:

    def __init__(self):
        self.APP_ROOT = app.config.get('BASE_DIR')
        self.ids = ['text4611', 'text4585', 'text4559', 'text4533', 'text4399', 'text4373', 'text4347', 'text4313']

    def do_text_fill(self, filename, fill):
        """
        Module to change color of badge's details
        :param `filename` - svg file to modify.
        :param `fill` - color to be applied on text
        """
        tree = etree.parse(open(os.path.join(self.APP_ROOT, filename), 'r'))
        element = tree.getroot()
        for _id in self.ids:
            path = element.xpath(("//*[@id='{}']").format(_id))[0]
            style_detail = path.get("style")
            style_detail = style_detail.split(";")
            if style_detail[7].split(':')[0] == 'fill':
                style_detail[7] = "fill:" + str(fill)
                print(style_detail[7])
            elif style_detail[6].split(':')[0] == 'fill':
                style_detail[6] = "fill:" + str(fill)
                print(style_detail[6])
            else:
                for ind, i in enumerate(style_detail):
                    if i.split(':')[0] == 'fill':
                        style_detail[ind] = "fill:" + str(fill)
            style_detail = ';'.join(style_detail)
            text_nodes = path.getchildren()
            path.set("style", style_detail)
            for t in text_nodes:
                text_style_detail = t.get("style")
                text_style_detail = text_style_detail.split(";")
                text_style_detail[-1] = "fill:" + str(fill)
                text_style_detail = ";".join(text_style_detail)
                t.set("style", text_style_detail)
        etree.ElementTree(element).write(filename, pretty_print=True)
        print("Text Fill saved!")
