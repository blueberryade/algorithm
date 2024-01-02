import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
d = deque()
for _ in range(n):
    num = list(map(int,input().split()))
    l = len(d)
    if num[0] == 1:
        d.appendleft(num[1])
    elif num[0] == 2:
        d.append(num[1])
    elif num[0] == 3:
        print(d.popleft() if l else -1)
    elif num[0] == 4:
        print(d.pop() if l else -1)
    elif num[0] == 5:
        print(len(d))
    elif num[0] == 6:
        print(0 if l else 1)
    elif num[0] == 7:
        print(d[0] if l else -1)
    elif num[0] == 8:
        print(d[-1] if l else -1)    
        
