t = int(input())
for _ in range(t):
    h,w,n = map(int,input().split())
    x = n%h
    y = n//h+1
    if x == 0:
        y -=1
        x = h
    print(x*100+y)