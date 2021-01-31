'''
The idea is that at any stage, we have a set of explored vertices and a set of unexplored vertices. 
We expand our search by choosing the edge with minimum sum of weight and the distance assigned to the vertex in the explored set. 
The distance for the vertex from the unexplored set is updated as this sum.

Dijkstra's Algorithm only works for graphs with positive edge weights.
The distances assigned to vertices never need to be updated. 
Proof: Assume that we have assigned the path length corresponding to the path s~u1-d to vertex d, 
where length(s~v-d)>length(s~u1-d) for all poosible options of v because we choose the path with min length. 
s~v~u2-d cannot have a shorter path length since length(s~v~u2-d)>length(s~v-d).
'''

k = open("dijkstraData.txt")
lines = k.readlines()

'''
A dictionary of edges, _dict, such that the value of each key is a list of elements such that there exists an edge 
in the graph with the key as the tail and the element in the list as the head.
'''

_dict, numV = {}, len(lines)
for line in lines:
    currLine = line.split()
    _dict[int(currLine.pop(0))] = sorted(list(map(lambda x: list(map(int, x.split(","))), currLine[1:])), key = lambda y: y[1])

'''
Variable distances is a list maintaining the distance of a vertex from the start vertex.
Variable exploredV is the set of vertices that have been explored. 
'''

start = int(input("Enter start vertex - "))
distances = [0]*numV
exploredV = [start]

while len(exploredV)!=numV:

    dist, lastVisited = [], exploredV[-1]
    for v in exploredV:
        for tempVar in _dict[lastVisited].copy():
            if tempVar[0]==v:
                _dict[lastVisited].remove(tempVar)
                break
        for tempVar in _dict[v].copy():
            if tempVar[0]==lastVisited:
                _dict[v].remove(tempVar)
                break
    for v in exploredV:
        if _dict[v]:
            dist.append([v,distances[v-1]+_dict[v][0][1]])

    v, minDist = sorted(dist, key = lambda x: x[1])[0]
    w = _dict[v][0][0]
    distances[w-1] = minDist
    exploredV.append(w)

'''
Random set of distances to print.
For start vertex = 1, the output should be 2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068
'''

print(distances[7-1], distances[37-1], distances[59-1], distances[82-1], distances[99-1], distances[115-1], distances[133-1], distances[165-1], distances[188-1], distances[197-1], sep=", ")
