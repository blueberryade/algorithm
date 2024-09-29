from collections import deque
import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]
graph = [list(input().rstrip()) for _ in range(12)]
result = 0

def bfs(i,j):   
    visited[i][j] = True
    q = deque([(i,j)])
    color = graph[i][j]
    puyo = [(i,j)]

    while q:
        x,y = q.popleft()

        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]

            if 0<=nx<12 and 0<=ny<6:
                if not visited[nx][ny] and graph[nx][ny]== color:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    puyo.append((nx,ny))

    if len(puyo)>=4:
        return puyo
    else:
        return []



while True:
    bomb = []
    visited = [[False]*6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if graph[i][j]!="." and not visited[i][j]:
                temp = bfs(i,j)
                if temp:
                    bomb.extend(temp)

    if not bomb:
        break
    
    for x,y in bomb:
        for i in range(x,0,-1):
            graph[i][y] = graph[i-1][y]
        graph[0][y] = '.'
        
    result+=1

print(result)