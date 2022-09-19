# Write a Python Program to Convert an Array to an Array of Machine Values and Return the Bytes Representation.
from array import *
print("Bytes to String: ")
x = array('b', [119, 51, 114, 101, 115, 111, 117, 114, 99, 101])
s = x.tobytes()
print(s)
