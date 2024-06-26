import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int,input().split())
graph = []


tomato = []

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            tomato.append((i,j))


q = deque(tomato)
    
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx< n and 0<=ny< m and graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y]+1
            q.append((nx,ny))


answer = 0

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    answer = max(answer,max(i))

print(answer-1)
