import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N,M = map(int,input().split())
    q = deque()
    lst = list(map(int,input().split()))
    result = 0
    for i in range(len(lst)):
        q.append((lst[i],i))
    while True:
        if q[0][0] == max(q,key=lambda x:x[0])[0]:
            result+=1
            if q[0][1] == M:
                print(result)
                break
            else:
                q.popleft()
        else:
            q.append(q.popleft())        