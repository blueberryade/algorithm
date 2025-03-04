import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
road = [[True]*N for _ in range(N)]

result = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i==j or i == k or k == j:
                continue
            if graph[i][j] == graph[i][k]+graph[k][j]:
                road[i][j] = False
            elif graph[i][j] > graph[i][k]+graph[k][j]:
                result = -1

if not result:
    for i in range(N):
        for j in range(i,N):
            if road[i][j]:
                result+=graph[i][j]

print(result)