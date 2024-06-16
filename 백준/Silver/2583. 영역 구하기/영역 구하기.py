from collections import deque

m,n,k = map(int,input().split())
graph = [[0]*n for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = 1

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(i,j):
    q = deque()
    q.append((i,j))  
    cnt = 1
    graph[i][j] = 1

    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x+ dx[d]
            ny = y+ dy[d]
            if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nx,ny))
                cnt+=1
    return cnt

result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result.append(bfs(i,j))

print(len(result))
print(*sorted(result))


