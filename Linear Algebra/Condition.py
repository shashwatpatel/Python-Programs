import numpy as x
from numpy import linalg as l
#Define matrix (Can be changed) and print it
p = x.array([[1, 0, -1], [0, 1, 0], [1, 0, 1]])
print("Given matrix: ")
print(p)
#Take the condition of the matrix and print the result
print("The condition of given matrix is: ")
print(l.cond(p))
