import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n,m,k = map(int,input().split())
s,d = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,w = map(int,input().split())
    graph[a].append((w,b))
    graph[b].append((w,a))

charge = [int(input()) for _ in range(k)]
distance = [[INF]*n for _ in range(n+1)]

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,0,start))
    distance[start][0] = 0

    while q:
        dist,cnt,now = heapq.heappop(q)
        flag = False

        for i in range(cnt+1):
            if dist > distance[now][i]:
                flag = True
                break
        
        if flag or cnt == n-1:
            continue

        for next_dist,next_node in graph[now]:
            cost = next_dist+distance[now][cnt]
            if cost < distance[next_node][cnt+1]:
                distance[next_node][cnt+1] = cost
                heapq.heappush(q,(cost,cnt+1,next_node))


dijkstra(s)

result = INF
count = 0
for i in range(n):
    if result > distance[d][i]:
        result = distance[d][i]
        count = i
print(result)

tax = 0
for c in charge:
    tax += c
    result = INF
    for i in range(count+1):
        if result > distance[d][i]+tax*i:
            result = distance[d][i]+ tax*i
            count = i

    print(result)


