t = int(input())
for i in range(t):
    stack = []
    n = input()
    for j in n:
        if j == '(':
            stack.append('(')
        elif j == ')':
            if len(stack) ==0:
                stack.append(')')
                break
            else:
                stack.pop()
    
    if len(stack)!=0:
        print('NO')
    else:
        print('YES')