import sys
input = sys.stdin.readline

n,m = map(int,input().split())
r,c,d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] *m for _ in range(n)]

dr = [-1,0,1,0]
dc = [0,1,0,-1]

count = 1
visited[r][c] = 1

while True:
    flag = 0
    for _ in range(4):
        d = (d+3)%4
        nr = r+dr[d]
        nc = c+dc[d]

        if 0<=nr<n and 0<=nc<m and graph[nr][nc]!=1:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                count+=1
                r = nr
                c = nc
                flag = 1
                break
    if flag == 0:
        if graph[r-dr[d]][c-dc[d]] == 1:
            print(count)
            break
        else:
            r = r-dr[d]
            c = c-dc[d]
