import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n,m = map(int,input().split())
for a in combinations_with_replacement(map(str,range(1,n+1)),m):
    print(' '.join(a))