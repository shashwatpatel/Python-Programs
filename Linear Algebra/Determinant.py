import numpy as x
#Linalg for performing various linear algebra functions
from numpy import linalg 
#Define 2D array (Can be edited)
a = x.array([[1, 0], [1, 2]])
#Print given array
print('Given array: ')
print(a)
#Print result after taking the determinant
print('Determinant of the array: ')
print(x.linalg.det(a))