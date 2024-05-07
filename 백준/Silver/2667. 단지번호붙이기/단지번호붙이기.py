import sys
n = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
result = []
cnt = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x, y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n:
        return

    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if graph[i][j]:
            dfs(i,j)
            result.append(cnt)
            cnt = 0

result.sort()

print(len(result))

for i in result:
    print(i)