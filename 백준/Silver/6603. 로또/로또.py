import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    data = list(map(int,input().split()))
    k = data[0]
    s = data[1:]
    if k == 0:
        break

    for c in combinations(s,6):
        print(*c)
    print()

