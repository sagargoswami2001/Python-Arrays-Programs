# Write a Python Program to Convert an Array to an Ordinary List with the Same Items.
from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original Array: " + str(array_num))
num_list = array_num.tolist()
print("Convert the Said Array to an Ordinary List with the Same Items:")
print(num_list)
