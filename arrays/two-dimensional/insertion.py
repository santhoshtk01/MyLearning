# Program to insert values to the 2D array
"""
We can insert values to 2D array in two ways.
1. Addition of rows and
2. Addition of columns.

NOTE : We can't insert one values or two values
[0, 0, 0]
[1, 1, 1]
[0, 1, 0]

[0, 0, 0, 0]
[1, 1, 1]
[0, 1, 0]
"""
import numpy as np

two_d_array = np.array([
    [0, 0, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 0, 0]
])
# Adding columns to the 2D array
new_twoDarray = np.insert(two_d_array, 0, [[0, 0, 0]], axis=1)
print(new_twoDarray)

# Adding rows to the 2D array
new_twoDarray = np.insert(new_twoDarray, 0, [[0, 0, 0, 0, 0]], axis=0)
print(new_twoDarray)

# Adding rows and columns at the end
print("Two Dimensional Array - {0}".format(two_d_array))
# two_d_array = np.append(two_d_array, [[0, 0, 0]], axis=1)
two_d_array = np.insert(two_d_array, 4, [[0, 0, 0]], axis=1)
print(two_d_array)
