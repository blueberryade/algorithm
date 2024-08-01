import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr[-1] = 0

graph = [[] for _ in range(n)]
for _ in range(m):
    a,b,t = map(int,input().split())
    graph[a].append((t,b))
    graph[b].append((t,a))
distance = [INF]*n

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)

        if distance[now]< dist:
            continue
        
        for next_cost,next in graph[now]:
            cost = dist+next_cost

            if cost < distance[next] and arr[next]==0:
                distance[next] = cost
                heapq.heappush(q,(cost,next))
    
          
dijkstra(0)

if distance[n-1] == INF:
    print(-1)
else:
    print(distance[n-1])
