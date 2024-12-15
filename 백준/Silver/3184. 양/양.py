from collections import deque

R,C = map(int,input().split())
board = [list(input().rstrip()) for _ in range(R)]

visited = [[False]*C for _ in range(R)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    o,v = 0,0
    if board[i][j] == 'o':
        o+=1
    elif board[i][j] == 'v':
        v+=1

    while q:
        x,y = q.popleft()

        for d in range(4):
            nx,ny = x+dx[d],y+dy[d]

            if 0<=nx<R and 0<=ny<C and board[nx][ny]!='#':
                if not visited[nx][ny]:
                    if board[nx][ny]=='o':
                        o+=1
                    elif board[nx][ny]=='v':
                        v+=1
                    q.append((nx,ny))
                    visited[nx][ny] = True
    if o > v:
        return o,0
    else:
        return 0,v


sheep = 0
wolf = 0

for i in range(R):
    for j in range(C):
        if board[i][j]!= '#' and not visited[i][j]:
            o,v = bfs(i,j)
            sheep+=o
            wolf+=v

print(sheep,wolf)