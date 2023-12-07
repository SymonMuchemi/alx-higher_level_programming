#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers

    Args:
        matrix (list, optional): list of lists.
        Defaults to [[]].
    """
    if matrix == [[]]:
        print()
        return
    for row in matrix:
        for column in row:
            print("{:d}".format(column),
                  end=' ' if column != row[-1] else '')
        print()
