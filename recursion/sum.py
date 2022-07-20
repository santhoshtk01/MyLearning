# Recursive function to return sum of a specific interval

def sum_(number: int):
    assert number >= 0, 'Invalid number, The number should be positive integer'
    if number == 0:
        return number
    else:
        return number + sum_(number - 1)


# Code to test my function
print(sum_(10))
