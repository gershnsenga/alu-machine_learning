#!/usr/bin/env python3
if __name__ == "__main__":
    
    # Matrix shape
    print("\nMatrix shape:\n------------")
    matrix_shape = __import__('2-size_me_please').matrix_shape

    mat1 = [[1, 2], [3, 4]]
    print(matrix_shape(mat1))
    mat2 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
            [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]]
    print(matrix_shape(mat2))
    
    # Transpose of a matrix
    print("\nTranspose of a matrix:\n-----------------------")
    matrix_transpose = __import__('3-flip_me_over').matrix_transpose

    mat1 = [[1, 2], [3, 4]]
    print(mat1)
    print(matrix_transpose(mat1))
    mat2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
    print(mat2)
    print(matrix_transpose(mat2))
    
    # Arrays addition
    print("\nArrays addition:\n---------------")
    add_arrays = __import__('4-line_up').add_arrays  # Importing the function from 4-line_up.py
    
    arr1 = [1, 2, 3, 4]
    arr2 = [5, 6, 7, 8]
    print(add_arrays(arr1, arr2))
    print(arr1)
    print(arr2)
    print(add_arrays(arr1, [1, 2, 3]))
    
    # Add matrices
    print("\nAdd matrices:\n---------------")
    add_matrices2D = __import__('5-across_the_planes').add_matrices2D

    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    print(add_matrices2D(mat1, mat2))
    print(mat1)
    print(mat2)
    print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))