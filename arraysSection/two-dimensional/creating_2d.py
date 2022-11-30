# Program to create a 2D array using numpy module
import numpy as np

two_d_array = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
])

# The below will raise errors because in 3rd row
# it has only 4 columns not 5
# two_d_array = np.array([
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14]
# ])
print(two_d_array)