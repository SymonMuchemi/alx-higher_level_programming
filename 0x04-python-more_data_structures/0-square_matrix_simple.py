#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """squares all elements in amtrix

    Args:
        matrix (list, optional): two dimensional array.
                                    Defaults to [].
    Returns:
        list: matrix containing squares
    """
    if len(matrix) == 0:
        return matrix
    else:
        new_matrix = []
        for i in range(len(matrix)):
            new_matrix.append(list(map(lambda x: x ** 2, matrix[i])))
        return new_matrix
