import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    heapq.heappush(q,int(input()))

result = 0

while len(q)!=1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    tmp = a+b
    result += tmp
    heapq.heappush(q,tmp)

print(result)
