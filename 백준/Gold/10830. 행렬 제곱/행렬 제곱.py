import sys
input= sys.stdin.readline

N,B = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]


def multi(a,b):
    x = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                x[i][j] += a[i][k]*b[k][j] 
            x[i][j]%=1000
    return x

def square(a,b):
    if b == 1:
        for i in range(len(a)):
            for j in range(len(a)):
                a[i][j]%=1000
        return a
    tmp = square(a,b//2)
    if b%2 == 0:
        return multi(tmp,tmp)
    else:
        return multi(multi(tmp,tmp),a)


result = square(A,B)

for i in result:
    print(*i)