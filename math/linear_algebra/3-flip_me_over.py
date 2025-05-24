#!/usr/bin/env python3
"""
Transpose a 2D matrix.

This module provides a function to return the transpose of a 2D matrix.
"""


def matrix_transpose(matrix):
    """
    Return the transpose of a 2D matrix.

    Args:
        matrix (list): A 2D list representing a matrix

    Returns:
        list: A new 2D list representing the transposed matrix
    """
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = []

    for col in range(cols):
        new_row = []
        for row in range(rows):
            new_row.append(matrix[row][col])
        transposed.append(new_row)

    return transposed
