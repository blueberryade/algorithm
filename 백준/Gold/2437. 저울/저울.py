import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
lst.sort()

num = 1

for l in lst:
    if num<l:
        break
    num+=l

print(num)