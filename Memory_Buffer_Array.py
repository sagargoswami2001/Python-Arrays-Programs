''' Write a Python Program to get the current memory address and the length in elements of the buffer used to 
hold an array's contents and also find the size of the memory buffer in bytes. '''

from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original Array: " + str(array_num))
print("Current Memory Address and the length in elements of the Buffer: " + str(array_num.buffer_info()))
print("The Size of the Memory Buffer in Bytes: " + str(array_num.buffer_info()[1] * array_num.itemsize))
