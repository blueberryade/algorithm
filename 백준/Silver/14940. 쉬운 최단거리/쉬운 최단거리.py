import sys
from collections import deque
input = sys.stdin.readline

direction = [(-1,0),(1,0),(0,-1),(0,1)]
N,M = map(int,input().split())
graph = list(input().split() for _ in range(N))
visited = [[False]* M for _ in range(N)]
res = [[0]* M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j]=="2":
            visited[i][j] = True
            q = deque([(i,j)])

while q:
    x, y = q.popleft()
    for dx, dy in direction:
        nx = x+dx
        ny = y+dy

        if 0<=nx<N and 0<=ny<M and graph[nx][ny]=="1" and not visited[nx][ny]:
            q.append((nx,ny))
            visited[nx][ny] = True
            res[nx][ny]= res[x][y]+1

for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j]=="1":
            print(-1,end=" ")
        else:
            print(res[i][j], end=" ")
    print()