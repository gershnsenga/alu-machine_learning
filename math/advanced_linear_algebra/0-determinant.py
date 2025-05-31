#!/usr/env/bin python3
""""
 function that calculates the determinant of a matrix
"""


def determinant(matrix):
    """
    Calculate the determinant of a matrix.
    
    Args:
        matrix: A list of lists representing a square matrix
        
    Returns:
        The determinant of the matrix
        
    Raises:
        TypeError: If matrix is not a list of lists
        ValueError: If matrix is not square
    """
    # Check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    
    # Check if matrix is a list of lists
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    
    # Handle empty matrix case
    if len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    
    # Handle 0x0 matrix case [[]]
    if len(matrix) == 1 and len(matrix[0]) == 0:
        return 1
    
    # Check if matrix is square
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a square matrix")
    
    # Base cases
    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Recursive case using cofactor expansion along the first row
    det = 0
    for j in range(n):
        # Create minor matrix by removing row 0 and column j
        minor = []
        for i in range(1, n):
            minor_row = []
            for k in range(n):
                if k != j:
                    minor_row.append(matrix[i][k])
            minor.append(minor_row)
        
        # Calculate cofactor and add to determinant
        cofactor = ((-1) ** j) * matrix[0][j] * determinant(minor)
        det += cofactor
    
    return det