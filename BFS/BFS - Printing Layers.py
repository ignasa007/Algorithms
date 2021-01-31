'''
Breadth First Search in an Directed Graph
The idea is to explore all the unvisited vertices of the current vertex until all the vertices have been visited.
'''

k = open("BFS.txt")
lines = k.readlines()

'''
A dictionary of edges, _dict, such that the value of each key is a list of elements such that there exists an edge 
in the graph with the key as the tail and the element in the list as the head.
'''

numV, _dict = len(lines), {}
for currLine in lines:
    currLine = list(map(int, currLine.split()))
    _dict[currLine[0]] = currLine[1:]

'''
Create a list of tails, tails, which will be the tails for any specific layer of the search.
Create a list of heads, heads, which will be the list of vertices visited by the list of tails.
Create a list of visited vertices, exploredVertices, which keeps track of the vertices not to be visited again.
Create a variable, distance, that keeps track of the layer of bfs we are in.
'''

start = int(input("Enter the start vertex - "))
tails, heads = [start], []
exploredVertices = [False]*(start-1) + [True] + [False]*(numV-start)
distance = 0
print("Layer", distance, "-", end=" ")

while(tails!=[] or heads!=[]):
    
    if tails==[]:
        if distance!=0:
            print()
        distance += 1
        print("Layer", distance, "-", end=" ")
        tails, heads = heads, tails

    tail = tails.pop(0)
    print(tail, end=" ")
    
    for head in _dict[tail]:        
        if not exploredVertices[head-1]:
            exploredVertices[head-1] = True
            heads.append(head)