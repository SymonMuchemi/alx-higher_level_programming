#!/usr/bin/python3
def no_c(my_string):
    """removes the all characters C and c 
        from a string

    Args:
        my_string (string): the stream of characters

    Returns:
        string: string with no C and c characters
    """
    new_str = ""
    for char in my_string:
        if char not in "cC":
            new_str += char
    return new_str
