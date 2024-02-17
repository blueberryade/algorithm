import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
stack = []
answer = 0

for i in lst:
    while stack and stack[-1][0] < i:
        answer+= stack.pop()[1]
    if not stack:
        stack.append((i,1))
    else:
        if stack[-1][0]==i:
            cnt = stack.pop()[1]
            answer+=cnt

            if stack: 
                answer+=1
            stack.append((i,cnt+1))
        else:
            stack.append((i,1))
            answer+=1
print(answer)