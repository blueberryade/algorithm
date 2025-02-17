T = int(input())
for _ in range(T):
    msg = input()
    n = int((len(msg))**0.5)

    result = ""
    for i in range(n,0,-1):
        for j in range(i,n*n+1,n):
            result+=msg[j-1]
    print(result)
    