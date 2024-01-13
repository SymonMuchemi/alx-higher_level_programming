#!/usr/bin/python3
"""function to add new text to a file"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as fp:
        chars_added = fp.write(text)

    return chars_added
