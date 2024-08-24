import heapq
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    q = list(map(int,input().split()))
    heapq.heapify(q)

    result = 0
    
    while len(q) > 1:
        tmp = heapq.heappop(q) + heapq.heappop(q)
        result += tmp
        heapq.heappush(q,tmp)

    print(result)