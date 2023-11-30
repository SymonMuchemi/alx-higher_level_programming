#!/usr/bin/python3
def remove_char_at(str, n):
    """removes a character at index n

    Args:
        str (string): string
        n (int): the index

    Return;
        string: the string with a removed char
    """
    final_str = ""
    for i in range(0, len(str)):
        if (i == n):
            continue
        final_str += str[i]
    return (final_str)
