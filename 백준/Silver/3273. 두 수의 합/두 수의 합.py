import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(list(map(int,input().split())))
x = int(input())

cnt = 0
start = 0
end = n-1
while start < end:
    num = lst[start] + lst[end]
    if num == x:
        cnt+=1
    if num <x:
        start+=1
        continue
    end-=1
print(cnt)