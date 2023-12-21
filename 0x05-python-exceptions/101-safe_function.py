#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """executes another function safely

    Args:
        fct (function): the function to be executed

    Returns:
        any: result of the function or None
    """
    try:
        result = fct(*args)
        return result
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
