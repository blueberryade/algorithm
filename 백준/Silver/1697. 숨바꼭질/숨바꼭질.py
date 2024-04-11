import sys
from collections import deque

input = sys.stdin.readline

N,K = map(int,input().split())
max = 100001
arr = [0]*max

def bfs():
    q = deque()
    q.append(N)
    while q:
        cur = q.popleft()
        if cur == K:
            return arr[cur]
            
        for next in (cur+1,cur-1,cur*2):
            if 0<=next<max and not arr[next]:
                arr[next] = arr[cur]+1
                q.append(next)

print(bfs())