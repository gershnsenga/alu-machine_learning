
#!/usr/bin/env python3
"""
Find a shape of a numpy.ndarray.
"""
import numpy as np
def np_shape(matrix):
    """
    Calculate the shape of a numpy.ndarray.
    
    Args:
        matrix: A numpy.ndarray
        
    Returns:
        tuple: A tuple of integers representing the shape of the matrix
    """
    return matrix.shape