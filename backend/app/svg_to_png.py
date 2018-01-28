from lxml import etree
from defusedxml.lxml import parse
from cairosvg import svg2png
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
SVGS_FOLDER = os.path.join(APP_ROOT, 'static/svgs')
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
ids = ['text4611', 'text4585', 'text4559', 'text4533', 'text4399', 'text4373', 'text4347', 'text4313']

def do_svg2png(filename, opacity, fill):
    """
    Module to convert svg to png
    :param `filename` - Destination file name
    :param `opacity` - Opacity for the output
    :param `fill` -  Background fill for the output
    :param `text_` - Text to be placed on the badge
    """
    png_filename = filename
    filename = filename.rsplit(".", 1)[0] + '.svg'
    filename = os.path.join(SVGS_FOLDER, filename)
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
    svg2png(url=filename, write_to=UPLOAD_FOLDER + '/' + png_filename)
    print("Image Saved")


def do_text_fill(filename, fill):
    """
    Module to change color of badge's details
    :param `filename` - svg file to modify.
    :param `fill` - color to be applied on text
    """
    tree = etree.parse(open(filename, 'r'))
    element = tree.getroot()
    for _id in ids:
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
