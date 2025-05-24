#!/usr/bin/env python3
"""
Matrix multiplication using NumPy.
This module provides a function to perform matrix multiplication using NumPy.
"""


import numpy as np

def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication.
    
    Args:
        mat1: First matrix (numpy.ndarray)
        mat2: Second matrix (numpy.ndarray)
        
    Returns:
        numpy.ndarray: The result of matrix multiplication mat1 @ mat2
    """
    return np.matmul(mat1, mat2)
