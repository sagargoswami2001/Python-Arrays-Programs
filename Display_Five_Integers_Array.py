''' Write a Python Program to create an array of 5 integers and display the array items. Access individual 
element through indexes. '''

from array import *
array_num = array('i', [1,3,5,7,9])
for i in array_num:
    print(i)
print("Access First Three Items Individually:")
print(array_num[0])
print(array_num[1])
print(array_num[2])