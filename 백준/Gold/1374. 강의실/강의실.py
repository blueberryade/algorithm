import heapq
import sys
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    i,s,e = map(int,input().split())
    lst.append((s,e))
lst.sort()

q = []
for s,e in lst:
    if q and q[0] <= s:
        heapq.heappop(q)
    heapq.heappush(q,e)

print(len(q))
