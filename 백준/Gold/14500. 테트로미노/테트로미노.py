import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

max_value = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y,dsum,cnt):
    global max_value
    if cnt == 4:
        max_value = max(max_value,dsum)
        return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx,ny,dsum+board[nx][ny],cnt+1)
            visited[nx][ny] = False

def exce(x,y):
    global max_value
    for i in range(4):
        tmp = board[x][y]
        for j in range(3):
            t = (i+j)%4
            nx = x+dx[t]
            ny = y+dy[t]

            if not (0<=nx<n and 0<=ny<m):
                tmp = 0
                break
            tmp+= board[nx][ny]
        max_value = max(max_value,tmp)

for x in range(n):
    for y in range(m):
        visited[x][y] = True
        dfs(x,y,board[x][y],1)
        visited[x][y] = False
        exce(x,y)
print(max_value)        
