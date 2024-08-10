import sys
input = sys.stdin.readline

def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a,b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n,m,k = map(int,input().split())
power = list(map(int,input().split()))
parent = [0]*(n+1)
for i in range(1,n+1):
    if i in power:
        continue
    parent[i] = i

edges = []
for _ in range(m):
    u,v,w = map(int,input().split())
    edges.append((w,u,v))

edges.sort()

result = 0

for edge in edges:
    cost,a,b = edge
    if find(a)!=find(b):
        union(a,b)
        result+=cost
        
print(result)
