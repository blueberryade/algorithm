k = int(input())

for _ in range(k):
    p,m = map(int,input().split())
    lst = [0]*(m+1)
    cnt = 0
    for _ in range(p):
        num = int(input())
        if lst[num]==1:
            cnt+=1
        else:
            lst[num]=1
    print(cnt)
