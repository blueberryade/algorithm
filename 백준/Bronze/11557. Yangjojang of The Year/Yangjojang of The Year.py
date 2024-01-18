t = int(input())

for _ in range(t):
    n = int(input())
    name = ''
    max = 0
    for _ in range(n):
        s,l = input().split()
        l = int(l)
        if l > max:
            name = s
            max = l
    print(name)