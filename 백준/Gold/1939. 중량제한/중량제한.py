import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

start,end = map(int,input().split())

def bfs(mid):
    visited = [False]*(n+1)
    q = deque()
    q.append(start)

    while q:
        x = q.popleft()
        for y,w in graph[x]:
            if not visited[y] and w>=mid:
                visited[y] = True
                q.append(y)

    return visited[end]                 

low,high = 1,sys.maxsize
result = low

while low <=high:
    mid = (low+high) //2
    if bfs(mid):
        result = mid
        low = mid+1
    else:
        high = mid-1
        
print(result)

