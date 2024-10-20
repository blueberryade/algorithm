import sys
input = sys.stdin.readline

m,n = map(int,input().split())
data = list(map(int,input().split()))
start = 1
end = max(data)
answer = 0

while start <= end:
    mid = (start+end) // 2
    cnt = 0
    for i in data:
        cnt+=i//mid
    if cnt>=m:
        answer = mid
        start = mid+1
    else:
        end = mid -1
print(answer)
