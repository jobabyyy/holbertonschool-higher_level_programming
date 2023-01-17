#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same dimensions as the input matrix
    n_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            n_matrix[i][j] = matrix[i][j] ** 2
    # Return the new matrix
    return n_matrix
