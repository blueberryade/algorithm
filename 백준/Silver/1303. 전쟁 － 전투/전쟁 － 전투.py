from collections import deque

N,M = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(M)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

visited = [[False]*N for _ in range(M)]

white,blue = 0,0

def bfs(i,j,color):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    cnt = 1

    while q:
        x,y = q.popleft()
        for d in range(4):
            nx,ny = x+dx[d],y+dy[d]

            if 0<=nx<M and 0<=ny<N and not visited[nx][ny]:
                if graph[nx][ny] == color:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    cnt+=1
    
    return cnt


for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            if graph[i][j] == 'W':
                white+=bfs(i,j,'W')**2
            else:
                blue+=bfs(i,j,'B')**2

print(white,blue)




