import sys
input = sys.stdin.readline

S = input().rstrip()
stack = []
cnt = 0
before = ''
for s in S:
    if s == '(':
        stack.append([cnt-1, before])
        cnt = 0
    elif s == ')':
        tmp = stack.pop()
        cnt = cnt*tmp[1]+tmp[0]
    else:
        cnt+=1
        before = int(s)

print(cnt)