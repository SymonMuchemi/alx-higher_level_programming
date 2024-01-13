#!/usr/bin/python3
"""program that adds all command line arguments and saves to a file"""
import sys

if __name__ == "__main__":
    # Importing functions from other modules
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        # Attempt to load existing items from the "add_item.json" file
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If the file is not found, create an empty list
        items = []

    # Extend the 'items' list with the command-line arguments (excluding the script name at sys.argv[0])
    items.extend(sys.argv[1:])

    # Save the updated 'items' list back to the "add_item.json" file
    save_to_json_file(items, "add_item.json")
