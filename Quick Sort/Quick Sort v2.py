def quickSort(start, end, key):
        
    if end-start==0 or end-start==1:
        return

    global inList, count

    if key=="start":
        pivotIndex = start
    elif key=="end":
        pivotIndex = end-1
    elif key=="median":
        a = inList[0]
        b = inList[(lenList-1)//2]
        c = inList[lenList-1]
        temp = [[0,a],[(lenList-1)//2,b],[lenList-1,c]]
        temp.sort(key=lambda x: int(x[1]))
        pivotIndex = temp[1][0]

    inList[start], inList[pivotIndex] = inList[pivotIndex], inList[start]
    pivot = inList[start]

    i = start
    count += (end-start-1)

    for j in range(start+1, end):
        if inList[j]<pivot:
            i += 1
            inList[i], inList[j] = inList[j], inList[i]
    inList[start], inList[i] = inList[i], inList[start]

    quickSort(start, i, key)
    quickSort(i+1, end, key)
    
input1 = open("QuickSort.txt", "r")
inList = input1.read().split("\n")
inList = list(map(int, inList))

count = 0
lenList = len(inList)
quickSort(0, lenList, "start")
print(count)