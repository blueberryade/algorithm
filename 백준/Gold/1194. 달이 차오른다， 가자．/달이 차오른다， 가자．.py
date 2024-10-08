from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
start_x,start_y = 0,0

for i in range(n):
    row = list(input().rstrip())
    graph.append(row)
    for j in range(m):
        if row[j] == '0':
            start_x,start_y = i,j


dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(i,j):
    visited = [[[False] * (1 << 6) for _ in range(m)] for _ in range(n)]
    q = deque([(i,j,0,0)])
    visited[i][j][0] = True

    while q:
        x,y,keys,cnt = q.popleft()

        if graph[x][y] == '1':
            return cnt

        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == '#':
                    continue

                if 'a' <= graph[nx][ny]<='f':
                    new_keys = keys | (1 << (ord(graph[nx][ny]) - ord('a')))
                    if not visited[nx][ny][new_keys]:
                        visited[nx][ny][new_keys] = True
                        q.append((nx,ny,new_keys,cnt+1))
                    

                elif 'A' <= graph[nx][ny]<='F':
                    if keys & (1 << (ord(graph[nx][ny]) - ord('A'))):
                        if not visited[nx][ny][keys]:
                            visited[nx][ny][keys] = True
                            q.append((nx,ny,keys,cnt+1))
                  

                else:
                    if not visited[nx][ny][keys]:
                        visited[nx][ny][keys] = True
                        q.append((nx,ny,keys,cnt+1))

    return -1


print(bfs(start_x,start_y))
