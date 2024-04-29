import sys
from collections import deque
from copy import deepcopy
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
x_y = [(x,y) for x in range(m) for y in range(n) if not graph[y][x]]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

result = 0

def bfs(graph):
    q = deque([(j, i) for i in range(n) for j in range(m) if graph[i][j] == 2])

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n and not graph[ny][nx]:
                graph[ny][nx] = 2
                q.append((nx,ny))
    global result
    cnt = sum(row.count(0) for row in graph)
    result = max(result,cnt)

for c in combinations(x_y,3):
    tmp_graph = deepcopy(graph)
    for x,y in c:
        tmp_graph[y][x] = 1
    bfs(tmp_graph)

print(result)