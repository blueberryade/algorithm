import sys
import math
input = sys.stdin.readline

n = int(input())
a = int(input())

lst = []

for i in range(n-1):
    num = int(input())
    lst.append(num-a)
    a = num

g = lst[0]
for j in range(1,len(lst)):
    g = math.gcd(g,lst[j])

result = 0
for e in lst:
    result+=e//g-1

print(result)