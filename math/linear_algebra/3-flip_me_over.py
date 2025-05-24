#!/usr/bin/env python3
def matrix_transpose(matrix):
    """
    Return the transpose of a 2D matrix.
    
    Args:
        matrix: A 2D list representing a matrix
        
    Returns:
        list: A new 2D list representing the transposed matrix
    """
    # Get dimensions of the original matrix
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create new matrix with swapped dimensions
    transposed = []
    
    # For each column in the original matrix
    for col in range(cols):
        new_row = []
        # For each row in the original matrix
        for row in range(rows):
            new_row.append(matrix[row][col])
        transposed.append(new_row)
    
    return transposed