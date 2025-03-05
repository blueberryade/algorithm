import sys
input = sys.stdin.readline

N,K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

visited = [False]*N
visited[K] = True
result = sys.maxsize

def find(cur,cost,cnt):
    global result

    if N == cnt:
        result = min(result,cost)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            find(i,cost+graph[cur][i],cnt+1)
            visited[i] = False

find(K,0,1)
print(result)
