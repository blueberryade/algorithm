r,c = map(int,input().split())
board = []

for _ in range(r):
    board.append(list(input()))
visited = set()
visited.add(board[0][0])
dx = [1,0,-1,0]
dy = [0,1,0,-1]

result = 1

def dfs(x,y,cnt):
    global result
    result = max(result,cnt)

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<r and 0<=ny<c and not board[nx][ny] in visited:
            visited.add(board[nx][ny])
            dfs(nx,ny,cnt+1)
            visited.remove(board[nx][ny])           
dfs(0,0,1)
print(result)
