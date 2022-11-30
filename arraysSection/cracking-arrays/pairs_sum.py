# Program to find a pair their sum equals to the target value
# NOTE : The pair must have distinct element (3, 3) is not valid pair.


def findPairs(values, target: int) -> tuple or str:
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] + values[j] == target and values[i] != values[j]:
                return i, j

    return "There is no pair of numbers their sum equals to target"


# Code to check my function
print(findPairs([1], 1))