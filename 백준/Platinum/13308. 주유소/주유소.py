import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
price = [0]+list(map(int,input().split()))

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

def dijkstra():
    distance = [[INF]*(max(price)+1) for _ in range(n+1)]
    distance[1][price[1]] = 0
    q = []
    heapq.heappush(q,(0,price[1],1))

    while q:
        dist,cost,now = heapq.heappop(q)

        if now == n:
            return dist

        if dist > distance[now][cost]:
            continue

        for next_dist,next in graph[now]:
            next_cost = min(price[next],cost)
            new_dist = dist + cost*next_dist

            if distance[next][next_cost] > new_dist :
                distance[next][next_cost] = new_dist
                heapq.heappush(q,(new_dist,next_cost,next))

    return -1

print(dijkstra())
