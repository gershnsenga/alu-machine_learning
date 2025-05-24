#!/usr/bin/env python3
"""
Add two 2D matrices element-wise.
This module provides a function to add two 2D matrices (lists of lists)
along corresponding elements.
"""


def add_matrices2D(mat1, mat2):
    """
    Add two 2D matrices element-wise.
    
    Args:
        mat1: First 2D matrix (list of lists containing ints/floats)
        mat2: Second 2D matrix (list of lists containing ints/floats)
        
    Returns:
        list: A new 2D matrix with element-wise sum, or None if shapes don't match
    """
    # Check if matrices have the same number of rows
    if len(mat1) != len(mat2):
        return None
    
    # Check if matrices have the same number of columns in each row
    for i in range(len(mat1)):
        if len(mat1[i]) != len(mat2[i]):
            return None
    
    # Create new matrix with element-wise addition
    result = []
    for i in range(len(mat1)):
        new_row = []
        for j in range(len(mat1[i])):
            new_row.append(mat1[i][j] + mat2[i][j])
        result.append(new_row)
    
    return result
