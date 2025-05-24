#!/usr/bin/env python3
"""
Multiply two matrices together.

This module provides a function to perform matrix multiplication on
two 2D matrices (lists of lists).
"""


def mat_mul(mat1, mat2):
    """
    Perform matrix multiplication of two 2D matrices.

    Args:
        mat1 (list of list): First 2D matrix (list of lists containing ints/floats)
        mat2 (list of list): Second 2D matrix (list of lists containing ints/floats)

    Returns:
        list: A new 2D matrix representing the product,
              or None if multiplication is not possible
    """
    rows_mat1 = len(mat1)
    cols_mat1 = len(mat1[0])
    rows_mat2 = len(mat2)
    cols_mat2 = len(mat2[0])

    # Check if matrices can be multiplied
    if cols_mat1 != rows_mat2:
        return None

    result = []
    for i in range(rows_mat1):
        new_row = []
        for j in range(cols_mat2):
            dot_product = sum(mat1[i][k] * mat2[k][j] for k in range(cols_mat1))
            new_row.append(dot_product)
        result.append(new_row)

    return result
