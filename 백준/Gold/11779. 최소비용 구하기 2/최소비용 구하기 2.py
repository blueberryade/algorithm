import heapq
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a,b,cost = map(int,input().split())
    graph[a].append((cost,b))

start,end = map(int,input().split())

cnt = 0
prev = [0]*(n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q,(start,0))
    distance[start] = 0
    while q:
        now,dist = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for c,next in graph[now]:
            cost = dist+c
            if cost < distance[next]:
                distance[next] = cost
                prev[next] = now
                heapq.heappush(q,(next,cost))
                
dijkstra(start)


result = []
tmp = end
while tmp!=start:
    result.append(str(tmp))
    tmp = prev[tmp]
result.append(str(start))
print(distance[end])
print(len(result))
print(*result[::-1])