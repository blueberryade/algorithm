import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
visited = [[False]*(n) for _ in range(n)]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x,y = q.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if graph[nx][ny] == graph[x][y]:
                    q.append((nx,ny))
                    visited[nx][ny] = True

result1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            result1+=1

result2 = 0   
visited = [[False]*(n) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            result2+=1
print(result1,result2)
