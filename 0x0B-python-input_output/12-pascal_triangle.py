#!/usr/bin/python3
"""program to represent a Pascal triangle"""


def factorial(n):
    """calculates the factorial of a number

    Args:
        n (int): the number to be calculated

    Returns:
        int: the factorial of the number
    """
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def combination(n, k):
    """calculates the combination of n to r
    formula:
        C(n, k) = n! / (k!(n -k)!)

    Args:
        n (int): object
        k (int): sample

    Returns:
        int: n choose r
    """
    return factorial(n) // (factorial(k) * factorial(n - k))


def pascal_triangle(n):
    """represents the Pascal triangle

    Args:
        n (int): the largest combinator

    Returns:
        lst: list of lists
    """
    if n <= 0:
        return []

    master_lst = []
    i = 0

    while i < n:
        lst = []
        j = i
        while (j >= 0):
            lst.append(combination(i, j))
            j -= 1
        master_lst.append(lst)
        i += 1
    return master_lst
