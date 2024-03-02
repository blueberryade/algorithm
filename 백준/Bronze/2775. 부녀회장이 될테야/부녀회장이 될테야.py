t = int(input())

for _ in range(t):
    floor = int(input())
    num = int(input())
    f = [i for i in range(1,num+1)]
    for k in range(floor):
        for i in range(1,num):
            f[i] += f[i-1]
    print(f[-1])  