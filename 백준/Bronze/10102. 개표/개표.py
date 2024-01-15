v = int(input())
n = input()
a = n.count('A')
b = n.count('B')
if a == b:
    print('Tie')
elif a>b:
    print('A')
else:
    print('B')