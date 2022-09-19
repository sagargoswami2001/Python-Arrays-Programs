# Write a Python Program to Remove a Specified Item Using the Index from an Array.
from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original Array: " + str(array_num))
print("Remove the Third Item from the Array: ")
array_num.pop(2)
print("New Array List: " + str(array_num))