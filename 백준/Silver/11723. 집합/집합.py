import sys
input = sys.stdin.readline

s = set()
M = int(input())
for _ in range(M):
    command = input().strip().split()
    if len(command) == 1:
        if command[0] == 'all':
            s = set(list(range(1,21)))
        else:
            s = set()
    else:
        c,num = command
        num = int(num)
        if c == 'add':
            s.add(num)
        elif c == 'remove':
            s.discard(num)
        elif c == 'check':
            print(1 if num in s else 0)
        elif c == 'toggle':
            if num in s:
                s.discard(num)
            else:
                s.add(num)