import numpy as x
#Define a matrix (Can be changed) and print it
a = x.matrix([[1, 2], [3, 4]])
print("Given matrix: ")
print(a)
#Take the determinant and print the result (rounding up)
result = x.linalg.det(a)
print("The result is: ")
print(round(result))