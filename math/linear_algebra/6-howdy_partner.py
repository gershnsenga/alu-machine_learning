#!/usr/bin/env python3
"""
Concatenate two 2D matrices along a specified axis.
This module provides a function to concatenate two 2D matrices (lists of lists)
along a specified axis (0 for rows, 1 for columns).
"""


def cat_arrays(arr1, arr2):
    """
    Concatenate two arrays.
    Args:
        arr1: First array (list of ints/floats)
        arr2: Second array (list of ints/floats)
    Returns:
        list: A new list containing all elements from arr1 followed by all elements from arr2
    """
    # Create a new list by combining both arrays
    result = arr1 + arr2
    return result
