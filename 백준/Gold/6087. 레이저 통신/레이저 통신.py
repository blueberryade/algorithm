import sys
from collections import deque
input = sys.stdin.readline

w, h = map(int, input().split())
board = [list(input().strip()) for _ in range(h)]
position = []

for i in range(h):
    for j in range(w):
        if board[i][j] == 'C':
            position.append((i, j))

(x1, y1), (x2, y2) = position

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    mirror = [[float('inf')] * w for _ in range(h)]
    q = deque()

    for d in range(4):
        nx, ny = x1 + dx[d], y1 + dy[d]
        if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != '*':
            q.append((nx, ny, d, 0))
            mirror[nx][ny] = 0

    mirror[x1][y1] = 0

    while q:
        x, y, direction, cnt = q.popleft()

        if (x, y) == (x2, y2):
            return cnt

        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != '*':
            if cnt <= mirror[nx][ny]:
                mirror[nx][ny] = cnt
                q.appendleft((nx, ny, direction, cnt))

        for d in range(4):
            if d != direction:
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != '*':
                    if cnt + 1 < mirror[nx][ny]:
                        mirror[nx][ny] = cnt + 1
                        q.append((nx, ny, d, cnt + 1))

    return float('inf')

print(bfs())
