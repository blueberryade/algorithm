import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
data = list(map(int,input().split()))

data.sort()

distance = []
for i in range(1,n):
    distance.append(data[i]-data[i-1])

distance.sort(reverse=True)

for i in range(k-1):
    if distance:
        distance.pop(0)

print(sum(distance))


