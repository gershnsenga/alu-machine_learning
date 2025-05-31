#!/usr/bin/env python3
"""
Function that calculates the definiteness of a matrix
"""

import numpy as np


def definiteness(matrix):
    """
    Calculate the definiteness of a matrix.

    Args:
        matrix: A numpy.ndarray of shape (n, n) whose definiteness should be calculated

    Returns:
        A string indicating the definiteness: 'Positive definite', 'Positive semi-definite',
        'Negative semi-definite', 'Negative definite', 'Indefinite',
        or None if invalid

    Raises:
        TypeError: If matrix is not a numpy.ndarray
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if matrix.size == 0 or len(matrix.shape) != 2:
        return None

    if matrix.shape[0] != matrix.shape[1]:
        return None

    n = matrix.shape[0]

    if not np.allclose(matrix, matrix.T):
        return None

    try:
        eigenvalues = np.linalg.eigvals(matrix)
        tolerance = 1e-10

        positive_count = np.sum(eigenvalues > tolerance)
        negative_count = np.sum(eigenvalues < -tolerance)
        zero_count = np.sum(np.abs(eigenvalues) <= tolerance)

        if positive_count == n:
            return "Positive definite"
        elif positive_count + zero_count == n and zero_count > 0:
            return "Positive semi-definite"
        elif negative_count == n:
            return "Negative definite"
        elif negative_count + zero_count == n and zero_count > 0:
            return "Negative semi-definite"
        elif positive_count > 0 and negative_count > 0:
            return "Indefinite"
        else:
            return None

    except np.linalg.LinAlgError:
        return None
