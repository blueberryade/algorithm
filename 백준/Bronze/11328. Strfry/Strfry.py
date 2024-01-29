n = int(input())
for _ in range(n):
    a,b = input().split()
    a = sorted(list(a))
    b = sorted(list(b))
    if a == b:
        print('Possible')
    else:
        print('Impossible')