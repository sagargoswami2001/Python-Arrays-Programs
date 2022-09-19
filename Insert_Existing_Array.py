# Write a Python Program to Insert a New Item Before the Second Element in an Existing Array.
from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original Array: " + str(array_num))
print("Insert New Value 4 Before 3: ")
array_num.insert(1, 4)
print("New Array: " + str(array_num))