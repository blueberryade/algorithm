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
        parent[b]= a
    else:
        parent[a] = b


n = int(input())
stars = []
edges = []
parent = [i for i in range(n+1)]
for _ in range(n):
    x,y = map(float,input().split())
    stars.append((x,y))

for i in range(n-1):
    for j in range(i+1,n):
        x1,y1 = stars[i]
        x2,y2 = stars[j]
        cost = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        edges.append((cost,i,j))

edges.sort()

result = 0
for edge in edges:
    cost,x,y = edge
    if find(x) != find(y):
        union(x,y)
        result += cost

print(round(result,2))