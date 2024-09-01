from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

lst = []

for i in data:
    idx = bisect_left(lst,i)
    if idx == len(lst):
        lst.append(i)
    else:
        lst[idx] = i
        
print(n-len(lst))    