import sys
input = sys.stdin.readline
import heapq

V,E = map(int,input().split())
K = int(input())
dp = [sys.maxsize]*(V+1)
graph = [[] for _ in range(V+1)]
pq = []

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))


def dijkstra(start):
    dp[start] = 0
    heapq.heappush(pq,(0,start))

    while pq:
        now_d, now = heapq.heappop(pq)
        if dp[now] < now_d:
            continue
        for next_d,next in graph[now]:
            cost = now_d+next_d
            if cost < dp[next]:
                dp[next] = cost
                heapq.heappush(pq,(cost,next))
            

dijkstra(K)
for i in range(1,V+1):
    if dp[i]==sys.maxsize:
        print("INF")
    else:
        print(dp[i])
