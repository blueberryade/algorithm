import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N,M = map(int,input().split())
s,e = map(int,input().split())

graph = [[] for _ in range(N+1)]
distance = [0]*(N+1)

for _ in range(M):
    a,b,k = map(int,input().split())
    graph[a].append((k,b))
    graph[b].append((k,a))

q = []
heapq.heappush(q,(-INF,s))
distance[s] = INF

while q:
    dist,now = heapq.heappop(q)
    dist = -dist
    if distance[now] > dist:
        continue

    for next_dist,next in graph[now]:
        cost = min(dist,next_dist)
        if distance[next] < cost:
            distance[next] = cost
            heapq.heappush(q,(-cost,next))

print(distance[e])