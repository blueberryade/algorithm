lst = input()

stack = []
result = 0

for i in range(len(lst)):
    if lst[i] == '(':
        stack.append('(')
    else:
        if lst[i-1] == '(':
            stack.pop()
            result+=len(stack)
        else:
            stack.pop()
            result+=1

    
print(result)