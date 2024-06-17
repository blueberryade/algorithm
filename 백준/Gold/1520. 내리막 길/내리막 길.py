import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m,n = map(int,input().split())
graph = []
dp = [[-1]*n for _ in range(m)]

for _ in range(m):
    graph.append(list(map(int,input().split())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(x,y):
    if x == m-1 and y == n-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    cnt = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<m and 0<=ny<n and graph[x][y]>graph[nx][ny]:
            cnt += dfs(nx,ny)

    dp[x][y] = cnt
    return dp[x][y]


print(dfs(0,0))
