# Depth First Search in an Directed Acyclic Graph (DAG) to find it's Topological Ordering.
# Topological Ordering is an ordering of vertices such that vertex i appears before vertex j in the ordering iff
# vertex i cannot be reached from vertex j, for every pair of vertices (i,j)

k = open(r"C:\Users\Jasraj Singh\Desktop\Codes\DFS (self written)\Topological Sort of DAG\DFS.txt", "r")
lines = k.readlines()

# A dictionary of edges, _dict, such that the value of each key is a list of elements such that there exists an edge 
# in the graph with the key as the tail and the element in the list as the head.
numV, _dict = len(lines), {}
for currLine in lines:
    currLine = list(map(int, currLine.split()))
    _dict[currLine[0]] = currLine[1:]   

# Function to carry out the DFS 
# The algorithm is that we keep jumping to the next vertex until all the neighbors of a vertex have been explored.
# Then we add this vertex to the topological ordering.
def dfs(head):
    global exploredVertices, _dict, topologicalOrdering, currentLabel
    exploredVertices[head-1] = True
    for tail in _dict[head].copy():
        if not exploredVertices[tail-1]:
            dfs(tail)
            _dict[head].remove(tail)
    topologicalOrdering[head-1] = currentLabel
    currentLabel += 1

# Driver code
exploredVertices, topologicalOrdering, currentLabel = [False]*numV, [False]*numV, 1
for vertex in range(1,numV+1):
    if not exploredVertices[vertex-1]:
        dfs(vertex)

print(*list(reversed(topologicalOrdering)))