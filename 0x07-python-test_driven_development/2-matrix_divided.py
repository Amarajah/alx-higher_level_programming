#!/usr/bin/python3
"""
Function that divides all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """
    Checks that matrix contains actual numbers.

    """
    if not isinstance(matrix, list) for row in matrix
            or not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a matrix
                (list of lists) of integers/floats')
    """
    Checks that matrix contains numbers.

    """
    if not all(isinstance(element, (int, float))
            for row in matrix for element in row):
        raise TypeError('matrix must be a matrix
                 (list of lists) of integers/floats')
    """
    Checks that all rows are of the same size.

    """
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    """
    Checks that div is actually a number.

    """
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    """
    Checks that div isn't 0, else an error is thrown.
    """
    if div == 0:
        raise ZeroDivisionError('division by zero')
    """
    Returns a new matrix, rounded up to two decimal places.

    """

    return [[round(element / div, 2) for element in row] for row in matrix]
