#!/usr/bin/python3
"""program to update a file by searching and replacing"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text after each line containing a specfic string

    Args:
        filename (str, optional): the name of the file. Defaults to "".
        search_string (str, optional): the string to look for. Defaults to "".
        new_string (str, optional): the string to add in a new line.
        Defaults to "".
    """
    if len(filename) == 0:
        return

    with open(filename, 'r+', encoding='utf-8') as file:
        list_of_lines = list(file)
        final_list_of_lines = []

        for line in list_of_lines:
            if search_string in line:
                new_line = line + new_string
                final_list_of_lines.append(new_line)
            else:
                final_list_of_lines.append(line)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(''.join(final_list_of_lines))
