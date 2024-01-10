#!/usr/bin/python3
"""program that print the name of a person
"""


def say_my_name(first_name, last_name=""):
    """print the name(s)

    Args:
        first_name (str): first name argument
        last_name (str): last name argument. Optional

    Raises:
        TypeError: if first_name is not a string
        TypeError: if last_name is not a string
    """
    if not isinstance(first_name, str) or first_name == "":
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
