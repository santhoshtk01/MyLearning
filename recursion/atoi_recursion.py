# Program to implement atoi() function recursively
# TODO : I am not sure this is an optimal solution
#  so try to find the optimal solution.

def atoi(string: str, integer_value: int):
    integer_value = integer_value
    if not string:
        return integer_value
    else:
        integer_value = integer_value * 10 + int(string[0])
        return atoi(string[1:], integer_value)


# Code to check my function
print(atoi('121', 0))
