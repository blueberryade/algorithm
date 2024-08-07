import sys
input = sys.stdin.readline

n = int(input())
costs = [list(map(int,input().split())) for _ in range(n)]
parent = [i for i in range(n+1)]
edges = []

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n):
    for j in range(i+1,n):
        edges.append((costs[i][j],i,j))



edges.sort()

result = 0

for edge in edges:
    cost,a,b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a,b)
        result+=cost
print(result)        