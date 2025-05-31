#!/usr/bin/env python3
"""
Function that calculates the cofactor matrix of a given matrix
"""


def cofactor(matrix):
    """
    Calculate the cofactor matrix of a matrix.

    Args:
        matrix: A list of lists representing a square matrix

    Returns:
        The cofactor matrix of the input matrix

    Raises:
        TypeError: If matrix is not a list of lists
        ValueError: If matrix is not a non-empty square matrix
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0:
        raise ValueError("matrix must be a non-empty square matrix")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    cofactor_matrix = []

    for i in range(n):
        cofactor_row = []
        for j in range(n):
            submatrix = []
            for row_idx in range(n):
                if row_idx != i:
                    sub_row = []
                    for col_idx in range(n):
                        if col_idx != j:
                            sub_row.append(matrix[row_idx][col_idx])
                    submatrix.append(sub_row)

            minor_value = determinant(submatrix)
            cofactor_value = ((-1) ** (i + j)) * minor_value
            cofactor_row.append(cofactor_value)

        cofactor_matrix.append(cofactor_row)

    return cofactor_matrix


def determinant(matrix):
    """
    Calculate the determinant of a matrix.
    Helper function for cofactor calculation.
    """
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(n):
        minor_sub = []
        for i in range(1, n):
            minor_row = []
            for k in range(n):
                if k != j:
                    minor_row.append(matrix[i][k])
            minor_sub.append(minor_row)

        cofactor = ((-1) ** j) * matrix[0][j] * determinant(minor_sub)
        det += cofactor

    return det
