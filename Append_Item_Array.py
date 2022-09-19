# Write a Python Program to Append a new item to the end of the Array.
from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original Array: " + str(array_num))
print("Append 11 at the end of the Array: ")
array_num.append(11)
print("New Array: " + str(array_num))