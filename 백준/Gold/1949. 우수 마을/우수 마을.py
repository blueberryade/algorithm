import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
data = list(map(int,input().split()))
dp = [[0,0] for _ in range(n+1)]
tree = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(node):
    visited[node] = True

    dp[node][1]+=data[node-1]
    for i in tree[node]:
        if not visited[i]:
            dfs(i)
            dp[node][0]+=max(dp[i])
            dp[node][1]+=dp[i][0]

dfs(1)
print(max(dp[1]))