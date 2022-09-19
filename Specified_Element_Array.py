# Write a Python Program to get the number of Occurrences of a Specified Element in an Array.
from array import *
array_num = array('i', [1,3,5,3,7,9,3])
print("Original Array: " + str(array_num))
print("Number of Occurrences of the Number 3 in the Said Array: " + str(array_num.count(3)))
