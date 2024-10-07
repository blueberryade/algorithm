from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    cnt = 2

    while q:
        x = q.popleft()
        
        for i in graph[x]:
            if not visited[i]:
                visited[i] = cnt
                q.append(i)
                cnt+=1


n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)    

for i in range(n+1):
    graph[i].sort()

bfs(r)
for i in visited[1:]:
    print(i)