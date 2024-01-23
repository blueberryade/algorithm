lst = sorted([int(input()) for _ in range(9)])
total = sum(lst)
a = 0
b = 0
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if total - lst[i] -lst[j] == 100:
            a = lst[i]
            b = lst[j]
lst.remove(a)
lst.remove(b)

for i in lst:
    print(i)
