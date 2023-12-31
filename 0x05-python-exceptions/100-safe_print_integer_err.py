#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """prints an integer or writes error to stderr

    Args:
        value (any): the integer to be printed

    Returns:
        bool: true if printing succeeds, false otherwise
    """
    try:
        print("{:d}".format(value))
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return False
    else:
        return True
