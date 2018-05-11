#!python3

import numpy as np
import pandas as pd 
import numpy as np
from sklearn.cluster import Birch
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns 

sns.set_style("whitegrid")
data = pd.read_csv('basketball.csv', encoding='gb2312')
# print(data.head())
 
# print(data.describe())


del data['heightInteger']
del data['time_playedReal'] 
del data['ageInteger']
X = data
x = data.assists_per_minuteReal
# x = data.heightInteger
# x = data.ageInteger
y = data.points_per_minuteReal

k = int(input("Please the number of classes: "))
# k = 3
classes = KMeans(n_clusters=k)
predictions = classes.fit_predict(X)
# print(classes)
# print(predictions)


print("The clustering results:")
for i in range(k):
    print("{}:".format(i))
    tmp = []
    for j in range(len(predictions)):
        if predictions[j] == i:
            tmp.append(j)
    print(tmp)



plt.scatter(x, y, c=predictions, marker='x')
plt.title("Kmeans-Basketball Data")
plt.xlabel("assists_per_minuteReal")
plt.ylabel("points_per_minute")
plt.legend(["Rank"])
plt.savefig("assists-position.png")


# plt.title("Kmeans-Basketball Data")
# plt.xlabel("age")
# plt.ylabel("points_per_minute")
# plt.legend(["Rank"])
# plt.savefig("age-position.png")
# plt.show()

