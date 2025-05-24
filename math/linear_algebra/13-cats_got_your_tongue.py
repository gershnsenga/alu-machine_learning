#!/usr/bin/env python3
"""
Concatenate two 2D matrices along a specified axis.
This module provides a function to concatenate two 2D matrices (lists of lists)
along a specified axis (0 for rows, 1 for columns).
"""


import numpy as np

def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.
    
    Args:
        mat1: First matrix (numpy.ndarray or convertible to numpy.ndarray)
        mat2: Second matrix (numpy.ndarray or convertible to numpy.ndarray)
        axis: The axis along which to concatenate (default: 0)
        
    Returns:
        numpy.ndarray: A new array containing the concatenated matrices
    """
    # Convert inputs to numpy arrays
    mat1 = np.array(mat1)
    mat2 = np.array(mat2)
    
    # Concatenate along the specified axis
    return np.concatenate((mat1, mat2), axis=axis)
