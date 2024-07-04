import heapq

n = int(input())
q = []
max_day = 0

for _ in range(n):
    d,w = map(int,input().split())
    heapq.heappush(q,(-w,d))
    if max_day<d:
        max_day = d

result = 0 
assigned = [False]*(max_day+1)       

while q:
    w,d = heapq.heappop(q)
    for i in range(d,0,-1):
        if assigned[i]:
            continue
        assigned[i] = True
        result-=w
        break
print(result)    