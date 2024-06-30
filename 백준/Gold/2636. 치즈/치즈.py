import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
total = 0

for i in range(n):
    graph.append(list(map(int,input().split())))
    total += sum(graph[i])


dx = [0,1,0,-1]
dy = [1,0,-1,0]
    

def bfs():
    q = deque()
    q.append((0,0))
    melt = []
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if graph[nx][ny] == 0:
                    q.append((nx,ny))
                elif graph[nx][ny] == 1:
                    melt.append((nx,ny))
      
    for x,y in melt:
        graph[x][y] = 0
    
    return len(melt)
                     

result = 1

while True:
    visited = [[0]*m  for _ in range(n)]
    melt = bfs()
    total-= melt

    if total == 0:
        print(result)
        print(melt)
        break
    result+=1
    
