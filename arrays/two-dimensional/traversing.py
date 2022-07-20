# Program to traverse through a 2D array
import numpy as np

new_array = np.array([
    [10, 101, 11, 1],
    [110, 111, 100, 51],
    [70, 80, 90, 91],
    [41, 51, 31, 30]
])


def traverse(array):
    # Traversing through the array
    for row in array:
        for val in row:
            print(val, end='')
        print()


def search(array: np.array, target: int) -> tuple or str:
    # Iterating rows
    for row in range(len(array)):
        if target in array[row]:
            # Iterating each columns
            for val in range(len(array[row])):
                if array[row][val] == target:
                    return row, val

    return "Requested element is not in the array"


print(search(new_array, 100))
