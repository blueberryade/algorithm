from bisect import bisect_left
import sys
input = sys.stdin.readline

M,N,L = map(int,input().split())
shooting = list(map(int,input().split()))
animals = []
for _ in range(N):
    x,y = map(int,input().split())
    animals.append((x,y))
shooting.sort()
result = 0

for x,y in animals:
    if y > L:
        continue

    pos = bisect_left(shooting,x)

    if pos < len(shooting) and abs(shooting[pos]-x)+y <=L:
        result+=1
    elif pos > 0 and abs(shooting[pos-1]-x)+y <=L:
        result+=1
print(result)
