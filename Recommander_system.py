#!python3

import numpy as np 
import pandas as pd
from sklearn.metrics import jaccard_similarity_score
from sklearn.metrics.pairwise import cosine_similarity
import scipy.cluster.hierarchy as hc
import matplotlib.pylab as plt

items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
users = ['A', 'B', 'C']
user_data = pd.DataFrame({'a': pd.Series([4, 0, 2], index=users),
                          'b': pd.Series([5, 3, 0], index=users),
                          'c': pd.Series([0, 1, 4], index=users),
                          'd': pd.Series([5, 3, 3], index=users),
                          'e': pd.Series([1, 1, 0], index=users),
                          'f': pd.Series([0, 2, 4], index=users),
                          'g': pd.Series([3, 1, 5], index=users),
                          'h': pd.Series([2, 0, 3], index=users)})

print(user_data)

def jaccard_distance(data):
    tmp_data = data.copy()
    print("Jaccard distance(bool)")
    for i in users:
        for j in range(tmp_data.loc[i].size):
            tmp_data.loc[i][j] = 1 if tmp_data.loc[i][j] > 0 else 0
    for i in range(len(users)):
        for j in range(i+1, len(users)):
            jaccard_value = jaccard_similarity_score(tmp_data.loc[users[i]], tmp_data.loc[users[j]])
            print("{} and {}: {:.3f}".format(users[i], users[j], jaccard_value))
            
def cos_distance(data):
    tmp_data = data.copy()
    print("Cosine distance(bool)")
    for i in users:
        for j in range(tmp_data.loc[i].size):
            tmp_data.loc[i][j] = 1 if tmp_data.loc[i][j] > 0 else 0
    for i in range(len(users)):
        for j in range(i+1, len(users)):
            cosine_value = sum(tmp_data.loc[users[i]].T*tmp_data.loc[users[j]])\
                / ((sum(tmp_data.loc[users[i]].T*tmp_data.loc[users[i]])**0.5)*\
                (sum(tmp_data.loc[users[j]].T*tmp_data.loc[users[j]])**0.5))
            print("{} and {}: {:.3f}".format(users[i], users[j], cosine_value))
            
def jaccard_distance2(data):
    tmp_data = data.copy()
    print("Jaccard distance(3-5: 1, 1-2: 0)")
    for i in users:
        for j in range(tmp_data.loc[i].size):
            tmp_data.loc[i][j] = 1 if tmp_data.loc[i][j] >= 3 and tmp_data.loc[i][j] <= 5 else 0
    for i in range(len(users)):
        for j in range(i+1, len(users)):
            jaccard_value = jaccard_similarity_score(tmp_data.loc[users[i]], tmp_data.loc[users[j]])
            print("{} and {}: {:.3f}".format(users[i], users[j], jaccard_value))

def cos_distance2(data):
    tmp_data = data.copy()
    print("Cosine distance(3-5: 1, 1-2: 0)")
    for i in users:
        for j in range(tmp_data.loc[i].size):
            tmp_data.loc[i][j] = 1 if tmp_data.loc[i][j] >= 3 and tmp_data.loc[i][j] <= 5 else 0
    for i in range(len(users)):
        for j in range(i+1, len(users)):
            cosine_value = sum(tmp_data.loc[users[i]].T*tmp_data.loc[users[j]])\
                / ((sum(tmp_data.loc[users[i]].T*tmp_data.loc[users[i]])**0.5) *
                   (sum(tmp_data.loc[users[j]].T*tmp_data.loc[users[j]])**0.5))
            print("{} and {}: {:.3f}".format(users[i], users[j], cosine_value))
    
def normalization(data):
    tmp_data = data.copy()
    print("Normalized data:")
    for i in users:
        average = 0.
        no = 0.
        for j in range(tmp_data.loc[i].size):
            no += 1 if tmp_data.loc[i][j] > 0 else 0
            average += tmp_data.loc[i][j]
        average = average/no
        for k in range(tmp_data.loc[i].size):
            tmp_data.loc[i][k] -= average if tmp_data.loc[i][j] > 0 else 0
    print(tmp_data)

def cos_distance_norm(data):
    tmp_data = data.copy()
    print("Normalized data before calculating cosine distance.")
    normalization(tmp_data)
    print("Calculate the cosine distance.")
    cos_distance(tmp_data)
    
    
def hierarchical_clustering(data):
    tmp_data = data.copy()
    new_data = []
    print("Hierarchical clustering...")
    for i in items:
        for j in range(tmp_data[i].size):
            tmp_data[i][j] = 1 if tmp_data[i][j] >= 3 and tmp_data[i][j] <= 5 else 0
        new_data.append(list(tmp_data[i]))
    distance_matrix = hc.distance.pdist(new_data, 'jaccard')
    clustering = hc.linkage(distance_matrix, method='single')
    hc.dendrogram(clustering)
    plt.title("Hierarchical Clustering Result")
    plt.savefig("hierarchical_clustering.png")
    print("Figure saved...")
    print("Result is showing...")
    # plt.show()
    clusters = hc.fcluster(clustering, 0, 'inconsistent')
    # print(clusters)
    return clusters

def avarage_for_blank(data, clusters):
    tmp_data = data.copy()
    print("New matrix constructed from hierarchical clustering:")
    for i in users:
        for j in range(tmp_data.loc[i].size):
            tmp_data.loc[i][j] = clusters[j] if tmp_data.loc[i][j] > 0 else 0
    return tmp_data

def cos_distance_clustering(data, clusters):
    tmp_data = avarage_for_blank(user_data, clusters)
    print("Jaccard distance for new data")
    # for i in users:
    #     for j in range(tmp_data.loc[i].size):
    #         tmp_data.loc[i][j] = 1 if tmp_data.loc[i][j] > 0 else 0
    for i in range(len(users)):
        for j in range(i+1, len(users)):
            jaccard_value = jaccard_similarity_score(
                tmp_data.loc[users[i]], tmp_data.loc[users[j]])
            print("{} and {}: {:.3f}".format(users[i], users[j], jaccard_value))



jaccard_distance(user_data)
cos_distance(user_data)
jaccard_distance2(user_data)
cos_distance2(user_data)
normalization(user_data)
cos_distance_norm(user_data)
clusters = hierarchical_clustering(user_data)
cos_distance_clustering(user_data, clusters)
