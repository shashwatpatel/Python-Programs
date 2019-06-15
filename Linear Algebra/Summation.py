import numpy as x
#Initialize arrays
a = x.array([1,2,3])
b = x.array([0,1,0])
#Print given arrays
print('Given arrays: ')
print(a)
print(b)
#Get Einstein's summation and print it
sol = x.einsum("n,n", a, b)
print('Einstein summation convention of arrays: ')
print(sol)
#Get higher dimension of same array and print it
p = x.arange(9).reshape(3, 3)
q = x.arange(3, 12).reshape(3, 3)
print('Higher dimension: ')
print(p)
print(q)
#Compute Einstein's summation and print it
res = x.einsum("mk,kn", p, q)
print('Einstein summation convention of arrays: ')
print(res)
