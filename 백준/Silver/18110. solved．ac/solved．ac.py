import sys
input = sys.stdin.readline

def roundUp(num):
    if num - int(num) >= 0.5:
        return int(num)+1
    else:
        return int(num)

n = int(input())
if n == 0:
    print(0)
else:
    lst = []
    for _ in range(n):
        num = int(input().rstrip())
        lst.append(num)

    lst.sort()
    l = roundUp(n*0.15)
    print(roundUp(sum(lst[l:n-l]) / len(lst[l:n-l])))
