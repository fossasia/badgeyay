#!/usr/bin/python3

import os
import csv
import shutil
import html
import json

NUMBER_OF_BADGES_PER_PAGE = 8
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')

paper_sizes = {}
paper_sizes['A3'] = ['297mm', '420mm']
paper_sizes['A4'] = ['210mm', '297mm']

input_files = [file for file in os.listdir("./static/uploads")
               if file.lower().endswith(".csv")]

with open("../badges/8BadgesOnA3.svg", encoding="UTF-8") as f:
    CONTENT = f.read()

def generate_badges(aggregate, folder, index, picture, paper_size):
    paper_width = paper_sizes[paper_size][0]
    paper_height = paper_sizes[paper_size][1]
    target = os.path.join(folder, "badges_{}.svg".format(index))
    print("Generating {}".format(target))
    content = CONTENT
    content = content.replace("paper_width", paper_width)
    content = content.replace("paper_height", paper_height)
    ext = os.path.splitext(picture)[1]
    picture_name = "badges_{}_background{}".format(index, ext)
    shutil.copyfile(picture, os.path.join(folder, picture_name))
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
            content = content.replace("person_{}_line_{}".format(i + 1, j + 1), text)
        content = content.replace("badge_{}.png".format(i + 1), picture_name)
    with open(target, "w", encoding="UTF-8") as f:
        f.write(content)


for input_file in input_files:
    config_json = 'default.config.json'

    #check if custom config.json is present for the file
    config_json_uploaded = os.path.splitext(input_file)[0] + '.json'
    config_json_uploaded_path = './static/uploads/' + config_json_uploaded
    if os.path.isfile(config_json_uploaded_path):
        config_json = config_json_uploaded
    config = json.loads(open('./static/uploads/'+ config_json).read())
    options = config['options']

    picture = os.path.splitext(input_file)[0]
    picpath = './static/uploads/' + picture
    if not os.path.isfile(picpath):
        print("SKIP: {} has no picture {}".format(input_file, picture))
        continue
    print("READING: {}".format(input_file))
    folder = APP_ROOT+'/static/badges/'+input_file + ".badges"
    shutil.rmtree(folder, ignore_errors=True)
    try:
        os.makedirs(folder, exist_ok=True)
    except Exception:
        pass

    with open(os.path.join(UPLOAD_FOLDER, input_file), encoding="UTF-8") as f:
        aggregate = []
        i = 1
        for row in csv.reader(f):
            aggregate.append(row)
            if options['badge_wrap']:
                aggregate.append(row)
            if len(aggregate) >= NUMBER_OF_BADGES_PER_PAGE:
                generate_badges(aggregate, folder, i, picpath, options['paper_size'])
                aggregate = []
                i += 1
        if aggregate:
            generate_badges(aggregate, folder, i, picpath, options['paper_size'])
