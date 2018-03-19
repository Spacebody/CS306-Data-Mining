#!python3
 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import fsum, fabs

indice = ['A', 'B', 'C', 'D', 'E']

# page links record
M = pd.DataFrame({'A': pd.Series([0., 1/3., 1/3., 1/3., 0.], index=indice),
                  'B': pd.Series([0., 0., 0., .5, .5], index=indice),
                  'C': pd.Series([0., 0., 0., 0., 1], index=indice),
                  'D': pd.Series([0., 0., 0., 0., 1], index=indice),
                  'E': pd.Series([1., 0., 0., 0., 0.], index=indice)})

alpha = 0.8
N = M.shape[1]
Max = 100
delta = 1e-10


R = (1 / N) * pd.DataFrame([1.,1.,1.,1.,1.], index=indice)
for i in range(100):
    pre_R = R
    R = ((1-alpha) / N) * \
        pd.DataFrame([1., 1., 1., 1., 1.], index=indice) + alpha * M.dot(R)
    if(float(abs(pre_R-R).sum(axis=0)) <= delta):
        break
print("delta: {}".format(delta))
print("Ietration: {}".format(i))
print("R:")
print(R[0])
