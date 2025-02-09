import sys
from collections import deque
input = sys.stdin.readline

graph = [[0]*501 for _ in range(501)]
visited = [[False]*501 for _ in range(501)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

N = int(input())
for _ in range(N):
    x1,y1,x2,y2 = list(map(int,input().split()))
    for i in range(min(x1,x2),max(x1,x2)+1):
        for j in range(min(y1,y2),max(y1,y2)+1):
            graph[i][j] = 1

M = int(input())
for _ in range(M):
    x1,y1,x2,y2 = list(map(int,input().split()))
    for i in range(min(x1,x2),max(x1,x2)+1):
        for j in range(min(y1,y2),max(y1,y2)+1):
            graph[i][j] = 2

def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0] = True

    while q:
        x,y,life = q.popleft()

        if x == 500 and y == 500:
            return life

        for d in range(4):
            nx,ny = x+dx[d],y+dy[d]

            if 0<=nx<501 and 0<=ny<501:
                if graph[nx][ny] != 2 and not visited[nx][ny]:
                    if graph[nx][ny]==1:
                        q.append((nx,ny,life+1))
                    else:
                        q.appendleft((nx,ny,life))
                    visited[nx][ny] = True

    return -1

print(bfs())