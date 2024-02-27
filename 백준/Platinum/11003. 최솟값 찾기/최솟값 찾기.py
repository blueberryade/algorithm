import sys
from collections import deque
input = sys.stdin.readline

n,l = map(int,input().split())
d = deque()
now = list(map(int,input().split()))

for i in range(n):
    while d and d[-1][0] > now[i]:
        d.pop()
    d.append((now[i],i))
    if d[0][1] <= i-l:
        d.popleft()
    print(d[0][0],end=' ')
