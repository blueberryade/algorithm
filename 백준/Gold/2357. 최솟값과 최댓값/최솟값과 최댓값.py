import sys
input = sys.stdin.readline

N,M = map(int,input().split())

treeHeight = 0
length = N

while length !=0:
    length//=2
    treeHeight+=1

treeSize = pow(2,treeHeight+1)
leftNodeStartIndex = treeSize // 2 -1
treeMin = [sys.maxsize] * (treeSize+1)
treeMax = [0] *(treeSize+1)

for i in range(leftNodeStartIndex+1,leftNodeStartIndex+N+1):
    treeMin[i] = treeMax[i] = int(input())

def setTree(i):
    while i != 1:
        if treeMin[i // 2] > treeMin[i]:
            treeMin[i // 2] = treeMin[i]
        if treeMax[i // 2] < treeMax[i]:
            treeMax[i // 2] = treeMax[i]
        i-=1


setTree(treeSize-1)

def getMin(s,e):
    minNum = sys.maxsize
    while s<=e:
        if s%2 == 1:
            minNum = min(minNum,treeMin[s])
            s+=1
        if e%2 == 0:
            minNum = min(minNum,treeMin[e])
            e-=1
        
        s = s//2
        e = e//2
    return minNum

def getMax(s,e):
    maxNum = 0
    while s<=e:
        if s%2 == 1:
            maxNum = max(maxNum,treeMax[s])
            s+=1
        if e%2 == 0:
            maxNum = max(maxNum,treeMax[e])
            e-=1
        
        s = s//2
        e = e//2
    return maxNum


for _ in range(M):
    s,e = map(int,input().split())
    s = s + leftNodeStartIndex
    e = e + leftNodeStartIndex

    print(getMin(s,e),getMax(s,e))
