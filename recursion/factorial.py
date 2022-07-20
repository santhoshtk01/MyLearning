# Recursive program to calculate factorial for a given number

def fact(number: int):

    assert number > 0, "Invalid Number, The number should be positive integer"
    # if number < 0:
    #     raise AssertionError('Invalid Number, The number should be positive integer')

    if number == 1:
        return number
    else:
        return number * fact(number - 1)


# Driver Code
print(fact(5))
