N,Q = map(int,input().split())

back = []
front = []
now = ''

for _ in range(Q):
    lst = input().split()

    if lst[0] == 'B':
        if back:
            front.append(now)
            now = back.pop()

    elif lst[0] == 'F':
        if front:
            back.append(now)
            now = front.pop()

    elif lst[0] == 'A':
        front.clear()
        if now:
            back.append(now)
        now = lst[1]    

    elif lst[0] == 'C':
        stack = []
        for i in back:
            if stack and stack[-1] == i:
                continue
            else:
                stack.append(i)
        back = stack


print(now)
if back:
    print(*reversed(back))
else:
    print(-1)
if front:
    print(*reversed(front))
else:
    print(-1)