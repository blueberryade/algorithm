import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

    k = int(input())
    friends = list(map(int,input().split()))
    total_distance = [0]*(n+1)

    def dijkstra(start):
        distance[start] = 0
        q = []
        heapq.heappush(q,(0,start))

        while q:
            dist,now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for next,c in graph[now]:
                cost = dist+c
                if cost < distance[next]:
                    distance[next] = cost
                    heapq.heappush(q,(cost,next)) 

    
    for i in friends:
        distance = [INF]*(n+1)
        dijkstra(i)
        for j in range(1,n+1):
            total_distance[j]+=distance[j]
    
    result = 0
    min_num = INF
    for i in range(1,n+1):
        if min_num > total_distance[i]:
            min_num = total_distance[i]
            result = i
    print(result)