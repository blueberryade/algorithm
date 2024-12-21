from collections import deque

N,M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [1,0,-1,0,1,1,-1,-1]
dy = [0,1,0,-1,-1,1,-1,1]
q = deque()

def bfs():
    while q:
        x, y = q.popleft()
        for d in range(8):
            nx,ny = x+dx[d],y+dy[d]	

            if 0<=nx<N and 0<=ny<M and not graph[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))


for i in range(N):
    for j in range(M):
        if graph[i][j]:
            q.append((i, j))

bfs()

print(max(map(max, graph))-1)