import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

N,P,K = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(P):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(mid):
    distance = [[INF]*(K+1) for _ in range(N+1)]
    distance[1][0] = 0
    q = []
    heapq.heappush(q,(0,1,0))

    while q:
        dist,now,free = heapq.heappop(q)

        if distance[now][free] < dist:
            continue

        for next,next_c in graph[now]:
            if next_c > mid and free < K:
                if distance[next][free+1] > dist:
                    distance[next][free+1] = dist
                    heapq.heappush(q,(dist,next,free+1))
            
            if next_c <=mid:
                if distance[next][free] > dist:
                    distance[next][free] = dist
                    heapq.heappush(q,(dist,next,free))

    return min(distance[N])

left,right = 0,10000000
result = -1

while left <= right:
    mid = (left+right) // 2

    if dijkstra(mid)!=INF:
        result = mid
        right = mid-1

    else:
        left = mid+1

print(result)
