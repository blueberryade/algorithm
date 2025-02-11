import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for r in range(n):
    for c in range(n):
        if 0>r-1 and 0>c-1:
            continue
        prev_r,prev_c = INF,INF

        if 0<=r-1:
            prev_r = dp[r-1][c] +(0 if graph[r][c]<graph[r-1][c] else graph[r][c]-graph[r-1][c]+1)
        
        if 0<=c-1:
            prev_c = dp[r][c-1] +(0 if graph[r][c]<graph[r][c-1] else graph[r][c]-graph[r][c-1]+1)
        dp[r][c] = min(prev_r,prev_c)

print(dp[n-1][n-1])