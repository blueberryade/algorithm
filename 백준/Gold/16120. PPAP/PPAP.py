word = input().rstrip()
stack = []
result = 'NP'
ppap = ['P','P','A','P']
for w in word:
    stack.append(w)
    if len(stack) >=4 and stack[-4:] == ppap:
        for _ in range(3):
            stack.pop()

if len(stack) == 1 and stack == ['P']:
    result = 'PPAP'

print(result)