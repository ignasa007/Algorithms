# Depth First Search in an Directed Graph to find the sizes of SCCs in large graph.
# The idea is to first compute a finishing order in the dfs of a graph and then use the reverse of this order to start dfs
# on the inverted graph.. In the inverted graph, where all the edges have been reversed, the vertices appearing before a given 
# vertex can be reached iff they are a part of the same scc. If an edge connects one scc to another, then the head of this 
# edge appears earlier in the finish order (think) and the dfs in the reversed graph starts from the tail before it starts 
# from the head. Now, because the edge connecting the head and the tail is reversed, we cannot reach from the tail to the head, 
# leaving the head scc unexplored in tail's dfs.

k = open(r"C:\Users\Jasraj Singh\Desktop\Codes\DFS (self written)\Size of SCCs without recursion\SCC.txt","r")
lines = k.readlines()
numV = len(lines)

# A dictionary of edges, _dict, such that the value of each key is a list of elements such that there exists an edge 
# in the graph with the key as the tail and the element in the list as the head.
_dict, _dictReverse = {}, {}
for head in range(1,numV+1):
    _dict[head], _dictReverse[head] = [], []
for line in lines:
    head, tail = list(map(int, line.split()))
    _dict[head].append(tail)
    _dictReverse[tail].append(head)

# Carry out dfs vertex by vertex, checking first if the vertex is unexplored, with the purpose of computing the finish order.
exploredVertices, finishOrder, stack, vertices = [False]*numV, [], [], list(range(1,numV+1))
while stack!=[] or vertices!=[]:

    if stack==[]:
        tail = vertices.pop(0)
        stack.append(tail)
        exploredVertices[tail-1] = True
    else:
        tail = stack[-1]

    if _dict[tail]==[]:
        stack.pop()
        finishOrder.append(tail)
    else:
        head = _dict[tail].pop(0)
        if not exploredVertices[head-1]:
            stack.append(tail)
            exploredVertices[head-1] = True
            vertices.remove(head)
            
# Compute the sizes and the vertices in different strongly connected components.
exploredVertices, size, sizes, stack = [False]*numV, 0, [], []
for vertex in reversed(finishOrder):
    
    if not exploredVertices[vertex-1]:
        stack = [vertex]
        tail = vertex

        while stack!=[]:
            tail = stack[len(stack)-1]
            exploredVertices[tail-1] = True
            if _dictReverse[tail]==[]:
                stack.pop()
                size += 1
            else:
                head = _dictReverse[head][0]
                _dictReverse[tail].pop(0)
                if not exploredVertices[head-1]:
                    stack.append(head)

        sizes.append(size)
        size = 0

sizes.append(size)

# Printing top 5 components with the maximum size
print(*(sorted(sizes, reverse=True)[:5]))