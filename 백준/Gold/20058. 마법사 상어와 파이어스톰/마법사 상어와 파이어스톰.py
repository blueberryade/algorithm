from collections import deque
import sys
input = sys.stdin.readline

N,Q = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(2**N)]
data = list(map(int,input().split()))


dx = [0,1,0,-1]
dy = [1,0,-1,0]

def rotate(level):
    n = 2**level
    new_graph = [[0]*(2**N) for _ in range(2**N)]
    for x in range(0,2**N,n):
        for y in range(0,2**N,n):
            for i in range(n):
                for j in range(n):
                    new_graph[y+j][x+n-i-1] = graph[y+i][x+j]

    return new_graph

def melt():
    new_graph = [[0]*(2**N) for _ in range(2**N)]

    for i in range(2**N):
        for j in range(2**N):
            ice_cnt = 0
            
            for d in range(4):
                nx,ny = i+dx[d],j+dy[d]

                if 0<=nx<2**N and 0<=ny<2**N:
                    if graph[nx][ny]>0:
                        ice_cnt+=1
            
            if ice_cnt < 3:
                new_graph[i][j] = graph[i][j]-1
            else:
                new_graph[i][j] = graph[i][j]
    return new_graph


for i in data:
    graph = rotate(i)
    graph = melt()


total = 0
max_size = 0

visited = [[False]*(2**N) for _ in range(2**N)]

for i in range(2**N):
    for j in range(2**N):
        if not visited[i][j] and graph[i][j]>0:
            q = deque()
            q.append((i,j))
            total+=graph[i][j]
            now_size = 1
            visited[i][j] = True

            while q:
                x,y = q.popleft()

                for d in range(4):
                    nx,ny = x+dx[d],y+dy[d]

                    if 0<=nx<2**N and 0<=ny<2**N and not visited[nx][ny]:
                        if graph[nx][ny]>0:
                            q.append((nx,ny))
                            total+=graph[nx][ny]
                            visited[nx][ny] = True
                            now_size+=1
            max_size = max(max_size,now_size)



print(total)
print(max_size)