n = input()
lst = list(map(int,str(n)))
lst.sort(reverse=True)
for i in lst:
    print(i,end='')
