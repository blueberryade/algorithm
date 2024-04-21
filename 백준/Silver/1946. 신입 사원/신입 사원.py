import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    lst.sort()
    cnt = 1
    top = lst[0][1]
    for i in range(1,N):
        if  lst[i][1]< top:
            top = lst[i][1]
            cnt +=1
    print(cnt)      