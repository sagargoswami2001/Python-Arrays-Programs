# Write a Python Program to Append Items from a Specified List.

from array import *
num_list = [1, 2, 6, -8]
array_num = array('i', [])
print("Items in the List: " + str(num_list))
print("Append Items from the List: ")
array_num.fromlist(num_list)
print("Items in the Array: " + str(array_num))
