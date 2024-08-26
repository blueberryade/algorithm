n,m = map(int,input().split())

heavy = [[0]*(n+1) for _ in range(n+1)]
light = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    heavy[a][b] = 1
    light[b][a] = 1


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if heavy[i][k] and heavy[k][j]:
                heavy[i][j]  = 1
            if light[i][k] and light[k][j]:
                light[i][j]  = 1
result = 0

for i in range(1,n+1):
    heavy_cnt = sum(heavy[i])
    light_cnt = sum(light[i])

    if heavy_cnt> n//2 or light_cnt > n//2:
        result+=1

print(result)