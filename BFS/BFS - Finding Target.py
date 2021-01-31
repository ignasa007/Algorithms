'''
Breadth First Search in an Directed Graph. 
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
Creat a flag to exit the loop once the end vertex is found.
'''

start = int(input("Enter the start vertex - "))
tails, heads = [start], []
end = int(input("Enter the target vertex - "))
exploredVertices = [False]*(start-1) + [True] + [False]*(numV-start)
distance, flag = 1, 0

while (exploredVertices!=[True]*numV):

    if not tails:
        if not heads:
            print("Vertex {} cannot be reached from vertex {}".format(end, start))
            break
        distance += 1
        tails, heads = heads, tails
    tail = tails.pop(0)

    for head in _dict[tail]:
        if not exploredVertices[head-1]:
            if head==end:
                print("The distance from vertex {} to vertex {} is {}".format(start, end, distance))
                break
            exploredVertices[head-1] = True
            heads.append(head)
    else:
        continue

    break