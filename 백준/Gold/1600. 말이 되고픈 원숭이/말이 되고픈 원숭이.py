import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
w,h = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(h)]
visited = [[[0]*(k+1) for _ in range(w)] for _ in range(h)]

dist = [(0,1),(1,0),(0,-1),(-1,0)]
horse = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]


def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1

    while q:
        x,y,z = q.popleft()

        if x == h-1 and y == w-1:
            return visited[x][y][z]-1
        
        for i,j in dist:
            nx = x+i
            ny = y+j

            if 0<=nx<h and 0<=ny<w and not visited[nx][ny][z] and not graph[nx][ny]:
                visited[nx][ny][z] = visited[x][y][z]+1
                q.append((nx,ny,z))
        
        if z<k:
            for hi,hj in horse:
                hx = x+hi
                hy = y+hj
                if 0<=hx<h and 0<=hy<w and not graph[hx][hy]:
                    if not visited[hx][hy][z+1]:
                        visited[hx][hy][z+1] = visited[x][y][z]+1
                        q.append((hx,hy,z+1))

    return -1

print(bfs())

