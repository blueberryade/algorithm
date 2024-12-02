import sys
input = sys.stdin.readline

word = list(input().rstrip())
bomb = list(input().rstrip())
stack = []
l = len(bomb)


for i in word:
    stack.append(i)
    if stack[-l:] == bomb:
        for _ in range(l):
            stack.pop()


if stack:
    print(''.join(stack))
else:
    print('FRULA')