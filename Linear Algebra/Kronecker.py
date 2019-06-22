import numpy as x
#Define 1D array and print it (Can be changed)
p = x.array([1, 2, 3])
q = x.array([0, 1, 0])
print("Given 1D arrary: ")
print(p)
print(q)
#Take the kronecker product and print the result
prod = x.kron(p, q)
print("Kronecker product is: ")
print(prod)
#Get the higher dimension array and take the kronecker product
a = x.arange(9).reshape(3, 3)
b = x.arange(3, 12).reshape(3, 3)
print("Higher dimension array: ")
print(a)
print(b)
#Print final result
sol =  x.kron(a, b)
print("Kronecker product of higher dimension array is: ")
print(sol)
