import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,r,q = map(int,input().split())
tree = [[] for _ in range(n+1)]
dp = [0]*(n+1)

def dfs(x):
    dp[x] = 1
    for i in tree[x]:
        if not dp[i]:
            dfs(i)
            dp[x] += dp[i]

for _ in range(n-1):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)
dfs(r)
for _ in range(q):
    u = int(input())
    print(dp[u])