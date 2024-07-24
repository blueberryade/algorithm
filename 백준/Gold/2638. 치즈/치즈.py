import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==0 and graph[nx][ny]==0:
                    q.append((nx,ny))
                    visited[nx][ny]=1
                elif graph[nx][ny]==1:
                    visited[nx][ny] = visited[nx][ny]+1

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

result = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]

while True:
    visited = [[0]*m for _ in range(n)]
    bfs()
    result+=1

    for i in range(n):
        for j in range(m):
            if visited[i][j]>=2:
                graph[i][j] = 0
    
    cnt = 0
    for i in range(n):
        cnt+=sum(graph[i])
    if cnt == 0:
        break

print(result)

