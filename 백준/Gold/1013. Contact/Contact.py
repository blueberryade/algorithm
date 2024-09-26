import sys
import re
input = sys.stdin.readline

p = re.compile("(100+1+|01)+")
t = int(input())

for _ in range(t):
    s = input().strip()
    if p.fullmatch(s):
        print("YES")
    else:
        print("NO")


