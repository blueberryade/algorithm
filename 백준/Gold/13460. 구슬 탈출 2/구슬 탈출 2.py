from collections import deque
import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def move(x,y,dx,dy):
    move_count = 0
    while graph[x+dx][y+dy]!= '#' and graph[x][y]!='O':
        x+=dx
        y+=dy
        move_count+=1
    return x,y,move_count

def bfs(rx,ry,bx,by):
    q = deque()
    q.append((rx,ry,bx,by,0))
    visited = set((rx,ry,bx,by))

    while q:
        rx,ry,bx,by,depth = q.popleft()

        if depth >= 10:
            continue

        for i in range(4):
            nrx,nry,r_moves = move(rx,ry,dx[i],dy[i])
            nbx,nby,b_moves = move(bx,by,dx[i],dy[i])

            if graph[nbx][nby] == 'O':
                continue

            if graph[nrx][nry] == 'O':
                return depth+1
            
            if nrx == nbx and nry == nby:
                if r_moves > b_moves:
                    nrx-=dx[i]
                    nry-=dy[i]
                else:
                    nbx-=dx[i]
                    nby-=dy[i]
            if (nrx,nry,nbx,nby) not in visited:
                visited.add((nrx,nry,nbx,nby))
                q.append((nrx,nry,nbx,nby,depth+1))
    
    return -1                


n,m = map(int,input().split())
graph = [list(input()) for _ in range(n)]

rx,ry,bx,by = 0,0,0,0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx,ry = i,j
        elif graph[i][j] == 'B':
            bx,by = i,j

print(bfs(rx,ry,bx,by))


