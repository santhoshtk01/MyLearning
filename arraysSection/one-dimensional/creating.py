# Program to perform basic operations in array
from array import *

# Creating array of integers
integer_array = array('i', [val for (val) in range(1, 11)])

# Traversing through the array
for value in integer_array:
    print(value, end=" ")
print()

# Printing all typecode available in the array object
print(typecodes)

# Itemsize by the internal representation
print(integer_array.itemsize)