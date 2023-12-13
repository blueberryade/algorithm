import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    c = input().rstrip()

    if len(c) >2:
        stack.append(int(c[2:]))
    elif c == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif c == '3':
        print(len(stack))
    elif c == '4':
        print(1 if len(stack)==0 else 0)
    elif c == '5':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
