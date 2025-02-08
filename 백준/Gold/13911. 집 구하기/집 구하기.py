import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V,E = map(int,input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))
M,x = map(int,input().split())
mac_nodes = list(map(int,input().split()))
S,y = map(int,input().split())
star_nodes = list(map(int,input().split()))


def dijkstra(nodes):
    distance = [INF]*(V+1)
    q = []

    for node in nodes:
        heapq.heappush(q,(0,node))
        distance[node] = 0
    
    while q:
        dist,now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for cost,next_node in graph[now]:
            new_dist = dist+cost
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(q,(new_dist,next_node))
    return distance


dist_mac = dijkstra(mac_nodes)
dist_star = dijkstra(star_nodes)

result = INF

for i in range(1,V+1):
    if i in mac_nodes or i in star_nodes:
        continue
    if dist_mac[i]<=x and dist_star[i]<=y:
        result = min(result,dist_mac[i]+dist_star[i])

print(result if result!=INF else -1)