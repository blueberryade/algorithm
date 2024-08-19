import sys
input = sys.stdin.readline

n,k = map(int,input().split())
data = list(map(int,input().split()))

result = []
for i in range(1,n):
    result.append(data[i]-data[i-1])

result.sort(reverse=True)
print(sum(result[k-1:]))