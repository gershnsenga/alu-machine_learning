#!/usr/bin/env python3
"""
Addition, subtraction, multiplication, and division of two matrices.

This module provides a function to perform element-wise addition, subtraction,
multiplication, and division of two matrices (lists of lists).
"""


def np_elementwise(mat1, mat2):
    """
    Perform element-wise addition, subtraction, multiplication, and division.

    Args:
        mat1 (numpy.ndarray): First matrix (or convertible to numpy.ndarray)
        mat2 (numpy.ndarray): Second matrix (or convertible to numpy.ndarray)

    Returns:
        tuple: A tuple containing (sum, difference, product, quotient)
    """
    
    addition = mat1 + mat2
    subtraction = mat1 - mat2
    multiplication = mat1 * mat2
    division = mat1 / mat2

    return addition, subtraction, multiplication, division
