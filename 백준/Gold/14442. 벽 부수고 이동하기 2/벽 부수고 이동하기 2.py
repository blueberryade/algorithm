from collections import deque
import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]

def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1

    while q:
        x,y,z = q.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][z]
        
        for d in range(4):
            nx,ny = x+dx[d],y+dy[d]

            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] == '0' and not visited[nx][ny][z]:
                    visited[nx][ny][z] = visited[x][y][z]+1
                    q.append((nx,ny,z))
                elif graph[nx][ny] == '1' and z<K and visited[nx][ny][z+1] == 0:
                    visited[nx][ny][z+1] = visited[x][y][z]+1
                    q.append((nx,ny,z+1))
    return -1

print(bfs())
