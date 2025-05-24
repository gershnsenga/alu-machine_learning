#!/usr/bin/env python3
"""
Concatenate two 2D matrices along a specified axis.

This module provides a function to concatenate two 2D matrices (lists of lists)
along a specified axis (0 for rows, 1 for columns).
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenate two 2D matrices along a specified axis.

    Args:
        mat1 (list of list): First 2D matrix
        mat2 (list of list): Second 2D matrix
        axis (int): Axis along which to concatenate (0 for rows, 1 for columns)

    Returns:
        list: A new 2D matrix with concatenated matrices, or None if incompatible shapes
    """
    if axis == 0:
        # Concatenate along rows (stack vertically)
        if len(mat1[0]) != len(mat2[0]):
            return None
        result = [row[:] for row in mat1] + [row[:] for row in mat2]
        return result

    if axis == 1:
        # Concatenate along columns (stack horizontally)
        if len(mat1) != len(mat2):
            return None
        result = [mat1[i][:] + mat2[i][:] for i in range(len(mat1))]
        return result

    return None
