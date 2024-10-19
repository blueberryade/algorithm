import sys
input = sys.stdin.readline

n,l = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
data.sort()

cur = 0
result = 0

for start,end in data:

    if cur >= end:
        continue
    
    cur = max(cur,start)

    length = end-cur

    if length % l == 0:
        cnt = length//l
        cur = end
    else:
        cnt = length//l+1
        cur=end+(l-length%l)
        
    result+=cnt

print(result)
