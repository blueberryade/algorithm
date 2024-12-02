import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = list(input().rstrip())
    n = int(input())
    q = deque(input().rstrip()[1:-1].split(","))
    flag = True
    r = 0

    if n == 0:
        q = deque()
    
    for i in p:
        if i == 'D':
            if len(q) == 0:
                flag = False
                print('error')
                break
            else:
                if r%2==0:
                    q.popleft()
                else:
                    q.pop()
        else:
            r+=1

    if flag:
        if r%2 == 0:
            print('['+','.join(q)+']') 
        else:
            q.reverse()
            print('['+','.join(q)+']') 