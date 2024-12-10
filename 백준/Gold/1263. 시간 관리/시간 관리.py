import sys
input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    t,s = map(int,input().split())
    data.append((s,t))

data.sort(reverse=True)
result = data[0][0] - data[0][1]

for i in range(1,N):
    if result > data[i][0]:
        result = data[i][0]-data[i][1]
    else:
        result-=data[i][1]

if result >=0:
    print(result)
else:
    print(-1)
