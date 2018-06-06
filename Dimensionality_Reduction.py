#!python3

import numpy as np
import pandas as pd

M = np.matrix([[1, 1], [2, 4], [3, 9], [4, 6]])
# print("M is:\n{}".format(M))

#(a)
print("M*M.T is:\n{}".format(np.matmul(M.T, M)))
print("M.T*M is:\n{}".format(np.matmul(M, M.T)))
#(b)
w, v = np.linalg.eig(np.matmul(M.T, M))
print("Eigenvalues w1 of M.T*M is: {}".format(w[0]))
print("Eigenvectors v1 of M.T*M is: {}".format(v.T[0]))
print("Eigenvalues w2 of M.T*M is: {}".format(w[1]))
print("Eigenvectors v2 of M.T*M is: {}".format(v.T[1]))
#(c)
w2, v2 = np.linalg.eig(np.matmul(M, M.T))
print("Eigenvalues w1, w2 and w3 of M*M.T is: {:.3f}, {:.3f}, {:.3f}".format(w2[0], w2[1], w2[3]))
#(d)
print("Eigenvalues w1, w2, w3, w4 of M*M.T is:\n {}".format(v2))

#SVD
A = np.matrix([[1, 1], [1, 1], [0, 0]])
print(A)
w3, v3 = np.linalg.eig(np.matmul(A, A.T))
w4, v4 = np.linalg.eig(np.matmul(A.T, A))
w3 = sorted(w3, reverse=True)
print(w3)
print(w4)
print(v3)
print(v4)
S = np.matrix([[w3[0]**0.5, 0.], [0., w3[1]**0.5]])
print("U is:\n{}".format(v3))
print("S is:\n{}".format(S))
print("V is:\n{}".format(v4.T))
#verifying
print("SVD is:\n{}".format(np.linalg.svd(A)))