#!/usr/bin/env python3
"""
Matrix multiplication using NumPy.

This module provides a function to perform matrix multiplication using NumPy.
"""

import numpy as np


def np_matmul(mat1, mat2):
    """
    Perform matrix multiplication using NumPy.

    Args:
        mat1 (numpy.ndarray): First matrix
        mat2 (numpy.ndarray): Second matrix

    Returns:
        numpy.ndarray: The result of matrix multiplication mat1 @ mat2
    """
    return np.matmul(mat1, mat2)
