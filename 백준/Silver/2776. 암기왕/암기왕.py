import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    data1 = set(map(int,input().split()))
    m = int(input())
    data2 = list(map(int,input().split()))
    
    for num in data2:
        if num in data1:
            print(1)
        else:
            print(0)
        