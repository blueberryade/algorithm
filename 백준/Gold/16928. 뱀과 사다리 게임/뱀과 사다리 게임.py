import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
board = [0]*101
visited = [False]* 101

ladder = dict()
snake = dict()

for _ in range(n):
    a,b = map(int,input().split())
    ladder[a] = b
for _ in range(m):
    a,b = map(int,input().split())
    snake[a] = b

q = deque([1])

while q:
    x = q.popleft()
    if x == 100:
        print(board[x])
    for d in range(1,7):
        next_place = x + d
        if next_place <= 100 and not visited[next_place]:
            if next_place in ladder.keys():
                next_place = ladder[next_place]
            if next_place in snake.keys():
                next_place = snake[next_place]
            if not visited[next_place]:
                visited[next_place] = True
                board[next_place] = board[x]+1
                q.append(next_place)
