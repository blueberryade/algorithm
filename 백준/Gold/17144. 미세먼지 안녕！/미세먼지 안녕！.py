import sys
input = sys.stdin.readline

R,C,T = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(R)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

purifier = []

for i in range(R):
    if graph[i][0] == -1:
        purifier.append((i,0))


def diffusion():
    graph_tmp = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j]!=0 and graph[i][j]!=-1:
                tmp = 0
                for d in range(4):
                    nx,ny = i+dx[d],j+dy[d]
                    if 0<=nx<R and 0<=ny<C and graph[nx][ny]!=-1:
                        graph_tmp[nx][ny]+=graph[i][j]//5
                        tmp+=graph[i][j]//5
                graph[i][j]-=tmp
    
    for i in range(R):
        for j in range(C):
            graph[i][j]+=graph_tmp[i][j]


def operate():
    i,j = purifier[0]
    temp = 0
    while 0<=j+1<C:
        temp,graph[i][j+1] = graph[i][j+1],temp
        j+=1
    while 0<= i-1 < R:
        temp,graph[i-1][j] = graph[i-1][j],temp
        i-=1
    while 0<= j-1 < C:
        temp,graph[i][j-1] = graph[i][j-1],temp
        j-=1
    while 0<=i+1<R and graph[i+1][j]!=-1:
        temp,graph[i+1][j] = graph[i+1][j],temp
        i+=1


    i,j = purifier[1]
    temp = 0
    while 0<=j+1<C:
        temp,graph[i][j+1] = graph[i][j+1],temp
        j+=1
    while 0<= i+1 < R:
        temp,graph[i+1][j] = graph[i+1][j],temp
        i+=1
    while 0<= j-1 < C:
        temp,graph[i][j-1] = graph[i][j-1],temp
        j-=1
    while 0<=i-1<R and graph[i-1][j]!=-1:
        temp,graph[i-1][j] = graph[i-1][j],temp
        i-=1



for _ in range(T):
    diffusion()
    operate()



result = 0

for i in range(R):
    for j in range(C):
        if graph[i][j] > 0:
            result+=graph[i][j]

print(result)