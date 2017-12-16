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
# get the file name via command line
anonymous_file = file + "-anonymous.json"
# Add "-anonymous.json" to this existing filename

with open(file, encoding="UTF-8") as f:
#open up the file
    export = json.load(f)
	#load the json to a variable "export"


def walk(e):
    if isinstance(e, list):
	# checks if the object (first argument) is an instance or subclass of classinfo class (second argument)
        for i, v in enumerate(e):
		#adds a counter to an iterable
            _walk(e, i, v)
    elif isinstance(e, dict):
	# checks if the object (first argument) is an instance or subclass of classinfo class (second argument)
        for k, v in e.items():
            _walk(e, k, v)


def _walk(element, key, value):
    if isinstance(value, str):
	# checks if the object (first argument) is an instance or subclass of classinfo class (second argument)
        element[key] = scramble(value)
		# use the function scramble() to fill the value of 'key'
    elif isinstance(value, int):
	# checks if the object (first argument) is an instance or subclass of classinfo class (second argument)
        element[key] = random.randint(0, value * 2)
		# use the random library to get an random between 0 to 2 * value
    else:
        walk(value)
		# use the function walk()


def scramble(string):
    result = []
	# initialize a list named `result`
    for c in string:
        if "A" <= c <= "Z":
            c = chr(random.randint(ord("A"), ord("Z")))
			# get an random letter between A to Z
        if "a" <= c <= "z":
            c = chr(random.randint(ord("a"), ord("z")))
			# get an random letter between a to z
        if "0" <= c <= "9":
            c = chr(random.randint(ord("0"), ord("9")))
			# get an random letter between 0 to 9
        result.append(c)
		# append the random variable `c` to `result`
    return "".join(result)
	# return the final output


walk(export)
# use the function walk()

with open(anonymous_file, 'w', encoding="UTF-8") as f:
# open `anonymous_file`
    json.dump(export, f)
	# put the json to `anonymous_file`
