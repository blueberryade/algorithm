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

def dist(a,b):
    x1,y1 = a
    x2,y2 = b
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
coordinate = [[]]
edges = []
result = 0

for _ in range(n):
    x,y = map(int,input().split())
    coordinate.append([x,y])

for _ in range(m):
    a,b = map(int,input().split())
    union(a,b)


for i in range(1,n+1):
    for j in range(i+1,n+1):
        cost = dist(coordinate[i],coordinate[j])
        edges.append((cost,i,j))

edges.sort()     

for edge in edges:
    cost,x,y = edge
    if find(x) != find(y):
        union(x,y)
        result += cost

print('%.2f' %result)