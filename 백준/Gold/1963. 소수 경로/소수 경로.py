from collections import deque
import sys
input = sys.stdin.readline

def findPrime():
    for i in range(2,100):
        if prime[i]:
            for j in range(2*i,10000,i):
                prime[j] = False

def bfs(a,b):
    q = deque()
    q.append((a,0))

    visited = [False]*10000
    visited[a] = True

    while q:
        now,cnt = q.popleft()
        if now == b:
            print(cnt)
            return
        
        for i in range(4):
            for j in range(10):
                temp = list(str(now))
                temp[i] = str(j)
                temp = int(''.join(temp))
                if 1000<=temp and not visited[temp] and prime[temp]:
                    visited[temp] = True
                    q.append((temp,cnt+1))


t = int(input())
prime = [True for _ in range(10000)]
findPrime()

for _ in range(t):
    a,b = map(int,input().split())
    bfs(a,b) 