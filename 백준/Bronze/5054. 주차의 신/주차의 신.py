t = int(input())
for _ in range(t):
    num = int(input())
    store = sorted(list(map(int,input().split())))
    print((store[-1]-store[0])*2)