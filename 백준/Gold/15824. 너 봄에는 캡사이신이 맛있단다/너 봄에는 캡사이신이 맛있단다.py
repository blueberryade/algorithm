import sys
input = sys.stdin.readline
MOD = 1000000007

N = int(input())
data = list(map(int,input().split()))

data.sort()

pw = [1]*N
for i in range(1,N):
    pw[i] = pw[i-1]*2%MOD

result = 0

for i in range(N):
    max_num = data[i]*pw[i]
    min_num = data[i]*pw[N-i-1]
    result+= (max_num-min_num)

print(result%MOD)