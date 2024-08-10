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



n,m = map(int,input().split())
gender = [0] + input().split()
parent = [i for i in range(n+1)]
edges = []
for _ in range(m):
    u,v,d = map(int,input().split())  
    edges.append((d,u,v))

edges.sort()

result = 0
cnt = 0

for edge in edges:
    d,a,b = edge
    if find(a)!=find(b) and gender[a]!=gender[b]:
        union(a,b)
        result+=d
        cnt+=1

if cnt == n-1:
    print(result)
else:
    print(-1)
