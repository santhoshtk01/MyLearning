from array import *

# TODO : Most of the operations are done here.
#  Pending : extend() and converting to string.

odd_values = [val for val in range(1, 10, 2)]
even_values = array('i', [val for val in range(0, 11, 2)])

even_values.fromlist(odd_values)
print("Before Conversion - {0}".format(even_values))

# Converting an array to the python's list
converted_list = even_values.tolist()
print("After conversion - {0}".format(converted_list))

# Find index of the item 8 in the even_values array
print("Index position - {0}".format(even_values.index(8)))

# Insert 100 to the array even_values in index position 0
even_values.insert(0, 100)
print("Updates even_arrays - {0}".format(even_values))

# Popping out the last element in the even_values array
print(even_values.pop())

# Removing an element from the array
to_remove = 100
even_values.remove(to_remove)
print("Removed 100 - {0}".format(even_values))
