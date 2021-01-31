# Depth First Search in an Directed Graph to Explore Distinct SCCs.
# The idea is to first compute a finishing order in the dfs of a graph and then use the reverse of this order to start dfs
# on the inverted graph.. In the inverted graph, where all the edges have been reversed, the vertices appearing before a given 
# vertex can be reached iff they are a part of the same scc. If an edge connects one scc to another, then the head of this 
# edge appears earlier in the finish order (think) and the dfs in the reversed graph starts from the tail before it starts 
# from the head. Now, because the edge connecting the head and the tail is reversed, we cannot reach from the tail to the head, 
# leaving the head scc unexplored in tail's dfs.

k = open("DFS.txt","r")
lines = k.readlines()

# A dictionary of edges, _dict, such that the value of each key is a list of elements such that there exists an edge 
# in the graph with the key as the tail and the element in the list as the head.
numV, _dict = len(lines), {}
for currLine in lines:
    currLine = list(map(int, currLine.split()))
    _dict[currLine[0]] = currLine[1:]

# Create a list of visited vertices, exploredVertices, which keeps track of the vertices not to be visited again.
# Create a list of finish order, finishOrder, in the initial dfs with edges in their original direction.
exploredVertices, finishOrder = [False]*numV, []

# dfs function for getting the finish order. Explore all the vertices adjacent to the current one, until you 
# have explored all of them. In that case, add the vertex to the finish order.
def dfs(tail):
    global exploredVertices, finishOrder
    exploredVertices[tail-1] = True
    for head in _dict[tail]:
        if not exploredVertices[head-1]:
            dfs(head)
        finishOrder.append(head)

# Carry out dfs vertex by vertex, checking first if the vertex is unexplored, with the purpose of computing the finish order.
for vertex in range(1,numV+1):
    if not exploredVertices[vertex-1]:
        dfs(vertex) 

# Now we make the graph again, but this time with all the vertices in the opposite direction.
_dict = {head:[] for head in _dict}
for currLine in lines:
    currLine = list(map(int, currLine.split()))
    head = currLine[0]
    for tail in currLine[1:]:
        _dict[tail].append(head)

# dfs function which adds a tail to the strongly connected component currently under consideration.
def dfs(tail):
    global exploredVertices, scc, size
    exploredVertices[tail-1] = True
    scc.append(tail)
    size += 1
    for head in _dict[tail]:
        if not exploredVertices[head-1]:
            dfs(head)

# Compute the sizes and the vertices in different strongly connected components.
exploredVertices, scc, sccs, sizes = [False]*numV, [], [], []
for vertex in reversed(finishOrder):
    if not exploredVertices[vertex-1]:
        if scc!=[]:
            sccs.append(scc)
            sizes.append(size)
        scc, size = [], 0
        dfs(vertex)
sccs.append(scc)
sizes.append(size)

print("Strongly Connected Components -", *sccs)
print("Sizes -", *sizes)
