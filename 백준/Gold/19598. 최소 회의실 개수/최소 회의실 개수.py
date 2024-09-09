import heapq
import sys
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    start,end = map(int,input().split())
    data.append((start,end))

data.sort()

q = []
for s,e in data:
    if q and q[0]<=s:
        heapq.heappop(q)
    heapq.heappush(q,e)
print(len(q))