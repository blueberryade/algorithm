import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

pre = [0]*(n+1)


def dijkstra(i,j):
    distance = [INF]*(n+1)
    distance[1] = 0
    q = []
    heapq.heappush(q,(0,1))

    while q:
        dist,now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for next,next_cost in graph[now]:
            if (now == i and next == j) or (now == j and next == i):
                continue
            cost = next_cost+dist
            if cost < distance[next]:
                distance[next] = cost
                if not i:
                    pre[next] = now
                heapq.heappush(q,(cost,next))
    return distance[n]

distance = dijkstra(0,0)

result = 0
e = n

while pre[e]!=0:
    s = pre[e]
    dist = dijkstra(s,e)

    if dist == INF:
        result = -1
        break
    result = max(result,dist-distance)
    e = s
        
print(result)