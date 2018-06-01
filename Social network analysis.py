#!python3

import networkx as nx 
import nxviz as nz
import numpy as np
import matplotlib.pyplot as plt
from networkx.algorithms.centrality import betweenness_centrality
from networkx.algorithms.dag import transitive_closure
from networkx.algorithms import all_simple_paths

nodes = list(range(1, 10))  # nodes 1~9
edges = [(1, 4), (1, 5), (1, 6), (4, 8), (4, 3), (5, 3),
         (5, 7), (6, 2), (7, 3), (7, 10), (7, 2), (2, 9)] #undirected edges

#create a simple undirected graph
G = nx.Graph() #call the constructor
G.add_nodes_from(nodes) #add nodes 1~9
G.add_edges_from(edges) #add edges

#draw graph
# pos = nx.shell_layout(G)
# nx.draw(G, pos, with_labels=True, node_color='black',
#         edge_color='black', node_size=100, alpha=0.5)
# plt.show()

#experiment 1: number of shortest paths passing node 1 and 2
all_shortest_paths = []
paths_go_through_1 = []
paths_go_through_2 = []

for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
        # print((nodes[i], nodes[j]))
        all_shortest_paths.append(nx.shortest_path(G, source=nodes[i], target=nodes[j], weight=None))

# print(all_shortest_paths)

for path in all_shortest_paths:
    if 1 in path:
        paths_go_through_1.append(path)
    if 2 in path:
        paths_go_through_2.append(path)
#(a)
print("The number of shortest path passing node 1 is {}.".format(len(paths_go_through_1)))
#(b)
print("The number of shortest path passing node 2 is {}.".format(len(paths_go_through_2)))

# centrality_1 = betweenness_centrality(G, normalized=False)
# print("The betweenness centrality of node 1 is {:.2f}".format(centrality_1[1]))

#experiment 2: neighbour profiles of node 1 and 2
#(a)
paths_src_1 = []
paths_src_2 = []
neighbor_profile_1 = {}
neighbor_profile_2 = {}
for path in all_shortest_paths:
    if path[0] == 1:
        paths_src_1.append(path)
    if path[0] == 2:
        paths_src_2.append(path)

# print(paths_src_1)
# print(paths_src_2)

sorted_paths_src_1 = sorted(paths_src_1, key=len)
sorted_paths_src_2 = sorted(paths_src_2, key=len)
# print(sorted(paths_src_1, key=len))
# print(sorted(paths_src_2, key=len))

for i in range(len(nodes)):
    neighbor_profile_1[nodes[i]] = {}
    neighbor_profile_2[nodes[i]] = {}
    for path in sorted_paths_src_1:
        if len(path)-1 not in neighbor_profile_1[nodes[i]]:
            neighbor_profile_1[nodes[i]][len(path)-1] = 1
        else:
            neighbor_profile_1[nodes[i]][len(path)-1] += 1
    for path in sorted_paths_src_2:
        if len(path)-1 not in neighbor_profile_2[nodes[i]]:
            neighbor_profile_2[nodes[i]][len(path)-1] = 1
        else:
            neighbor_profile_2[nodes[i]][len(path)-1] += 1

# print(all_paths)
print("Neighbor profile of node 1 is {}".format(neighbor_profile_1))
print("Neighbor profile of node 2 is {}".format(neighbor_profile_2))


#(b)
G_diameter = max([len(p) for p in all_shortest_paths]) 
print("The diameter of the graph is {}.".format(G_diameter))

#(c)
print("The number of transitive closure is %d." % (len(nodes)*(len(nodes)+1)/2))
print("Need |V|*(|V|+1)/2 loops for calculating, in this graph, is %d." % (len(nodes)*(len(nodes)+1)/2))
