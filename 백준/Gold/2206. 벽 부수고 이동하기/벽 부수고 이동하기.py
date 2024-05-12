import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

visited = [[[0,0] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y,z):
    q = deque()
    q.append((x,y,z))

    while q:
        a,b,c = q.popleft()

        if a == n-1 and b == m-1:
            return visited[a][b][c]
        for i in range(4):
            nx = a+ dx[i]
            ny = b+ dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1 and c == 0:
                    visited[nx][ny][1] = visited[a][b][0]+1
                    q.append((nx,ny,1))
                elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[a][b][c]+1
                    q.append((nx,ny,c))
    return -1

print(bfs(0,0,0))