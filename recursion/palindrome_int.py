# Recursive function to find given number is palindrome or not
# Author : T.K.Santhosh
# Created : Feb 20, 2022
def is_palindrome(number: int, val):
    value = val
    original = number

    if number == 0:
        return value == original
    else:
        value = value * 10 + number % 10
        return is_palindrome(number // 10, value)


print(is_palindrome(000, 0))
