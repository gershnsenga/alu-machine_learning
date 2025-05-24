#!/usr/bin/env python3
"""
Concatenate matrices
"""


def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
        mat1 (list): First matrix (nested list structure).
        mat2 (list): Second matrix (nested list structure).
        axis (int): The axis along which to concatenate (default: 0).

    Returns:
        list: A new matrix containing the concatenated matrices,
              or None if shapes are incompatible.
    """
    def get_shape(matrix):
        """Recursively get the shape of a nested list structure."""
        if not isinstance(matrix, list):
            return []
        shape = [len(matrix)]
        if matrix and isinstance(matrix[0], list):
            inner_shape = get_shape(matrix[0])
            for element in matrix:
                if get_shape(element) != inner_shape:
                    return None
            shape.extend(inner_shape)
        return shape

    def can_concatenate(shape1, shape2, axis):
        """Check if two shapes can be concatenated along the given axis."""
        if shape1 is None or shape2 is None:
            return False
        if len(shape1) != len(shape2):
            return False
        if axis >= len(shape1):
            return False
        for i in range(len(shape1)):
            if i != axis and shape1[i] != shape2[i]:
                return False
        return True

    def concatenate_recursive(m1, m2, current_axis, target_axis):
        """Recursively concatenate matrices along the target axis."""
        if current_axis == target_axis:
            if isinstance(m1, list) and isinstance(m2, list):
                return m1 + m2
            return None
        if not isinstance(m1, list) or not isinstance(m2, list):
            return None
        if len(m1) != len(m2):
            return None

        result = []
        for i in range(len(m1)):
            concatenated = concatenate_recursive(
                m1[i], m2[i], current_axis + 1, target_axis)
            if concatenated is None:
                return None
            result.append(concatenated)
        return result

    shape1 = get_shape(mat1)
    shape2 = get_shape(mat2)

    if not can_concatenate(shape1, shape2, axis):
        return None

    return concatenate_recursive(mat1, mat2, 0, axis)
