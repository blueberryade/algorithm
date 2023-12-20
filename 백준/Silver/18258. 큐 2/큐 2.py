import sys
from collections import deque

input = sys.stdin.readline
queue = deque()
n = int(input())

for _ in range(n):
    i = input().split()

    if i[0] == 'push':
        queue.append(i[1])
    elif i[0] == 'pop':
        if len(queue):
            print(queue.popleft())
        else:
            print(-1)
            
    elif i[0] == 'size':
        print(len(queue))
    elif i[0] == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)
    elif i[0] == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif i[0] == 'back':
        if len(queue):
            print(queue[-1])
        else:
            print(-1)