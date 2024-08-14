import sys
input = sys.stdin.readline

N,e,w,s,n = map(int,input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]
direction = [e/100,w/100,s/100,n/100]

def dfs(x,y,percent,step):
    global answer
    if step == N:
        answer+=percent
        return

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if visited[nx][ny]:
            continue

        visited[nx][ny] = True
        dfs(nx,ny,percent*direction[i],step+1)
        visited[nx][ny] = False

answer = 0
visited = [[False]*(2*N+1) for _ in range(2*N+1)]
visited[N][N] = True

dfs(N,N,1,0)

print(answer)