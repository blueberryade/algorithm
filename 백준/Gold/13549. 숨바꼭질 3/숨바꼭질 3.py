import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
limit = 100001
time = [0]*limit
visited = [False]*limit

def bfs(x,y):
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        if x == y:
            return time[x]

        if -1<x*2<limit and visited[x*2]==0:
            q.appendleft(x*2)
            time[x*2] = time[x]
            visited[x*2] = True
        if -1<x-1<limit and visited[x-1] == 0:
            q.append(x-1)
            time[x-1] = time[x]+1
            visited[x-1] = True
        if -1<x+1<limit and visited[x+1] == 0:
            q.append(x+1)
            time[x+1] = time[x]+1
            visited[x+1] = True

print(bfs(n,k))        


