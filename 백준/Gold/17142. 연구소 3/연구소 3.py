from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i,j))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(active_virus):
    visited = [[-1]*n for _ in range(n)]
    q = deque()
    
    for (i,j) in active_virus:
        q.append((i,j))
        visited[i][j] = 0

    max_time = 0
    empty_space = sum(row.count(0) for row in graph)
    virus_space = 0

    while q:
        x,y = q.popleft()

        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]

            if 0<=nx <n and 0<=ny<n and visited[nx][ny]==-1:
                    if graph[nx][ny]!=1:
                        visited[nx][ny] = visited[x][y]+1
                        q.append((nx,ny))

                        if graph[nx][ny] == 0:
                            virus_space+=1
                            max_time = visited[nx][ny]

                            if virus_space == empty_space:
                                return max_time
    
    if virus_space != empty_space:
        return float('inf')
    
    return max_time     
    

result = float('inf')

for c in combinations(virus,m):
    time = bfs(c)
    result = min(result,time)

if result != float('inf'):
    print(result)
else:
    print(-1)
