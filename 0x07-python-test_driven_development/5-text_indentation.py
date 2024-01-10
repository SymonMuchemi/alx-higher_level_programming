#!/usr/bin/python3
"""program to print text indentations"""


def text_indentation(text):
    """prints a text with 2 new lines after each of 
    these characters: ., ? and :

    Args:
        text (str): input string

    Raises:
        TypeError: if text is not a string or it is empty
    """
    if not isinstance(text, str) or len(text) == 0:
        raise TypeError("text must be a string")

    new_str = ''
    ignore_space = False

    for char in text:
        if ignore_space and char == ' ':
            continue

        new_str += char
        if char in ['.', '?', ':']:
            new_str += '\n\n'
            ignore_space = True
        else:
            ignore_space = False
    new_str = new_str.rstrip()
    print(new_str)
