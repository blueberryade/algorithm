from collections import deque
import sys
input = sys.stdin.readline

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def bfs(sy, sx):
    q = deque()
    visited = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]
    for d in range(4):
        q.append((sy, sx, d))
        visited[sy][sx][d] = 1
    while q:
        cy, cx, cdir = q.popleft()
        dy, dx = direction[cdir]
        ny, nx = cy, cx
        while True:
            ny, nx = ny + dy, nx + dx
            if not (0 <= ny < n and 0 <= nx < n) or board[ny][nx] == '*':
                break
            if board[ny][nx] == '!':
                if not visited[ny][nx][cdir]:
                    q.append((ny, nx, cdir))
                    visited[ny][nx][cdir] = visited[cy][cx][cdir]
                if not visited[ny][nx][(cdir + 1) % 4]:
                    q.append((ny, nx, (cdir + 1) % 4))
                    visited[ny][nx][(cdir + 1) % 4] = visited[cy][cx][cdir] + 1
                if not visited[ny][nx][(cdir - 1) % 4]:
                    q.append((ny, nx, (cdir - 1) % 4))
                    visited[ny][nx][(cdir - 1) % 4] = visited[cy][cx][cdir] + 1
            elif board[ny][nx] == '#':
                return visited[cy][cx][cdir] - 1


n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

sy = sx = ey = ex = -1
for r in range(n):
    for c in range(n):
        if board[r][c] == '#':
            if sy == -1:
                sy, sx = r, c
                board[sy][sx] = 'S'
            else:
                ey, ex = r, c

print(bfs(sy, sx))