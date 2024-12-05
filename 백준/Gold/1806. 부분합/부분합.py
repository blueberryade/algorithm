import sys
input = sys.stdin.readline

N,S = map(int,input().split())
data = list(map(int,input().split()))

result = sys.maxsize
left,right,total = 0,0,0

while True:
    if total >= S:
        result = min(result,right-left)
        total -= data[left]
        left+=1
    elif right == N:
        break
    else:
        total+=data[right]
        right+=1

if result == sys.maxsize:
    print(0)
else:
    print(result)