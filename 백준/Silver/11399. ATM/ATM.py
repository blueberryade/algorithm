N = int(input())
lst = sorted(list(map(int,input().split())))
lst_sum = []
temp = 0
for i in lst:
    temp = temp+i
    lst_sum.append(temp)
print(sum(lst_sum))