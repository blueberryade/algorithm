import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))
    if n == 0:
        arr = deque()

    r = 0
    flag = 0

    for f in p:
        if f == 'D':
            if len(arr) == 0:
                flag = 1
                print('error')
                break
            else:
                if r%2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
        else:
            r+=1                   
    if flag == 0:
        if r % 2 == 0:
            print('['+','.join(arr)+']')     
        else:
            arr.reverse()
            print('['+','.join(arr)+']')