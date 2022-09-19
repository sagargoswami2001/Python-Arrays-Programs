# Write a Python Program to Reverse the Order of the items in the Array.
from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original Array: " + str(array_num))
array_num.reverse()
print("Reverse the Order of the Items: ")
print(str(array_num))