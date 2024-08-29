import sys
from itertools import combinations
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

def attack(archor):
    temp = deepcopy(graph)
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(N-1,-1,-1):
        die = []
        for a in archor:
            q = deque()
            q.append((i,a,1))
            while q:
                x,y,d = q.popleft()
                if temp[x][y] == 1:
                    die.append((x,y))
                    if visited[x][y] == 0:
                        visited[x][y] = 1
                        cnt+=1
                    break
                if d < D:
                    for j in range(3):
                        nx = x+dx[j]
                        ny = y+dy[j]
                        if 0<=nx<N and 0<=ny<M:
                            q.append((nx,ny,d+1))
        for x,y in die:
            temp[x][y] = 0

    return cnt

N,M,D = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

dx = [0,-1,0]
dy = [-1,0,1]
result = 0

for c in combinations(range(M),3):
    result = max(result,attack(c))

print(result)

