import sys
input = sys.stdin.readline

graph = []
N = int(input())
for _ in range(N):
    lst = list(map(int,input().split()))
    graph.append(lst)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] ==1 and graph[k][j] == 1:
                graph[i][j] = 1

for i in graph:
    print(*i)