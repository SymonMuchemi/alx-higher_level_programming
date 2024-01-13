#!/usr/bin/python3
"""program that adds all command line arguments and saves to a file"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

file_name = "add_item.json"

try:
    items = load_from_json_file(file_name)
except FileNotFoundError:
    obj_list = []
    if (len(sys.argv) > 1):
        for i in range(1, len(sys.argv)):
            obj_list.append(sys.argv[i])
    save_to_json_file(obj_list, file_name)
