import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
bamboo = [list(map(int,input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
dp = [[-1]*n for _ in range(n)]

def dfs(x,y):
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 1
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]

        if 0<=nx<n and 0<=ny<n and bamboo[x][y] < bamboo[nx][ny]:
            dp[x][y] = max(dp[x][y],dfs(nx,ny)+1)

    return dp[x][y]



result = 0
for i in range(n):
    for j in range(n):
        result = max(result,dfs(i,j))

print(result)