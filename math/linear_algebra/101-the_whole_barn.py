#!/usr/bin/env python3
"""
Add matrices
"""


def add_matrices(mat1, mat2):
    """
    Adds two matrices of arbitrary dimensions.

    Args:
        mat1: First matrix (list of lists, potentially nested)
        mat2: Second matrix (list of lists, potentially nested)

    Returns:
        list: A new matrix containing the element-wise sum,
              or None if shapes do not match.
    """
    def get_shape(matrix):
        """Recursively get the shape of a nested list structure."""
        if not isinstance(matrix, list):
            return []
        if not matrix:
            return [0]
        shape = [len(matrix)]
        if isinstance(matrix[0], list):
            inner_shape = get_shape(matrix[0])
            for element in matrix:
                if get_shape(element) != inner_shape:
                    return None
            shape.extend(inner_shape)
        return shape

    def add_recursive(m1, m2):
        """Recursively add matrices element by element."""
        if not isinstance(m1, list) and not isinstance(m2, list):
            return m1 + m2
        if isinstance(m1, list) != isinstance(m2, list):
            return None
        if len(m1) != len(m2):
            return None

        result = []
        for i in range(len(m1)):
            element_sum = add_recursive(m1[i], m2[i])
            if element_sum is None:
                return None
            result.append(element_sum)
        return result

    shape1 = get_shape(mat1)
    shape2 = get_shape(mat2)

    if shape1 is None or shape2 is None or shape1 != shape2:
        return None

    return add_recursive(mat1, mat2)
