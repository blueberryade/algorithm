def solution(order):
    answer = []
    stack = []
    now = 1
    for i in order:
        while now <= i:
            stack.append(now)
            now+=1
        if stack[-1] == i:
            answer.append(stack.pop())
        else:
            break
    return len(answer)