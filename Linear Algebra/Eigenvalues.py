import numpy as x
a = x.mat("3 -2;1 0")
print('Givwn matrix: ')
print("a\n", a)
p, q = x.linalg.eig(a)
print('Eigenvalues of given matrix ', p)
print('Eigenvectors of given matrix ', q)
