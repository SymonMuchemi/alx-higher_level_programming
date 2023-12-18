#!/usr/bin/python3
def safe_print_integer(value):
    """prints an integer with a '{:d}' format

    Args:
        value (any): the value to be printed if int

    Returns:
        bool: true if value is int
    """
    try:
        num = int(value)
        print("{:d}".format(num))
    except ValueError:
        return False
    return True
