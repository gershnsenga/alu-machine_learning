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
        'Negative semi-definite', 'Negative definite', 'Indefinite', or None if invalid
        
    Raises:
        TypeError: If matrix is not a numpy.ndarray
    """
    # Check if matrix is a numpy.ndarray
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    
    # Check if matrix is valid (not empty and 2D)
    if matrix.size == 0 or len(matrix.shape) != 2:
        return None
    
    # Check if matrix is square
    if matrix.shape[0] != matrix.shape[1]:
        return None
    
    n = matrix.shape[0]
    
    # Check if matrix is symmetric (required for definiteness)
    if not np.allclose(matrix, matrix.T):
        return None
    
    try:
        # Calculate eigenvalues to determine definiteness
        eigenvalues = np.linalg.eigvals(matrix)
        
        # Handle numerical precision issues by using a small tolerance
        tolerance = 1e-10
        
        # Count positive, negative, and zero eigenvalues
        positive_count = np.sum(eigenvalues > tolerance)
        negative_count = np.sum(eigenvalues < -tolerance)
        zero_count = np.sum(np.abs(eigenvalues) <= tolerance)
        
        # Determine definiteness based on eigenvalues
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
        # Return None if eigenvalue computation fails
        return None
