import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
superior = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for i in range(2, n+1):  
    graph[superior[i-1]].append(i)  

result = [0] * (n + 1)
for _ in range(m):
    i, w = map(int, input().split())
    result[i] += w


def dfs(node):
    for child in graph[node]:
        result[child] += result[node] 
        dfs(child)

dfs(1)

print(*result[1:])  