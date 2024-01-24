k = int(input())

for _ in range(k):
    p,m = map(int,input().split())
    lst = list(range(1,m+1))
    cnt = 0
    for _ in range(p):
        num = int(input())
        if num in lst:
            lst.remove(num)
        else:
            cnt+=1
    print(cnt)