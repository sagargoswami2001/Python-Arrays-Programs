# Write a Python Program to get the length in bytes of one array item in the Internal Representation.

from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original Array: " + str(array_num))
print("Length in Bytes of One Array Item: " + str(array_num.itemsize))
