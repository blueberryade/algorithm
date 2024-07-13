import heapq
import sys
from collections import deque,defaultdict
input = sys.stdin.readline
INF = int(1e9)

def dijkstra():
    distance = [INF]*n
    q = []
    heapq.heappush(q,(0,s))
    distance[s] = 0
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

def bfs(start,end):
    q = deque([end])
    remove_lst = defaultdict(list)
    visited = [False]*n

    while q:
        cur = q.popleft()
        if cur == start or visited[cur]:
            continue
        visited[cur] = True

        for prev,weight in reversed_graph[cur]:
            if distance[prev] + weight == distance[cur]:
                if (cur,weight) in graph[prev]:
                    graph[prev].remove((cur,weight))
                if not visited[prev]:
                    q.append(prev)


    
    

while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    graph = defaultdict(list)
    reversed_graph = defaultdict(list)
    s,d = map(int,input().split())
    for _ in range(m):
        u,v,p = map(int,input().split())
        graph[u].append((v,p))
        reversed_graph[v].append((u,p))

    distance = dijkstra()
    bfs(s,d)
    new_distance = dijkstra()
    
    if new_distance[d] == INF:
        print(-1)
    else:
        print(new_distance[d])