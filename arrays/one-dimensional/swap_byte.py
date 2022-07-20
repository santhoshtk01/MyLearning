# Program to change size of the item in the array
# TODO : Here I didn't see any change in the bytes
#  so make sure how to swap bytes using byteswap()
from array import *

even_values = array('i', [val for val in range(0, 11, 2)])
print("Before swapping - {0}".format(even_values.itemsize))

even_values.byteswap()

print("After swapping - {0}".format(even_values.itemsize))
