from bisect import bisect_right
from itertools import combinations
import sys
input = sys.stdin.readline

n,c = map(int,input().split())
weights = list(map(int,input().split()))
w1,w2 = weights[:n//2],weights[n//2:]

def get_sums(arr):
    arr_sums = []
    for i in range(len(arr)+1):
        for comb in combinations(arr,i):
            arr_sums.append(sum(comb))
    return arr_sums

w1_sums = get_sums(w1)
w2_sums = get_sums(w2)

w2_sums.sort()
result = 0

for w in w1_sums:
    if w <= c:
        result+= bisect_right(w2_sums, c-w)

print(result)