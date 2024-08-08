import sys
import math
input = sys.stdin.readline

def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b



t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    parent = [i for i in range(n+1)]
    
    for i in range(n):
        x1,y1,r1 = arr[i]
        for j in range(i+1,n):
            x2,y2,r2 = arr[j]

            if math.sqrt((x1-x2)**2 + (y1-y2)**2) <= r1+r2:
                union(i,j)
    
    result = set()

    for i in range(n):
        temp = find(i)
        if temp not in result:
            result.add(temp)

    print(len(result)) 