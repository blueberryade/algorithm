import sys
input = sys.stdin.readline
import heapq

N = int(input())
M = int(input())
dp = [sys.maxsize]*(N+1)
graph = [[] for _ in range(N+1)]
pq = []

for _ in range(M):
    s,e,w = map(int,input().split())
    graph[s].append((w,e))

start_index,end_index = map(int,input().split())

def dijkstra(start):
    dp[start] = 0
    heapq.heappush(pq,(0,start))

    while pq:
        now_cost,now = heapq.heappop(pq)
        if dp[now] < now_cost:
            continue
        for next_cost,next in graph[now]:
            cost = now_cost+next_cost
            if cost < dp[next]:
                dp[next] = cost
                heapq.heappush(pq,(cost,next))


dijkstra(start_index)
print(dp[end_index])