#!/usr/bin/python3

import os

input_files = [file for file in os.listdir(".")
               if file.lower().endswith(".csv")]

for input_file in input_files:
    picture = os.path.splitext(input_file)[0]
    if not os.path.isfile(picture):
        print("SKIP: {} has no picture {}".format(input_file, picture))
        continue
    folder = input_file + ".badges"
    os.makedirs(folder, exist_ok=True)
    