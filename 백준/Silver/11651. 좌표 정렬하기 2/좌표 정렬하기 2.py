n = int(input())
lst = []

for i in range(n):
    a,b = map(int,input().split())
    lst.append([b,a])

lst.sort()

for i in lst:
    print(i[1],i[0])
