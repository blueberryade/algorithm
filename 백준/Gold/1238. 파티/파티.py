import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,t = map(int,input().split())
    graph[s].append((e,t))

def dijkstra(start):
    distance = [INF]*(n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q:
        cur_cost,now = heapq.heappop(q)
        if distance[now] < cur_cost:
            continue
        for next,c in graph[now]:
            cost = distance[now] + c
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q,(cost,next))
    return distance


result = []                                                                     
for i in range(1,n+1):
    result.append(dijkstra(i)[x]+dijkstra(x)[i])
print(max(result))