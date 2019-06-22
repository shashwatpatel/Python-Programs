import numpy as x
#Define vector and take the normal
a = x.arange(7)
sol = x.linalg.norm(a)
print("Vector normal: ")
print(sol)
#Deifne matrix and take the normal
b = x.matrix('1, 2; 3, 4')
sol2 = x.linalg.norm(b)
print("Matrix normal: ")
print(sol2)