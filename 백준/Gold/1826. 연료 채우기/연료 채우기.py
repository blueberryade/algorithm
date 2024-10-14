import heapq
import sys
input = sys.stdin.readline

N = int(input())
oil = [list(map(int,input().split())) for _ in range(N)]
L,P = map(int,input().split())

oil.sort(key=lambda x : (x[0],-x[1]))
oil.append([L,0])
result = 0
q = []

for l,p in oil:
    if P >= L:
        break
    
    while P < l and q:
        P+= -heapq.heappop(q)
        result+=1
    if P < l:
        break
    heapq.heappush(q,-p)

print(result if P>=L else -1)
