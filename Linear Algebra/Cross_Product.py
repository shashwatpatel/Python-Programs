import numpy as x
#Initialize matrix (Can be edited)
a = [[1, 0], [0, 1]]
b = [[1, 2], [3, 4]]
#Print given matrix
print("Given Matrix: ")
print(a)
print(b)
#Computing cross product both ways and printing solution
sol1 = x.cross(a, b)
sol2 = x.cross(b, a)
print('Cross product of a and b: ')
print(sol1)
print('Cross product of b and a: ')
print(sol2)