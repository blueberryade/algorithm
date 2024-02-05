import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    c = input().split()
    if c[0] == 'push':
        stack.append(c[1])
    if c[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    if c[0] == 'size':
        print(len(stack))
    if c[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if c[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])