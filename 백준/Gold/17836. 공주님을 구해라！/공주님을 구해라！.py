from collections import deque
import sys
input = sys.stdin.readline

n,m,t = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    q = deque()
    q.append((0,0))
    visited = [[-1]*m for _ in range(n)]
    visited[0][0] = 0
    sword = 10001

    while q:
        x,y = q.popleft()

        if x == n-1 and y == m-1:
            return min(sword,visited[x][y])
        if graph[x][y] == 2:
            sword = visited[x][y]+ n-x-1 + m-y-1

        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]

            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1:
                if graph[nx][ny]!=1:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y]+1
                  
    return sword
result = bfs()
if result > t:
    print("Fail")
else:
    print(result)