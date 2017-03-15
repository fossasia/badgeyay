#!/usr/bin/python3

import os
import csv
import itertools
import shutil

input_files = [file for file in os.listdir(".")
               if file.lower().endswith(".csv")]

NUMBER_OF_BADGES_PER_PAGE = 8               
with open("badges/8BadgesOnA3.svg") as f:
    CONTENT = f.read()

def generate_badges(aggregate, folder, index, picture):
    target = os.path.join(folder, "speakers_{}.svg".format(index))
    content = CONTENT
    ext = os.path.splitext(picture)[1]
    picture_name = "speakers_{}_background{}".format(index, ext)
    shutil.copyfile(picture, os.path.join(folder, picture_name))
    for i, row in enumerate(aggregate):
        first, last, twitter = (row + ["", "", ""])[:3]
        content = content.replace("firstname_{}".format(i), first)
        content = content.replace("lastname_{}".format(i), last)
        content = content.replace("twitter_{}".format(i), twitter)
        content = content.replace("badge_{}.png".format(i), picture_name)
    with open(target, "w") as f:
        f.write(content)
    

for input_file in input_files:
    picture = os.path.splitext(input_file)[0]
    if not os.path.isfile(picture):
        print("SKIP: {} has no picture {}".format(input_file, picture))
        continue
    print("READING: {}".format(input_file))
    folder = input_file + ".badges"
    os.makedirs(folder, exist_ok=True)
    
    with open(input_file, encoding="UTF-8") as f:
        aggregate = []
        for row in csv.reader(f):
            i = 1
            aggregate.append(row)
            if len(row) >= NUMBER_OF_BADGES_PER_PAGE:
                generate_badges(aggregate, folder, i, picture)
                aggregate = []
                i += 1
        generate_badges(aggregate, folder, i, picture)