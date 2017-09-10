#!/usr/bin/python3

import os
import csv
import itertools
import shutil
import html

input_files = [file for file in os.listdir(".")
               if file.lower().endswith(".csv")]

NUMBER_OF_BADGES_PER_PAGE = 8
with open("../../../badges/8BadgesOnA3.svg", encoding="UTF-8") as f:
    CONTENT = f.read()

def generate_badges(aggregate, folder, index, picture):
    target = os.path.join(folder, "badges_{}.svg".format(index))
    print("Generating {}".format(target))
    content = CONTENT
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
    picture = os.path.splitext(input_file)[0]
    if not os.path.isfile(picture):
        print("SKIP: {} has no picture {}".format(input_file, picture))
        continue
    print("READING: {}".format(input_file))
    folder = input_file + ".badges"
    shutil.rmtree(folder, ignore_errors=True)
    try:
        os.makedirs(folder, exist_ok=True)
    except PermissionError:
        pass
    
    with open(input_file, encoding="UTF-8") as f:
        aggregate = []
        i = 1
        for row in csv.reader(f):
            aggregate.append(row)
            aggregate.append(row)
            if len(aggregate) >= NUMBER_OF_BADGES_PER_PAGE:
                generate_badges(aggregate, folder, i, picture)
                aggregate = []
                i += 1
        if aggregate:
            generate_badges(aggregate, folder, i, picture)
