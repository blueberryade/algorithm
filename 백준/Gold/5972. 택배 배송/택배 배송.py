import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue
        for next,next_dist in graph[cur]:
            cost = dist+next_dist
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q,(cost,next))

dijkstra(1)
print(distance[n])