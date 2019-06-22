import numpy as x
#Define matrix/squared array (Can be changed)
a = x.mat("3 -2;1 0")
#Print the given matrix
print('Givwn matrix: ')
print("a\n", a)
#Perform operations to get the eigenvalues and eigenvectors and print them
p, q = x.linalg.eig(a)
print('Eigenvalues of given matrix ', p)
print('Eigenvectors of given matrix ', q)
