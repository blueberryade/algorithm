import sys
input = sys.stdin.readline

n = int(input())
building = [int(input()) for _ in range(n)]
stack = []
answer = 0

for b in building:
    while stack and stack[-1]<=b:
        stack.pop()
    stack.append(b)
    answer+=len(stack)-1

print(answer)