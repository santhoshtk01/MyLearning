import numpy as np


def rotate_matrix(matrix):
    """rotates a matrix 90 degrees clockwise"""
    n = len(matrix)
    for layer in range(n // 2):
        # To find the layers of the array. (How many iterations to do)
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i] 

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix


new_array = np.array([[1, 2, 3, 121], [4, 5, 6, 122], [7, 8, 9, 123], [10, 11, 12, 124]])
print(new_array)
print(rotate_matrix(new_array))
