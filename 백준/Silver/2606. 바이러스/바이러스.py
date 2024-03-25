c = int(input())
n = int(input())

A = [[] for _ in range(c+1)]
visited = [0]*(c+1)

for _ in range(n):
    a,b = map(int,input().split())
    A[a].append(b)
    A[b].append(a)

def dfs(cur_v):
    visited[cur_v] = 1
    for v in A[cur_v]:
        if visited[v]==0:
            dfs(v)
dfs(1)
print(sum(visited)-1)
