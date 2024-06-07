import sys
input = sys.stdin.readline
INF = int(1e9)

v,e = map(int,input().split())
graph = [[INF]*(v+1) for _ in range(v+1)]


for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a][b] = c

for k in range(1,v+1):
    for a in range(1,v+1):
        for b in range(1,v+1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]

min_cycle = INF
for i in range(1,v+1):
    if graph[i][i] < min_cycle:
        min_cycle = graph[i][i]


if min_cycle == INF:
    print(-1)
else:
    print(min_cycle)    