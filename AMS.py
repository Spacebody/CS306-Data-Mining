#!python3

import random
#data stream
data = [3, 1, 4, 1, 3, 4, 2, 1, 2]

#simpel calculation of moments
def cal_secondary_moment(s):
    return sum([x**2 for x in s])

def cal_third_moment(s):
    return sum([x**3 for x in s])

print("Secondary moment: {}".format(cal_secondary_moment(data)))
print("Third moment: {}".format(cal_third_moment(data)))

#AMS algorithm, two variables X1, X2
def AMS(s, n=9):
    position = random.sample(range(0, len(s)), n)
    # print(position)
    X_value = {}
    X_element = {}
    for i in range(n):
        X_value[i] = 1
        X_element[i] = s[position[i]]
    # print("X.values:", X_value)
    # print(X_element)
    j = 0
    for pos in position:
        for k in range(pos+1, len(s)):
            X_value[j] += 1 if s[k] == X_element[j] else 0
        j += 1
    print("X.value:", X_value)

AMS(data)