from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

indegree = [0] *(n+1)
graph = [[] for _ in range(n+1)]
part = [[0]*(n+1) for _ in range(n+1)]
 
for _ in range(m):
    x,y,k = map(int,input().split())
    graph[y].append((x,k))
    indegree[x]+=1

q = deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()

    for next,cnt in graph[now]:
        if part[now].count(0) == n+1:
            part[next][now]+=cnt
        else:
            for i in range(1,n+1):
                part[next][i]+=part[now][i]*cnt

        indegree[next]-=1
   
        if indegree[next] == 0:
            q.append(next)

for x in enumerate(part[n]):
    if x[1] > 0:
        print(*x)
 