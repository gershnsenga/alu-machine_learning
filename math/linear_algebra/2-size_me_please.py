#!/usr/bin/env python3

def matrix_shape(matrix):
    """
    Calculate the shape of a matrix (nested list structure).
    
    Args:
        matrix: A nested list structure representing a matrix
        
    Returns:
        list: A list of integers representing the dimensions of the matrix
    """
    shape = []
    current = matrix
    
    # Keep drilling down into the structure until we reach a non-list element
    while isinstance(current, list):
        shape.append(len(current))
        if len(current) > 0:
            current = current[0]  # Move to the first element of current dimension
        else:
            break  # Handle empty lists
    
    return shape
