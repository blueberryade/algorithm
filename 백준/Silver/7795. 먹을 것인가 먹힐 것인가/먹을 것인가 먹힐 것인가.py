import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()

    result = 0
    count = 0

    for i in range(n):
        while True:
            if count == m or a[i]<=b[count]:
                result+=count
                break
            else:
                count+=1
    print(result)                

