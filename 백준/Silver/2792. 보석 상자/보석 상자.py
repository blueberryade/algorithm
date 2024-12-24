import sys
input = sys.stdin.readline

N,M = map(int,input().split())
data = [int(input()) for _ in range(M)]

start = 1
end = max(data)
result = 0

while start<=end:
    mid = (start+end) // 2
    total = 0

    for i in range(M):
        total+=data[i]//mid
        if data[i]%mid !=0:
            total+=1
    
    if total > N:
        start = mid+1
    else:
        result = mid
        end = mid-1

print(result)