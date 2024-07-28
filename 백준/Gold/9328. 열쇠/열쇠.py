from collections import deque
import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def unlock():
    for r in range(h+2):
        for c in range(w+2):
            if maps[r][c].lower() in keys:
                maps[r][c] = '.'
    keys.clear()

def bfs():
    global result
    q = deque([(0,0)])
    visited = [[0]*(w+2) for _ in range(h+2)]
    visited[0][0] = 1

    while q:
        x,y = q.popleft()

        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]

            if 0<= nx < h+2 and 0<= ny < w+2 and not visited[nx][ny]:
                if maps[nx][ny] == '*':
                    continue
                if ord('A') <= ord(maps[nx][ny]) <= ord('Z'):
                    continue
                if maps[nx][ny] == '$':
                    result+=1
                if ord('a')<=ord(maps[nx][ny]) <= ord('z'):
                    keys.append(maps[nx][ny])
                q.append((nx,ny))
                maps[nx][ny] = '.'
                visited[nx][ny] = 1
                    



t = int(input())
for _ in range(t):
    h,w = map(int,input().split())
    maps = [['.'] * (w+2)]
    for _ in range(h):
        row = '.'+ input().rstrip() +'.'
        maps.append(list(''.join(row)))
    maps.append(['.']*(w+2))
    keys = deque(list(''.join(input().rstrip())))
    result = 0
    while keys:
        if keys[0] == '0':
            keys.clear()
        if keys:
            unlock()
        bfs()
    print(result)

