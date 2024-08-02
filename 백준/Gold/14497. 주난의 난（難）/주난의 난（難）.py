import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
x1,y1,x2,y2 = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x1,y1):
    distance = [[INF]*m for _ in range(n)]
    q = deque()
    q.append((x1,y1))
    distance[x1][y1] = 0

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                cost = 1 if graph[nx][ny]!='0' else 0
                if cost + distance[x][y] < distance[nx][ny]:
                    distance[nx][ny] = cost + distance[x][y]
                    if cost == 1:
                        q.append((nx,ny))
                    else:
                        q.appendleft((nx,ny))

    return distance[x2-1][y2-1]
    
                   
print(bfs(x1-1,y1-1))