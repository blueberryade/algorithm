import sys
input = sys.stdin.readline
INF = sys.maxsize

def find(x):
    if parent[x]!=x:
        return find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0


for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

    if find(a)!=find(b):
        union(a,b)

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])



group = {}
for i in range(1,n+1):
    temp = find(i)
    if temp not in group:
        group[temp] = []
    group[temp].append(i)

result = []
for group in group.values():
    dist = INF
    representative = None
    for member in group:
        temp = max(graph[member][other] for other in group)
        if temp < dist:
            dist = temp
            representative = member
    result.append(representative)


result.sort()

print(len(result))
for i in result:
    print(i)
