from heapFunctions import *

input1 = open("Medians.txt", "r")
inList = list(map(int, input1.read().split("\n")))

left, right = [inList[0]], []
lenLeft, lenRight = 1, 0
sumMedians = inList[0]

for i in range(1,len(inList)):

    element = inList[i]
    if element<=left[0]:
        left, lenLeft = insertMaxHeap(left, lenLeft, element)
    else:
        right, lenRight = insertMinHeap(right, lenRight, element)

    if lenLeft-lenRight==2:
        value, left, lenLeft = extractMaxHeap(left, lenLeft)
        right, lenRight = insertMinHeap(right, lenRight, value)
    elif lenRight-lenLeft==2:
        value, right, lenRight = extractMinHeap(right, lenRight)
        left, lenLeft = insertMaxHeap(left, lenLeft, value)

    if (i+1)%2==0:
        sumMedians += left[0]
    else:
        if lenLeft>lenRight:
            sumMedians += left[0]
        else:
            sumMedians += right[0]

print(sumMedians%10000)