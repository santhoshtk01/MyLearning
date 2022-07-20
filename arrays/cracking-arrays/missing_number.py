# Program to find a missing number in an Array
from array import *


def findMissing(values, n: int) -> int:
    """
    Finds a missing element in the given array and return it.
    Args:
        values: The array to be processed
        n: Length of the array.

    Returns: Missing number in the array.

    """
    sum1 = n * (n + 1) // 2
    sum2 = sum(values)

    return sum1 - sum2


# Code to check my function
# Here adding 1 with the length is because
# if the list contains 0 we don't need to add 1
values = [1, 2, 3, 5]
print(findMissing(values, len(values) + 1))
