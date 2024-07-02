from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
num = 1
result = int(1e9)

def bfs(i,j):
    q = deque()
    q.append((i,j))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    graph[nx][ny] = num
                    q.append((nx,ny))

def bfs2(island):
    q = deque()
    distance = [[-1]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == island:
                q.append((i,j)) 
                distance[i][j] = 0
    
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]!= island and graph[nx][ny]:
                    return distance[x][y]
                elif graph[nx][ny]==0 and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y]+1
                    q.append((nx,ny))
    return int(1e9)


for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and not visited[i][j]:
            visited[i][j] = True
            graph[i][j] = num
            bfs(i,j)
            num+=1

for i in range(1,num):
    result = min(result,bfs2(i))

print(result)    