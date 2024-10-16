import sys
import heapq
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    house,office = map(int,input().split())
    start = min(house,office)
    end = max(house,office)
    data.append((start,end))

d = int(input())
data.sort(key=lambda x:x[1])

q = []
max_cnt = 0

for start,end in data:
    if end-start <=d :
        heapq.heappush(q,start)
    
    while q and q[0] < end-d:
        heapq.heappop(q)
    max_cnt = max(max_cnt,len(q))

print(max_cnt)