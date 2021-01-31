def quickSort(inList, key): 

    lenList = len(inList)
    if lenList==0 or lenList==1:
        return inList

    global count

    if key=="start":
        pivotIndex = 0
    elif key=="end":
        pivotIndex = lenList-1
    elif key=="median":
        a = inList[0]
        b = inList[(lenList-1)//2]
        c = inList[lenList-1]
        temp = [[0,a],[(lenList-1)//2,b],[lenList-1,c]]
        temp.sort(key=lambda x: int(x[1]))
        pivotIndex = temp[1][0]

    inList[0], inList[pivotIndex] = inList[pivotIndex], inList[0]
    pivot = inList[0]

    i = 1
    for j in range(1,lenList):
        if inList[j]<pivot:
            inList[i], inList[j] = inList[j], inList[i]
            i += 1

    inList[0], inList[i-1] = inList[i-1], inList[0]
    count += lenList-1

    left = quickSort(inList[:i-1],key)
    right = quickSort(inList[i:],key)
    left.append(pivot)
    left.extend(right)

    return left

input1 = open("QuickSort.txt", "r")
inList = input1.read().split("\n")
inList = list(map(int, inList))

count = 0
quickSort(inList, "start")
print(count)