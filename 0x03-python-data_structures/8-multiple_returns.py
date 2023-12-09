#!/usr/bin/python3
def multiple_returns(sentence):
    """returns a tuple with the length of a string and its first character

    Args:
        sentence (str): the string to be evaluated

    Returns:
        tuple: the length of the string and its first character
    """
    if sentence == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])
