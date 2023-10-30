while True:
    n = int(input())
    if n == -1:
        break
    lst = []
    for i in range(1,n):
        if n%i==0:
            lst.append(i)
    if sum(lst) != n:
        print(n,'is NOT perfect.')
    else:
        print( n," = ", " + ".join(str(i) for i in lst), sep="")