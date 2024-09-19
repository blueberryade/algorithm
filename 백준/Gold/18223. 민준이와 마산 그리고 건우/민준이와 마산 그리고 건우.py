import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

V,E,P = map(int,input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


def dijkstra(start,end):    
    distance = [INF]*(V+1)
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dist,now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance[end]

if dijkstra(1,V) == dijkstra(1,P)+dijkstra(P,V):
    print("SAVE HIM")
else:
    print("GOOD BYE")
