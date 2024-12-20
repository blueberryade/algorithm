from collections import deque

N = int(input())
r1,c1,r2,c2 = map(int,input().split())

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]
visited = [[-1]*N for _ in range(N)]

def bfs():
    q = deque([(r1,c1)])
    visited[r1][c1] = 0

    while q:
        x,y = q.popleft()

        if x==r2 and y==c2:
            return visited[x][y]

        for d in range(6):
            nx,ny = x+dx[d],y+dy[d]

            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==-1:
                q.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
    return -1

print(bfs())