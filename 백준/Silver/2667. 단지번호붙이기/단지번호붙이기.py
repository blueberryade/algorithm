from collections import deque

n = int(input())

graph = [list(map(int,input())) for _ in range(n)]

cnt = []

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    cnt = 1
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<n and graph[nx][ny]:
                graph[nx][ny] = 0
                q.append((nx,ny))
                cnt +=1
    return cnt      

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(i,j))


cnt.sort()
print(len(cnt))
for c in cnt:
    print(c)

