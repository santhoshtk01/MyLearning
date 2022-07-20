# Recursive function to find power of a given number
# The `power` function below is written by me because of
# misunderstanding of the power of numbers problem but it might be useful
# for some problems I hope so..
def power(number: int):
    """
    Returns the exponent of a number for power of `2`
    :param number: number to be processed
    :return: Exponent of the number
    """
    count = 0
    if number == 2:
        return 1
    else:
        count += 1
        return count + power(number // 2)


# Recursive function to find power of a given number
def power_num(number: int, exponent: int):
    if exponent == 0 or exponent == 1:
        return number
    else:
        return number * power_num(number, exponent - 1)


# Code to check the function
print(power_num(2, 5))