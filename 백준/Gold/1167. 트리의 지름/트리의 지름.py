import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
tree =[[] for _ in range(v+1)]

for _ in range(v):
    data = list(map(int,input().split()))
    u = data[0]
    idx = 1
    while data[idx] !=-1:
        a = data[idx]
        b = data[idx+1]
        tree[u].append((a,b))
        idx+=2


def bfs(start):
    visited = [-1]*(v+1)
    q = deque()
    q.append(start)
    visited[start] = 0
    res = [0,0]

    while q:
        cur = q.popleft()
        for next,d in tree[cur]:
            if visited[next] == -1:
                visited[next] = visited[cur]+d
                q.append(next)
                if res[0] < visited[next]:
                    res = visited[next],next
    return res


dis,node = bfs(1)
dis,node = bfs(node)

print(dis)
    