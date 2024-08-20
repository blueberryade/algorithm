import sys
from collections import deque
input = sys.stdin.readline

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    while fire:
        x, y = fire.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != '#' and fire_visited[nx][ny] == -1:
                fire_visited[nx][ny] = fire_visited[x][y] + 1
                fire.append((nx, ny))
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == '.' and visited[nx][ny] == -1:
                    if fire_visited[nx][ny] == -1 or visited[x][y] + 1 < fire_visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
            else:
                return visited[x][y] + 1
    
    return "IMPOSSIBLE"


T = int(input())

for _ in range(T):
    w, h = map(int, input().split())
    graph = [list(input().rstrip()) for i in range(h)]

    fire_visited = [[-1] * w for _ in range(h)]
    visited = [[-1] * w for _ in range(h)]
    fire = deque()
    q = deque()

    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*': 
                fire.append((i, j))
                fire_visited[i][j] = 0
            elif graph[i][j] == '@':  
                q.append((i, j))
                visited[i][j] = 0

    print(bfs())

