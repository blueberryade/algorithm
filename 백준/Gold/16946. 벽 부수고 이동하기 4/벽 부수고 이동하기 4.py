from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(N)]

visited = [[False]*M for _ in range(N)]
zeros = [[0]*M for _ in range(N)]
result = [[0]*M for _ in range(N)]

group = 1
info = {}

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    cnt = 1

    while q:
        x,y = q.popleft()
        zeros[x][y] = group

        for d in range(4):
            nx,ny = x+dx[d],y+dy[d]

            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    cnt+=1
    return cnt

def move_count(x,y):
    data = set()

    for d in range(4):
        nx,ny = x+dx[d],y+dy[d]
        if 0<=nx<N and 0<=ny<M and zeros[nx][ny]:
            data.add(zeros[nx][ny])

    cnt = 1
    for c in data:
        cnt+=info[c]
        cnt%=10
    
    return cnt


for i in range(N):
    for j in range(M):
        if not graph[i][j] and not visited[i][j]:
            cnt = bfs(i,j)
            info[group] = cnt
            group+=1

for i in range(N):
    for j in range(M):
        if graph[i][j]:
            result[i][j] = move_count(i,j)

for i in result:
    print(''.join(map(str,i)))


