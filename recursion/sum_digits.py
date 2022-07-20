# Recursive function to sum the digits of the given number

def sum_digits(number: int):

    assert number >= 0 and type(number) is not float, 'Invalid number, The number should be positive integer'

    if number // 10 <= 0:
        return number
    else:
        remin = number % 10
        return remin + sum_digits(number // 10)


# Code to check my function
print(sum_digits(1.2))
