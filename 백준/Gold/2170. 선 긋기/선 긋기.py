import sys
input = sys.stdin.readline

n = int(input())
lines = []
result = 0

for _ in range(n):
    a,b = map(int,input().split())
    lines.append((a,b))

lines.sort()

start,end = lines[0]

for i in range(1,n):
    x,y = lines[i]

    if x<=end:
        end = max(y,end)
    else:
        result+= (end-start)
        start,end = x,y

result += (end-start)
print(result)


