# Write a Python Program to Remove the First Occurrence of a Specified Element from an Array.
from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original Array: " + str(array_num))
print("Remove the First Occurrence of 3 from the said Array:")
array_num.remove(3)
print("New Array List: " + str(array_num))
