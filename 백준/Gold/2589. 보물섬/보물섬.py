import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(input().rstrip()))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(a,b):
    visited = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((a,b))
    visited[a][b] = 0
    cnt = 0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1:
                if graph[nx][ny]== 'L':
                    visited[nx][ny] = visited[x][y]+1
                    cnt = max(cnt,visited[nx][ny])
                    q.append((nx,ny))

    return cnt  

result = 0
for i in range(n):
    for j in range(m):
      if graph[i][j] == 'L':
        result = max(result,bfs(i,j))

print(result)

      


