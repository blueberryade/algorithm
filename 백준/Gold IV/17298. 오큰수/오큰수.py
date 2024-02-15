import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))

answer = [-1]*n
stack = [0]

for i in range(1,n):
    while stack and lst[stack[-1]]< lst[i]:
        answer[stack.pop()] = lst[i]
    stack.append(i)

print(*answer)