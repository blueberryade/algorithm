n = int(input())
lst = []

for i in range(n):
    n = int(input())
    lst.append(n)

lst = sorted(lst)
for i in lst:
    print(i)