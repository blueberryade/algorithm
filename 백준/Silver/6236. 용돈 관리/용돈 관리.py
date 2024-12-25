N,M = map(int,input().split())
data = [int(input()) for _ in range(N)]

start = min(data)
end = sum(data)
result = 0

while start<=end:
    mid = (start+end) // 2
    now = mid
    count = 1

    for i in range(N):
        if now < data[i]:
            now = mid
            count+=1
        now-=data[i]

    if count > M or mid < max(data):
        start = mid+1
    else:
        result= mid
        end = mid-1

print(result)