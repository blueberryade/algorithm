import sys
input = sys.stdin.readline

N = int(input())
data = [int(input()) for _ in range(N)]
data.sort()

result = 0

for i in range(1,N+1):
    if i!=data[i-1]:
        result+=abs(i-data[i-1])

print(result)