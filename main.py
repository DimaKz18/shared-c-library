import ctypes
import os
from sys import platform

if platform == 'darwin' or platform == "linux" or platform == "linux2":
    clibrary = ctypes.cdll.LoadLibrary('./clibrary.so')
if platform == "win32":
    clibrary = ctypes.cdll.LoadLibrary('./clibrary.dll')

clibrary.addIntNumbers.argtypes = [ctypes.c_int, ctypes.c_int]
clibrary.addIntNumbers.restype = ctypes.c_int
sum = clibrary.addIntNumbers(2, 3)

clibrary.subtractDoubleNumbers.argtypes = [ctypes.c_double, ctypes.c_double]
clibrary.subtractDoubleNumbers.restype = ctypes.c_double
subtraction = clibrary.subtractDoubleNumbers(10.5, 5.0)

clibrary.divideFloatNumbers.argtypes = [ctypes.c_float, ctypes.c_float]
clibrary.divideFloatNumbers.restype = ctypes.c_float
division = clibrary.divideFloatNumbers(14.5, 4.3)

print(sum)
print(subtraction)
print(division)
clibrary.printSomeText(b"Some text from python")
