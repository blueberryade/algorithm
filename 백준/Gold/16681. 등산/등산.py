import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N,M,D,E = map(int,input().split())
graph = [[] for _ in range(N+1)]
data = [0]+list(map(int,input().split()))
for _ in range(M):
    a,b,n = map(int,input().split())
    graph[a].append((n,b))
    graph[b].append((n,a))

def dijkstra(node):
    distance = [INF]*(N+1)
    q = []
    heapq.heappush(q,(0,node))
    distance[node] = 0

    while q:
        dist,now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for cost,next_node in graph[now]:
            new_dist = dist+cost
            if data[now]<data[next_node] and new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(q,(new_dist,next_node))

    return distance

start = dijkstra(1)
end = dijkstra(N)
result = []

for i in range(1,N+1):
    if start[i]!= INF and end[i]!=INF:
        result.append(data[i]*E - D*(start[i]+end[i]))

print(max(result) if result else 'Impossible')
