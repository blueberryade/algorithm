from collections import deque

dx = [0,1,0,-1,-1,-1,1,1]
dy = [1,0,-1,0,-1,1,-1,1]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    graph[i][j] = 0

    while q:
        x,y = q.popleft()

        for d in range(8):
            nx,ny = x+dx[d],y+dy[d]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==1:
                q.append((nx,ny))
                graph[nx][ny] = 0


N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

result = 0

for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            bfs(i,j)
            result+=1

print(result)