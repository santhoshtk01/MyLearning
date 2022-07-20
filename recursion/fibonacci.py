# Recursive function to generate fibonacci series
# for a given number

def fibonacci(num):
    assert num > 1 or type(num) is not float, 'Invalid number, The number should be positive integer'
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


# Code to check my function
# Code to print each fibonacci number
number = int(input("Enter a number :"))
for index in range(1, number + 1):
    print(fibonacci(index))