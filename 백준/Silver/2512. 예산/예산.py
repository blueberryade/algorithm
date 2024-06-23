import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
budget = int(input())
start = 0
end = max(data)

while start<=end:
    mid = (start+end) // 2
    total = 0
    for i in data:
        if i > mid:
            total+=mid
        else:
            total+=i
    if total <= budget:
        start = mid+1
    else:
        end = mid-1
print(end)        


