#!/usr/bin/python3
"""program that adds all commandline arguments and saves to a file"""
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

file_name = "add_item.json"

if (len(sys.argv) > 1):
    obj_list = []
    for argument in sys.argv:
        obj_list.append(argument)

with open("add_item.json", 'a', encoding='utf-8') as fp:
    save_to_json_file()
