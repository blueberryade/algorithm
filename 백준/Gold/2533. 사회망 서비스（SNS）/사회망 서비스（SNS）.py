import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n+1)]
dp = [[0,1] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(start):
    visited[start] = True
    for next in tree[start]:
        if not visited[next]:
            visited[next] = True
            dfs(next)
            dp[start][0]+=dp[next][1]
            dp[start][1]+=min(dp[next])

dfs(1)
print(min(dp[1]))
