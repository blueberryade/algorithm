import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    global n
    distance = [-INF]*(n+1)
    distance[start] = 0
    route = [0]*(n+1)
    result = []

    for i in range(n):
        for cur in range(1,n+1):
            if distance[cur] == -INF:
                continue

            for next_node,next_cost in graph[cur]:
                if distance[next_node] < distance[cur] +next_cost:
                    distance[next_node] = distance[cur]+next_cost
                    route[next_node] = cur
                
                    if i == n-1:
                        distance[next_node] = INF

    if distance[n] == INF:
        print(-1)
        return
    else:
        result.append(n)
        while(n!=1):
            result.append(route[n])
            n = route[n]

        result.reverse()
        print(*result)
        return


n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))


bf(1)

