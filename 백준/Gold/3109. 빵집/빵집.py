import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

r,c = map(int,input().split())
dx = [-1,0,1]
dy = [1,1,1]
result = 0

def dfs(x,y):
    if y == c-1:
        return True
    
    for i in range(3):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<r and 0<=ny<c and graph[nx][ny]=='.':
            graph[nx][ny] = 'x'
            if dfs(nx,ny):
                return True
    return False

graph = []
for _ in range(r):
    graph.append(list(input()))

for x in range(r):
    if dfs(x,0):
        result+=1

print(result)