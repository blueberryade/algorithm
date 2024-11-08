import sys
import heapq
input = sys.stdin.readline

n,k = map(int,input().split())
cus = []
items = []

for _ in range(n):
    id, w = map(int, input().split())
    cus.append(id)
    items.append(w)

cashier = []
for i in range(k):
    heapq.heappush(cashier, (0, i))

time_needed = [0] * k

finished = []
for i in range(n):
    t, x = heapq.heappop(cashier)
    time_needed[x] += items[i]
    heapq.heappush(cashier, (time_needed[x], x))
    finished.append((time_needed[x], -x, i))

answer = 0

for i, t in enumerate(sorted(finished)):
    answer += cus[t[2]] * (i+1)

print(answer)

