import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
d = deque(enumerate(map(int,input().split())))
result = []
while d:
    idx,paper = d.popleft()
    result.append(idx+1)

    if paper > 0:
        d.rotate(-(paper-1))
    elif paper < 0:
        d.rotate(-paper)
print(' '.join(map(str,result)))