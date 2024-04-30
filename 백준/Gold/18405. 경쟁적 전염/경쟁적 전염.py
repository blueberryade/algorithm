import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
graph = []

for _ in range(1,n+1):
    graph.append(list(map(int,input().split())))

s,x,y = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            virus.append((graph[i][j],i,j,0))
virus.sort()
q = deque(virus)

while q:
    v,row,col,time = q.popleft()
    if s == time:
        break
    for i in range(4):
        nx = row+dx[i]
        ny = col+dy[i]
        if 0<=nx<n and 0<=ny<n and not graph[nx][ny]:
            graph[nx][ny] = v
            q.append((v,nx,ny,time+1))
            
print(graph[x-1][y-1])