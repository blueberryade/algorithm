from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
lis = []

for i in data:
    idx = bisect_left(lis,i)
    if idx == len(lis):
        lis.append(i)
    else:
        lis[idx] = i
print(len(lis))       