import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,cost = map(int,input().split())
    graph[a].append((cost,b))
    graph[b].append((cost,a))

distance = [[INF]*(k+1) for _ in range(n+1)]

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start,0))
    distance[start][0] = 0

    while q:
        dist,now,cnt = heapq.heappop(q)

        if dist > distance[now][cnt]:
            continue

        for next_dist,next in graph[now]:
            cost = dist+next_dist
            if cost < distance[next][cnt]:
                distance[next][cnt] = cost
                heapq.heappush(q,(cost,next,cnt))
            
            if cnt < k and dist <distance[next][cnt+1]:
                distance[next][cnt+1] = dist
                heapq.heappush(q,(dist,next,cnt+1))


dijkstra(1)
print(min(distance[n]))