#!python3

import pandas as pd
import numpy as np

# hash functions
def h1(s):
    return pd.Series((2*x+1)%6 for x in range(len(s)))

def h2(s):
    return pd.Series((3*x+2) % 6 for x in range(len(s)))

def h3(s):
    return pd.Series((5*x+2) % 6 for x in range(len(s)))

m = pd.DataFrame({'S1': pd.Series([0, 0, 1, 0, 0, 1]),
                  'S2': pd.Series([1, 1, 0, 0, 0, 0]),
                  'S3': pd.Series([0, 0, 0, 1, 1, 0]),
                  'S4': pd.Series([1, 0, 1, 0, 1, 0])})

hash_h1 = pd.DataFrame({'S1': h1(m.S1),
                        'S2': h1(m.S2),
                        'S3': h1(m.S3),
                        'S4': h1(m.S4)})

hash_h2 = pd.DataFrame({'S1': h2(m.S1),
                        'S2': h2(m.S2),
                        'S3': h2(m.S3),
                        'S4': h2(m.S4)})

hash_h3 = pd.DataFrame({'S1': h3(m.S1),
                        'S2': h3(m.S2),
                        'S3': h3(m.S3),
                        'S4': h3(m.S4)})
# print(m)
# print(hash_h1)
# print(hash_h2)
# print(hash_h3)


def get_sig(s, h):
    return min([h[i] for i in s[s == 1].index.tolist()])
 
# S1
s1_sig = pd.Series([get_sig(m.S1, hash_h1.S1), get_sig(
    m.S1, hash_h2.S1), get_sig(m.S1, hash_h3.S1)])

# S2
s2_sig = pd.Series([get_sig(m.S2, hash_h1.S2), get_sig(
    m.S2, hash_h2.S2), get_sig(m.S2, hash_h3.S2)])

# S3
s3_sig = pd.Series([get_sig(m.S3, hash_h1.S3), get_sig(
    m.S3, hash_h2.S3), get_sig(m.S3, hash_h3.S3)])

# S4
s4_sig = pd.Series([get_sig(m.S4, hash_h1.S4), get_sig(
    m.S4, hash_h2.S4), get_sig(m.S4, hash_h3.S4)])


sig = pd.DataFrame({'S1': s1_sig,
                    'S2': s2_sig,
                    'S3': s3_sig,
                    'S4': s4_sig})
print(sig)
