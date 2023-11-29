#!/usr/bin/python3

def print_last_digit(number):
    """prints the last digit of a number

    Args:
        number (int): value

    Returns:
        int: the last digit
    """
    if number < 0:
        number *= -1
        print(number % 10)
    else:
        print(number % 10)
