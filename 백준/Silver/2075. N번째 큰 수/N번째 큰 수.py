import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    numbers = map(int,input().split())
    for number in numbers:
        if len(q) < n:
            heapq.heappush(q,number)
        else:
            if q[0] < number:
                heapq.heappop(q)
                heapq.heappush(q,number)

print(q[0])

