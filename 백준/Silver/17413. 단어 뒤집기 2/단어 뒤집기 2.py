import sys
input = sys.stdin.readline

s = input().rstrip()
result = []
temp = []
check = False

for char in s:
    if char == '<':
        if temp:
            result.append(''.join(temp[::-1]))
            temp = []
        check = True
        result.append(char)
    
    elif char == '>':
        check = False
        result.append(char)

    elif char == ' ' and not check:
        result.append(''.join(temp[::-1]))
        result.append(' ')
        temp = []
    else:
        if check:
            result.append(char)
        else:
            temp.append(char)

if temp:
    result.append(''.join(temp[::-1]))
print(''.join(result))