import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

s,t = map(int,input().split())

distance = [INF]*(n+1)

def dijkstra(start,end):
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dist,now = heapq.heappop(q)

        if distance[now]< dist:
            continue

        for next_cost,next in graph[now]:
            cost = dist+next_cost
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q,(cost,next))
    return distance[end]

print(dijkstra(s,t))