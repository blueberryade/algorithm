import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,c = map(int,input().split())
    graph[v].append((c,u))
target = list(map(int,input().split()))


def dijkstra():
    q = []
    for t in target:
        heapq.heappush(q,(0,t))
        result[t] = 0

    while q:
        dist,now = heapq.heappop(q)

        if result[now] < dist:
            continue

        for next_dist,next in graph[now]:
            cost = next_dist+dist
            if cost < result[next]:
                result[next] = cost
                heapq.heappush(q,(cost,next))
                
max_start,max_cost = 0,0
result = [INF]*(n+1)
dijkstra()
for i,e in enumerate(result):
    if e > max_cost and e != INF:
        max_start,max_cost = i,e
print(max_start)
print(max_cost)
