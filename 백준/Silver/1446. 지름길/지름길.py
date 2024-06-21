import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue
        for i in graph[cur]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
n,d = map(int,input().split())
graph = [[] for _ in range(d+1)]
distance = [INF]*(d+1)

for i in range(d):
    graph[i].append((i+1,1))


for _ in range(n):
    s,e,l = map(int,input().split())
    if e > d:
        continue
    graph[s].append((e,l))



dijkstra(0)
print(distance[d])
