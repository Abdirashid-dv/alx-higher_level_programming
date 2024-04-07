#!/usr/bin/python3
"""Defines a function to divide all elements of a matrix by a scalar."""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The input matrix (list of lists of integers or floats).
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with elements divided by div (rounded to 2 decimal places).
    """
    # if is None values
    if matrix is None and div is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # Validate input matrix
    if not all(isinstance(row, list) and all(isinstance(val, (int, float)) for val in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate row sizes
    row_sizes = set(len(row) for row in matrix)

    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Validate divisor
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and round to 2 decimal places
    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]
    return new_matrix

