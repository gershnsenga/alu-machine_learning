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
        mat1: First 2D matrix (list of lists)
        mat2: Second 2D matrix (list of lists)
        axis: Axis along which to concatenate (0 for rows, 1 for columns)
        
    Returns:
        list: A new 2D matrix with concatenated matrices, or None if incompatible shapes
    """
    if axis == 0:
        # Concatenate along rows (stack vertically)
        # Check if both matrices have the same number of columns
        if len(mat1[0]) != len(mat2[0]):
            return None
        
        # Create new matrix by copying all rows from both matrices
        result = []
        for row in mat1:
            result.append(row[:])  # Create a copy of each row
        for row in mat2:
            result.append(row[:])  # Create a copy of each row
        
        return result
    
    elif axis == 1:
        # Concatenate along columns (stack horizontally)
        # Check if both matrices have the same number of rows
        if len(mat1) != len(mat2):
            return None
        
        # Create new matrix by concatenating corresponding rows
        result = []
        for i in range(len(mat1)):
            new_row = mat1[i][:] + mat2[i][:]  # Copy and concatenate rows
            result.append(new_row)
        
        return result
    
    else:
        return None
    