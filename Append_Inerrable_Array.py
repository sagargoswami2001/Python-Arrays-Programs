# Write a Python Program to Append Items from Inerrable to the End of the Array.
from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original Array: " + str(array_num))
array_num.extend(array_num)
print("Extended Array: " + str(array_num))