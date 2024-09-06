import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,d = map(int,input().split())
    graph[a].append((b,d*2))
    graph[b].append((a,d*2))

def dijkstra_fox():
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q,(0,1))
    distance[1] = 0

    while q:
        dist,now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for next,c in graph[now]:
            cost = dist+c
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q,(cost,next))
    
    return distance

def dijkstra_wolf():
    distance = [[INF]*(n+1) for _ in range(2)]
    q = []
    heapq.heappush(q,(0,1,0))
    distance[0][1] = 0

    while q:
        cur_dist,cur,state = heapq.heappop(q)

        if distance[state][cur] < cur_dist:
            continue

        for next,weight in graph[cur]:
            if state == 0:
                cost = cur_dist + weight //2
                if distance[1][next] > cost:
                    distance[1][next] = cost
                    heapq.heappush(q,(cost,next,1))
            else:
                cost = cur_dist + weight *2
                if distance[0][next] > cost:
                    distance[0][next] = cost
                    heapq.heappush(q,(cost,next,0))
    
    return distance

fox = dijkstra_fox()
wolf = dijkstra_wolf()

result = 0
for i in range(1,n+1):
    if fox[i] < min(wolf[0][i],wolf[1][i]):
        result+=1
print(result)