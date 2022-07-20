# Input : test_tup = (3, 7, 1, 18, 9), k = 2
# Output : (3, 1, 9, 18)
# Input : test_tup = (3, 7, 1), k=1
# Output : (1, 3)


def extract_max(values: tuple, k: int) -> tuple:
    """
    Iterate through the tuple and remove `k` max elements and return a new
    tuple.
    Args:
        values: The tuple to be modified.
        k:  Number of maximum elements to be removed in the tuple `values`.

    Returns: The new modified tuple.

    """
    sorted_values = sorted(values)
    # for index in range(k):
    #     sorted_values.remove(max(sorted_values))
    sorted_values.remove(sorted_values.index(k))

    return tuple(sorted_values)


# Code to check my function
print(extract_max(k=2, values=(5, 20, 3, 7, 6, 8)))
