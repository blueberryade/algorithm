import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra():
    q = []
    heapq.heappush(q,(0,c))
    time[c] = 0

    while q:
        cur_time,cur = heapq.heappop(q)

        for next,next_time in graph[cur]:
            t = next_time + cur_time
            if t < time[next]:
                time[next] = t
                heapq.heappush(q,(t,next))
            

t = int(input())

for _ in range(t):
    n,d,c = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    time = [INF] * (n+1)
    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((a,s))

    dijkstra()
    cnt = 0
    endTime = 0
    for t in time:
        if t < INF:
            cnt+=1
            if t > endTime:
                endTime = t
    print(cnt,endTime)                

