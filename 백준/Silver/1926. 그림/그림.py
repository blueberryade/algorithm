from collections import deque

n,m = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))


dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    count = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny]==1:
                count+=1
                visited[nx][ny] = True
                q.append((nx,ny))
    return count


visited = [[False]*m for _ in range(n)]
cnt = 0
result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            result = max(result,bfs(i,j))
            cnt+=1

print(cnt)
print(result)


