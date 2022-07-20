# Recursive function to convert decimal to binary

def decimal_binary(number: int):
    if number // 2 == 0:
        return number % 2
    else:
        num = decimal_binary(number // 2)
        return num * 10 + (number % 2)


# Code to check my function
print(decimal_binary(20))
