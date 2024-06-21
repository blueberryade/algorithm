import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(s):
    q = []
    distance = [INF]*(n+1)
    heapq.heappush(q,(0,s))
    distance[s] = 0
    
    while q:
        dist,cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue
        for next,next_dist in graph[cur]:
            cost = next_dist+dist
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q,(cost,next))
    return distance


T = int(input())
for _ in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))

    xList = [int(input()) for _ in range(t)]
    result = []
    total = dijkstra(s)
    if total[g] > total[h]:
        stop = g
    else:
        stop = h
    stop_dist = dijkstra(stop)
    for x in xList:
        if total[stop] + stop_dist[x] == total[x]:
            result.append(x)
    result.sort()        
    print(*result)
