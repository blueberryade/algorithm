from collections import deque
import sys
input = sys.stdin.readline

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs(i,j,k):
    q.append((i,j,k))
    visited[i][j][k] = 1

    while q:
        x,y,z = q.popleft()

        for d in range(6):
            nx = x+dx[d]
            ny = y+dy[d]
            nz = z+dz[d]

            if 0<=nx<l and 0<=ny<r and 0<=nz<c:
                if graph[nx][ny][nz] == "E":
                    print(f"Escaped in {visited[x][y][z]} minute(s).")
                    return
                
                if graph[nx][ny][nz] == "." and visited[nx][ny][nz] == 0:
                    visited[nx][ny][nz] = visited[x][y][z]+1
                    q.append((nx,ny,nz))
                    
    print("Trapped!")

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    graph = []
    visited = [[[0]*c for _ in range(r)] for _ in range(l)]
    q = deque()

    for _ in range(l):
        graph.append([list(input().rstrip()) for _ in range(r)])
        input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == "S":
                    bfs(i,j,k)
                    