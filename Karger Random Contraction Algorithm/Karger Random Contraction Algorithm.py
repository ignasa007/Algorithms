'''
Karger's minimum cut algorithm is a randomized algorithm used to calculate the minimum cut of a connected graph, i.e., the 
minimum number of edges that can be removed to obtain two disjoint set of vertices.

The algorithm predicts the correct number of minimum cuts with a probability 1/(nC2) = 2(n(n-1)), where n is the number of vertices. 
Therefore, we need to run the algorithm multiple times in order to get the right answer.

The algorthm suggests that we take a random edge from the set of edges and 'contract' it. This means that we merge the two edges
into one, deleting either one of the two (here, we retain the first vertex, edge[0]). All edges (v1, v2) are removed and all edges
of the type (v2, u) are turned to (v1, u).
Note that the algorithm allows for multiple edges between any two vertices.
We keep repeating the process until there are only two vertices left. In a sense, the two vertices represent the two independent
set of vertices, while the number of edges between them is the number of edges crossing the two sets.
'''

import random

min_edges_in_cut = float("inf")
k = open(r"kargerMinCut.txt",'r')
lines = k.readlines()

origEdges = {}
for line in lines:
    currLine = list(map(int, line.split()))
    u = currLine[0]
    for v in currLine[1:]:
        if tuple((u,v)) not in origEdges:
            origEdges[tuple((v,u))] = 1

for i in range(50):
    
    edges = origEdges.copy()
    
    while(len(edges)>1):
        
        colapseEdge = (random.choices(list(edges.keys())))[0]
        del edges[colapseEdge]

        for edge in edges.copy():
            
            if colapseEdge[1]==edge[0]:
                if tuple((colapseEdge[0], edge[1])) in edges:
                    edges[tuple((colapseEdge[0], edge[1]))] += edges[edge]
                elif tuple((edge[1], colapseEdge[0])) in edges:
                    edges[tuple((edge[1], colapseEdge[0]))] += edges[edge]
                else:
                    edges[tuple((edge[1], colapseEdge[0]))] = edges[edge]
                del edges[edge]
                
            elif edge[1]==colapseEdge[1]:
                if tuple((colapseEdge[0], edge[0])) in edges:
                    edges[tuple((colapseEdge[0], edge[0]))] += edges[edge]
                elif tuple((edge[0], colapseEdge[0])) in edges:
                    edges[tuple((edge[0], colapseEdge[0]))] += edges[edge]
                else:
                    edges[tuple((edge[0], colapseEdge[0]))] = edges[edge]
                del edges[edge]

    min_edges_in_cut = min(min_edges_in_cut, list(edges.values())[0])
    
print(min_edges_in_cut)
