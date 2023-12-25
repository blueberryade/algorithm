import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = []
now = 1
line = deque(list(map(int,input().split())))

while line:
    if now == line[0]:
        line.popleft()
        now+=1
    elif len(q) != 0 and now == q[-1]:
        q.pop()
        now +=1
    else:
        if len(q) == 0 or (len(q) != 0 and q[-1] > line[0]):
            q.append(line.popleft())
        else:
            print("Sad")
            exit(0)
if len(q) != 0:
    for i in range(len(q)-1,-1,-1):
        if now == q[i]:
            now +=1
        else:
            print("Sad")
            exit(0)
print("Nice")
