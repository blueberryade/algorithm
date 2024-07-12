INF = int(1e9)
n = int(input())
m = int(input())

distance  = [[INF]*(n+1) for _ in range(n+1)]
path = [[()]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    distance[i][i] = 0
    path[i][i] = [0]

for _ in range(m):
    a,b,c = map(int,input().split())
    if c < distance[a][b]:
        distance[a][b] = c
    path[a][b] = (a,b)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if distance[i][j] > distance[i][k]+distance[k][j]:
                distance[i][j] = distance[i][k]+distance[k][j]
                path[i][j] = path[i][k] + path[k][j][1:]


for i in range(1,n+1):
    for j in range(1,n+1):
        if distance[i][j] == INF:
            print(0,end=' ')
        else:
            print(distance[i][j],end=' ')
    print()    

for i in range(1,n+1):
    for j in range(1,n+1):
        if len(path[i][j]) ==1:
            print(0)
        else:
            print(len(path[i][j]),*path[i][j])
