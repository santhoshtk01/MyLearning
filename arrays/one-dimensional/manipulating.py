# Program to perform simple manipulations in the array
from array import *

values = array('i', [val for val in range(10, 101, 10)])
print(values)

# Appending values to the array `values`
values.append(110)
print(values)

# Using buffer_info method
print(values.buffer_info())

# Calculating size of memory buffer
address = values.buffer_info()[0]
item_size = values.itemsize
print("Memory buffer size - {0}".format(address * item_size))