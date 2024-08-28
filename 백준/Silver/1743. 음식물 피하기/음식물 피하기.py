import sys
sys.setrecursionlimit(10**6)

n,m,k = map(int,input().split())
graph = [[0]*m for _ in range(n)]

for _ in range(k):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1

visited = [[False]*m for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(x,y):
    global cnt
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny]:
            visited[nx][ny] = True
            cnt+=1
            dfs(nx,ny)

result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = 0
            dfs(i,j)
            result = max(result,cnt)

print(result)