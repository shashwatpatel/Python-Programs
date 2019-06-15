import numpy as x
#Initialize array (Can be edited)
a = x.array([1,2,5])
b = x.array([2,1,0])
#Print given array
print('Given array: ')
print(a)
print(b)
#Compute inner product and print the solution
sol = x.inner(a, b)
print('Inner product of vectors: ')
print(sol)
#Get higher dimension arrays and print them
p = x.arange(9).reshape(3, 3)
q = x.arange(3, 12).reshape(3, 3)
print('Higher dimenstion arrays: ')
print(p)
print(q)
#Compute inner product of higher dimension and print it
res = x.inner(p, q)
print('Inner product of vectors: ')
print(res)
