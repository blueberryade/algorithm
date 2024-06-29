import sys
from collections import deque
input = sys.stdin.readline

r,c = map(int,input().split())

graph = [list(input().rstrip()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]
water = deque()
q = deque()

for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            water.append((i,j))
        elif graph[i][j] == 'S':
            q.append((i,j,0))
            visited[i][j] = True

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    while q:
        for _ in range(len(water)):
            wx,wy = water.popleft()
            for i in range(4):
                nwx = wx+dx[i]
                nwy = wy+dy[i]
                if 0<=nwx<r and 0<=nwy<c and graph[nwx][nwy] == '.':
                    graph[nwx][nwy] = '*'
                    water.append((nwx,nwy))
        
        for _ in range(len(q)):
            x,y,step = q.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:
                    if graph[nx][ny] == 'D':
                        return step+1
                    if graph[nx][ny] == '.':
                        visited[nx][ny] = True
                        q.append((nx,ny,step+1))                
    return 'KAKTUS'


print(bfs())

