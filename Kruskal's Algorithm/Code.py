'''
Kruskal's ALgorithm is used for finding the minimum spanning tree of a weighted undirected graph.

The algorithm suggests picking edges with minimum weight and adding them to the spanning tree if they don not form a cycle.
So, if we pick an edge with minimum weight (of the edges not yet checked), if at least one of its vertices is not visited, we add
it to the tree. In this sense, Kruskal's Algorithm is a greedy algorithm.

The complexity of the algorithm is O(ElogV) = O(ElogE), as E < V^2
'''

def minHeapify(minHeap, lenMinHeap, index):   

    while 2*index+2<=lenMinHeap-1:
        parent, leftChild, rightChild = minHeap[index], minHeap[2*index+1], minHeap[2*index+2]
        if parent[2]>leftChild[2] or parent[2]>rightChild[2]:
            if leftChild[2]<=rightChild[2]:
                minHeap[index], minHeap[2*index+1] = leftChild, parent
                index = 2*index+1
            else:
                minHeap[index], minHeap[2*index+2] = rightChild, parent
                index = 2*index+2
        else:
            break
    if 2*index+1==lenMinHeap-1 and minHeap[lenMinHeap-1][2]<minHeap[index][2]:
        minHeap[index], minHeap[lenMinHeap-1] = minHeap[lenMinHeap-1], minHeap[index]

    return minHeap

def extractMinHeap(minHeap, lenMinHeap):   

    returnMin = minHeap[0]
    if lenMinHeap==1:
        minHeap = []
    else:
        minHeap[0] = minHeap.pop()
    lenMinHeap -= 1
    minHeap = minHeapify(minHeap, lenMinHeap, 0)

    return returnMin, minHeap, lenMinHeap

def insertMinHeap(minHeap, lenMinHeap, edge):    

    minHeap.append(edge)
    index = lenMinHeap
    lenMinHeap += 1    
    while index>0:
        parent, child = minHeap[(index-1)//2], minHeap[index]
        if parent[2]>child[2]:
            minHeap[(index-1)//2], minHeap[index] = child, parent
            index = (index-1)//2
        else:
            break

    return minHeap, lenMinHeap
    
k = open("edges.txt")
numVertices, numEdges = list(map(int, k.readline().split()))

edgesHeap, lenHeap = [], 0
for i in range(numEdges):
    edge = list(map(int, k.readline().split()))
    edgesHeap, lenHeap = insertMinHeap(edgesHeap, lenHeap, edge)

cost, visited = 0, [False]*numVertices

while visited!=[True]*numVertices:
    
    minEdge, edgesHeap, lenHeap = extractMinHeap(edgesHeap, lenHeap)
    v1, v2, weight = minEdge
    if not visited[v1-1] or not visited[v2-1]:
        cost += weight
        visited[v1-1], visited[v2-1] = True, True

print(cost)