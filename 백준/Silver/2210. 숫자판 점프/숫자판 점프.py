board = [list(input().split()) for _ in range(5)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

result = set()

def dfs(x,y,w):
    if len(w) == 6:
        result.add(w)
        return

    for d in range(4):
        nx,ny = x+dx[d],y+dy[d]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx,ny,w+board[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i,j,board[i][j])

print(len(result))