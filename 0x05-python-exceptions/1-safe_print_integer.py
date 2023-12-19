#!/usr/bin/python3
def safe_print_integer(value):
    """prints an integer with a '{:d}' format

    Args:
        value (any): the value to be printed if int

    Returns:
        bool: true if value is int
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
        return True
