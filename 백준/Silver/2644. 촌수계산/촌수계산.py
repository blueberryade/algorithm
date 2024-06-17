n = int(input())
a,b = map(int,input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
result = [0]*(n+1)

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(cur):
    visited[cur] = True
    for i in graph[cur]:
        if not visited[i]:
            result[i] = result[cur]+1
            dfs(i)

dfs(a)

if result[b]>0:
    print(result[b])
else:
    print(-1)