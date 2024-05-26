import sys
from itertools import combinations
input = sys.stdin.readline

def dist(a,b):
    d = 0
    for i,j in zip(a,b):
        if i!=j:
            d+=1
    return d

t = int(input())
for _ in range(t):
    n = int(input())
    mbti = input().rstrip().split()
    if n > 32:
        print(0)
    else:
        result = 13
        case = combinations(mbti,3)
        for a,b,c in case:
            d = 0
            d += dist(a,b)
            d += dist(b,c)
            d += dist(a,c)
            result = min(result,d)
        print(result)