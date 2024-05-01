import sys
input = sys.stdin.readline

n = int(input())
graph = []
teacher = []

for i in range(n):
    graph.append(input().split())
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append([i,j])

dx = [-1,0,1,0]
dy = [0,1,0,-1]

answer = False

def backtracking(cnt):
    global answer
    if cnt == 3:
        if bfs():
            answer = True
            return
    else:
        for x in range(n):
            for y in range(n):
                if graph[x][y] == 'X':
                    graph[x][y] = 'O'
                    backtracking(cnt+1)
                    graph[x][y] = 'X'

def bfs():
    for t in teacher:
        for d in range(4):
            nx,ny = t
            while 0<= nx < n and 0<=ny<n:
                if graph[nx][ny] == 'O':
                    break

                if graph[nx][ny] == 'S':
                    return False
                nx += dx[d]
                ny += dy[d]
    return True

backtracking(0)

if answer:
    print('YES')
else:
    print('NO')

