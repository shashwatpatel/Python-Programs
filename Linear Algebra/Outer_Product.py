import numpy as x
#Initialize the matrix (Can be edited)
a = [[1, 0], [0, 1]]
b = [[1, 2], [3, 4]]
#Print given matrix
print('Given Matrix: ')
print(a)
print(b)
#Compute the outer product and print the result
outer = x.outer(a, b)
print("Result after outer product is: ")
print(outer)
