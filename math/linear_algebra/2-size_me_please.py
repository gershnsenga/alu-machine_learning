#!/usr/bin/env python3
"""
Determine the shape of a matrix (nested list structure).
"""


def matrix_shape(matrix):
    """
    Calculate the shape of a matrix (nested list structure).

    Args:
        matrix (list): A nested list representing a matrix

    Returns:
        list: A list of integers representing the dimensions of the matrix
    """
    shape = []
    current = matrix

    while isinstance(current, list):
        shape.append(len(current))
        if len(current) > 0:
            current = current[0]
        else:
            break

    return shape
