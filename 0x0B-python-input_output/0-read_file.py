#!/usr/bin/python3
"""Simple file reading function"""


def read_file(filename=""):
    """reads and prints out the contents of a file

    Args:
        filename (str, optional): name of the file. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as fp:
        read_lines = fp.read()
        if len(read_lines):
            print(read_lines[:-1])
