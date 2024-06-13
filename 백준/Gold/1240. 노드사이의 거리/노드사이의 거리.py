from collections import deque

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,dist = map(int,input().split())
    graph[a].append((b,dist))
    graph[b].append((a,dist))

def bfs(a,b):
    q = deque()
    q.append((a,0))
    visited = [False]*(n+1)
    visited[a] = True
    
    while q:
        x,dist = q.popleft()

        if x == b:
            return dist
        for i,d in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append((i,dist+d))


for _ in range(m):
    a,b = map(int,input().split())
    print(bfs(a,b))