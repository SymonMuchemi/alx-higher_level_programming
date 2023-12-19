#!/usr/bin/python3
def safe_print_division(a, b):
    """divides two integers

    Args:
        a (int): operand 1
        b (int): operand 2

    Returns:
        int: the summation
    """
    try:
        result = float(a) / b
    except (ZeroDivisionError):
        result = None
    finally:
        if result is not None:
            print("Inside result: {:.1f}".format(result))
        else:
            print("Inside result: None")
        return result
