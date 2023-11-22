import sys
n = int(input())
lst = [int(sys.stdin.readline()) for i in range(n)]
lst.sort()
for i in lst:
    print(i)
