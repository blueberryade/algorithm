import sys
input = sys.stdin.readline

def dfs(v,i):
    visited[v] = True

    for k in graph[v]:
        if not visited[k]:
            dfs(k,i)
        elif visited[k] and k == i:
            result.append(k)


n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(1,n+1):
    graph[int(input())].append(i)

result = []

for i in range(1,n+1):
    visited = [False]*(n+1)
    dfs(i,i)

print(len(result))
for i in result:
    print(i)