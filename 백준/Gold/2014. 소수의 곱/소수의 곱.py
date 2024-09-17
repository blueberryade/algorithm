import sys
import heapq
input = sys.stdin.readline

k,n = map(int,input().split())
data = list(map(int,input().split()))
q = []

for d in data:
    heapq.heappush(q,d)

for _ in range(n):
    num = heapq.heappop(q)
    for i in range(k):
        temp = num*data[i]
        heapq.heappush(q,temp)

        if num%data[i] == 0:
            break
print(num)