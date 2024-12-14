from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False]*(N+1)
visited[1] = True
q = deque([(0,1)])
result = 0

while q:
    depth,x = q.popleft()
    if depth == 2:
        break
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            result+=1
            q.append((depth+1,i))

print(result)