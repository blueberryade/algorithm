n = int(input())
INF = int(1e9)
distance = [[INF]*(n+1) for _ in range(n+1)]

while True:
    a,b = map(int,input().split())
    if a == -1 and b == -1:
        break
    distance[a][b] = 1
    distance[b][a] = 1

for i in range(1,n+1):
    distance[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if distance[i][j] > distance[i][k]+distance[k][j]:
                distance[i][j] = distance[i][k]+distance[k][j]
scores = []
for i in range(1,n+1):
    scores.append(max(distance[i][1:]))
min_score = min(scores)    

print(min_score,scores.count(min_score))

for i in range(len(scores)):
    if scores[i] == min_score:
        print(i+1,end=' ')