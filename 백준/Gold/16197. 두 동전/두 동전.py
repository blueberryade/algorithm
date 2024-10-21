from collections import deque

n,m = map(int,input().split())

graph = [list(input().rstrip()) for _ in range(n)]
coins = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'o':
            coins.append((i,j))

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def bfs():
    q = deque()
    q.append((coins[0][0],coins[0][1],coins[1][0],coins[1][1],0))

    while q:
        x1,y1,x2,y2,cnt = q.popleft()

        if cnt >=10:
            return -1
        
        for d in range(4):
            nx1,ny1 = x1+dx[d],y1+dy[d]
            nx2,ny2 = x2+dx[d],y2+dy[d]

            if 0<=nx1<n and 0<=ny1<m and 0<=nx2<n and 0<=ny2<m:
                if graph[nx1][ny1] == '#':
                    nx1,ny1 = x1,y1
                if graph[nx2][ny2] == '#':
                    nx2,ny2 = x2,y2
                q.append((nx1,ny1,nx2,ny2,cnt+1))
            elif 0<=nx1<n and 0<=ny1 < m:
                return cnt+1
            elif 0<=nx2<n and 0<=ny2<m:
                return cnt+1
            
            
    return -1

print(bfs())
