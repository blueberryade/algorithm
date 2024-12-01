n,m = map(int,input().split())
data = list(map(int,input().split()))

start,end,cnt = 0,0,0

while end<n:
    total = sum(data[start:end+1])

    if total == m:
        cnt+=1
        end+=1
    elif total > m:
        start+=1
    else:
        end+=1

print(cnt)