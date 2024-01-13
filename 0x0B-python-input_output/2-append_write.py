#!/usr/bin/python3
"""function to add new text to a file"""


def append_write(filename="", text=""):
    """adds new text to the end of a file

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): the character to be added. Defaults to "".

    Returns:
        int: the number of characters appended to the file
    """
    with open(filename, 'a', encoding='utf-8') as fp:
        chars_added = fp.write(text)

    return chars_added
