import sys
import heapq
input = sys.stdin.readline

n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a,b,cost = map(int,input().split())
    graph[a].append((cost,b))
    graph[b].append((cost,a))



def dijkstra(start):
    distance = [sys.maxsize]*(n+1)
    distance [start] = 0
    pq = []
    heapq.heappush(pq,(0,start))    

    while pq:
        dist,now = heapq.heappop(pq)

        if  distance[now] < dist:
            continue
        
        for i,j in graph[now]:
            cost = dist + i

            if distance[j] > cost:
                distance[j] = cost
                heapq.heappush(pq,(cost,j))
    return distance

stop1,stop2 = map(int,input().split())

total = dijkstra(1)
stop1_distance = dijkstra(stop1)
stop2_distance = dijkstra(stop2)

path1 = total[stop1] + stop1_distance[stop2] + stop2_distance[n]
path2 = total[stop2] + stop2_distance[stop1] + stop1_distance[n]

result = min(path1,path2)
if result < sys.maxsize:
    print(result)
else:
    print(-1)
    