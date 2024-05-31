import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    time = list(map(int,input().split()))
    dp = [0]*(n+1)
    
    for _ in range(k):
        a,b = map(int,input().split())
        graph[a].append(b)
        indegree[b]+=1

    w = int(input())  

    q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i-1]
    while q:
        now = q.popleft()
        for i in graph[now]:
            dp[i] = max(time[i-1]+dp[now],dp[i])
            indegree[i]-=1
            if indegree[i] == 0:
                q.append(i)

    print(dp[w])