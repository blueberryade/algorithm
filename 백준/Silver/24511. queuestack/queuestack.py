import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
m = int(input())
c = list(map(int,input().split()))

res = deque()

for i in range(n):
    if a[i] == 0:
        res.appendleft(b[i])
for i in range(m):
    res.append(c[i])
    print(res.popleft(),end=' ')

