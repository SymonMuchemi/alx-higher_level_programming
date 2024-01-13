#!/usr/bin/python3
"""writing to a file"""


def write_file(filename="", text=""):
    """writes text to a file and create it if it doesn't exist

    Args:
        filename (str, optional): name of file. Defaults to "".
        text (str, optional): text to be written. Defaults to "".
    """
    with open(filename, 'w', encoding='utf-8') as fp:
        written_chars = fp.write(text)

    return written_chars
