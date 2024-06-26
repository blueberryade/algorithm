import sys
import heapq
input = sys.stdin.readline

n,k = map(int,input().split())
bag = []
jewel = []

for i in range(n):
    m,v = map(int,input().split())
    heapq.heappush(jewel,(m,v))

for _ in range(k):
    bag.append(int(input()))

bag.sort()

result = 0
tmp = []

for b in bag:
    while jewel and jewel[0][0] <= b:
        heapq.heappush(tmp,-jewel[0][1])
        heapq.heappop(jewel)
    if tmp:
        result -= heapq.heappop(tmp)
print(result)        
