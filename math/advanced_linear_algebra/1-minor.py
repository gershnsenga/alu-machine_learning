#!/usr/bin/env python3
"""
Function that calculates the minor matrix of a given matrix
"""


def minor(matrix):
    """
    Calculate the minor matrix of a matrix.
    
    Args:
        matrix: A list of lists representing a square matrix
        
    Returns:
        The minor matrix of the input matrix
        
    Raises:
        TypeError: If matrix is not a list of lists
        ValueError: If matrix is not a non-empty square matrix
    """
    # Check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    
    # Check if matrix is empty
    if len(matrix) == 0:
        raise ValueError("matrix must be a non-empty square matrix")
    
    # Check if matrix is a list of lists
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    
    # Check if matrix is square and non-empty
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a non-empty square matrix")
    
    # Handle 1x1 matrix case
    if n == 1:
        return [[1]]
    
    # Calculate minor matrix
    minor_matrix = []
    
    for i in range(n):
        minor_row = []
        for j in range(n):
            # Create submatrix by removing row i and column j
            submatrix = []
            for row_idx in range(n):
                if row_idx != i:
                    sub_row = []
                    for col_idx in range(n):
                        if col_idx != j:
                            sub_row.append(matrix[row_idx][col_idx])
                    submatrix.append(sub_row)
            
            # Calculate determinant of submatrix
            minor_value = determinant(submatrix)
            minor_row.append(minor_value)
        
        minor_matrix.append(minor_row)
    
    return minor_matrix


def determinant(matrix):
    """
    Calculate the determinant of a matrix.
    Helper function for minor calculation.
    """
    n = len(matrix)
    
    # Base cases
    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Recursive case using cofactor expansion along the first row
    det = 0
    for j in range(n):
        # Create minor matrix by removing row 0 and column j
        minor_sub = []
        for i in range(1, n):
            minor_row = []
            for k in range(n):
                if k != j:
                    minor_row.append(matrix[i][k])
            minor_sub.append(minor_row)
        
        # Calculate cofactor and add to determinant
        cofactor = ((-1) ** j) * matrix[0][j] * determinant(minor_sub)
        det += cofactor
    
    return det
