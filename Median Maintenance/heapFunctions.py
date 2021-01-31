#OPERATIONS

#Find-max (or Find-min): find a maximum item of a max-heap, or a minimum item of a min-heap, respectively (a.k.a. peek)

def findMax(maxHeap):

    return maxHeap[0]

def findMin(minHeap):

    return minHeap[0]

#Insert - adding a new key to the heap (a.k.a., push)

def insertMaxHeap(maxHeap, lenMaxHeap, value):
    
    maxHeap.append(value)
    index = lenMaxHeap
    lenMaxHeap += 1
    
    while index>0:
        parent, child = maxHeap[(index-1)//2], maxHeap[index]
        if parent<child:
            maxHeap[(index-1)//2], maxHeap[index] = child, parent
            index = (index-1)//2
        else:
            break

    return maxHeap, lenMaxHeap

def insertMinHeap(minHeap, lenMinHeap, value):
    
    minHeap.append(value)
    index = lenMinHeap
    lenMinHeap += 1
    
    while index>0:
        parent, child = minHeap[(index-1)//2], minHeap[index]
        if parent>child:
            minHeap[(index-1)//2], minHeap[index] = child, parent
            index = (index-1)//2
        else:
            break

    return minHeap, lenMinHeap

#Heapify: Restore the heap property given where a change has been made

def maxHeapify(maxHeap, lenMaxHeap, index, key = "go down"):
    
    if key == "go up":
    
        while index>0:
            parent, child = maxHeap[(index-1)//2], maxHeap[index]
            if parent<child:
                maxHeap[(index-1)//2], maxHeap[index] = child, parent
                index = (index-1)//2
            else:
                break
    
    elif key == "go down":

        while 2*index+2<=lenMaxHeap-1:
            parent, leftChild, rightChild = maxHeap[index], maxHeap[2*index+1], maxHeap[2*index+2]
            if parent<leftChild or parent<rightChild:
                if leftChild>=rightChild:
                    maxHeap[index], maxHeap[2*index+1] = leftChild, parent
                    index = 2*index+1
                else:
                    maxHeap[index], maxHeap[2*index+2] = rightChild, parent
                    index = 2*index+2
            else:
                break

        if 2*index+1==lenMaxHeap-1 and maxHeap[lenMaxHeap-1]>maxHeap[index]:
            maxHeap[index], maxHeap[lenMaxHeap-1] = maxHeap[lenMaxHeap-1], maxHeap[index]

    return maxHeap

def minHeapify(minHeap, lenMinHeap, index, key = "go down"):

    if key == "go up":

        while index>0:
            parent, child = minHeap[(index-1)//2], minHeap[index]
            if parent>child:
                minHeap[(index-1)//2], minHeap[index] = child, parent
                index = (index-1)//2
            else:
                break
    
    elif key == "go down":
    
        while 2*index+2<=lenMinHeap-1:
            parent, leftChild, rightChild = minHeap[index], minHeap[2*index+1], minHeap[2*index+2]
            if parent>leftChild or parent>rightChild:
                if leftChild<=rightChild:
                    minHeap[index], minHeap[2*index+1] = leftChild, parent
                    index = 2*index+1
                else:
                    minHeap[index], minHeap[2*index+2] = rightChild, parent
                    index = 2*index+2
            else:
                break

        if 2*index+1==lenMinHeap-1 and minHeap[lenMinHeap-1]<minHeap[index]:
            minHeap[index], minHeap[lenMinHeap-1] = minHeap[lenMinHeap-1], minHeap[index]

    return minHeap

#Extract: returns the node of maximum (minimum) value from a max (min) heap after removing it from the heap (a.k.a., pop)

def extractMaxHeap(maxHeap, lenMaxHeap):
    
    returnMax = maxHeap[0]
    maxHeap[0] = maxHeap.pop()
    lenMaxHeap -= 1
    maxHeap = maxHeapify(maxHeap, lenMaxHeap, 0)
    return returnMax, maxHeap, lenMaxHeap

def extractMinHeap(minHeap, lenMinHeap):

    returnMin = minHeap[0]
    minHeap[0] = minHeap.pop()
    lenMinHeap -= 1
    minHeap = minHeapify(minHeap, lenMinHeap, 0)
    return returnMin, minHeap, lenMinHeap

#Delete: delete an arbitrary node (followed by moving last node and sifting to maintain heap)

def deleteMaxHeap(maxHeap, lenMaxHeap, index):
    
    orig = maxHeap[index]
    value = maxHeap.pop()
    maxHeap[index] = value
    lenMaxHeap -= 1

    if value>orig:
        maxHeap = maxHeapify(maxHeap, lenMaxHeap, index, "go up")
    elif value<orig:
        maxHeap = maxHeapify(maxHeap, lenMaxHeap, index, "go down")

    return maxHeap, lenMaxHeap

def deleteRootMinHeap(minHeap, lenMinHeap, index):
    
    orig = minHeap[index]
    value = minHeap.pop()
    minHeap[index] = value
    lenMinHeap -= 1

    if value<orig:
        minHeap = minHeapify(minHeap, lenMinHeap, index, "go up")
    elif value>orig:
        minHeap = minHeapify(minHeap, lenMinHeap, index, "go down")
    
    return minHeap, lenMinHeap

#Replace: pop an old key and push a new key; more efficient than pop followed by push, since only need to balance once, not twice

def replaceMaxHeap(maxHeap, lenMaxHeap, value, index):

    orig = maxHeap[index]
    maxHeap[index] = value

    if value>orig:
        maxHeap = maxHeapify(maxHeap, lenMaxHeap, index, "go up")
    elif value<orig:
        maxHeap = maxHeapify(maxHeap, lenMaxHeap, index, "go down")

    return maxHeap  

def replaceMinHeap(minHeap, lenMinHeap, value, index):
    
    orig = minHeap[index]
    minHeap[index] = value

    if value<orig:
        minHeap = minHeapify(minHeap, lenMinHeap, index, "go up")
    elif value>orig:
        minHeap = minHeapify(minHeap, lenMinHeap, index, "go down")
    
    return minHeap

#Create-heap: create an empty heap

def createEmptyHeap():
    
    return []

#Build - build a heap out of given array of elements

def buildMaxHeap(maxHeap, lenMaxHeap):

    for index in range(lenMaxHeap//2,-1,-1):
        maxHeap = maxHeapify(maxHeap, lenMaxHeap, index)
    return maxHeap

def buildMinHeap(minHeap, lenMinHeap):
    
    for index in range(lenMinHeap//2,-1,-1):
        minHeap = minHeapify(minHeap, lenMinHeap, index)
    return minHeap

#Merge - joining two heaps to form a valid new heap containing all the elements of both

def mergeMaxHeap(maxHeap1, lenMaxHeap1, maxHeap2, lenMaxHeap2):

    return buildMaxHeap(maxHeap1+maxHeap2, lenMaxHeap1+lenMaxHeap2)

def mergeMinHeap(minHeap1, lenMinHeap1, minHeap2, lenMinHeap2):
    
    return buildMinHeap(minHeap1+minHeap2, lenMinHeap1+lenMinHeap2)