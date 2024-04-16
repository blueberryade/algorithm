import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]


for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start):
    visited = [start]
    num = [0]*(N+1)
    queue = deque()
    queue.append(start)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                num[v] = num[cur_v]+1
                visited.append(v)
                queue.append(v)
    return sum(num)

result = []
for i in range(1,N+1):
    result.append(bfs(graph,i))

print(result.index(min(result))+1)