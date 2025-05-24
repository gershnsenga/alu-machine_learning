#!/usr/bin/env python3
"""
Add arrays element-wise.
This module provides a function to add two arrays element-wise.
"""


def add_arrays(arr1, arr2):
    
    
    """
    Add two arrays element-wise.
    Args:
        arr1: First array (list of ints/floats)
        arr2: Second array (list of ints/floats)
    Returns:
        list: A new list with element-wise sum, or None if shapes don't match
    """
    # Check if arrays have the same length
    if len(arr1) != len(arr2):
        return None
    # Create new array with element-wise addition
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
    return result
