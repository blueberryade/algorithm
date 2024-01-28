t = int(input())
for _ in range(t):
    a,b = input().split()
    lst = []
    for i in range(len(a)):
        x = ord(a[i])
        y = ord(b[i])
        if y<x:
            lst.append((y+26)-x)
        else:
            lst.append(y-x)
    print('Distances:',*lst)