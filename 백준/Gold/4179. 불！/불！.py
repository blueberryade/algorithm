from collections import deque
import sys
input = sys.stdin.readline

r,c = map(int,input().split())
graph = [list(input()) for _ in range(r)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

jihoon = deque()
fires = deque()

j_visited = [[0]*c for _ in range(r)]
f_visited = [[0]*c for _ in range(r)]


for i in range(r):
    for j in range(c):
        if graph[i][j]=='J':
            jihoon.append((i,j))
            j_visited[i][j] = 1
        if graph[i][j]=='F':
            fires.append((i,j))
            f_visited[i][j] = 1

def bfs():
    while fires:
        x,y = fires.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<r and 0<=ny<c and graph[nx][ny]!='#' and not f_visited[nx][ny]:
                f_visited[nx][ny] = f_visited[x][y]+1
                fires.append((nx,ny))
    while jihoon:
        x,y = jihoon.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >=c:
                return j_visited[x][y]
            if graph[nx][ny]=='#' or j_visited[nx][ny]:
                continue
            if not f_visited[nx][ny] or f_visited[nx][ny]> j_visited[x][y]+1:
                j_visited[nx][ny] = j_visited[x][y]+1
                jihoon.append((nx,ny))

    return 'IMPOSSIBLE'
  
print(bfs())