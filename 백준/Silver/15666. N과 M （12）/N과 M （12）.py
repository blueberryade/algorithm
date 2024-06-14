import sys
input = sys.stdin.readline

n,m = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
temp = []

def backtracking(start):
    if len(temp) == m:
        print(*temp)
        return
    remember = 0
    for i in range(start,n):
        if remember!=data[i]:
            temp.append(data[i])
            remember = data[i]
            backtracking(i)
            temp.pop()

backtracking(0)
