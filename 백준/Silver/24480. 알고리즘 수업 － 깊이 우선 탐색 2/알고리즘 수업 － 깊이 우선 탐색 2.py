import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(n+1)
result = [0]*(n+1)
cnt = 1

def dfs(v):
    global cnt

    visited[v] = True
    result[v] = cnt

    for i in sorted(graph[v],reverse=True):
        if not visited[i]:
            cnt+=1
            dfs(i)

dfs(r)
for i in result[1:]:
    print(i)