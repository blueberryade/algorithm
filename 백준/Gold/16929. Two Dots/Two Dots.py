import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(x,y,start_x,start_y,color):
    if visited[x][y]:
        return True
    visited[x][y] = True
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m and board[nx][ny]==color:
            if not (nx == start_x and ny == start_y):
                if dfs(nx,ny,x,y,color):
                    return True
                
    return False
    


n,m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
result = False

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if dfs(i,j,-1,-1,board[i][j]):
                result = True
                break

if result:
    print('Yes')
else:
    print('No')                
                

