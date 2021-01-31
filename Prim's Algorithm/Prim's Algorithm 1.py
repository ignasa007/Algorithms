def minHeapify(minHeap, lenMinHeap, index, key = "go down"):
    
    if key == "go up":
        while index>0:
            parent, child = minHeap[(index-1)//2], minHeap[index]
            if parent[1]>child[1]:
                minHeap[(index-1)//2], minHeap[index] = child, parent
                index = (index-1)//2
            else:
                break
    
    elif key == "go down":   
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
    
def replaceMinHeap(minHeap, lenMinHeap, value, index):
    
    orig = minHeap[index][1]
    minHeap[index][1] = value
    if value<orig:
        minHeap = minHeapify(minHeap, lenMinHeap, index, "go up")
    elif value>orig:
        minHeap = minHeapify(minHeap, lenMinHeap, index, "go down")
    
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
    
k = open("edges.txt", "r")
numVertices, numEdges = list(map(int, k.readline().split()))
edges, heap = {}, []
for i in range(numVertices):
    heap.append([i+1,float("inf")])
    edges[i+1] = []
heap[0][1] = 0
lenHeap = numVertices
for i in range(numEdges):
    vertex1, vertex2, weight = list(map(int, k.readline().split()))
    edges[vertex1].append([vertex2, weight])
    edges[vertex2].append([vertex1, weight])

cost = 0
dist = [0]+[float("inf")]*(numVertices-1)

while heap!=[]:

    root, heap, lenHeap = extractMinHeap(heap, lenHeap)
    tail, weight = root
    print(tail, weight)
    cost += weight
    dist[tail-1] = None # meaning vertex visited

    for edge in edges[tail]:
        head, weight = edge
        if dist[head-1]!=None and weight<dist[head-1]:
            dist[head-1] = weight
            for i in range(lenHeap):
                if heap[i][0]==head:
                    heap = replaceMinHeap(heap, lenHeap, weight, i)
                    break

print(cost)