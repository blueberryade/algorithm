import sys
input = sys.stdin.readline

n,c = map(int,input().split())
m = int(input())
lst = []
for _ in range(m):
    s,e,box = map(int,input().split())
    lst.append((s,e,box))

lst.sort(key=lambda x:x[1])

capacity = [c]*n
result = 0

for s,e,box in lst:
    temp = c
    for i in range(s,e):
        if temp>min(capacity[i],box):
            temp = min(capacity[i],box)
    for i in range(s,e):
        capacity[i]-=temp
    result+=temp
            
print(result)