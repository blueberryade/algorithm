import sys
import math
input = sys.stdin.readline
INF = math.inf

t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        u,v,c,d = map(int,input().split())
        graph[u].append((v,c,d))        

    dp = [[INF]*(m+1) for _ in range(n+1)]
    dp[1][0] = 0
    
    for cost in range(m+1):
        for city in range(1,n+1):
            if dp[city][cost] != INF:
                for next,c,d in graph[city]:
                    new_dist = dp[city][cost]+d
                    new_cost = cost+c

                    if new_cost <=m and new_dist <dp[next][new_cost]:
                        dp[next][new_cost] = new_dist

    answer = min(dp[n])

    if answer!=INF:
        print(answer)
    else:
        print("Poor KCM")


