#!/usr/bin/python3


def read_file(filename=""):
    """reads and prints out the contents of a file

    Args:
        filename (str, optional): name of the file. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as fp:
        read_lines = fp.read()
        print(read_lines[:-1])
