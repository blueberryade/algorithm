import sys
input = sys.stdin.readline

n,m,l = map(int,input().split())
data = [0]+list(map(int,input().split()))+[l]
data.sort()

start = 1
end = l-1
result = 0

while start <= end:
    mid = (start+end) // 2
    cnt = 0

    for i in range(1,len(data)):
        if data[i]-data[i-1] > mid:
            cnt += (data[i]-data[i-1]-1)//mid
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        result = mid
print(result)
