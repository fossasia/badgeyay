#!/usr/bin/python3

import json
import os

MAX_STRING = "chaftsladen Potsdam (F"

with open("speaker.json") as f:
    speakers = json.load(f)
    
with open("speaker.png.csv", "w") as f:
    f.write("Given Name,Family Name,Project\n")
    for speaker in speakers:
        fields = [speaker[field] for field in "name organisation website twitter facebook github linkedin position".split() if speaker[field]]
        i = 0
        while i < len(fields):
            field = fields[i]
            for s in ["http://", "https://", "www.", ""]:
                if field.startswith(s):
                    field = field[len(s):]
            field = field.strip("/")
            t = "twitter.com/"
            if field.startswith(t):
                field = "@" + field[len(t):]
            if len(field) > len(MAX_STRING):
                if i < 3:
                    huge_field = field.split()
                    if any(len(sf) > len(MAX_STRING) for sf in huge_field):
                        del fields[i]
                    else:
                        print(huge_field)
                        fields[i:i+1] = [" ".join(huge_field[:len(huge_field)//2]), " ".join(huge_field[len(huge_field)//2:])]
                else:
                    del fields[i] # skip split of huge field in the end
            elif field in fields[i+1:]:
                del fields[i] # remove duplicates
            else:
                fields[i] = field
                i += 1
        fields += [""] * 4
        f.write("{},{},{},{}\n".format(*fields[:4]))





