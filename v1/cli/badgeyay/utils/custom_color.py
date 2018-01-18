import os

import click
from cairosvg import svg2png
from defusedxml.lxml import parse
from lxml import etree


APP_ROOT = os.path.abspath(os.path.join(os.path.abspath(os.path.join(__file__, os.pardir)), os.pardir))
STATIC_ASSET = os.path.join(APP_ROOT, 'static')
GENERATED = os.path.join(os.getcwd(), 'generated')


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
    filename = os.path.join(STATIC_ASSET, filename)
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
    svg2png(url=filename, write_to=GENERATED + '/' + png_filename)
    click.echo('Custom Image Saved')
