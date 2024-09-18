import heapq

n,m = map(int,input().split())
q = list(map(int,input().split()))
heapq.heapify(q)

for _ in range(m):
    x = heapq.heappop(q)
    y = heapq.heappop(q)
    temp = x+y
    heapq.heappush(q,temp)
    heapq.heappush(q,temp)

print(sum(q))