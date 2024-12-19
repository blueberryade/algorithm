from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

graph = [list(input().rstrip()) for _ in range(5)]
positions = [(i,j) for i in range(5) for j in range(5)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
result = 0

def check(comb):
    dasom = 0
    for x,y in comb:
        if graph[x][y] == 'S':
            dasom+=1
    
        if dasom>=4:
            return True

    return False

def bfs(comb):
    visited = [False]*7
    cnt = 1

    q = deque()
    q.append(comb[0])
    visited[0] = True
    

    while q:
        x,y = q.popleft()

        for d in range(4):
            nx,ny = x+dx[d],y+dy[d]

            if (nx,ny) in comb:
                next = comb.index((nx,ny))
                if not visited[next]:
                    q.append((nx,ny))
                    visited[next] = True
                    cnt+=1
    return cnt == 7

for comb in combinations(positions,7):
    if check(comb):
        if bfs(comb):
            result+=1

print(result)