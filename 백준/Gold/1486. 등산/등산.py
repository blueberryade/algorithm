import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N,M,T,D = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j].isupper():
            graph[i][j] = ord(graph[i][j])-ord("A")
        else:
            graph[i][j] = ord(graph[i][j]) - ord("a")+26

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def dijkstra(i,j):
    time = [[INF]*M for _ in range(N)]
    time[i][j] = 0
    q = []
    heapq.heappush(q,(0,i,j))

    while q:
        now_t,x,y = heapq.heappop(q)
        if time[x][y] < now_t:
            continue

        height = graph[x][y]
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]

            if 0<=nx<N and 0<=ny<M:
                next_height = graph[nx][ny]

                if abs(next_height-height) <= T:
                    if height>= next_height:
                        next_t = now_t +1
                    else:
                        next_t = now_t+(next_height-height)**2

                    if time[nx][ny] > next_t:
                        time[nx][ny] = next_t
                        heapq.heappush(q,(next_t,nx,ny))
    return time

time_lst = dijkstra(0,0)

lst = []
for i in range(N):
    for j in range(M):
        if time_lst[i][j] < D:
            heapq.heappush(lst,(-1*graph[i][j],i,j))

while lst:
    t,x,y = heapq.heappop(lst)
    possible_time = dijkstra(x,y)
    if time_lst[x][y] + possible_time[0][0] <= D:
        print(graph[x][y])
        break