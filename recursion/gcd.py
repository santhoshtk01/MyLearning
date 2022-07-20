# Recursive function to find GCD of given numbers
# We can use the Euclidean Algorithm to find GCD

def greatest_com_div(a: int, b: int):
    if a == 0:
        return b
    else:
        # Recursive case
        return greatest_com_div(b % a, a)


# Code to check my function
print(greatest_com_div(10, 15))
