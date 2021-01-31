def minHeapify(minHeap, lenMinHeap, index):   

    while 2*index+2<=lenMinHeap-1:
        parent, leftChild, rightChild = minHeap[index], minHeap[2*index+1], minHeap[2*index+2]
        if parent[1]>leftChild[1] or parent[1]>rightChild[1]:
            if leftChild[1]<=rightChild[1]:
                minHeap[index], minHeap[2*index+1] = leftChild, parent
                index = 2*index+1
            else:
                minHeap[index], minHeap[2*index+2] = rightChild, parent
                index = 2*index+2
        else:
            break
    if 2*index+1==lenMinHeap-1 and minHeap[lenMinHeap-1][1]<minHeap[index][1]:
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

    return returnMin, [minHeap, lenMinHeap]

def insertMinHeap(minHeap, lenMinHeap, edge):    

    minHeap.append(edge)
    index = lenMinHeap
    lenMinHeap += 1    
    while index>0:
        parent, child = minHeap[(index-1)//2], minHeap[index]
        if parent[1]>child[1]:
            minHeap[(index-1)//2], minHeap[index] = child, parent
            index = (index-1)//2
        else:
            break

    return [minHeap, lenMinHeap]
    
k = open("edges.txt", "r")
numVertices, numEdges = list(map(int, k.readline().split()))

# "edges" is a dictionary with vertices as keys and corresponding edges stored in a heap as values
edges = {}
for i in range(numVertices):
    edges[i+1] = [[],0]
for i in range(numEdges):
    vertex1, vertex2, weight = list(map(int, k.readline().split()))
    edges[vertex1] = insertMinHeap(edges[vertex1][0], edges[vertex1][1], [vertex2, weight])
    edges[vertex2] = insertMinHeap(edges[vertex2][0], edges[vertex2][1], [vertex1, weight])

cost, visited, visitedLst, target = 0, [1], [True]+[False]*(numVertices-1), [True]*numVertices

while visitedLst!=target:

    minWeight = float("inf")
    for tail in visited.copy():
        while True:
            if edges[tail][1]==0:
                visited.remove(tail)
                break
            returnMin = edges[tail][0][0]
            head, weight = returnMin
            if visitedLst[head-1]==False:
                if weight<minWeight:
                    minCutEdge = [tail, head, weight]
                    minWeight = weight
                break
            else:
                _, edges[tail] = extractMinHeap(edges[tail][0], edges[tail][1])

    tail, head, weight = minCutEdge
    _, edges[tail] = extractMinHeap(edges[tail][0], edges[tail][1])
    visitedLst[head-1] = True
    visited.append(head)
    cost += weight

print(cost)
