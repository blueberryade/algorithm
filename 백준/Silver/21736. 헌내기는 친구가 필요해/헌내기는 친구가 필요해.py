import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
start_x,start_y = 0,0

for i in range(n):
    tmp = list(input().rstrip())
    for j in range(m):
        if tmp[j] == 'I':
            start_x = i
            start_y = j
    graph.append(tmp)

dx = [1,0,-1,0]
dy = [0,1,0,-1]
visited = [[False]*m for _ in range(n)]

q = deque()
q.append((start_x,start_y))
visited[start_x][start_y] = True
result = 0
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny]!='X':
            visited[nx][ny] = True
            q.append((nx,ny))
            if graph[nx][ny] == 'P':
                result+=1

if result:
    print(result)
else:
    print('TT')    


               