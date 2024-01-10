#!/usr/bin/python3
"""program to divide a matrix
"""

typeerror_msg = "matrix must be a matrix (list of lists) of integers/floats"
row_len_error = "Each row of the matrix must have the same size"


def matrix_divided(matrix, div):
    """divides a matrix

    Args:
        matrix (list): list of lists of int or float
        div (int, float): the divider value

    Raises:
        TypeError: if matrix is not a list
        TypeError: if matrix is not a list of lists
        ZeroDivisionError: if div is zero
        TypeError: if div is not a number
        TypeError: if list item is not a number
        TypeError: if rows are not of the same size

    Returns:
        list: matrix of divided numbers
    """
    if not isinstance(matrix, list):
        raise TypeError("{}".format(typeerror_msg))
    if not isinstance(div, (int, float)):
        raise TypeError("div must be an number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) == 0:
        raise TypeError("{}".format(typeerror_msg))

    new_matrix = []
    row_len = len(matrix[0])

    for row in matrix:
        new_row = []
        if len(row) != row_len:
            raise TypeError("{}".format(row_len_error))
        if len(row) == 0:
            raise TypeError(typeerror_msg)
        if not isinstance(row, list):
            raise TypeError("{}".format(typeerror_msg))
        for item in row:
            if isinstance(item, (float, int)):
                item = item / div
                new_row.append(round(item, 2))
            else:
                raise TypeError("{}".format(typeerror_msg))
        new_matrix += new_row
    return new_matrix
