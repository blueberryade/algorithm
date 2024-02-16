m = int(input())
n = int(input())

lst = []
tmp = 0
for i in range(1,101):
    if m<=i**2 and i**2<=n:
        tmp+=i**2
        lst.append(i**2)
if tmp == 0 and len(lst)==0:
    print(-1)
else:
    print(tmp)
    print(lst[0])
    