#!python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

A = ['a', 'd']
B = ['c']
C = ['b', 'd', 'e']
D = ['a', 'c', 'd']


def jaccard(A, B):
    if(not A or not B):
        return len(A) if len(A) >= len(B) else len(B)
    else:
        return len(set(A).intersection(set(B)))/len(set(A).union(set(B)))
    
# test
print(jaccard([], []))
print(jaccard(A, B))
print(jaccard(A, C))
print(jaccard(A, D))
print(jaccard(B, C))
print(jaccard(D, B))
print(jaccard(C, D))
