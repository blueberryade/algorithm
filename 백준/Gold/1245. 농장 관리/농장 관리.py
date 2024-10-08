n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,1,-1,-1,0,1]

def dfs(x,y):
    global flag
    visited[x][y] = True

    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny] > graph[x][y]:
                flag = False
            if graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                dfs(nx,ny)



result = 0
visited = [[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m): 
        if not visited[i][j]:
            flag = True
            dfs(i,j)
            if flag:
                result+=1

print(result)