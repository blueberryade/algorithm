import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))
result = [0]*N
stack = []

for i in range(N):
    while stack and data[stack[-1]] < data[i]:
        result[stack.pop()] = data[i]
    stack.append(i)

while stack:
    result[stack.pop()] = -1

print(*result)