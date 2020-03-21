#!/usr/bin/python
"""
-

"""

import json   # json in and out
import pprint # pretty print - print to screen nicely

show_to_screen = True
ugly_one_lined_json_file = '/home/bpt/Desktop/terriblejson.json'
output_pretty_json       = '/home/bpt/Desktop/pretty_cool_json_gosh-its_pretty.json'


json_as_dict = {}

with open(ugly_one_lined_json_file, 'r') as f:
    json_as_dict = json.load(f)

# I am now in dicts and lists.
print(type(json_as_dict))
pprint.pprint(json_as_dict)

with open(output_pretty_json, 'w', encoding='utf-8') as f:
    json.dump(json_as_dict, f, ensure_ascii=False, indent=4)
