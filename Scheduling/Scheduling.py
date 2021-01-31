'''
Problem: Given a list of n jobs, we have their weights and the time needed to complete them. 
The cost of completing each job is the product of its weight and the cumulative time that has passed once the job is completed.
Find a schedule to complete all the jobs such that the sum of the costs is minimized.

Claim: The best schedule is the one in which the jobs are completed in decreasing order of their w/l values, 
and ties are handled by scheduling the jobs with higher weights first.

Proof: Supposedly there exists a better schedule which does not follow this rule.
In this schedule, there exist two consecutive jobs, i, j, such that wi/li < wj/lj but i is completed before j.
Notice that if we flip the order of these two jobs, the completion time, and hence the cost, of all other jobs remains the same.
cost1 = cx + wi(lx+li) + wj(lx+li+lj) + cy = (cx + (wi+wj)*lx + wi*li + wj*lj) + wj*li
cost2 = cx + wj(lx+lj) + wi(lx+li+lj) + cy = (cx + (wi+wj)*lx + wi*li + wj*lj) + wi*lj
But since wj*li > wi*lj, cost2 < cost1. However, this is a contradiction since cost1 one was supposed to come from the better strategy.
'''

from collections import Counter

k = open(r"C:\Users\Jasraj Singh\Desktop\Codes\jobs.txt", "r")
n = k.readline()
weightLength, ratioList = [], []

for i in range(int(n)):
    job = list(map(int,k.readline().split()))
    weightLength.append(job)
    ratioList.append(job[0]/job[1])

weightLength.sort(reverse = True, key = lambda x: x[0]/x[1])
ratioList.sort(reverse = True)
ratioList = Counter(ratioList)

length, cost = 0, 0 #Initialise cumulative length thus far and cost thus far

while weightLength!=[]:

    sliceIndex = ratioList[weightLength[0][0]/weightLength[0][1]]
    temp = weightLength[:sliceIndex]
    weightLength = weightLength[sliceIndex:]
    temp.sort(reverse = True, key = lambda x: x[0])
    for i in temp:
        length += i[1]
        cost += length*i[0]

print(cost)