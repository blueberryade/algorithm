import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
visited = [[-1]*n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 0

    while q:
        x,y = q.popleft()

        if x == n-1 and y == n-1:
            return visited[x][y]
    
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1:
                if graph[nx][ny] == 1:
                    q.appendleft((nx,ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y]+1

print(bfs())

