import sys
input = sys.stdin.readline

def calculate(m,n,x,y):
    while x <= m*n:
        if (x-y)%n == 0:
            return x
        x+= m
    return -1
t = int(input())

for _ in range(t):
    m,n,x,y = map(int,input().split())
    print(calculate(m,n,x,y))