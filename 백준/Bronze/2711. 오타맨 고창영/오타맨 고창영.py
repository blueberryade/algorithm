t = int(input())
for _ in range(t):
    i,word = input().split()
    i = int(i)
    word = list(word)
    word.pop(i-1)
    print(''.join(word))