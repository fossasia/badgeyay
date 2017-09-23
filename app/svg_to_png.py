from lxml import etree
from cairosvg import svg2png
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
SVGS_FOLDER = os.path.join(APP_ROOT, 'static/svgs')
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')

def do_svg2png(filename,opacity,fill,text):
    png_filename = filename
    filename = filename.rsplit(".",1)[0] + '.svg'
    filename = os.path.join(SVGS_FOLDER, filename)
    tree = etree.parse(open(filename, 'r'))
    for element in tree.iter():
        if element.tag.split("}")[1] == "rect":
            if element.get("id") == "rect4504":
                style_detail = element.get("style")
                style_detail = style_detail.split(";")
                style_detail[0] = "opacity:"+str(opacity)
                style_detail[1] = "fill:"+str(fill)
                style_detail = ';'.join(style_detail)
                element.set("style", style_detail)

        if element.tag.split("}")[1] == "tspan":
            if element.get("id") == "tspan932":
                #Code to change the text in SVG
                #Change value of tspan932 to function argument text
                print("Write Code")

    svg2png(url=filename,write_to=UPLOAD_FOLDER+'/'+png_filename)
    print("Image Saved")
