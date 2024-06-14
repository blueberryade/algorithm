import sys
input = sys.stdin.readline

word = input().rstrip()
bomb = input().rstrip()

stack = []
bomb_len = len(bomb)

for w in word:
    stack.append(w)
    if ''.join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()

if stack:        
    print(''.join(stack))
else:
    print('FRULA')    
