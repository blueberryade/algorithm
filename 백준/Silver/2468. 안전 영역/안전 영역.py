import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
max_num = 0
graph = []

for i in range(n):
    row = list(map(int,input().split()))
    graph.append(row)
    for i in row:
        if i > max_num:
            max_num = i


dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y,num):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1 

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]>num and visited[nx][ny]==0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))

result = []

for i in range(max_num):
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j,k,i)
                cnt+=1
    result.append(cnt)

print(max(result))