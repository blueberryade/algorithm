import sys
from collections import deque
input = sys.stdin.readline

r,c = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(r)]

visited_water = [[False] * c for _ in range(r)]
visited_swan = [[False] * c for _ in range(r)]

swan_q = deque()
sq_tmp = deque()
water_q = deque()
wq_tmp = deque()

dx = [0,1,0,-1]
dy = [1,0,-1,0]
x1,y1 = 0,0
result = 0

def melt():
    while water_q:
        x,y = water_q.popleft()
        graph[x][y] = '.'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited_water[nx][ny]:
                if graph[nx][ny] == '.':
                    water_q.append((nx, ny))
                elif graph[nx][ny] == 'X':
                    wq_tmp.append((nx,ny))    
                visited_water[nx][ny] = True

def find():
    while swan_q:
        x,y = swan_q.popleft()

        if x == x1 and y == y1:
            return True
 
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<r and 0<=ny<c and not visited_swan[nx][ny]:
                visited_swan[nx][ny] = True
                if graph[nx][ny] == '.':
                    swan_q.append((nx,ny))
                else:
                    sq_tmp.append((nx,ny))
    return False   

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'L':
            if not swan_q:
                swan_q.append((i,j))
                visited_swan[i][j] = True
            else:
                x1,y1 = i,j
            graph[i][j] = '.'
                
        if graph[i][j] == '.':
            water_q.append((i,j))
            visited_water[i][j] = True



while True:
    melt()
    if find(): 
        break
   
    swan_q = sq_tmp
    water_q = wq_tmp
    sq_tmp = deque()
    wq_tmp = deque()
    result+=1

print(result) 
  