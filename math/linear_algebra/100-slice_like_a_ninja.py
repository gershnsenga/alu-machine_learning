#!/usr/bin/env python3
"""
Slice a matrix like a ninja.
"""


def np_slice(matrix, axes={}):
    """
    Slices a matrix along specific axes.

    Args:
        matrix (numpy.ndarray): The array to slice.
        axes (dict): Keys are axis indices, values are tuples defining 
                     slices (start, stop[, step]) for that axis.

    Returns:
        numpy.ndarray: A new array with the specified slices applied.
    """
    # Initialize list of slices for each dimension
    slices = [slice(None)] * matrix.ndim

    # Update slices for specified axes
    for axis, slice_tuple in axes.items():
        slices[axis] = slice(*slice_tuple)

    return matrix[tuple(slices)]
