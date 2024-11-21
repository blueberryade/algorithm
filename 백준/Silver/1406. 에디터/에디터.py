import sys
input = sys.stdin.readline

word1 = list(input().rstrip())
word2 = []
M = int(input())

for _ in range(M):
    command = input().split()

    if command[0] == 'L' and word1:
        word2.append(word1.pop())
    elif command[0] == 'D' and word2:
        word1.append(word2.pop())
    elif command[0] == 'B' and word1:
        word1.pop()
    elif command[0] == 'P':
        word1.append(command[1])

word1.extend(reversed(word2))
print(''.join(word1))

