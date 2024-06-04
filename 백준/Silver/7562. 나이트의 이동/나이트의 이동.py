import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    dx = [-1,1,-2,2,2,-2,1,-1]
    dy = [-2,-2,-1,-1,1,1,2,2]

    q = deque()
    q.append((start_x,start_y))
    graph[start_x][start_y] = 1
    
    while q:
        x,y = q.popleft()
        if x == end_x and y == end_y:
            return graph[x][y]-1
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx < l and 0 <= ny<l and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx,ny))

t = int(input())
for _ in range(t):
    l = int(input())
    start_x,start_y = map(int,input().split())
    end_x,end_y = map(int,input().split())
    graph = [[0]*l for _ in range(l)]
    
    print(bfs())



