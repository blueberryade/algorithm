from collections import deque
import sys
input = sys.stdin.readline

F,S,G,U,D = map(int,input().split())
visited = [-1]*(F+1)

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 0

    while q:
        cur = q.popleft()

        if cur == G:
            return visited[cur]
        
        if cur+U <=F and visited[cur+U] == -1:
            visited[cur+U] = visited[cur]+1
            q.append(cur+U)

        if cur-D >0 and visited[cur-D] == -1:
            visited[cur-D] = visited[cur]+1
            q.append(cur-D)

    return "use the stairs"


print(bfs(S))
