from lxml import etree
from defusedxml.lxml import parse
from cairosvg import svg2png
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
SVGS_FOLDER = os.path.join(APP_ROOT, 'static/svgs')
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')


def do_svg2png(filename, opacity, fill, text_):
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
    path.text = text_
    # Saving in the original XML tree
    etree.ElementTree(element).write(filename, pretty_print=True)
    print("done")
    svg2png(url=filename, write_to=UPLOAD_FOLDER + '/' + png_filename)
    print("Image Saved")
