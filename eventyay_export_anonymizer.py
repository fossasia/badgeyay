#!/usr/bin/python3
import sys
import json
import random

if len(sys.argv) <= 1:
    print("Please pass the name of the file with the exported json as "
          "the first argument. A file with \"anonymous\" will be created"
          "next to it.")
    exit(1)

file = sys.argv[1]
anonymous_file = file + "-anonymous.json"

with open(file, encoding="UTF-8") as f:
    export = json.load(f)


def walk(e):
    if isinstance(e, list):
        for i, v in enumerate(e):
            _walk(e, i, v)
    elif isinstance(e, dict):
        for k, v in e.items():
            _walk(e, k, v)


def _walk(element, key, value):
    if isinstance(value, str):
        element[key] = scramble(value)
    elif isinstance(value, int):
        element[key] = random.randint(0, value * 2)
    else:
        walk(value)


def scramble(string):
    result = []
    for c in string:
        if "A" <= c <= "Z":
            c = chr(random.randint(ord("A"), ord("Z")))
        if "a" <= c <= "z":
            c = chr(random.randint(ord("a"), ord("z")))
        if "0" <= c <= "9":
            c = chr(random.randint(ord("0"), ord("9")))
        result.append(c)
    return "".join(result)


walk(export)

with open(anonymous_file, 'w', encoding="UTF-8") as f:
    json.dump(export, f)
