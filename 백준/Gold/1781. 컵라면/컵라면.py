import heapq

n = int(input())

lst = []
for _ in range(n):
    t,v = map(int,input().split())
    lst.append((v,t))
lst.sort(key=lambda x:x[1])

q = []
for i in lst:
    heapq.heappush(q,i[0])
    if len(q)>i[1]:
        heapq.heappop(q)

print(sum(q))
